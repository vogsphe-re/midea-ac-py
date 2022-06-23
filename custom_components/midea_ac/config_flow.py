"""Config flow for Midea Smart AC."""

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_ID, CONF_PORT, CONF_TOKEN
import homeassistant.helpers.config_validation as cv

import voluptuous as vol
from msmart.device import air_conditioning as ac

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

class MideaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, config):
        errors = {}
        if config is not None:
            # Fetch ID from the user
            id = config.get(CONF_ID)

            # Set the unique ID and allow updates to host and port
            await self.async_set_unique_id(id)
            self._abort_if_unique_id_configured(
                updates={CONF_HOST: config.get(CONF_HOST), CONF_PORT: config.get(CONF_PORT)})

            # Attempt to verify the user settings
            device = await self._test_connection(config)

            if device:
                # Save the device into global data
                self.hass.data.setdefault(DOMAIN, {})
                self.hass.data[DOMAIN][id] = device
                # Create a setup entry with all the config data
                return self.async_create_entry(title=device.name, data=config)
            else:
                errors["base"] = "connection"

        data_schema = vol.Schema({
            vol.Required(CONF_ID): cv.string,
            vol.Required(CONF_HOST): cv.string,
            vol.Optional(CONF_PORT, default=6444): cv.port,
            vol.Optional(CONF_TOKEN, default=""): cv.string,
            vol.Optional(CONF_K1, default=""): cv.string,
            vol.Optional(CONF_PROMPT_TONE, default=True): cv.boolean,
            vol.Optional(CONF_TEMP_STEP, default=1.0): vol.All(vol.Coerce(float), vol.Range(min=0.5, max=5)),
            vol.Optional(CONF_INCLUDE_OFF_AS_STATE, default=True): cv.boolean,
            vol.Optional(CONF_USE_FAN_ONLY_WORKAROUND, default=False):  cv.boolean,
            vol.Optional(CONF_KEEP_LAST_KNOWN_ONLINE_STATE, default=False):  cv.boolean
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)

    async def _test_connection(self, config):
        # Construct the device
        id = config.get(CONF_ID)
        host = config.get(CONF_HOST)
        port = config.get(CONF_PORT)
        device = ac(host, int(id), port)

        # Configure token and k1 as needed
        token = config.get(CONF_TOKEN)
        k1 = config.get(CONF_K1)
        if token and k1:
            success = await self.hass.async_add_executor_job(device.authenticate, k1, token)
        else:
            await self.hass.async_add_executor_job(device.refresh)
            success = device.online

        return device if success else None
