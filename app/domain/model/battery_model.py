from typing import Optional
from pydantic import BaseModel

class BatteryCreate(BaseModel):
    name: str
    voltage: float
    capacity: float
    life_time: int

class BatteryGet(BaseModel):
    id: int
    name: str
    voltage: float
    capacity: float
    life_time: int

    class Config:
        from_attributes = True

class BatteryUpdate(BaseModel):
    name: Optional[str] = None
    voltage: Optional[float] = None
    capacity: Optional[float] = None
    life_time: Optional[int] = None
