"""Componente Mes del Año para Home Assistant."""
from .const import DOMAIN


async def async_setup(hass, config):
    """Configuración legacy (configuration.yaml). No hace nada; usamos Config Flow."""
    return True


async def async_setup_entry(hass, entry):
    """Configurar la integración desde una entrada del Config Flow."""
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True


async def async_unload_entry(hass, entry):
    """Descargar la integración correctamente."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
