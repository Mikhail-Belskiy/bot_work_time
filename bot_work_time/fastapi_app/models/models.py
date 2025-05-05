from datetime import date

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    password: str
    date_birth: date

class LocationBase(BaseModel):
    name_location: str
    address: str
    is_exit: bool = False

class MarkCreate(BaseModel):
    location_id: int
    geo_in: dict

class MarkOut(BaseModel):
    location_id: int
    geo_out: dict

class TimeRange(BaseModel):
    start_time: date
    end_time: date


