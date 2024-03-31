from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.adapters import Event
from nonebot.permission import SUPERUSER

__plugin_meta__ = PluginMetadata(
    name="工具插件",
    description="一些实用工具",
    usage="输入 /后门 以使用后门 :)",
    type="application",
    config=None,
    supported_adapters=None
)

user_id = on_command("get_user_id")
backdoor = on_command(
    "backdoor",
    aliases={"后门"},
    permission=SUPERUSER
)


@user_id.handle()
async def _user_id(event: Event):
    await user_id.finish(event.get_user_id())


@backdoor.handle()
async def _backdoor():
    await backdoor.finish("To do.")
