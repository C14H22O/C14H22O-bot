from nonebot import on_command
from nonebot.adapters import Event

user_id = on_command("get_user_id")
backdoor = on_command("backdoor")


@user_id.handle()
async def _user_id(event: Event):
    user_id.finish(event.get_user_id())
