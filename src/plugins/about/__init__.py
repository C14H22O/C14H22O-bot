from nonebot import on_command
from nonebot import __version__
# from nonebot.adapters.qq.models import MessageKeyboard
# from nonebot.adapters.qq import Message
# from nonebot.adapters.qq import MessageSegment

nonebot_version = __version__
about = on_command("about", aliases={"关于"})

VERSION = "0.1.1"
ABOUT = f"""
C14H22O-bot v{VERSION}
Powered by Nonebot v{nonebot_version}"""


@about.handle()
async def _about():
    '''
    keyboard = MessageKeyboard.model_validate({
        "content": {
            "rows": [{"buttons": [
                {
                    "id": "1",
                    "render_data": {
                        "label": "Github",
                        "visited_label": "Github",
                        "style": 0
                    },
                    "action": {
                        "type": 0,
                        "permission": {
                            "type": 2,
                        },
                        "unsupport_tips": "客户端不支持",
                        "data": "https://github.com/C14H22O/C14H22O-bot",
                    }
                }

            ]},
            ]
        }
    })
    '''
    # await about.finish(Message([MessageSegment.text(ABOUT), MessageSegment.keyboard(keyboard)]))
    await about.finish(ABOUT)
