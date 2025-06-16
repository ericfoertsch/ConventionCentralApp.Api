from pydantic import BaseModel

class Person(BaseModel):
    id_person: int

    class Config:
        from_attributes = True