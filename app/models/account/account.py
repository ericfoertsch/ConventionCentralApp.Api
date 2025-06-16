from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime, timezone
from app.models.series.convention_series import ConventionSeries
from app.models.person.person import Person

class Account(BaseModel):
    id_account: int
    convention_series: Optional[ConventionSeries]
    person: Optional[Person]
    name: str
    description: str
    utc_begin: Optional[datetime]
    utc_end: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True

    @validator("utc_begin", "utc_end", pre=True)
    def make_datetime_timezone_aware(cls, v):
        if v is None:
            return None
        if isinstance(v, datetime) and v.tzinfo is None:
            return v.replace(tzinfo=timezone.utc)
        return v