from nonebot import on_command
from nonebot import get_plugin_config
from nonebot import __version__
from nonebot import require
require("nonebot_plugin_fishing")  # noqa
from nonebot_plugin_fishing.config import Config

nonebot_version = __version__
plugin_config = get_plugin_config(Config)
about = on_command("about", aliases={"关于"})

VERSION = "0.1.0"
ABOUT = f"""
C14H22O-bot v{VERSION}
Powered by Nonebot v{nonebot_version}
钓鱼频率限制: s{str(plugin_config.fishing_limit)}"""


@about.handle()
async def _about():
    await about.finish(ABOUT)
