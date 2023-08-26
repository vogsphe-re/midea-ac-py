# Midea Smart AC
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

A Home Assistant custom integration to control Midea (and associated brands) air conditioners via LAN.

Midea is an OEM for many brands including:
Hualing, Senville, Klimaire, AirCon, Century, Pridiom, Thermocore, Comfee, Alpine Home Air, Artel, Beko, Electrolux, Galactic, Idea, Inventor, Kaisai, Mitsui, Mr. Cool, Neoclima, Olimpia Splendid, Pioneer, QLIMA, Rotenso, Royal Clima, Qzen, Toshiba, Carrier, Goodman, Friedrich, Samsung, Kenmore, Trane, Lennox, LG and more.

## Features
* Automatic device discovery and configuration via the GUI.
* Device capability detection. Only supported modes and functions are available.
* Support for sleep, eco, boost (turbo) and away (freeze protection) presets.
* Switch entity for device display.
* Binary sensor entity for device filter alert.
* Minimum and maximum target temperatures from device.

## Install Via HACS

1. Add this repository (https://github.com/mill1000/midea-ac-py) as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories/).
2. Install via HACS normally.

## Install Manually
1. Locate the `custom_components` directory in your Home Assistant configuration directory. It may need to be created.
2. Copy the `custom_components/midea_ac` directory into the `custom_components` directory.
3. Restart Home Assistant.

## Configuration & Options
Midea Smart AC is configured via the GUI. See [the HA docs](https://www.home-assistant.io/getting-started/integration/) for more details.

Devices can be automatically discovered and configured or manually configured.

### Automatic Configuration
For automatic configuration, select "Discover devices". Leave the host field blank to search the local network, or provide an IP/hostname to configure a specific device.

### Manual Configuration
For manual configuration, select "Configure manually". Enter the device ID, IP, and port. V3 devices require the token and key parameter. This information must be [acquired manually](#getting-device-info).

#### Integration Configuration
---
Name | Description | Required | Example 
:--- | :--- | :--- | :---
**ID** | Device ID | Yes | 123456789012345
**Host** | Device IP address | Yes| 192.168.1.100
**Port** | Device port | Yes | 6444
**Token** | Device token | For V3 devices | ACEDDA53831AE5DC... (Length 128)
**Key** | Device key | For V3 devices | CFFA10FC... (Length 64)

#### Integration Options
---
Name | Description 
:--- | :--- 
**Beep** | Enable beep on setting changes.
**Temperature Step** | Step size for temperature set point.
**Include "Off" State** | Include "Off" as a valid device state.
**Use Fan-only Workaround** | Enable this option if device updates cause the device to turn on and switch to fan-only.
**Keep Last Known State** | Enable this option if there are too many `Unavailable` reports in the log.

## Getting Device Info
Use the `midea-discover` command from msmart-ng to obtain device information.
```shell
pip install msmart-ng
midea-discover
```
_Note: Only devices of type 0xAC are supported. Ensure the supported property is True._

## Gratitude
This project is a fork of [mac-zhou/midea-ac-py](https://github.com/mac-zhou/midea-ac-py), and builds upon the work of:
* [NeoAcheron/midea-ac-py](https://github.com/NeoAcheron/midea-ac-py)
* [andersonshatch/midea-ac-py](https://github.com/andersonshatch/midea-ac-py)
* [yitsushi/midea-air-condition](https://github.com/yitsushi/midea-air-condition)