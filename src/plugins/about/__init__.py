from nonebot import on_command
from nonebot import __version__
from nonebot import get_plugin_config
from nonebot.adapters.qq.models import MessageKeyboard, MessageMarkdown
from nonebot.adapters.qq import Message
from nonebot.adapters.qq import MessageSegment

from .config import Config

nonebot_version = __version__
about = on_command("about", aliases={"关于"})

VERSION = "0.1.2"
config = get_plugin_config(Config)


@about.handle()
async def _about():
    markdown = MessageMarkdown.model_validate({
        "custom_template_id": config.markdown_template_id,
        "params": [{"key": "bot_name", "values": ["C14H22O-bot"]},
                   {"key": "version", "values": [VERSION]},
                   {"key": "nonebot_version", "values": [nonebot_version]}
                   ]
    })
    keyboard = MessageKeyboard.model_validate({
        "id": config.keyboard_template_id
    })
    await about.finish(Message([MessageSegment.markdown(markdown), MessageSegment.keyboard(keyboard)]))
