
English Version | [中文版](./README_CN.md#)

This is a custom component for Home Assistant to integrate the Midea Air Conditioners via the Local area network.

Tested with hass version 0.108.0

## Installation

### Install from HACS
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

Please Waiting...

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
**use_fan_only_workaround (Optional)** | Set this to true if you need to turn off device updates because they turn device on and to fan_only | true

**How to Get applianceId:**

- if you use android，you can use ```adb```，filter from log:
```shell
adb logcat | grep -i deviceid
```

- if you use iPhone，iPhone connects to macOS with a data cable and filters the applianceId from the console log

- If you do not have the above environment and conditions, you need to capture the air conditioner and save the files, after can be used [pcap-decrypt.py](./pcap-decrypt.py#) to Get. Remember to use the number, not hex string.

**Example configuration.yaml:**
* Single device
```yaml
climate:
  - platform: midea_ac
    host: 192.168.1.100
    id: 123456789012345
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