from nonebot import on_command
from nonebot.adapters import Event
from nonebot.permission import SUPERUSER

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
    await backdoor.finish("To do.")
