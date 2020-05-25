**Example configuration.yaml:**

```yaml
climate:
  platform: midea_ac
  host: midea_device_ip_address
  id: midea_device_applianceId
```

**Configuration variables:**  
  
key | description | example 
:--- | :--- | :---
**platform (Required)** | The platform name. | midea_ac
**host (Required)** | Midea AC Device's IP Address. | 192.168.1.100
**id (Required)** | Midea AC Device's applianceId. | 123456789012345
**use_fan_only_workaround (Optional)** | Set this to true if you need to turn off device updates because they turn device on and to fan_only | true
