Тестовое задание Backend с api и подключением к db.
Автор: Кунакбаев Д.

Инструкция запуска
#1. Подкачка зависимостей

pip install -r requirements.txt

#2. Настройка бд
Используется PostgreSQL. 
 1) Создайте БД check_device
 2) Создай файл .env или измените его
 3) Укажите свои данные в файле .env
Вид файла .env

DATABASE_URL=postgresql://username:password@localhost:5432/check_device

#3. Запустите программу

python run.py

Готово! Локальный сервер запущен, можно тестировать запросы.

Доступные эндпоинты

#АКБ
POST /api/batteries/ - создать АКБ
GET /api/batteries/ - получить все АКБ
GET /api/batteries/{id} - найти АКБ по Id
PUT /api/batteries/{id} -  обновить АКБ по Id
DELETE /api/batteries/{id} - удалить АКБ по Id

#Устройства
POST /api/devices/ - создать устройство
GET /api/devices/ - получить все устройства
GET /api/devices/{id} - найти устройство по Id
PUT /api/devices/{id} - обновить  устройство по Id
DELETE /api/devices/{id} - удалить устройство по ID

POST /api/devices/{id}/batteries/{battery_id} - подключить АКБ к устройстпу по Id
DELETE /api/devices/{id}/batteries/{battery_id} - отключить АКБ от устройства по Id

