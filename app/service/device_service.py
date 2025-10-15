from sqlalchemy.orm import Session
from app.domain import DeviceCreate, DeviceUpdate, DeviceGet
from app.repository import DeviceRepository, BatteryRepository
from app.service import BatteryService
from app.exception import DeviceNotFoundException, BatteryNotInDeviceException, BatteryAlreadyConnectException, MaxBatteriesInDeviceException


class DeviceService:
    def __init__(self, db: Session):
        self.db = db
        self.device_repository = DeviceRepository(db)
        self.battery_repository = BatteryRepository(db)
        self.battery_service = BatteryService(db)

    def create_device(self, device_data: DeviceCreate) -> DeviceGet:
        device = self.device_repository.create_device(device_data)
        return DeviceGet.from_orm(device)

    def get_all_devices(self) -> list[DeviceGet]:
        devices = self.device_repository.get_all_devices()
        return [DeviceGet.from_orm(device) for device in devices]

    def get_device_by_id(self, device_id: int) -> DeviceGet:
        device_model  = self.device_repository.get_device_by_id(device_id)
        if not device_model :
            raise DeviceNotFoundException(device_id)
        return DeviceGet.from_orm(device_model)

    def update_device(self, device_id: int, device_data: DeviceUpdate) -> DeviceGet:
        existing_device = self.get_device_by_id(device_id)
        device = self.device_repository.update_device(device_id, device_data)
        return DeviceGet.from_orm(device)

    def delete_device(self, device_id: int) -> bool:
        existing_device = self.get_device_by_id(device_id)
        return self.device_repository.delete_device(device_id)

    def connect_battery(self, device_id: int, battery_id: int):
        device_model = self.device_repository.get_device_by_id(device_id)
        battery_model = self.battery_repository.get_battery_by_id(battery_id)

        if battery_model in device_model.batteries:
            raise BatteryAlreadyConnectException(battery_id, device_id)

        if len(device_model.batteries) >= 5:
            raise MaxBatteriesInDeviceException(device_id)

        device_model.batteries.append(battery_model)
        self.db.commit()

        return {"message": f"АКБ с id: {battery_id} подключён"}

    def disconnect_battery(self, device_id: int, battery_id: int):
        device_model = self.device_repository.get_device_by_id(device_id)
        battery_model = self.battery_repository.get_battery_by_id(battery_id)

        if battery_model not in device_model.batteries:
            raise BatteryNotInDeviceException(battery_id, device_id)

        device_model.batteries.remove(battery_model)
        self.db.commit()

        return {"message": f"АКБ с Id: {battery_id} отключен"}