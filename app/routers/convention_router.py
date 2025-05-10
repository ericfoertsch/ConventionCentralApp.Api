from fastapi import APIRouter#, Depends
# from sqlalchemy.orm import Session
# from app.db import SessionLocal
from app.repositories.convention_repository import get_all_conventions

router = APIRouter(
    prefix="/api/conventions",
    tags=["conventions"]
)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@router.get("/")
def read_conventionss():#db: Session = Depends(get_db)):
    conventions = get_all_conventions()#db)
    return conventions
