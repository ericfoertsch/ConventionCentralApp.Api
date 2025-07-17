from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app.models.convention.convention import Convention
from app.models.convention.convention_series import ConventionSeries
from app.repositories.convention_repository import query_all_conventions, query_convention, query_all_convention_series

router = APIRouter(
    prefix="/api/conventions",
    tags=["conventions"]
)

@router.get("", response_model=List[Convention])
def get_all_conventions(db: Session = Depends(get_db)):
    return query_all_conventions(db)

@router.get("/series", response_model=List[ConventionSeries])
def get_all_convention_series(db: Session = Depends(get_db)):
    return query_all_convention_series(db)

@router.get("/{convention_id}", response_model=Convention)
def get_convention(convention_id: int, db: Session = Depends(get_db)):
    return query_convention(convention_id, db)

