from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship

from db.database import Base


class WorkType(Base):
    __tablename__ = "work_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)

    work_list = relationship("WorkData", back_populates="work_type")


class Work(Base):
    __tablename__ = "works"

    id = Column(Integer, primary_key=True)

    work_data_list = relationship("WorkData", back_populates="work")


class WorkData(Base):
    __tablename__ = "work_datas"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), index=True)
    released_date = Column(Date)
    revision = Column(Integer)
    is_valid = Column(Boolean)
    created_at = Column(DateTime)
    work_id = Column(Integer, ForeignKey("works.id"))
    work_type_id = Column(Integer, ForeignKey("work_types.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    work = relationship("Work", back_populates="work_data_list")
    work_type = relationship("WorkType", back_populates="work_list")
    user = relationship("User", back_populates="work_data_requests")