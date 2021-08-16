This is a custom component for Home Assistant to integrate the Midea Air Conditioners via the Local area network.

Tested with hass version 0.110.2

## Attention!!!
Version >= 0.1.27, The ENTITY ID of the climate devices has been changed. if you have any problem with an old entity being "unavailable", you should check whats the new ID name of the entity and change it in lovlace.

## Installation

### Install from HACS
[![Type](https://img.shields.io/badge/Type-Custom_Component-orange.svg)](https://github.com/mac-zhou/midea-ac-py) [![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

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
**temp_step (Optional)** | Step size for temperature set point, default is 1.0 | 0.5
**prompt_tone (Optional)** | Prompt Tone, default is true. | false
**keep_last_known_online_state (Optional)** | Set this to true if you see too many  `unavailable` in log. | true
**use_fan_only_workaround (Optional)** | Set this to true if you need to turn off device updates because they turn device on and to fan_only | true

**Example configuration.yaml:**
```yaml
climate:
  - platform: midea_ac
    host: 192.168.1.100
    id: 123456789012345
    # v3 need token and id
    # token: ACEDDA53831AE5DC...(Length 128)
    # k1: CFFA10FC...(Length 64)
```

## How to Get ApplianceId:
- Use command `midea-discover` to discover midea devices on the host in the same LAN. 
  Note: This component only supports devices with model 0xac (air conditioner) and words `supported` in the output. V3(8370) need to get token and k1.
    ```shell
    pip3 install msmart
    midea-discover
    ```

## How to Get Token and K1:
- If your device's version is V2, please ignore.
- Use Android phone or emulator (which can use bridge, such as [LDPlayer](https://en.ldplayer.net/?from=en)) `must be in the same LAN as the device`.
- If you are in China, please install [meiju-gettoken-only-china.apk](https://www.mediafire.com/file/ma4exquqa5rhy8f/meiju-gettoken-only-china.apk/file).
- If you are OverSea(Outside China), please install [Midea-Air-gettoken-only-oversea.apk](https://www.mediafire.com/file/g38vhkdf4r3icbv/Midea-Air-gettoken-only-oversea.apk/file).
- **I just changed the log level of APP, you can modify it yourself**.
- You may need to be patient, it may take 5-30 minutes, you can reopen or relogin APP.
- Use `adb`，filter from logcat:

  ***shell:***
  ```shell
  adb logcat | grep doKeyAgree
  ```
  ***cmd:***
  ```cmd
  adb logcat | findstr doKeyAgree
  ```


## Buy me a cup of coffee

- [via Paypal](https://www.paypal.me/himaczhou)
- [via Bitcoin](bitcoin:3GAvud4ZcppF5xeTPEqF9FcX2buvTsi2Hy) (**3GAvud4ZcppF5xeTPEqF9FcX2buvTsi2Hy**)
- [via AliPay(支付宝)](https://i.loli.net/2020/05/08/nNSTAPUGDgX2sBe.png)
- [via WeChatPay(微信)](https://i.loli.net/2020/05/08/ouj6SdnVirDzRw9.jpg)

Your donation will make me work better for this project.
