from core.tools.provider.builtin.pahomqtt.tools.single_publish import SinglePublishTool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController

class PahoMqttProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: dict) -> None:
        SinglePublishTool()
        pass