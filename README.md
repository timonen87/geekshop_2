Запуск проект на сервере:

Клонируем репозиторий git clone https://github.com/timonen87/geekshop_2
Переходим в папку с проектом cd project/geekshop_2 
Устанавливаем виртуальное окружение python -m virtualenv venv
Запускаем виртуальное окружение source venv/bin/activate
Обновляем sudo apt update && sudo apt install python3-pip
Устанавливаем в виртуальном окружении зависимости для проекта pip3 install -r requirements.txt
Делаем миграции для создания базы данных python manage.py makemigrations && python manage.py migrate
Заполняем данными модели python manage.py filldb
Запускаем локальный сервер python3 manage.py runserver 139.162.154.106:8000
По адресу python3 manage.py runserver 139.162.154.106:8000 
