import logging
from datetime import datetime
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.helpers.entity_platform import async_setup_platform
import homeassistant.util.dt as dt_util

_LOGGER = logging.getLogger(__name__)

DOMAIN = "mes_del_ano"

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Configurar la plataforma del sensor."""
    name = config.get(CONF_NAME, "Mes actual")
    async_add_entities([MesSensor(name)], True)

class MesSensor(SensorEntity):
    """Sensor que devuelve el mes actual."""

    def __init__(self, name):
        self._attr_name = name
        self._attr_unique_id = f"mes_del_ano_{name}"
        self._attr_icon = "mdi:calendar-month"
        self._state = None
        self._last_month = None
        self._hass = None

    @property
    def native_value(self):
        return self._state

    async def async_added_to_hass(self):
        """Cuando se añade la entidad, programar actualizaciones."""
        await super().async_added_to_hass()
        # Actualizar cada hora para detectar cambio de mes
        async_track_time_interval(self.hass, self.async_update, interval=3600)
        # Actualización inicial
        await self.async_update()

    async def async_update(self, now=None):
        """Actualizar el estado del sensor."""
        now = dt_util.now()
        current_month = now.month
        if current_month != self._last_month:
            self._last_month = current_month
            # Aquí puedes personalizar el valor: número, texto, etc.
            # Por ejemplo, devolvemos el número
            self._state = current_month
            # También podrías tener atributos adicionales
            self._attr_extra_state_attributes = {
                "month_name": now.strftime("%B"),
                "year": now.year,
                "month_number": current_month
            }
            self.async_write_ha_state()
            _LOGGER.debug("Sensor actualizado: mes %s", current_month)
