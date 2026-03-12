"""Sensor Mes del Año para Home Assistant."""
import logging
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME
from homeassistant.helpers.event import async_track_time_interval
import homeassistant.util.dt as dt_util

from .const import DOMAIN, DEFAULT_NAME

_LOGGER = logging.getLogger(__name__)

MESES_ES = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

# Estado del sensor: nombre en español en minúsculas (enero … diciembre)
MESES_STATE = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Configurar el sensor desde una entrada del Config Flow (UI)."""
    name = config_entry.data.get(CONF_NAME, DEFAULT_NAME)
    async_add_entities([MesSensor(name)], True)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Configurar el sensor desde configuration.yaml (compatibilidad legacy)."""
    name = config.get(CONF_NAME, DEFAULT_NAME)
    async_add_entities([MesSensor(name)], True)


class MesSensor(SensorEntity):
    """Sensor que devuelve el mes actual del año como nombre en inglés."""

    def __init__(self, name):
        self._attr_name = name
        self._attr_unique_id = f"mes_del_ano_{name.lower().replace(' ', '_')}"
        self._attr_icon = "mdi:calendar-month"
        self._state = None
        self._last_month = None

    @property
    def native_value(self):
        """Devuelve el nombre del mes en español en minúsculas (enero ... diciembre)."""
        return self._state

    async def async_added_to_hass(self):
        """Registrar actualizaciones automáticas al añadir la entidad."""
        await super().async_added_to_hass()
        async_track_time_interval(
            self.hass, self.async_update, timedelta(hours=1)
        )
        await self.async_update()

    async def async_update(self, now=None):
        """Actualizar el estado del sensor."""
        current_time = dt_util.now()
        current_month = current_time.month

        if current_month != self._last_month:
            self._last_month = current_month
            self._state = MESES_STATE[current_month - 1]
            self._attr_extra_state_attributes = {
                "month_name_es": MESES_ES[current_month - 1],
                "month_number": current_month,
                "year": current_time.year,
            }
            self.async_write_ha_state()
            _LOGGER.debug(
                "Sensor actualizado: %s (mes %s)",
                self._state,
                current_month,
            )
