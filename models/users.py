from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(100), unique=True, index=True)
    username = Column(String(100), index=True)
    hashed_password = Column(String(256))
    picture = Column(String(100), default="default.png")
    is_activated = Column(Boolean, default=False)
    created_at = Column(DateTime)

    person_data_requests = relationship("PersonData", back_populates="user")
    character_data_requests = relationship("CharacterData", back_populates="user")
    work_data_requests = relationship("WorkData", back_populates="user")
    franchise_data_requests = relationship("FranchiseData", back_populates="user")
