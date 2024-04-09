# dify_paho_mqtt_tool

安装方法，进入到 dify-api 的 docker 中。

```bash
pip install paho-mqtt
cd /app/api/core/tools/provider/builtin
apt-get update && \
apt-get install -y git && \
git clone https://github.com/yoyicue/dify_mqtt_tool.git pahomqtt
```

重启 dify-api 即可使用。

