from sqlalchemy.orm import Session
from app.models.vendor import VendorRequest

def get_all_vendors(db: Session):
    return db.query(VendorRequest).all()
