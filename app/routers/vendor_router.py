from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.repositories.vendor_repository import get_all_vendors

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
def read_vendors(db: Session = Depends(get_db)):
    vendors = get_all_vendors(db)
    return vendors
