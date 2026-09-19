from typing import Annotated
from pydantic import BaseModel, EmailStr , field, StringConstraints

class UserCreate(BaseModel):
    uder_id: int = field(gt=0)
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)]
    email: EmailStr
    age: int = field(gt=18, lt=120)
    student_id: Annotated[str, StringConstraints(pattern=r"^\d{7}$")]