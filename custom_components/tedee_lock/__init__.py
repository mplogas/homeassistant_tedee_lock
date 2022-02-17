from homeassistant import core
from homeassistant.const import CONF_ACCESS_TOKEN
import logging
from datetime import timedelta
from pytedee import (
    TedeeClient,
    TedeeClientException
) 
from .lock import TedeeLock

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Tedee Lock platform."""
    try:
         #_LOGGER.error("Creds: %s, %s", config[CONF_ACCESS_TOKEN])
        tedee = TedeeClient(config[CONF_ACCESS_TOKEN])
    except TedeeClientException as exc:
        _LOGGER.error(exc)
        return
    available_locks = tedee.get_locks()
    _LOGGER.debug("available_locks: %s", available_locks)
    if not available_locks:
        # No locks found; abort setup routine.
        _LOGGER.info("No locks found in your account")
        return
    add_entities([TedeeLock(lock, tedee) for lock in available_locks], True)

# async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
#     """Set up the Tedee Lock component."""
#     # @TODO: Add setup code.
#     return True
