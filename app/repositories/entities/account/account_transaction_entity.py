from sqlalchemy import Column, Integer, Text, Double, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from app.repositories.entities.base import Base

class AccountTransactionEntity(Base):
    __tablename__ = 'transaction'
    __table_args__ = {'schema': 'account'}

    id_account = Column(Integer)
    id_account_receiving = Column(Integer)
    id_admittence = Column(Integer)
    id_person = Column(Integer)
    id_person_receiving = Column(Integer)
    name = Column(Text)
    description = Column(Text)
    amount = Column(Double)
    utc_timestamp = Column(TIMESTAMP(timezone=True))
