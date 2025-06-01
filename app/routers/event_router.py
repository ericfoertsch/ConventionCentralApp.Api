from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.repositories.event_repository import get_event_settings, get_event
from app.repositories.vendor_repository import get_all_vendors
from app.models.event.event import Event

router = APIRouter(
    prefix="/api/event",
    tags=["event"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/settings/{event_id}")
def read_conventionss(event_id: int):#db: Session = Depends(get_db)):
    settings = get_event_settings(event_id)#db)
    return settings

@router.get("/{event_id}", response_model=Event)
def event(event_id: int, db: Session = Depends(get_db)):
    event = get_event(event_id)

    count = len(get_all_vendors(db))

    updated_metrics = event.metrics.copy(update={
        "vendor_count": count,
        "income": count * event.settings.vendor_cost
    })

    updated_event = event.copy(update={
        "metrics": updated_metrics
    })

    return updated_event
