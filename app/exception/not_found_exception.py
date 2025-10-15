class NotFoundException(BaseException):
    def __init__(self, entity_name: str, entity_id: int = None):
        if entity_id:
            message = f"{entity_name} с Id: {entity_id} не найден(а/о)"
        else:
            message = f"{entity_name} не найден(а/о)"
        super().__init__(message)

class DeviceNotFoundException(NotFoundException):
    def __init__(self, device_id: int):
        super().__init__("Устройство", device_id)

class BatteryNotFoundException(NotFoundException):
    def __init__(self, battery_id: int):
        super().__init__("АКБ", battery_id)
