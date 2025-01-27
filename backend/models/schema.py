from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True


class OrphanBase(BaseSchema):
    identity_number: str
    first_name: str
    last_name: str
    birth_date: Optional[date]
    gender: str
    age_group: str


class RelativeBase(BaseSchema):
    fl_name: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    relationship_type: Optional[str]


class BankAccountBase(BaseSchema):
    bank_number: str
    branch: str
    account_number: str
    holder_name: str


class AddressBase(BaseSchema):
    city: str
    street: str
    num_building: str


class SchoolBase(BaseSchema):
    school_name: str
    class_name: str
    teacher_name: str
    teacher_phone: str


class EventBase(BaseSchema):
    category: str
    event_date: date
    description_event: str
    place: str
    expenses: float
    widows: List[int]
    orphans: List[int]


class WidowBase(BaseSchema):
    identity_number: str
    first_name: str
    last_name: str
    home_phone: Optional[str]
    mobile_phone: Optional[str]
    email: Optional[str]
    birth_date: date
    widowhood_date: date
    num_of_unmarried_children: int
    num_of_minor_children: Optional[int]


class WidowSchema(WidowBase):
    id: int
    orphans: List[OrphanBase]
    relatives: List[RelativeBase]
    bank_account: BankAccountBase
    address: AddressBase


class OrphanSchema(OrphanBase):
    id: int
    mother_id: int
    school_id: Optional[int]


class RelativeSchema(RelativeBase):
    id: int
    widow_id: int


class BankAccountSchema(BankAccountBase):
    id: int


class AddressSchema(AddressBase):
    id: int


class SchoolSchema(SchoolBase):
    id: int


class EventSchema(EventBase):
    id: int
