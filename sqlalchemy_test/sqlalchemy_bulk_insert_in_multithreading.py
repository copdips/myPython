from multiprocessing.dummy import Pool as ThreadPool
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    all_address = relationship("Address", backref="person")


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"))


def thread_worker(number):
    print("thread {}".format(number))
    session = Session()
    people = [{"name": str(uuid4())} for _ in range(100)]
    session.bulk_insert_mappings(Person, people)
    session.commit()


def work_parallel(numbers, thread_number=4):
    pool = ThreadPool(thread_number)
    pool.map(thread_worker, numbers)


if __name__ == "__main__":
    engine = create_engine("postgresql+psycopg2://postgres@localhost:5432")
    Base.metadata.bind = engine
    Base.metadata.drop_all()
    Base.metadata.create_all()
    DBSession = sessionmaker(bind=engine)
    Session = scoped_session(DBSession)

    session = Session()

    print("before insert: {}".format(len(session.query(Person).all())))
    numbers = [i for i in range(200)]
    work_parallel(numbers, 8)
    print("after insert: {}".format(len(session.query(Person).all())))

    Session.remove()
