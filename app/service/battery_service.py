from sqlalchemy.orm import Session
from app.domain import BatteryCreate, BatteryUpdate, BatteryGet
from app.repository import BatteryRepository
from app.exception import BatteryNotFoundException


class BatteryService:
    def __init__(self, db: Session):
        self.battery_repository = BatteryRepository(db)

    def create_battery(self, battery_data: BatteryCreate) -> BatteryGet:
        battery = self.battery_repository.create_battery(battery_data)
        return BatteryGet.from_orm(battery)

    def get_all_batteries(self) -> list[BatteryGet]:
        batteries = self.battery_repository.get_all_batteries()
        return [BatteryGet.from_orm(battery) for battery in batteries]

    def get_battery_by_id(self, battery_id: int) -> BatteryGet:
        battery = self.battery_repository.get_battery_by_id(battery_id)
        if not battery:
            raise BatteryNotFoundException(battery_id)
        return BatteryGet.from_orm(battery)

    def update_battery(self, battery_id: int, battery_data: BatteryUpdate) -> BatteryGet:
        existing_battery = self.get_battery_by_id(battery_id)
        battery = self.battery_repository.update_battery(battery_id, battery_data)
        return BatteryGet.from_orm(battery)

    def delete_battery(self, battery_id: int) -> bool:
        existing_battery = self.get_battery_by_id(battery_id)
        return self.battery_repository.delete_battery(battery_id)