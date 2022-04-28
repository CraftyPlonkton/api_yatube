### Описание проекта:

Проект дает доступ к некоторому функционалу проекта yatube с помощью REST Api.

Проект написан на основе фреймворка djangorestframework 3.12.4

Проект позволяет читать, добавлять, редактировать и удалять записи из базы данных yatube.
Полный список доступных запросов и ендпоинтов описан в документации ReDoc
```
http://127.0.0.1:8000/redoc/
```
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/CraftyPlonkton/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры использования Api

##### Создание поста POST запросом на эндпоинт /api/v1/posts/
{

    "text": "string",
    "image": "string",
    "group": 0

}
##### Ответ:
{

    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0

}

##### Получение информации о комментарии GET запросом на эндпоинт /api/v1/posts/{post_id}/comments/{id}/
##### Ответ:
{

    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0

}
##### Получение списка постов GET запросом на эндпоинт с пагинацией /api/v1/posts/?limit=1&offset=5
##### Ответ будет содержать 1 элемент на странице, начиная с пятого:
{

    "count": 123,
    "next": "http://api.example.org/accounts/?offset=6&limit=1",
    "previous": "",
    "results": [

        {
            "id": 5,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]

}
