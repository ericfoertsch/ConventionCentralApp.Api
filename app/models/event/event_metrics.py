from pydantic import BaseModel

class EventMetrics(BaseModel):
    event_id: int
    vendor_count: int
    income: float