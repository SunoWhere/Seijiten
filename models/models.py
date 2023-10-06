from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(100), unique=True, index=True)
    username = Column(String(100), index=True)
    hashed_password = Column(String(256))
    is_activated = Column(Boolean, default=False)
    created_at = Column(DateTime)

    seiyuu_data_requests = relationship("SeiyuuData", back_populates="user")

class Seiyuu(Base):
    __tablename__ = "seiyuus"

    id = Column(Integer, primary_key = True)

    seiyuu_data_list = relationship("SeiyuuData", back_populates="seiyuu")


class SeiyuuData(Base):
    __tablename__ = "seiyuu_datas"

    id = Column(Integer, primary_key = True)
    first_name = Column(String(100), index=True)
    last_name = Column(String(100), index=True)
    picture = Column(String(100), default="default.png")
    revision = Column(Integer)
    is_valid = Column(Boolean, default=False)
    created_at = Column(DateTime)
    seiyuu_id = Column(Integer, ForeignKey("seiyuus.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    seiyuu = relationship("Seiyuu", back_populates="seiyuu_data_list")
    user = relationship("User", back_populates="seiyuu_data_requests")
