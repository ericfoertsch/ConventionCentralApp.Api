from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field, validator

from app.models.person.person import Person
from app.models.series.convention_series import ConventionSeries

class Convention(BaseModel):
    description: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    conventionId: int = Field(..., alias="id_convention")
    conventionSeriesId: Optional[int] = Field(None, alias="id_convention_series")
    imageId: Optional[int] = Field(None, alias="id_image")
    personId: int = Field(..., alias="id_person")
    statusId: int = Field(..., alias="id_status")
    venueId: Optional[int] = Field(None, alias="id_venue")
    videoId: Optional[int] = Field(None, alias="id_video")
    link: Optional[str] = Field(None)
    name: str = Field(...)
    begin: Optional[datetime] = Field(None, alias="utc_begin")
    end: Optional[datetime] = Field(None, alias="utc_end")
    timestamp: datetime = Field(..., alias="utc_timestamp")

    person: Optional[Person] = None
    conventionSeries: Optional[ConventionSeries] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        validate_by_name = True

    @validator("begin", "end", "timestamp", pre=True)
    def make_datetime_timezone_aware(cls, v):
        if v is None:
            return None
        if isinstance(v, datetime) and v.tzinfo is None:
            return v.replace(tzinfo=timezone.utc)
        return v
