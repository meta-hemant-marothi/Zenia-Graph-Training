from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    director: str
    year: int

class MovieCreate(MovieBase):
    pass

class MovieUpdate(MovieBase):
    pass

class MovieOut(MovieBase):
    id: int

    class Config:
        orm_mode = True
