from sqlalchemy import Column, String, Integer, Date, TypeDecorator

from base import Base


class DatetimeType(TypeDecorator):
    impl = Date

    def process_literal_param(self, value, dialect):
        return value.isoformat()


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date, DatetimeType())

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date