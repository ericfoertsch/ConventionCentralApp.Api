from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Person(BaseModel):
    id_person: int
    email: Optional[str]
    description: Optional[str]
    utc_begin: Optional[datetime]

    class Config:
        from_attributes = True