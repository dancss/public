from sqlalchemy import Column, Integer, String
from database import Base


class Task(Base):
    tb_name = "tasks"
    __tablename__ = tb_name

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
