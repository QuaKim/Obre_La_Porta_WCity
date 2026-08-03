import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

# Definimos las plataformas que soporta la integración
PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.CALENDAR,
]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configura la integración Obre la Porta a partir de una entrada."""
    _LOGGER.debug("Cargando plataformas para Obre la Porta: %s", PLATFORMS)
    
    # Carga las entidades de sensor.py y calendar.py
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Descarga las plataformas cuando se elimina o recarga la integración."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    return unload_ok