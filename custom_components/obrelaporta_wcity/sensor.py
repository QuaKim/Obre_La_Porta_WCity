import logging
import aiohttp
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import CONF_USERNAME, CONF_PASSWORD, URL_BASE

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=30)

TOKEN_PWA = "MWMxNDNmNTM3YjQ3NDhkNzgyY2RmYWZmODZhYmFmYmU2NGNiMGU4ZmY1MzE1MjhjYWQ2ZDExZGQ1Njg0NWRkZQ=="

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    username = entry.data.get(CONF_USERNAME, "")
    password = entry.data.get(CONF_PASSWORD, "")

    async_add_entities([ObreLaPortaHoySensor(username, password)], update_before_add=True)
    
class ObreLaPortaHoySensor(SensorEntity):
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password
        self._attr_name = "Basura Hoy"
        self._attr_unique_id = f"obrelaporta_basura_hoy_{username}"
        self._attr_icon = "mdi:trash-can"
        self._attr_native_value = "Cargando..."
        self._attr_extra_state_attributes = {}

    async def async_update(self) -> None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 OPR/133.0.0.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "es-ES,es;q=0.9,ca;q=0.8",
            "X-Requested-With": "XMLHttpRequest",
            "X-TOKEN": TOKEN_PWA,
            "X-LANG": "ca",
            "Content-Type": "text/plain",
            "Referer": f"{URL_BASE}/",
        }

        cookies = {
            "aWRfd2FzdGVpbmRleHBocA": "rpvc7elvhtbi3r9040l0r9ljf4"
        }

        url_sector = f"{URL_BASE}/modules/WCITY/api/v1/sector"

        try:
            async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:
                async with session.get(url_sector, timeout=15) as resp_sector:
                    if resp_sector.status == 200:
                        json_sector = await resp_sector.json(content_type=None)

                        if isinstance(json_sector, dict) and json_sector.get("result") == "OK":
                            data = json_sector.get("data", {})
                            recollides = data.get("recollides", [])

                            if recollides:
                                nombres = [item.get("desc") for item in recollides if item.get("desc")]
                                self._attr_native_value = ", ".join(nombres) if nombres else "Ninguna"
                                self._attr_extra_state_attributes = {
                                    "recollides_detall": recollides,
                                    "total_recogidas_hoy": len(recollides),
                                }
                            else:
                                self._attr_native_value = "Sin recogida hoy"
                                self._attr_extra_state_attributes = {"recollides_detall": []}
                        else:
                            self._attr_native_value = "Error API Sector"
                    else:
                        self._attr_native_value = f"Error HTTP {resp_sector.status}"

        except Exception as e:
            _LOGGER.error("Error consultando la API de Wcity: %s", e, exc_info=True)
            self._attr_native_value = "Error de conexión"