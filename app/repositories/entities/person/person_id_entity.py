from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.repositories.entities.base import Base

class PersonIdEntity(Base):
    __tablename__ = 'id'
    __table_args__ = {'schema': 'person'}

    id_person = Column(Integer, primary_key=True)
    #id_image = Column(Integer, ForeignKey("image.id"))
    #id_status = Column(Integer, ForeignKey("status.id"))
    email = Column(Text)
    description = Column(Text)
    password_sha256 = Column(String(64), nullable=False)
    utc_begin = Column(TIMESTAMP(timezone=True))

    #image = relationship("ImageIdEntity")
    #status = relationship("StatusIdEntity")
