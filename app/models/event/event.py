from pydantic import BaseModel
from app.models.event.event_settings import EventSettings
from app.models.event.event_metrics import EventMetrics

class Event(BaseModel):
    event_id: int
    settings: EventSettings
    metrics: EventMetrics

    class Config:
        arbitrary_types_allowed = True