from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ConventionRequest(Base):
    __tablename__ = 'id'
    __table_args__ = {'schema': 'vendor'}

    description = Column(String(500), nullable=True)
    email = Column(String(255), nullable=True)
    capacity = Column(Integer, nullable=True)
    id_image = Column(Integer, nullable=True)
    id_person = Column(Integer, nullable=False)
    id_status = Column(Integer, nullable=True)
    id_vendor = Column(Integer, primary_key=True, nullable=False, index=True)
    id_video = Column(Integer, nullable=True)
    link = Column(String(500), nullable=True)
    name = Column(String(500), nullable=False)
    requests_open = Column(Boolean, nullable=True)
    utc_timestamp = Column(DateTime, nullable=False)