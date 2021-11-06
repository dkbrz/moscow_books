import datetime as _dt
from typing import List
import pydantic as _pydantic


class Book(_pydantic.BaseModel):
    id: int = None
    title: str = None
    author: str = None


class Recommendation(_pydantic.BaseModel):
    id: int = None
    history: List[Book] = None
    recommendations: List[Book] = None

    class Config:
        orm_mode = True
