from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Student(Base):
    __tablename__ = "rahul_new_student2"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    roll = Column(Integer)
    branch = Column(String)
