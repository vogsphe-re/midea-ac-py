"""Platform for sensor integration."""
from __future__ import annotations

import logging

from homeassistant.components.sensor import (SensorDeviceClass, SensorEntity,
                                             SensorStateClass)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import MideaCoordinatorEntity, MideaDeviceUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    add_entities: AddEntitiesCallback,
) -> None:
    """Setup the sensor platform for Midea Smart AC."""

    _LOGGER.info("Setting up sensor platform.")

    # Fetch coordinator from global data
    coordinator = hass.data[DOMAIN][config_entry.entry_id]

    # Create sensor entities from device
    add_entities([
        MideaTemperatureSensor(coordinator, "indoor_temperature"),
        MideaTemperatureSensor(coordinator, "outdoor_temperature"),
    ])


class MideaTemperatureSensor(MideaCoordinatorEntity, SensorEntity):
    """Temperature sensor for Midea AC."""

    def __init__(self,
                 coordinator: MideaDeviceUpdateCoordinator,
                 prop: str) -> None:
        MideaCoordinatorEntity.__init__(self, coordinator)

        self._prop = prop

    @property
    def device_info(self) -> dict:
        return {
            "identifiers": {
                (DOMAIN, self._device.id)
            },
        }

    @property
    def name(self) -> str:
        return f"{DOMAIN}_{self._prop}_{self._device.id}"

    @property
    def unique_id(self) -> str:
        return f"{self._device.id}-{self._prop}"

    @property
    def available(self) -> bool:
        """Check entity availablity."""
        # Sensor is unavailable if device is offline
        if not super().available:
            return False

        # Sensor is unavailable if value is None
        return self.native_value is not None

    @property
    def device_class(self) -> str:
        return SensorDeviceClass.TEMPERATURE

    @property
    def state_class(self) -> str:
        return SensorStateClass.MEASUREMENT

    @property
    def native_unit_of_measurement(self) -> str:
        return TEMP_CELSIUS

    @property
    def native_value(self) -> float | None:
        """Return the current native value."""
        return getattr(self._device, self._prop, None)
