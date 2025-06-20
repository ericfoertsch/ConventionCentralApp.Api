from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.repositories.entities.base import Base
from app.repositories.entities.person.person_id_entity import PersonIdEntity

class ConventionSeriesEntity(Base):
    __tablename__ = 'series'
    __table_args__ = {'schema': 'convention'}

    description = Column(Text)
    email = Column(Text)
    id_convention_series = Column(Integer, primary_key=True)
    id_image = Column(Integer)
    id_person = Column(Integer, ForeignKey('person.id.id_person'))
    id_video = Column(Integer)
    link = Column(Text)
    name = Column(Text)
    utc_begin = Column(TIMESTAMP(timezone=True))
    utc_timestamp = Column(TIMESTAMP(timezone=True))

    person = relationship(
        PersonIdEntity,
        foreign_keys=[id_person]
    )
