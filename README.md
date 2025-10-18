Тестовое задание Backend с api и подключением к db.

Автор: Кунакбаев Д.

Инструкция запуска

# Подготовка окружения

1) Скачайте и распакуйте проект в отдельную папку
2) Установить Docker Desktop 4.12+

# Запуск программы

В командной строке открытой в папке прокта запустите билд докер файла

docker-compose up --build

Подождите пока пройдут все этапы развёртывания

Готово! Локальный сервер запущен, можно тестировать запросы. 

URL для подключения:  

http://0.0.0.0:8005


или  http://localhost:8005

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
