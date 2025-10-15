from typing import Optional, List
from pydantic import BaseModel
from .battery_model import BatteryGet

class DeviceCreate(BaseModel):
    name: str
    version: str
    condition: bool

class DeviceGet(BaseModel):
    id: int
    name: str
    version: str
    condition: bool
    batteries: List[BatteryGet] = []

    class Config:
        from_attributes = True

class DeviceUpdate(BaseModel):
    name: Optional[str] = None
    version: Optional[str] = None
    condition: Optional[bool] = None
