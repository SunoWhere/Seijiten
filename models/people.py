from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date, Text
from sqlalchemy.orm import relationship

from db.database import Base


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key = True)

    person_data_list = relationship("PersonData", back_populates="person")


class PersonData(Base):
    __tablename__ = "person_datas"

    id = Column(Integer, primary_key = True)
    first_name = Column(String(100), index=True)
    last_name = Column(String(100), index=True)
    description = Column(Text)
    picture = Column(String(100), default="default.png")
    birthdate = Column(Date)
    revision = Column(Integer)
    is_valid = Column(Boolean, default=False)
    created_at = Column(DateTime)
    people_id = Column(Integer, ForeignKey("people.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    person = relationship("Person", back_populates="person_data_list")
    user = relationship("User", back_populates="person_data_requests")
