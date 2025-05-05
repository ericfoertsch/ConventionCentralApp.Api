from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.repositories.vendor_repository import get_all_convention_requests

router = APIRouter(
    prefix="/api/vendors",
    tags=["vendors"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_convention_requests(db: Session = Depends(get_db)):
    requests = get_all_convention_requests(db)
    return requests
