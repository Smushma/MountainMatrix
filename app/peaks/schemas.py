from pydantic import BaseModel


class PeakBase(BaseModel):
    name: str
    elevation_meters: int


class Peak(PeakBase):
    id: int

    class Config:
        orm_mode = True
