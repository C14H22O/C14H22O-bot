from nonebot import on_command
from nonebot.adapters.qq import MessageSegment
from nonebot.adapters.qq.exception import ActionFailed
from nonebot.log import logger

from .config import config

import random

loong = on_command("龙")


async def choice_image() -> str:
    loong_data = config.loong_data.split("\n")
    return random.choice(loong_data)


@loong.handle()
async def _loong():
    await loong.send("正在选取龙图…")
    image = await choice_image()
    image = image.replace('\n', '')
    logger.info(image)
    try:
        await loong.finish(MessageSegment.image(image))
    except ActionFailed as e:
        logger.exception(e)
        await loong.finish("发生了未知错误, 请联系🐔气人管理员")
