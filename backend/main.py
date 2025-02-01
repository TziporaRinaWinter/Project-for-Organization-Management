# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum, Date, Table
# from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from enum import Enum as PyEnum

# Base = declarative_base()


# class GenderEnum(PyEnum):
#     MALE = "בן"
#     FEMALE = "בת"


# class AgeGroupEnum(PyEnum):
#     KINDERGARTEN = "גן"
#     ELEMENTARY = "בית ספר יסודי"
#     HIGH_SCHOOL = "סמינר"
#     CHEDER = "חיידר"
#     SMALL_YESHIVA = "ישיבה קטנה"
#     LARGE_YESHIVA = "ישיבה גדולה"


# class EventCategoryEnum(PyEnum):
#     MONTHLY_EVENT = "אירוע חודשי"
#     PURIM = "פורים"
#     HANUKKAH = "חנוכה"
#     SHABBAT = "שבת"


# event_widow_association = Table('event_widow', Base.metadata,
#                                 Column('event_id', Integer, ForeignKey('events.id')),
#                                 Column('widow_id', Integer, ForeignKey('widows.id'))
#                                 )

# event_orphan_association = Table('event_orphan', Base.metadata,
#                                  Column('event_id', Integer, ForeignKey('events.id')),
#                                  Column('orphan_id', Integer, ForeignKey('orphans.id'))
#                                  )


# class Widow(Base):
#     __tablename__ = 'widows'

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     home_phone = Column(String)
#     mobile_phone = Column(String)
#     address = Column(String)
#     email = Column(String)
#     birth_date = Column(Date)
#     yahrzeit = Column(String)
#     married_children_count = Column(Integer)
#     children_at_home_count = Column(Integer)

#     orphans = relationship("Orphan", back_populates="mother")
#     relatives = relationship("Relative", back_populates="widow")
#     events = relationship("Event", secondary=event_widow_association, back_populates="widows")


# class Orphan(Base):
#     __tablename__ = 'orphans'

#     id = Column(Integer, primary_key=True)
#     mother_id = Column(Integer, ForeignKey('widows.id'))
#     first_name = Column(String)
#     school_id = Column(Integer, ForeignKey('schools.id'))
#     birth_date = Column(Date)
#     gender = Column(Enum(GenderEnum), nullable=False)

#     mother = relationship("Widow", back_populates="orphans")
#     school = relationship("School", back_populates="orphans")
#     events = relationship("Event", secondary=event_orphan_association, back_populates="orphans")


# class Relative(Base):
#     __tablename__ = 'relatives'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     phone = Column(String)
#     email = Column(String)
#     relationship_type = Column(String)

#     widow_id = Column(Integer, ForeignKey('widows.id'))
#     widow = relationship("Widow", back_populates="relatives")


# class School(Base):
#     __tablename__ = 'schools'

#     id = Column(Integer, primary_key=True)
#     age_group = Column(Enum(AgeGroupEnum))
#     name = Column(String)
#     class_name = Column(String)

#     orphans = relationship("Orphan", back_populates="school")


# class Event(Base):
#     __tablename__ = 'events'

#     id = Column(Integer, primary_key=True)
#     category = Column(Enum(EventCategoryEnum), nullable=False)
#     description = Column(String)
#     event_date = Column(Date)

#     orphans = relationship("Orphan", secondary=event_orphan_association, back_populates="events")
#     widows = relationship("Widow", secondary=event_widow_association, back_populates="events")


# engine = create_engine('sqlite:///example.db')
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# session.close()

from fastapi import FastAPI
from controller.widow_controller import router as widow_router
from controller.event_controller import router as event_router
from controller.orphan_controller import router as orphan_router
import uvicorn

app = FastAPI()

app.include_router(widow_router, prefix="/api")
app.include_router(event_router, prefix="/api")
app.include_router(orphan_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


# לאחר שכתבת את הקוד, תוכל להריץ את השרת באמצעות הפקודה הבאה:

# uvicorn main:app --reload
# 4. גישה ל-API
# לאחר שהשרת רץ, תוכל לגשת ל-API שלך דרך הדפדפן או באמצעות כלי כמו Postman בכתובת:

# http://127.0.0.1:8000/widows/
