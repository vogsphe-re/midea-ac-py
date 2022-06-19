"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
    RestoreSensor,
)
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

import logging

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Setup the sensor platform for Midea Smart AC."""

    # Only setup via discovery
    if discovery_info is None:
        return

    _LOGGER.info("Setting up sensor platform.")

    device = hass.data[DOMAIN]["device"]

    add_entities([
        MideaTemperatureSensor(
            device, "Indoor Temperature", "indoor_temperature"),
        MideaTemperatureSensor(
            device, "Outdoor Temperature", "outdoor_temperature"),
    ])


class MideaTemperatureSensor(RestoreSensor):
    """Temperature sensor for Midea AC."""

    def __init__(self, device, friendly_name, prop):
        self._device = device
        self._name = friendly_name
        self._prop = prop

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()

        if (last_sensor_data := await self.async_get_last_sensor_data()) is None:
            return

        # Restore previous native value
        self._native_value = last_sensor_data.native_value

    async def async_update(self):
        # Grab the property from the device
        self._native_value = getattr(self._device, self._prop)

    @property
    def name(self) -> str:
        return f"{self._name}"

    @property
    def unique_id(self) -> str:
        return f"{self._device.id}-{self._prop}"

    @property
    def available(self) -> bool:
        return self._device.online

    @property
    def device_class(self):
        return SensorDeviceClass.TEMPERATURE

    @property
    def state_class(self):
        return SensorStateClass.MEASUREMENT

    @property
    def native_unit_of_measurement(self):
        return TEMP_CELSIUS

    @property
    def native_value(self):
        return self._native_value
