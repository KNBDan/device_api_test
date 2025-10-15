from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core import get_db
from app.service import BatteryService
from app.domain import BatteryCreate, BatteryUpdate, BatteryGet

battery_router = APIRouter()

@battery_router.post("/", response_model=BatteryGet)
def create_battery(battery_data: BatteryCreate, db: Session = Depends(get_db)):
    battery_service = BatteryService(db)
    return battery_service.create_battery(battery_data)

@battery_router.get("/", response_model=list[BatteryGet])
def get_all_batteries(db: Session = Depends(get_db)):
    battery_service = BatteryService(db)
    return battery_service.get_all_batteries()

@battery_router.get("/{battery_id}", response_model=BatteryGet)
def get_battery(battery_id: int, db: Session = Depends(get_db)):
    battery_service = BatteryService(db)
    try:
        return battery_service.get_battery_by_id(battery_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@battery_router.put("/{battery_id}", response_model=BatteryGet)
def update_battery(battery_id: int, battery_data: BatteryUpdate, db: Session = Depends(get_db)):
    battery_service = BatteryService(db)
    try:
        return battery_service.update_battery(battery_id, battery_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@battery_router.delete("/{battery_id}")
def delete_battery(battery_id: int, db: Session = Depends(get_db)):
    battery_service = BatteryService(db)
    try:
        success = battery_service.delete_battery(battery_id)
        if success:
            return {"message": "АКБ удалён"}
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ошибка"
            )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )