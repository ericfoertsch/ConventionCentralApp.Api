from pydantic import BaseModel

class EventMetrics(BaseModel):
    vendor_count: int
    income: float