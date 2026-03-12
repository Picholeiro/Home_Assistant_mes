"""Sensor Mes del Año para Home Assistant."""
import logging
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME
from homeassistant.helpers.event import async_track_time_interval
import homeassistant.util.dt as dt_util

_LOGGER = logging.getLogger(__name__)

DOMAIN = "mes_del_ano"


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Configurar la plataforma del sensor."""
    name = config.get(CONF_NAME, "Mes actual")
    async_add_entities([MesSensor(name)], True)


class MesSensor(SensorEntity):
    """Sensor que devuelve el mes actual del año."""

    def __init__(self, name):
        self._attr_name = name
        self._attr_unique_id = f"mes_del_ano_{name}"
        self._attr_icon = "mdi:calendar-month"
        self._state = None
        self._last_month = None

    @property
    def native_value(self):
        """Devuelve el número del mes actual."""
        return self._state

    async def async_added_to_hass(self):
        """Cuando se añade la entidad, programar actualizaciones cada hora."""
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
            self._state = current_month
            self._attr_extra_state_attributes = {
                "month_name": current_time.strftime("%B"),
                "month_name_es": [
                    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
                ][current_month - 1],
                "year": current_time.year,
                "month_number": current_month,
            }
            self.async_write_ha_state()
            _LOGGER.debug("Sensor actualizado: mes %s", current_month)
