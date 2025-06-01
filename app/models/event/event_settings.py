from pydantic import BaseModel

class EventSettings(BaseModel):
    vendor_cost: float