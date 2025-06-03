from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ConventionRequest(Base):
    __tablename__ = 'id'
    __table_args__ = {'schema': 'convention'}

    id_convention = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text)
    email = Column(Text)
    id_convention_series = Column(Integer)
    id_image = Column(Integer)
    id_person = Column(Integer)
    id_status = Column(Integer)
    id_venue = Column(Integer)
    id_video = Column(Integer)
    link = Column(Text)
    name = Column(Text)
    utc_begin = Column(DateTime(timezone=False))
    utc_end = Column(DateTime(timezone=False))
    utc_timestamp = Column(DateTime(timezone=False))