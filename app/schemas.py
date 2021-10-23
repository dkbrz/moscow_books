import datetime as _dt
from typing import List
import pydantic as _pydantic


class Recommendation(_pydantic.BaseModel):
    id: int = None
    history: list = None
    recommendations: list = None

    class Config:
        orm_mode = True
