from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from app.repositories.entities.convention.convention_series_entity import ConventionSeriesEntity
from app.repositories.entities.base import Base

class ConventionIdEntity(Base):
    __tablename__ = 'id'
    __table_args__ = {'schema': 'convention'}

    description = Column(Text)
    email = Column(Text)
    id_convention = Column(Integer, primary_key=True)
    id_convention_series = Column(Integer, ForeignKey('convention.series.id_convention_series'))
    id_image = Column(Integer)
    id_person = Column(Integer)
    id_status = Column(Integer)
    id_venue = Column(Integer)
    id_video = Column(Integer)
    link = Column(Text)
    name = Column(Text)
    utc_begin = Column(TIMESTAMP(timezone=True))
    utc_end = Column(TIMESTAMP(timezone=True))
    utc_timestamp = Column(TIMESTAMP(timezone=True))

    convention_series = relationship(
        ConventionSeriesEntity,
        foreign_keys=[id_convention_series]
    )
