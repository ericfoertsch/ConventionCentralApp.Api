from pydantic import BaseModel

class EventSettings(BaseModel):
    event_id: int
    vendor_cost: float