Запуск проект на сервере:<br>
Клонируем репозиторий git clone https://github.com/timonen87/geekshop_2<br>
Переходим в папку с проектом cd project/geekshop_2 <br>
Устанавливаем виртуальное окружение python -m virtualenv venv<br>
Запускаем виртуальное окружение source venv/bin/activate<br>
Обновляем sudo apt update && sudo apt install python3-pip<br>
Устанавливаем в виртуальном окружении зависимости для проекта pip3 install -r requirements.txt<br>
Делаем миграции для создания базы данных python manage.py makemigrations && python manage.py migrate<br>
Заполняем данными модели python manage.py filldb<br>
Запускаем локальный сервер python3 manage.py runserver 139.162.154.106:8000<br>
По адресу python3 manage.py runserver 139.162.154.106:8000 <br>
