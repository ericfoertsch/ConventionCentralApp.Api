from sqlalchemy.orm import Session
from app.models.entities.convention import ConventionRequest

def get_all_conventions(db: Session):
    return db.query(ConventionRequest).all()
