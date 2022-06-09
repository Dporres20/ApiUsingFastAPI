from enum import Enum
from tokenize import String
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class Gender(str,Enum):
    male = "male"
    female = "female"
    other = "other"

class Role(str,Enum):
    admin = "admin"
    teacher = "teacher"
    student = "student"
    applicant = "applicant"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]