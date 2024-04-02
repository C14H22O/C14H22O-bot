from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot_plugin_alconna.uniseg import Image, UniMessage
from nonebot.adapters.qq import Message, MessageSegment
from nonebot.adapters.qq.models import MessageKeyboard, MessageMarkdown
from nonebot.adapters.qq.exception import ActionFailed
from nonebot.log import logger

from .config import config, Config

import random

__plugin_meta__ = PluginMetadata(
    name="龙图插件",
    description="发送龙图",
    usage="输入 /龙 以获取龙图",
    type="application",
    config=Config,
    supported_adapters={"~qq"}
)

loong = on_command("龙")


async def choice_image() -> str:
    loong_data = config.loong_data.split("\n")
    return random.choice(loong_data)


@loong.handle()
async def _loong():
    image = await choice_image()
    image = image.replace("_", "%5F")
    logger.info(image)
    markdown = MessageMarkdown.model_validate(
        {
            "custom_template_id": config.markdown_text_template_id,
            "params": [
                {"key": "t1", "values": ["再来一张"]}
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
                                "label": "龙 + 1",
                                "visited_label": "龙 + 1",
                                "style": 1
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
    try:
        await loong.send(
            await UniMessage(Image(url=image)).export()
        )
        await loong.finish(
            Message(
                [MessageSegment.markdown(markdown), MessageSegment.keyboard(keyboard)]
            )
        )
    except ActionFailed as e:
        logger.exception(e)
        await loong.finish("发生了未知错误, 请联系🐔气人管理员")
