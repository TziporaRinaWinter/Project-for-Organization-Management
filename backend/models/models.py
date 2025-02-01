from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Table, Float
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum

from models.schema import WidowSchema, AddressSchema, OrphanSchema, RelativeSchema, BankAccountSchema, SchoolSchema, EventSchema


Base = declarative_base()

class AgeGroupEnum(PyEnum):
    KINDERGARTEN = "גן"
    ELEMENTARY = "בית ספר יסודי"
    HIGH_SCHOOL = "סמינר"
    CHEDER = "חיידר"
    SMALL_YESHIVA = "ישיבה קטנה"
    LARGE_YESHIVA = "ישיבה גדולה"

event_widow_association = Table('event_widow', Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id')),
    Column('widow_id', Integer, ForeignKey('widows.id'))
)

event_orphan_association = Table('event_orphan', Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id')),
    Column('orphan_id', Integer, ForeignKey('orphans.id'))
)


class Widow(Base):
    __tablename__ = 'widows'
    
    id = Column(Integer, primary_key=True)
    identity_number = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    home_phone = Column(String)
    mobile_phone = Column(String)
    email = Column(String)
    birth_date = Column(Date)
    hebrew_birth_date = Column(String)
    widowhood_date = Column(Date)
    num_of_unmarried_children = Column(Integer)
    num_of_minor_children = Column(Integer)
    bank_account_id = Column(Integer, ForeignKey('bank_accounts.id'))
    address_id = Column(Integer, ForeignKey('addresses.id'))
    
    bank_account = relationship("BankAccount", back_populates="widow")
    address = relationship("Address", back_populates="widow")
    orphans = relationship("Orphan", back_populates="mother")
    relatives = relationship("Relative", back_populates="widow")
    events = relationship("Event", secondary=event_widow_association, back_populates="widows")

    @classmethod
    def schema(cls):
        return WidowSchema


class Orphan(Base):
    __tablename__ = 'orphans'

    id = Column(Integer, primary_key=True)
    identity_number = Column(String)
    mother_id = Column(Integer, ForeignKey('widows.id'))
    first_name = Column(String)
    last_name = Column(String)
    school_id = Column(Integer, ForeignKey('schools.id'))
    birth_date = Column(Date)
    hebrew_birth_date = Column(String)
    gender = Column(String)
    age_group = Column(String)

    mother = relationship("Widow", back_populates="orphans")
    school = relationship("School", back_populates="orphan", uselist=False)
    events = relationship("Event", secondary=event_orphan_association, back_populates="orphans")

    @classmethod
    def schema(cls):
        return OrphanSchema


class Relative(Base):
    __tablename__ = 'relatives'

    id = Column(Integer, primary_key=True)
    fl_name = Column(String)
    phone = Column(String)
    email = Column(String)
    relationship_type = Column(String)

    widow_id = Column(Integer, ForeignKey('widows.id'))
    widow = relationship("Widow", back_populates="relatives")

    @classmethod
    def schema(cls):
        return RelativeSchema


class School(Base):
    __tablename__ = 'schools'

    id = Column(Integer, primary_key=True)
    school_name = Column(String)
    class_name = Column(String)
    teacher_name = Column(String)
    teacher_phone = Column(String)

    orphan = relationship("Orphan", back_populates="school", uselist=False)

    @classmethod
    def schema(cls):
        return SchoolSchema

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    event_date = Column(Date)
    description_event = Column(String)
    place = Column(String)
    expenses = Column(Float)

    widows = relationship("Widow", secondary=event_widow_association, back_populates="events")
    orphans = relationship("Orphan", secondary=event_orphan_association, back_populates="events")

    @classmethod
    def schema(cls):
        return EventSchema


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    street = Column(String)
    num_building = Column(String)

    widow = relationship("Widow", back_populates="address")

    @classmethod
    def schema(cls):
        return AddressSchema


class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = Column(Integer, primary_key=True)
    bank_number = Column(String)
    branch = Column(String)
    account_number = Column(String)
    holder_name = Column(String)

    widow = relationship("Widow", back_populates="bank_account")

    @classmethod
    def schema(cls):
        return BankAccountSchema