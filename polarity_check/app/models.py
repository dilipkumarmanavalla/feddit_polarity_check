"""
Models module for the Polarity Check data validation and serialization.
"""

from typing import List

# BaseModel for defining the data models
from pydantic import BaseModel


class Comment(BaseModel):
    """
    Comments Data Model
    """
    id: int
    username: str
    text: str
    created_at: int
    polarity: str


class Subfeddit(BaseModel):
    """
    Subfeddit Data Model
    """
    id: int
    username: str
    title: str
    description: str
    comments: List[Comment]
