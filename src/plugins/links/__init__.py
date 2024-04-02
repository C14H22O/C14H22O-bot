from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.adapters.qq.models import MessageKeyboard, MessageMarkdown
from nonebot.adapters.qq import Message, MessageSegment

from .config import config, Config
from .utils import get_links_json

__plugin_meta__ = PluginMetadata(
    name="友链插件",
    description="输出添加其他人的友链",
    usage="使用 /友链 获取友情链接",
    type="application",
    config=Config,
    supported_adapters={"~qq"}
)

links = on_command("/links", aliases={"友链"})


@links.handle()
async def _links():
    markdown = MessageMarkdown.model_validate({
        "custom_template_id": config.markdown_text_template_id,
        "params": [
            {
                "key": "t1", "values": ["友链"]
            }
        ]
    })
    buttons = []
    links_config = config.links
    button_id = 1
    for link in links_config:
        buttons.append(get_links_json(button_id, link["name"], link["url"]))
        button_id += 1
    button_dict = {
        "content": {
            "rows": [
                {
                    "buttons": buttons
                }
            ]
        }
    }
    keyboard = MessageKeyboard.model_validate(button_dict)
    await links.finish(
        Message(
            [MessageSegment.markdown(markdown), MessageSegment.keyboard(keyboard)]
        )
    )
