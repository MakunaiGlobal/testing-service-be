from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    posts: Optional[List['Post']] = []

class Post(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    author_name: str
    created_at: datetime
    updated_at: Optional[datetime] = None