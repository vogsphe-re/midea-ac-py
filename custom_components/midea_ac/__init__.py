"""Integration for Midea Smart AC."""
from __future__ import annotations

from homeassistant.const import CONF_HOST, CONF_ID, CONF_PORT, CONF_TOKEN
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.typing import ConfigType

import logging
from msmart.device import air_conditioning as ac
import voluptuous as vol

# Local consts
from .const import (
    DOMAIN,
    CONF_K1,
    CONF_PROMPT_TONE,
    CONF_TEMP_STEP,
    CONF_INCLUDE_OFF_AS_STATE,
    CONF_USE_FAN_ONLY_WORKAROUND,
    CONF_KEEP_LAST_KNOWN_ONLINE_STATE
)

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_ID): cv.string,
                vol.Required(CONF_HOST): cv.string,
                vol.Optional(CONF_PORT, default=6444): vol.Coerce(int),
                vol.Optional(CONF_TOKEN, default=""): cv.string,
                vol.Optional(CONF_K1, default=""): cv.string,
                vol.Optional(CONF_PROMPT_TONE, default=True): vol.Coerce(bool),
                vol.Optional(CONF_TEMP_STEP, default=1.0): vol.Coerce(float),
                vol.Optional(CONF_INCLUDE_OFF_AS_STATE, default=True): vol.Coerce(bool),
                vol.Optional(CONF_USE_FAN_ONLY_WORKAROUND, default=False): vol.Coerce(bool),
                vol.Optional(CONF_KEEP_LAST_KNOWN_ONLINE_STATE, default=False): vol.Coerce(bool)
            }
        )
    },
    extra=vol.ALLOW_EXTRA
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the connection to Midea device."""

    # Fetch domain config
    config = config[DOMAIN]

    # Construct the device
    id = config.get(CONF_ID)
    host = config.get(CONF_HOST)
    port = config.get(CONF_PORT)
    device = ac(host, int(id), port)

    # Configure token and k1 as needed
    token = config.get(CONF_TOKEN)
    k1 = config.get(CONF_K1)
    if token and k1:
        device._protocol_version = 3
        device._token = bytearray.fromhex(token)
        device._key = bytearray.fromhex(k1)
        device._lan_service._token = device._token
        device._lan_service._key = device._key

    # Save the device for our platforms
    hass.data[DOMAIN] = {
        "device": device
    }

    # Load the platforms
    hass.helpers.discovery.load_platform("sensor", DOMAIN, {}, config)
    hass.helpers.discovery.load_platform("climate", DOMAIN, {}, config)

    return True
