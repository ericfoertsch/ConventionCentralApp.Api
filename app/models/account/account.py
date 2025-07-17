from typing import Optional
from pydantic import BaseModel, validator, Field
from datetime import datetime, timezone
from app.models.convention.convention_series import ConventionSeries
from app.models.person.person import Person

class Account(BaseModel):
    accountId: int = Field(..., alias="id_account")
    conventionSeries: ConventionSeries = Field(..., alias="convention_series")
    person: Person = Field(...)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    begin: datetime = Field(..., alias="utc_begin")
    end: Optional[datetime] = Field(None, alias="utc_end")

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        validate_by_name = True

    @validator("begin", "end", pre=True)
    def make_datetime_timezone_aware(cls, v):
        if v is None:
            return None
        if isinstance(v, datetime) and v.tzinfo is None:
            return v.replace(tzinfo=timezone.utc)
        return v