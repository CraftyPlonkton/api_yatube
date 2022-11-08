## API интерфейс для сайта YaTube (https://github.com/CraftyPlonkton/yatube)
### Описание проекта:

Проект дает доступ к функционалу проекта YaTube с помощью REST Api.

Проект позволяет читать, добавлять, редактировать и удалять записи из базы данных yatube.
Полный список запросов и эндпоинтов описан в документации ReDoc, доступна после запуска проекта по адресу:
```
http://127.0.0.1:8000/redoc/
```
### Как запустить проект на тестовом сервере:

<details><summary> Linux </summary>
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
python3 yatube_api/manage.py migrate
```

Запустить проект:

```
python3 yatube_api/manage.py runserver
```
</details>

<details><summary> Windows </summary>
Клонировать репозиторий, перейти в директорию с проектом.

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Source/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python yatube_api/manage.py migrate
```

Запустить проект:

```
python yatube_api/manage.py runserver
```
</details>

### Авторизация

Для авторизации используется JWT токен, для его получения необходимы данные существующего пользователя:

POST `http://127.0.0.1:8000/api/v1/jwt/create/`

    {  
        "username": "string",  
        "password": "string"  
    }  

Ответ:

    {
        "refresh": "string",  
        "access": "string"
    }

Полученный access токен передается в заголовке запроса

    Authorization: Bearer <token>

### Примеры использования API

Создание публикации:  
POST `http://127.0.0.1:8000/api/v1/posts/`  
<details><summary> Запрос </summary>  

    {  
        "text": "string",  
    }  

</details>  

<details><summary> Ответ </summary>

    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2019-08-24T14:15:22Z",
        "image": null,
        "group": null
    }
</details>  

Получение комментариев к публикации:  
GET `http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/`
<details><summary> Ответ </summary>  

    [
        -{
            "id": 0,
            "author": "string",
            "text": "string",
            "created": "2019-08-24T14:15:22Z",
            "post": 0
        }
    ]
</details>  