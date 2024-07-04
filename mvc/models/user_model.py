from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    height: float
    weight: float