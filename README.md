## API интерфейс для сайта YaTube (https://github.com/CraftyPlonkton/yatube)
### Описание проекта:

Проект дает доступ к функционалу проекта YaTube с помощью REST Api.

Проект позволяет читать, добавлять, редактировать и удалять записи из базы данных yatube.
Полный список запросов и эндпоинтов описан в документации ReDoc, доступна после запуска проекта по адресу:
```
http://127.0.0.1:8000/redoc/
```
### Как запустить проект на тестовом сервере:
Клонировать репозиторий, перейти в директорию с проектом.

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
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
