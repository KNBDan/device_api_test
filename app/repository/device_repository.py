from sqlalchemy.orm import Session
from app.domain import Device, DeviceCreate


class DeviceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_device(self, device_data: DeviceCreate) -> Device:
        db_device = Device(**device_data.dict())
        self.db.add(db_device)
        self.db.commit()
        self.db.refresh(db_device)
        return db_device

    def get_all_devices(self) -> list[Device]:
        return self.db.query(Device).all()

    def get_device_by_id(self, device_id: int) -> Device:
        return self.db.query(Device).filter(Device.id == device_id).first()

    def update_device(self, device_id: int, device_data: DeviceCreate) -> Device:
        device = self.get_device_by_id(device_id)
        if device:
            for key, value in device_data.dict().items():
                setattr(device, key, value)
            self.db.commit()
            self.db.refresh(device)
        return device

    def delete_device(self, device_id: int) -> bool:
        device = self.get_device_by_id(device_id)
        if device:
            self.db.delete(device)
            self.db.commit()
            return True
        return False