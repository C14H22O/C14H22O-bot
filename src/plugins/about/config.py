from pydantic import BaseModel


class Config(BaseModel):
    markdown_template_id: str
