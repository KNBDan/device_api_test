from sqlalchemy.orm import Session
from app.domain import Battery, BatteryCreate


class BatteryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_battery(self, battery_data: BatteryCreate) -> Battery:
        db_battery = Battery(**battery_data.dict())
        self.db.add(db_battery)
        self.db.commit()
        self.db.refresh(db_battery)
        return db_battery

    def get_all_batteries(self) -> list[Battery]:
        return self.db.query(Battery).all()

    def get_battery_by_id(self, battery_id: int) -> Battery:
        return self.db.query(Battery).filter(Battery.id == battery_id).first()

    def update_battery(self, battery_id: int, battery_data: BatteryCreate) -> Battery:
        battery = self.get_battery_by_id(battery_id)
        if battery:
            for key, value in battery_data.dict().items():
                setattr(battery, key, value)
            self.db.commit()
            self.db.refresh(battery)
        return battery

    def delete_battery(self, battery_id: int) -> bool:
        battery = self.get_battery_by_id(battery_id)
        if battery:
            self.db.delete(battery)
            self.db.commit()
            return True
        return False