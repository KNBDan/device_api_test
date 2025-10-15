from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.core.connection import Base

class Battery(Base):
    __tablename__ = 'battery'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    voltage = Column(Float, nullable=False)
    capacity = Column(Float, nullable=False)
    life_time = Column(Integer, nullable=False)

    devices = relationship("Device", secondary="battery_device", back_populates="batteries")

# Many to Many
class BatteryDevice(Base):
    __tablename__ = "battery_device"

    id = Column(Integer, primary_key=True, index=True)
    battery_id = Column(Integer, ForeignKey("battery.id"))
    device_id = Column(Integer, ForeignKey("device.id"))
