"""Config Flow para Mes del Año — configuración desde la interfaz de Home Assistant."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME

from .const import DOMAIN, DEFAULT_NAME


class MesDelAnoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Flujo de configuración para Mes del Año."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Paso inicial: formulario que muestra la UI."""
        errors = {}

        if user_input is not None:
            # Evitar duplicados: solo una entrada por nombre
            await self.async_set_unique_id(user_input[CONF_NAME].lower().replace(" ", "_"))
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )

        schema = vol.Schema({
            vol.Optional(CONF_NAME, default=DEFAULT_NAME): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
