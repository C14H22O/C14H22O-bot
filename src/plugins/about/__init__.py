from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot import __version__
from nonebot.adapters.qq.models import MessageKeyboard, MessageMarkdown
from nonebot.adapters.qq import Message
from nonebot.adapters.qq import MessageSegment

from .config import Config, config

__plugin_meta__ = PluginMetadata(
    name="关于插件",
    description="关于 C14H22O-bot",
    usage="输入 /关于 获取机器人关于信息",
    type="application",
    config=Config,
    supported_adapters={"~qq"}
)

nonebot_version = __version__
about = on_command("about", aliases={"关于"})

VERSION = "0.1.2"
URL = "https://github.com/C14H22O/C14H22O-bot"


@about.handle()
async def _about():
    markdown = MessageMarkdown.model_validate(
        {
            "custom_template_id": config.markdown_template_id,
            "params": [
                {"key": "bot_name", "values": ["C14H22O-bot"]},
                {"key": "version", "values": [VERSION]},
                {"key": "nonebot_version", "values": [nonebot_version]}
            ]
        }
    )
    keyboard = MessageKeyboard.model_validate({
        "content": {
            "rows": [
                {
                    "buttons": [
                        {
                            "id": "1",
                            "render_data": {
                                "label": "Github",
                                "visited_label": "Github"
                            },
                            "action": {
                                "type": 0,
                                "permission": {
                                    "type": 2
                                },
                                "data": URL
                            }
                        },
                        {
                            "id": "2",
                            "render_data": {
                                "label": "友链",
                                "visited_label": "友链"
                            },
                            "action": {
                                "type": 2,
                                "permission": {
                                    "type": 2
                                },
                                "enter": True,
                                "data": "/友链"
                            }
                        }
                    ]
                }
            ]
        }
    })
    await about.finish(
        Message(
            [MessageSegment.markdown(markdown), MessageSegment.keyboard(keyboard)]
        )
    )
