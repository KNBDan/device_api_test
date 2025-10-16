Тестовое задание Backend с api и подключением к db.

Автор: Кунакбаев Д.

Инструкция запуска
# Подкачка зависимостей

pip install -r requirements.txt

# Настройка бд
Используется PostgreSQL. 
 1) Создайте БД check_device
 2) Создай файл .env или измените его
 3) Укажите свои данные в файле .env
Вид файла .env

DATABASE_URL=postgresql://username:password@localhost:5432/check_device

 4) При необходимости укажите свои порты для запуска в run.py (по умолчанию 0.0.0.0:8005)
# Запуск программы

python run.py

Готово! Локальный сервер запущен, можно тестировать запросы. 

URL для подключения:  http://0.0.0.0:8005/api/

# Доступные эндпоинты

АКБ
1) POST /api/batteries/ - создать АКБ
2) GET /api/batteries/ - получить все АКБ
3) GET /api/batteries/{id} - найти АКБ по Id
4) PUT /api/batteries/{id} -  обновить АКБ по Id
5) DELETE /api/batteries/{id} - удалить АКБ по Id

Стандартное тело для создания и изменнеия АКБ:

{
    "name": "name",
    "voltage": 1.0,
    "capacity": 1.0,
    "life_time": 1
}

Устройства
1) POST /api/devices/ - создать устройство)
2) GET /api/devices/ - получить все устройства
3) GET /api/devices/{id} - найти устройство по Id
4) PUT /api/devices/{id} - обновить  устройство по Id
5) DELETE /api/devices/{id} - удалить устройство по ID

6) POST /api/devices/{id}/batteries/{battery_id} - подключить АКБ к устройстпу по Id
7) DELETE /api/devices/{id}/batteries/{battery_id} - отключить АКБ от устройства по Id

Стандартное тело для создания и изменнеия устройства:

{ "name": "name", "version": "1.0.0", "condition": false}
