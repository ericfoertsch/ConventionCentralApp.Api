from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ConventionRequest(Base):
    __tablename__ = 'convention_request'
    __table_args__ = {'schema': 'vendor'}

    id_booth = Column(Integer, primary_key=True, index=True)
