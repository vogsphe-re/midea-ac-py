
美的空调的Home Assistant插件，通过局域网来控制设备。

Tested with hass version 0.108.0

## Installation (安装)

### Install from HACS (HACS商店安装)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

Please Waiting...

### Install manually (手工安装)
1. 克隆此仓库
2. 将 `custom_components/midea` 目录复制到你的 `custom_components` 目录下

## Configuration (配置)

**Configuration variables (配置变量说明):**  
参数 | 说明 | 示例 
:--- | :--- | :---
**platform (必填)** | 插件名称 | midea
**host (必填)** | 美的空调的IP地址 | 192.168.1.100
**id (必填)** | 美的空调的applianceId. | 123456789012345
**use_fan_only_workaround (可选)** | Set this to true if you need to turn off device updates because they turn device on and to fan_only | true

**How to Get applianceId(如何获取设备id):**

- 如果你使用安卓手机，可以使用adb logcat命令，从log中获取:
```shell
adb logcat | grep -i deviceid
```

- 如果你使用iPhone和macOS设备的话，可以将iPhone用数据线连到macOS，从控制台log中筛选applianceId

- 如果以上环境和条件，你都不具备的话，你需要对空调进行抓包，抓包后的文件可以用[pcap-decrypt.py](./pcap-decrypt.py#)从中获取，记得使用int部分的数字

**Example configuration.yaml (配置文件示例) :**
* 单台设备
```yaml
climate:
  - platform: midea
    host: 192.168.1.100
    id: 123456789012345
```
* 多台设备
```yaml
climate:
  - platform: midea
    host: 192.168.1.100
    id: 123456789012345
  - platform: midea
    host: 192.168.1.200
    id: 543210987654321
```

## 赞赏一下, 请我喝杯咖啡?

- [via Paypal](https://www.paypal.me/himaczhou)
- [via Bitcoin](bitcoin:3GAvud4ZcppF5xeTPEqF9FcX2buvTsi2Hy) (**3GAvud4ZcppF5xeTPEqF9FcX2buvTsi2Hy**)
- [via AliPay(支付宝)](https://i.loli.net/2020/05/08/nNSTAPUGDgX2sBe.png)
- [via WeChatPay(微信)](https://i.loli.net/2020/05/08/ouj6SdnVirDzRw9.jpg)
