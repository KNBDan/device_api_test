from datetime import time
from sqlite3 import OperationalError

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:1234@db:5432/check_device"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def wait_for_db():
    print("Подключение к бд...")
    for i in range(30):
        try:
            with engine.connect() as conn:
                print("Подключено!")
                return True
        except OperationalError:
            if i < 29:  # Не показываем на последней попытке
                print(f"Попытка {i+1}/30...")
            time.sleep(1)
    raise Exception("Ошибка подключения")