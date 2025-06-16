from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.repositories.event_repository import get_event_settings, get_event
from app.repositories.account_repository import get_account
from app.models.account.account import Account

router = APIRouter(
    prefix="/api",
    tags=["account"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/account/{account_id}", response_model=Account)
def read_account(account_id: int, db: Session = Depends(get_db)):
    return get_account(account_id, db)
