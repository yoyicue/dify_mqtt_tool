import json
from typing import Any, Union
import paho.mqtt.publish as publish

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool

class SinglePublishTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        """
        Paho Matt Publish Invoke
        publish.single("paho/test/topic", "payload", hostname="mqtt.eclipseprojects.io")
        https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html
        """

        message = tool_parameters.get('message')
        if not message:return self.create_text_message('Invalid parameter message')
        
        topic = tool_parameters.get('topic')
        if not topic:return self.create_text_message('Invalid parameter topic')
        
        
        host = self.runtime.credentials.get('hostname')
        port = int(self.runtime.credentials.get('port'))
        username = self.runtime.credentials.get('username')
        password = self.runtime.credentials.get('password')
        
        try:
            if username:
                publish.single(topic, message, hostname=host, port=port, auth={'username': username, 'password': password})
                return self.create_text_message(self.summary(user_id=user_id, content=json.dumps(message, ensure_ascii=False)))
            else:
                publish.single(topic, message, hostname=host, port=port)
                return self.create_text_message(self.summary(user_id=user_id, content=json.dumps(message, ensure_ascii=False)))
        except Exception as e:
            return self.create_text_message(f"Failed to send the message, error: {e}")
