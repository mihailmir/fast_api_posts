import typing

from pydantic import BaseModel, Field


class PostResponse(BaseModel):
    id_: int = Field(alias='id')


class PostModel(BaseModel):
    id_: int = Field(alias='id')
    text: str = Field()


class PostListResponse(BaseModel):
    posts: typing.List[PostModel]


