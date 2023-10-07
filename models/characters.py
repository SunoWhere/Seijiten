from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

from db.database import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key = True)

    character_data_list = relationship("CharacterData", back_populates="character")


class CharacterData(Base):
    __tablename__ = "character_datas"

    id = Column(Integer, primary_key = True)
    full_name = Column(String(512), index=True)
    desciption = Column(Text)
    picture = Column(String(100), default="default.png")
    revision = Column(Integer)
    is_valid = Column(Boolean, default=False)
    created_at = Column(DateTime)
    character_id = Column(Integer, ForeignKey("characters.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    character = relationship("Character", back_populates="character_data_list")
    user = relationship("User", back_populates="character_data_requests")