class BusinessLogicException(BaseException):
    pass

class BatteryAlreadyConnectException(BusinessLogicException):
    def __init__(self, battery_id: int , device_id: int):
        message = f"АКБ с Id: {battery_id} уже подключено к устройству с Id: {device_id}"
        super().__init__(message)

class MaxBatteriesInDeviceException(BusinessLogicException):
    def __init__(self, device_id: int):
        message = f"К устройству с Id: {device_id} уже подключено 5 АКБ"
        super().__init__(message)

class BatteryNotInDeviceException(BusinessLogicException):
    def __init__(self, battery_id: int, device_id: int):
        message = f"АКБ с Id: {battery_id} не подключен к  устройству с Id: {device_id}"
        super().__init__(message)