# Midea Smart AC
Home Assistant Custom Integration for Midea Group (Hualing, Senville, Klimaire, AirCon, Century, Pridiom, Thermocore, Comfee, Alpine Home Air, Artel, Beko, Electrolux, Galactic, Idea, Inventor, Kaisai, Mitsui, Mr. Cool, Neoclima, Olimpia Splendid, Pioneer, QLIMA, Rotenso, Royal Clima, Qzen, Toshiba, Carrier, Goodman, Friedrich, Samsung, Kenmore, Trane, Lennox, LG and much more) Air Conditioners via LAN.

Tested with Home Assistant versions:
  * 2021.7.2
  * 2022.6.5
  * 2022.8.7

## Attention!!!
Version >= 0.2.4, The integration no longer supports YAML configuration. Devices must be configured via the GUI.

Version >= 0.1.27, The ENTITY ID of the climate devices has been changed. if you have any problem with an old entity being "unavailable", you should check whats the new ID name of the entity and change it in lovelace.

## Installation

### Install from HACS
[![Type](https://img.shields.io/badge/Type-Custom_Component-orange.svg)](https://github.com/mac-zhou/midea-ac-py) [![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

Search the HACS Store for ```midea_ac```

### Install manually
1. Clone this repo
2. Place the `custom_components/midea_ac` folder into your `custom_components` folder

## Configuration & Options

**Integration configuration:**  
Name | Description | Required | Example 
:--- | :--- | :--- | :---
**ID** | Device's appliance ID | Yes | 123456789012345
**Host** | Device's IP address | Yes| 192.168.1.100
**Port** | Device's port | Yes | 6444
**Token** | Device's token | Required for V3 devices | ACEDDA53831AE5DC... (Length 128)
**K1** | Device's K1 | Required for V3 devices | CFFA10FC... (Length 64)

**Integration options:**
Name | Description 
:--- | :--- 
**Temperature Step** | Step size for temperature set point.
**Include "Off" State** | Include "Off" as a valid device state.
**Use Fan-only Workaround** | Enable this option if device updates cause the device to turn on and switch to fan-only.
**Keep Last Known State** | Enable this option if there are too many `Unavailable` reports in the log.

## How to get configuration variables:
`midea-discover` can help you discover Midea devices from the LAN.
```zsh
pip3 install msmart
midea-discover
```

Basic Usage
```
Usage: midea-discover [OPTIONS]

  Discover Midea Devices and Get Device's info

Options:
  -d, --debug           Enable debug logging
  -c, --amount INTEGER  Number of broadcast packets, default is 1.
                        if you have many devices, you may change this value.
  -a, --account TEXT    Your email address for your Midea account.
  -p, --password TEXT   Your password for your Midea account.
  -i, --ip TEXT         IP address of Midea device. you can use:
                        - broadcasts don't work.
                        - just get one device's info.
                        - an error occurred.
  --help                Show this message and exit.
```

***Note***: 
- This component only supports devices with `'type': 'ac'` (air conditioner) and `'support': True` in the output. 
- V3 devices require `token` and `k1`.
- By default, `midea-discover` uses an open account for `MSmartHome` [[AppStore]](https://apps.apple.com/sg/app/midea-home/id1254346490) [[GooglePlay]](https://play.google.com/store/apps/details?id=com.midea.ai.overseas) to get Token and K1 (key) values. If you only get Token and K1 (key) with this account, others can't access your information. Don't use this account to login to the app and add devices, as this may reveal your information.

  It is recommended to use your own account to maximize privacy.
  ```zsh
  midea-discover -a YOUR_ACCOUNT -p YOUR_PASSWORD
  ```

## Buy me a cup of coffee

- [via Paypal](https://www.paypal.me/himaczhou)
- [via Bitcoin](bitcoin:3GAvud4ZcppF5xeTPEqF9FcX2buvTsi2Hy) (**3GAvud4ZcppF5xeTPEqF9FcX2buvTsi2Hy**)
- [via AliPay(支付宝)](https://i.loli.net/2020/05/08/nNSTAPUGDgX2sBe.png)
- [via WeChatPay(微信)](https://i.loli.net/2020/05/08/ouj6SdnVirDzRw9.jpg)

Your donation will make me work better for this project.
