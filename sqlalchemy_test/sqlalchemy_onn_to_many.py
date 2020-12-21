from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    # relationship takes the class Name as string, but not the real DB table name
    # with backref=person, address instance will have implicitly an attribute person
    # and don't need to delcare relationship at Address side neither
    all_address = relationship("Address", backref="person")


class Address(Base):
    __tablename__ = "address"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    person_id = Column(Integer, ForeignKey("person.id"))


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine("sqlite:///sqlalchemy_example.db")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

p1 = Person(name="p1")
p2 = Person(name="p2")
a1 = Address(street_name="a1", person=p1)
a2 = Address(street_name="a2", person_id=1)
session.add(p1)
session.add(p2)
session.add(a1)
session.add(a2)
session.commit()

a1 = session.query(Address).filter(Address.street_name == "a1").first()
a1.person.name

p1 = session.query(Person).filter_by(name="p1").first()
p1.all_address.street_name

p1.all_address
a3 = Address(street_name="a3")
a3.person
p1.all_addres.append(a3)
p1.all_addres
a3.person
session.commit()
