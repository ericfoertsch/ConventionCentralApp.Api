from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ConventionSeries(BaseModel):
    id_convention_series: int
    description: Optional[str]
    email: Optional[str]
    id_image: Optional[int]
    id_person: Optional[int]
    id_video: Optional[int]
    link: Optional[str]
    name: Optional[str]
    utc_begin: Optional[datetime]
    utc_timestamp: Optional[datetime]

    class Config:
        from_attributes = True