import logging
import aiohttp
from datetime import datetime, date, timedelta

from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .const import CONF_USERNAME, CONF_PASSWORD, URL_BASE

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(hours=8)

TOKEN_PWA = "MWMxNDNmNTM3YjQ3NDhkNzgyY2RmYWZmODZhYmFmYmU2NGNiMGU4ZmY1MzE1MjhjYWQ2ZDExZGQ1Njg0NWRkZQ=="


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Configura la entidad de calendario desde una entrada de configuración."""
    _LOGGER.info("Inicializando entidad de calendario Obre la porta")
    username = entry.data.get(CONF_USERNAME, "")
    password = entry.data.get(CONF_PASSWORD, "")

    entity = ObreLaPortaCalendar(username, password)
    async_add_entities([entity], update_before_add=True)


class ObreLaPortaCalendar(CalendarEntity):
    """Entidad de Calendario para Obre la porta Wcity."""

    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password
        self._attr_name = "Calendario Recogida Basura"
        self._attr_unique_id = f"obrelaporta_calendar_{username}"
        self._dates_data = {}
        self._tipus_recollides = {}

    def _parse_event_date(self, key_date: str) -> date | None:
        """Parsea la fecha usando directamente la clave del diccionario (ej: 2026-08-01)."""
        if not key_date or str(key_date).startswith("0000"):
            return None

        for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%Y/%m/%d"):
            try:
                return datetime.strptime(str(key_date).strip(), fmt).date()
            except (ValueError, TypeError):
                continue

        return None

    def _extract_residuos(self, day_info: dict) -> list[str]:
        """Extrae la lista de residuos mapeando campos dinámicos e IDs."""
        residuos = []
        if not isinstance(day_info, dict):
            return residuos

        # 1. Buscar campos conocidos dentro del objeto del día
        for key in ("types", "tipus", "residuos", "recollides", "fraccions", "items", "tipus_rec"):
            val = day_info.get(key)
            if val:
                lista = list(val.values()) if isinstance(val, dict) else (val if isinstance(val, list) else [val])
                for item in lista:
                    if isinstance(item, dict):
                        nom = item.get("desc") or item.get("nom") or item.get("description")
                        if nom:
                            residuos.append(str(nom).strip())
                    elif isinstance(item, (str, int)):
                        str_id = str(item).strip()
                        if str_id in self._tipus_recollides:
                            t_info = self._tipus_recollides[str_id]
                            nom = t_info.get("desc") or t_info.get("nom") if isinstance(t_info, dict) else t_info
                            residuos.append(str(nom).strip())
                        else:
                            residuos.append(str_id)

        # 2. Si no hay subclaves directas, buscar si las claves numéricas son IDs de residuos
        if not residuos:
            for k, v in day_info.items():
                if k in ("dia_setmana", "date", "today", "t1", "t2"):
                    continue

                # Si el valor o la clave coinciden con tipus_recollides
                str_val = str(v).strip() if v is not None else ""
                str_k = str(k).strip()

                if str_val in self._tipus_recollides:
                    t_info = self._tipus_recollides[str_val]
                    nom = t_info.get("desc") or t_info.get("nom") if isinstance(t_info, dict) else t_info
                    residuos.append(str(nom).strip())
                elif str_k in self._tipus_recollides:
                    t_info = self._tipus_recollides[str_k]
                    nom = t_info.get("desc") or t_info.get("nom") if isinstance(t_info, dict) else t_info
                    residuos.append(str(nom).strip())

        return list(set(residuos))

    @property
    def event(self) -> CalendarEvent | None:
        """Devuelve el evento de recogida para el día actual."""
        today_date = date.today()

        if not isinstance(self._dates_data, dict):
            return None

        for key_date, day_info in self._dates_data.items():
            event_date = self._parse_event_date(key_date)
            if event_date == today_date:
                residuos = self._extract_residuos(day_info)
                if residuos:
                    return CalendarEvent(
                        start=today_date,
                        end=today_date + timedelta(days=1),
                        summary=f"Recogida: {', '.join(residuos)}",
                        description=f"Día: {day_info.get('dia_setmana', '') if isinstance(day_info, dict) else ''}",
                    )
        return None

    async def async_get_events(
        self, hass: HomeAssistant, start_date: datetime, end_date: datetime
    ) -> list[CalendarEvent]:
        """Entrega los eventos a la interfaz de Home Assistant."""
        if not self._dates_data:
            await self.async_update()

        events = []
        if not isinstance(self._dates_data, dict):
            return events

        start_d = start_date.date() if isinstance(start_date, datetime) else start_date
        end_d = end_date.date() if isinstance(end_date, datetime) else end_date

        for key_date, day_info in self._dates_data.items():
            event_date = self._parse_event_date(key_date)
            if not event_date:
                continue

            if start_d <= event_date <= end_d:
                residuos = self._extract_residuos(day_info)
                dia_semana = day_info.get("dia_setmana", "") if isinstance(day_info, dict) else ""

                if residuos:
                    for residuo in residuos:
                        events.append(
                            CalendarEvent(
                                start=event_date,
                                end=event_date + timedelta(days=1),
                                summary=f"Recogida: {residuo}",
                                description=f"Fracción: {residuo} | Día: {dia_semana}",
                            )
                        )
 #               else:
 #                   # Si la fecha es válida pero no especifica residuo
 #                   events.append(
 #                       CalendarEvent(
 #                           start=event_date,
 #                           end=event_date + timedelta(days=1),
 #                           summary="Recogida programada",
 #                           description=f"Día: {dia_semana}",
 #                       )
  #                  )

        return events

    async def async_update(self) -> None:
        """Obtiene el calendario manteniendo la sesión viva mediante CookieJar dinámico."""
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

        jar = aiohttp.CookieJar(unsafe=True)
        url_calendari = f"{URL_BASE}/modules/WCITY/api/v1/sector/calendari?que=mes"

        try:
            async with aiohttp.ClientSession(headers=headers, cookie_jar=jar) as session:
                # 1. Inicializar sesión y cookies
                async with session.get(f"{URL_BASE}/", timeout=10) as resp_init:
                    pass

                # 2. Consultar el endpoint real del calendario
                async with session.get(url_calendari, timeout=15) as resp:
                    if resp.status == 200:
                        json_data = await resp.json(content_type=None)

                        if isinstance(json_data, dict) and json_data.get("result") == "OK":
                            data_content = json_data.get("data", {})

                            if isinstance(data_content, dict):
                                self._dates_data = data_content.get("dates", {})
                                self._tipus_recollides = data_content.get("tipus_recollides", {})

                                _LOGGER.info(
                                    "Calendario Obre La Porta actualizado: %d días cargados",
                                    len(self._dates_data),
                                )
                        else:
                            _LOGGER.error("Respuesta no OK en calendario: %s", json_data)
                    else:
                        _LOGGER.error("Error HTTP %s al consultar calendario", resp.status)

        except Exception as e:
            _LOGGER.error("Excepción al consultar calendario: %s", e, exc_info=True)