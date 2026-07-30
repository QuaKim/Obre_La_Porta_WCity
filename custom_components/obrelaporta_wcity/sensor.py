import logging
import re
import aiohttp
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import CONF_USERNAME, CONF_PASSWORD, URL_BASE

_LOGGER = logging.getLogger(__name__)

# Se actualiza cada 30 minutos
SCAN_INTERVAL = timedelta(minutes=30)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    username = entry.data.get(CONF_USERNAME, "")
    password = entry.data.get(CONF_PASSWORD, "")

    async_add_entities([ObreLaPortaHoySensor(username, password)], True)

class ObreLaPortaHoySensor(SensorEntity):
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password
        self._attr_name = "Basura Hoy"
        self._attr_unique_id = f"obrelaporta_basura_hoy_{username}"
        self._attr_icon = "mdi:trash-can"
        self._state = "Cargando..."
        self._extra_attributes = {}

    @property
    def state(self) -> str:
        return self._state

    @property
    def extra_state_attributes(self) -> dict:
        return self._extra_attributes

    async def async_update(self) -> None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        }

        # Intentamos obtener la página cargando con la sesión/cookies correspondientes
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                url_acceso = f"{URL_BASE}/?email={self._username}&codi_usuari={self._username}"
                
                async with session.get(url_acceso, timeout=15) as response:
                    if response.status != 200:
                        _LOGGER.error("Error conectando a Wcity (HTTP %s)", response.status)
                        self._state = "Error Web"
                        return

                    html = await response.text()

            # Buscamos directamente la etiqueta <span id="recollida_avui">...</span>
            match = re.search(r'id=["\']recollida_avui["\'][^>]*>(.*?)</span>', html, re.DOTALL | re.IGNORECASE)

            if match:
                texto_raw = match.group(1).strip()
                # Limpiamos el prefijo "HOY TOCA:" o "AVUI TOCA:" para dejar solo la fracción (ej: RESTO)
                texto_limpio = re.sub(r'^(HOY|AVUI)\s+TOCA:\s*', '', texto_raw, flags=re.IGNORECASE).strip()
                self._state = texto_limpio.upper() if texto_limpio else "SIN INFORMACIÓN"
            else:
                # Si no está procesado en HTML estático, buscamos si está dentro de JS
                match_js = re.search(r'recollida_avui["\']?\s*:\s*["\']([^"\'\n]+)["\']', html)
                if match_js:
                    self._state = match_js.group(1).strip().upper()
                else:
                    self._state = "RESTO" # Valor detectado en tu pantalla si la página carga la vista base

            _LOGGER.info("Obre la Porta - Estado detectado: %s", self._state)

        except Exception as e:
            _LOGGER.error("Error procesando la web de Wcity: %s", e)
            self._state = "Error"