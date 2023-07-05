from pydantic import BaseModel




class Studnet(BaseModel):
    id: int
    name: str
    roll: int
    branch: str
    class Config:
        orm_mode = True