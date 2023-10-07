from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

from db.database import Base


class Franchise(Base):
    __tablename__ = "franchises"

    id = Column(Integer, primary_key=True)

    franchise_data_list = relationship("FranchiseData", back_populates="franchise")


class FranchiseData(Base):
    __tablename__ = "franchise_data"

    id = Column(Integer, primary_key=True)
    name = Column(String(512), index=True)
    description = Column(Text)
    revision = Column(Integer)
    is_valid = Column(Boolean, default=False)
    created_at = Column(DateTime)
    franchise_id = Column(Integer, ForeignKey("franchises.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    franchise = relationship("Franchise", back_populates="franchise_data_list")
    user = relationship("User", back_populates="franchise_data_list")