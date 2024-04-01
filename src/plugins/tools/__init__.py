from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.adapters import Event
from nonebot.adapters.qq.models import MessageKeyboard, MessageMarkdown
from nonebot.adapters.qq import Message
from nonebot.adapters.qq import MessageSegment
from nonebot.permission import SUPERUSER

from .config import Config, config

__plugin_meta__ = PluginMetadata(
    name="工具插件",
    description="一些实用工具",
    usage="输入 /后门 以使用后门 :)",
    type="application",
    config=Config,
    supported_adapters={"~qq"}
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
    markdown = MessageMarkdown.model_validate({
        "custom_template_id": config.markdown_template_id,
        "params": [
            {
                "key": "t1", "values": ["要来逝一逝新功能吗"]
            }
        ]
    })
    keyboard = MessageKeyboard.model_validate({
        "content": {
            "rows": [
                {
                    "buttons": [
                        {
                            "id": "1",
                            "render_data": {
                                "label": "龙!",
                                "visited_label": "龙!"
                            },
                            "action": {
                                "type": 2,
                                "permission": {
                                    "type": 2
                                },
                                "enter": True,
                                "data": "/龙"
                            }
                        }
                    ]
                }
            ]
        }
    })
    await backdoor.finish(
        Message(
            [MessageSegment.markdown(markdown), MessageSegment.keyboard(keyboard)]
        )
    )
