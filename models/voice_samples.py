from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class VoiceSample(Base):
    __tablename__= "voice_samples"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), index=True)
    path = Column(String(64))
    is_valid = Column(Boolean)