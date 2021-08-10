
English Version | [中文版](./中文.md#)

This is a custom component for Home Assistant to integrate the Midea Air Conditioners via the Local area network.

Tested with hass version 0.110.2

## Attention!!!
Version >= 0.1.27, the device naming rules have changed.

## Installation

### Install from HACS
[![Type](https://img.shields.io/badge/Type-Custom_Component-orange.svg)](https://github.com/dlarrick/hass-kumo) [![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

Search the HACS Store for ```midea_ac```

### Install manually
1. Clone this repo
2. Place the `custom_components/midea_ac` folder into your `custom_components` folder

## Configuration

**Configuration variables:**  
key | description | example 
:--- | :--- | :---
**platform (Required)** | The platform name. | midea_ac
**host (Required)** | Midea AC Device's IP Address. | 192.168.1.100
**id (Required)** | Midea AC Device's applianceId. | 123456789012345
**token (Optional)** | Midea AC Device's token, V3 is required. | ACEDDA53831AE5DC...(Length 128)
**k1 (Optional)** | Midea AC Device's k1, V3 is required. | CFFA10FC...(Length 64)
**prompt_tone (Optional)** | Prompt Tone, default is true. | false
**keep_last_known_online_state (Optional)** | Set this to true if you see too many  `unavailable` in log. | true
**use_fan_only_workaround (Optional)** | Set this to true if you need to turn off device updates because they turn device on and to fan_only | true

**How to Get applianceId:**

- you can use command ```midea-discover``` to discover midea devices on the host in the same Local area network. Note: This component only supports devices with model 0xac (air conditioner) and words ```supported``` in the output.
    ```shell
    pip3 install msmart
    midea-discover
    ```

**How to Get Token and K1:**
- If your device's version is V2, please ignore.
- If you are in China, please install [meiju-gettoken-only-china.apk](https://media.githubusercontent.com/media/mac-zhou/LFS/main/meiju-gettoken-only-china.apk) first.
- If you are OverSea(Outside China), please install [Midea-Air-gettoken-only-oversea.apk](https://media.githubusercontent.com/media/mac-zhou/LFS/main/Midea-Air-gettoken-only-oversea.apk) first.
- I just changed the log level of APP, you can modify it yourself.
- Use `adb`，filter from logcat:
```shell
adb logcat | grep doKeyAgree
```
- You may need to be patient, it may take 5-30 minutes, you can reopen or relogin.

**Example configuration.yaml:**
* Single device
```yaml
climate:
  - platform: midea_ac
    host: 192.168.1.100
    id: 123456789012345
```
* V3 device
```yaml
climate:
  - platform: midea_ac
    host: 192.168.1.101
    id: 123456789012345
    token: ACEDDA53831AE5DC...(Length 128)
    k1: CFFA10FC...(Length 64)
```
* Multiple device
```yaml
climate:
  - platform: midea_ac
    host: 192.168.1.100
    id: 123456789012345
  - platform: midea_ac
    host: 192.168.1.200
    id: 543210987654321
```

## Buy me a cup of coffee to help maintain this project further?

- [via Paypal](https://www.paypal.me/himaczhou)
- [via Bitcoin](bitcoin:3GAvud4ZcppF5xeTPEqF9FcX2buvTsi2Hy) (**3GAvud4ZcppF5xeTPEqF9FcX2buvTsi2Hy**)
- [via AliPay(支付宝)](https://i.loli.net/2020/05/08/nNSTAPUGDgX2sBe.png)
- [via WeChatPay(微信)](https://i.loli.net/2020/05/08/ouj6SdnVirDzRw9.jpg)

Your donation will make me work better for this project.
