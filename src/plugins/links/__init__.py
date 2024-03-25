from nonebot import on_command
from nonebot.adapters.qq.models import MessageKeyboard, MessageMarkdown
from nonebot.adapters.qq import Message, MessageSegment

from .config import config
from .utils import get_links_json

links = on_command("/links", aliases={"友链"})
add_link_command = on_command("/add_link", aliases={"添加友链"})


@links.handle()
async def _links():
    markdown = MessageMarkdown.model_validate({
        "custom_template_id": config.markdown_link_template_id,
        "params": [
            {
                "key": ".t1", "values": ["友链"]
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
