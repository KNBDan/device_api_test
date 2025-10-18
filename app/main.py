from fastapi import FastAPI
from app.controller import battery_router, device_router
from app.core import Base, engine, wait_for_db

wait_for_db()
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Test api",
    version="0.1.0",
)

app.include_router(battery_router, prefix="/api/batteries", tags=["batteries"])
app.include_router(device_router, prefix="/api/devices", tags=["devices"])
