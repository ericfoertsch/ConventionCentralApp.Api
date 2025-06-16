from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AccountIdEntity(Base):
    __tablename__ = 'id'
    __table_args__ = {'schema': 'account'}

    id_account = Column(Integer, primary_key=True)
    id_convention_series = Column(Integer)
    id_person = Column(Integer)
    name = Column(Text)
    description = Column(Text)
    utc_begin = Column(TIMESTAMP(timezone=True))
    utc_end = Column(TIMESTAMP(timezone=True))
