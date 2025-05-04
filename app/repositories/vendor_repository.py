from sqlalchemy.orm import Session
from app.models.vendor import ConventionRequest

def get_all_convention_requests(db: Session):
    return db.query(ConventionRequest).all()
