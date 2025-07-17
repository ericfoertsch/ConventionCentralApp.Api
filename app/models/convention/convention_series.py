from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field, validator

from app.models.person.person import Person

class ConventionSeries(BaseModel):
    conventionSeriesId: int = Field(..., alias="id_convention_series")
    name: str = Field(...)
    timestamp: datetime = Field(..., alias="utc_timestamp")
    description: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    imageId: Optional[int] = Field(None, alias="id_image")
    personId: int = Field(..., alias="id_person")  # Required in this version
    videoId: Optional[int] = Field(None, alias="id_video")
    link: Optional[str] = Field(None)
    begin: Optional[datetime] = Field(None, alias="utc_begin")
    
    person: Optional[Person] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        validate_by_name = True

    @validator("begin", "timestamp", pre=True)
    def make_datetime_timezone_aware(cls, v):
        if v is None:
            return None
        if isinstance(v, datetime) and v.tzinfo is None:
            v = v.replace(tzinfo=timezone.utc)
        return v
