Updated home-assistant component for hass version 0.108.0 and the "climate-1.0" changes.

## Installation

### HACS 
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
1. Search the HACS Store for Midea
2. Install the Midea Aircon component

### Manual
1. Clone this repo
2. Place the `custom_components/midea` folder into your `custom_components` folder

## Configuration

**Configuration variables:**  
key | description | example 
:--- | :--- | :---
**platform (Required)** | The platform name. | midea
**host (Required)** | Midea AC Device's IP Address. | 192.168.1.100
**id (Required)** | Midea AC Device's applianceId. | 123456789012345
**use_fan_only_workaround (Optional)** | Set this to true if you need to turn off device updates because they turn device on and to fan_only | true

**Example configuration.yaml:**
* Single device
```yaml
climate:
  - platform: midea
    host: 192.168.1.100
    id: 123456789012345
```
* Multiple device
```yaml
climate:
  - platform: midea
    host: 192.168.1.100
    id: 123456789012345
  - platform: midea
    host: 192.168.1.200
    id: 543210987654321
```
