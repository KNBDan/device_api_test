from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core import get_db
from app.service import DeviceService
from app.domain import DeviceCreate, DeviceUpdate, DeviceGet

device_router = APIRouter()

@device_router.post("/", response_model=DeviceGet)
def create_device(device_data: DeviceCreate, db: Session = Depends(get_db)):
    device_service = DeviceService(db)
    return device_service.create_device(device_data)

@device_router.get("/", response_model=list[DeviceGet])
def get_all_devices(db: Session = Depends(get_db)):
    device_service = DeviceService(db)
    return device_service.get_all_devices()

@device_router.get("/{device_id}", response_model=DeviceGet)
def get_device(device_id: int, db: Session = Depends(get_db)):
    device_service = DeviceService(db)
    try:
        return device_service.get_device_by_id(device_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@device_router.put("/{device_id}", response_model=DeviceGet)
def update_device(device_id: int, device_data: DeviceUpdate, db: Session = Depends(get_db)):
    device_service = DeviceService(db)
    try:
        return device_service.update_device(device_id, device_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@device_router.delete("/{device_id}")
def delete_device(device_id: int, db: Session = Depends(get_db)):
    device_service = DeviceService(db)
    try:
        success = device_service.delete_device(device_id)
        if success:
            return {"message": "Устройство удалено"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )



@device_router.post("/{device_id}/batteries/{battery_id}")
def connect_battery_to_device(device_id: int, battery_id: int, db: Session = Depends(get_db)):
    device_service = DeviceService(db)
    try:

        result = device_service.connect_battery(device_id, battery_id)
        return {"message": f"АКБ с Id:{battery_id} подключена к устройству с Id: {device_id}"}

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@device_router.delete("/{device_id}/batteries/{battery_id}")
def disconnect_battery_from_device(device_id: int, battery_id: int, db: Session = Depends(get_db)):
    device_service = DeviceService(db)
    try:
        result = device_service.disconnect_battery(device_id, battery_id)
        return {"message": f"АКБ с Id:{battery_id} отключена от устройства с Id: {device_id}"}

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )