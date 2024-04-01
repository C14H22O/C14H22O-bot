from nonebot import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    markdown_link_template_id: str


config = get_plugin_config(Config)
