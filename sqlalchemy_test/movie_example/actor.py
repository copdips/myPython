from base import Base
from sqlalchemy import Column, Date, Integer, String


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
