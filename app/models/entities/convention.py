from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ConventionRequest(Base):
    # __tablename__ = 'id'
    # __table_args__ = {'schema': 'vendor'}

    id = Column(Integer, nullable=True)
    name = Column(String(500), nullable=False)
    description = Column(String(500), nullable=True)
    logo = Column(String(255), nullable=True)