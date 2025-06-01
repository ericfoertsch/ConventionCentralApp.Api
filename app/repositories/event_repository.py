from app.models.event.event_settings import EventSettings
from app.models.event.event_metrics import EventMetrics
from app.models.event.event import Event

def get_event_settings(event_id: int) -> EventSettings:
    return EventSettings(event_id=event_id, vendor_cost=300.00)

def get_event(event_id: int) -> Event:
    settings = EventSettings(vendor_cost=300.00)
    metrics = EventMetrics(vendor_count=0, income=0.00)

    return Event(event_id=event_id, settings=settings, metrics=metrics)