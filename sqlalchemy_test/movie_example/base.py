from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
engine = create_engine("sqlite:///moive_example.db")
Session = sessionmaker(bind=engine)

Base = declarative_base()


# sub_vm_association = Table(
#     "sub_vm", Base.metadata,
#     Column("sub_vmname", String, ForeignKey("sub.vmname")),
#     Column("vm_vmname", String, ForeignKey("vm.vmname"))
# )


class Sub(Base):
    __tablename__ = "sub"

    subid = Column(String, primary_key=True)
    subname = Column(String)
    vmname = Column(String)
    # vms = relationship("VM",  secondary=sub_vm_association)
    eco = Column(String)


class VM(Base):
    __tablename__ = "vm"

    vmid = Column(String, primary_key=True)
    # subid = Column(String, ForeignKey("sub.subid"))
    vmname = Column(String)
    # vmname = relationship("Sub", backref="vm")
