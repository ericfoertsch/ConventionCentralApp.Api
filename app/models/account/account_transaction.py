from typing import Optional
from pydantic import BaseModel, validator, Field
from datetime import datetime, timezone
from app.models.person.person import Person
from decimal import Decimal

class AccountTransaction(BaseModel):
    temp_id: int
    # accountId: int = Field(..., alias="id_account")
    # accountReceiving: Optional[int] = Field(None, alias="id_account_receiving")
    # admittenceId: Optional[int] = Field(None, alias="id_admittence")
    # personId: Optional[int] = Field(None, alias="id_person")
    # personReceivingId: Optional[int] = Field(None, alias="id_person_receiving")
    # name: Optional[str] = Field(None)
    # description: Optional[str] = Field(None)
    # amount: Optional[Decimal] = Field(None)
    # timestamp: Optional[datetime] = Field(None, alias="utc_timestamp")

    # person: Optional[Person] = None
    # personReceiving: Optional[Person] = None

    # class Config:
    #     arbitrary_types_allowed = True
    #     from_attributes = True
    #     allow_population_by_field_name = True

    # @validator("timestamp", pre=True)
    # def ensure_utc_timezone(cls, v):
    #     if v is None:
    #         return None
    #     if isinstance(v, datetime):
    #         if v.tzinfo is None:
    #             v = v.replace(tzinfo=timezone.utc)
    #         return v.astimezone(timezone.utc)
    #     return v
