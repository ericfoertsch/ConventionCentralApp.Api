from sqlalchemy.orm import Session
from app.repositories.entities.vendor.vendor_id_entity import VendorIdEntity

def get_all_vendors(db: Session):
    return db.query(VendorIdEntity).all()
