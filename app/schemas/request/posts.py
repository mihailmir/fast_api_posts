from pydantic import BaseModel, Field


class PostCreateRequest(BaseModel):
    text: str = Field()

