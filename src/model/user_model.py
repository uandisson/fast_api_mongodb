from datetime import datetime
from enum import Enum
from typing import Optional

from bson import ObjectId

from model.mongodb_model import OID, MongoModel


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class User(MongoModel):
    id: OID = str(ObjectId())  # TODO
    name: str
    age: int
    gender: Gender
    born_date: datetime
    phone_number: Optional[str]
