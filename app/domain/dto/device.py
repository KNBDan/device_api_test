from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.connection import Base


class Device(Base):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True)
    name = Column(String(100),unique=True, nullable=False)
    version = Column(String(20), nullable=False)
    condition = Column(Boolean, nullable=False)

    batteries = relationship("Battery", secondary="battery_device", back_populates="devices")

