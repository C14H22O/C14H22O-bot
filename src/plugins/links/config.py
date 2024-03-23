from typing import List

from pydantic import BaseModel
from nonebot import get_plugin_config


class Config(BaseModel):
    markdown_template_id: str
    links: List


config = get_plugin_config(Config)
