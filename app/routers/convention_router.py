from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.repositories.convention_repository import get_all_conventions, get_convention
from app.models.convention.convention import Convention

router = APIRouter(
    prefix="/api/conventions",
    tags=["conventions"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_conventions(db: Session = Depends(get_db)):
    conventions = get_all_conventions(db)
    return conventions

# Test
@router.get("/{conventionId}", response_model=Convention)
def read_account(conventionId: int, db: Session = Depends(get_db)):
    return get_convention(conventionId, db)
