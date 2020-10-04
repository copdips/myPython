from sqlalchemy import Column, ForeignKey, Integer, String, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///sqlalchemy_many_to_many.db")
Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("left_id", Integer, ForeignKey("left.id")),
    Column("right_id", Integer, ForeignKey("right.id")),
)


class Parent(Base):
    __tablename__ = "left"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship("Child", secondary=association_table, backref="parents")

    def __repr__(self):
        return "Parent {}".format(self.name)


class Child(Base):
    __tablename__ = "right"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "Child {}".format(self.name)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

p1 = Parent(name="p1")
p2 = Parent(name="p2")
c1 = Child(name="c1")
c2 = Child(name="c2")

session.add(p1)
session.add(p2)
session.add(c1)
session.add(c2)

p1.children.append(c1)
p1.children.append(c2)
p2.children.append(c2)

session.commit()

print(p1.children)
#>>> [Child c1, Child c2]

print(p2.children)
#>>>  [Child c2]

# bad filter
print(session.query(Parent).filter(Child.name == "c1").all())
#>>>  [Parent p1, Parent p2]

# good filter
print(session.query(Parent).join(Parent.children).filter(Child.name == 'c1').all())
#>>>  [Parent p1]
