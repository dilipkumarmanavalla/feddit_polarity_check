from pydantic import BaseModel
from typing import List


class Comment(BaseModel):
    id: int
    username: str
    text: str
    created_at: int  # Unix epoch timestamp
    polarity: str


class Subfeddit(BaseModel):
    id: int
    username: str
    title: str
    description: str
    comments: List[Comment]
