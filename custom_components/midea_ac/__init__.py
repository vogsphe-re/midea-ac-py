"""Integration for Midea Smart AC."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_HOST, CONF_ID, CONF_PORT, CONF_TOKEN
from homeassistant.helpers import device_registry as dr
from homeassistant.config_entries import ConfigEntry

import logging
from msmart.device import air_conditioning as ac
import voluptuous as vol

# Local consts
from .const import (
    DOMAIN,
    CONF_K1
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    """Set up a Midea AC device entry."""
    
    # Ensure the global data dict exists
    hass.data.setdefault(DOMAIN, {})

    # Get config data from entry
    config = config_entry.data

    # Attempt to get device from global data
    id = config.get(CONF_ID)
    device = hass.data[DOMAIN].get(id)

    # Construct a new device if necessary
    if device is None:
        # Construct the device
        id = config.get(CONF_ID)
        host = config.get(CONF_HOST)
        port = config.get(CONF_PORT)
        device = ac(host, int(id), port)

        # Configure token and k1 as needed
        token = config.get(CONF_TOKEN)
        k1 = config.get(CONF_K1)
        if token and k1:
            await hass.async_add_executor_job(device.authenticate, k1, token)

        hass.data[DOMAIN][id] = device

    # Create platform entries
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(config_entry, "climate"))
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(config_entry, "sensor"))

    return True
