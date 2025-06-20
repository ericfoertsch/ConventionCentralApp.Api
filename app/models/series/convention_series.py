from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator, Field
from datetime import datetime, timezone
from app.models.person.person import Person

class ConventionSeries(BaseModel):
    conventionSeriesId: int = Field(..., alias="id_convention_series")
    description: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    imageId: Optional[int] = Field(None, alias="id_image")
    personId: Optional[int] = Field(None, alias="id_person")
    videoId: Optional[int] = Field(None, alias="id_video")
    link: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    begin: Optional[datetime] = Field(None, alias="utc_begin")
    timestamp: Optional[datetime] = Field(None, alias="utc_timestamp")

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
            return v.replace(tzinfo=timezone.utc)
        return v