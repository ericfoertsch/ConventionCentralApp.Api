from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.repositories.entities.convention.convention_series_entity import ConventionSeriesEntity
from app.repositories.entities.person.person_id_entity import PersonIdEntity
from app.repositories.entities.base import Base

class AccountIdEntity(Base):
    __tablename__ = 'id'
    __table_args__ = {'schema': 'account'}

    id_account = Column(Integer, primary_key=True)
    id_convention_series = Column(Integer, ForeignKey('convention.series.id_convention_series'))
    id_person = Column(Integer, ForeignKey('person.id.id_person'))
    name = Column(Text)
    description = Column(Text)
    utc_begin = Column(TIMESTAMP(timezone=True))
    utc_end = Column(TIMESTAMP(timezone=True))

    convention_series = relationship(
        ConventionSeriesEntity,
        foreign_keys=[id_convention_series]
    )

    person = relationship(
        PersonIdEntity,
        foreign_keys=[id_person]
    )
