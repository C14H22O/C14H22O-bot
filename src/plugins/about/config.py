from pydantic import BaseModel


class Config(BaseModel):
    keyboard_template_id: str
    markdown_template_id: str
