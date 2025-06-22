from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.convention.convention import Convention
from app.repositories.entities.convention.convention_id_entity import ConventionIdEntity

def get_all_conventions(db: Session) -> List[Convention]:
    entities = db.query(ConventionIdEntity).all()
    return [Convention.model_validate(e) for e in entities]

def get_convention(conventionId: int, db: Session) -> Convention:
    entity = db.query(ConventionIdEntity).filter(
        ConventionIdEntity.id_convention == conventionId
    ).first()

    if not entity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Convention with ID {conventionId} not found"
        )

    return Convention.model_validate(entity)
