from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date, Table, Text
from sqlalchemy.orm import relationship

from db.database import Base


works_external_sites = Table(
    "works_external_sites",
    Base.metadata,
    Column("work_id", ForeignKey("works.id")),
    Column("external_site_id", ForeignKey("external_sites.id")),
    Column("id", Integer)
)

class Work(Base):
    __tablename__ = "works"

    id = Column(Integer, primary_key=True)

    work_data_list = relationship("WorkData", back_populates="work")
    external_sites = relationship("ExternalSite", secondary="works_external_sites", backref="Work")


class WorkType(Base):
    __tablename__ = "work_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)

    work_list = relationship("WorkData", back_populates="work_type")


class WorkData(Base):
    __tablename__ = "work_datas"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), index=True)
    description = Column(Text)
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


class ExternalSite(Base):
    __tablename__ = "external_sites"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), index=True)

    works = relationship("Work", secondary="works_external_sites", backref="ExternalSite")