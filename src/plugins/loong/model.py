from nonebot_plugin_orm import Model
from sqlalchemy.orm import Mapped, mapped_column


class LoongRecord(Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str]
    time: Mapped[int]
