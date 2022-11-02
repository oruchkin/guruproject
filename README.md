# Тестовое задание для Гуру Групп

## Как запустить через Docker:

```
docker-compose up
```

После того как контейнер соберется в любом другом терминале выполнить комманду

```
docker exec -it infra_backend_1 python manage.py collectstatic
```

Проект успешно запущен по адресу [вот здесь](http://127.0.0.1) (http://127.0.0.1)

Админка [вот здесь](http://127.0.0.1/admin) (http://127.0.0.1/admin)

#### Доступ в админку:

- ``username:`` ``admin``
- ``password:`` ``admin``

Админка нужна для удобства, в ней удобно создавать обьекты (Города, Улицы, Магазины)

#### Запросы:

- ``GET /city/`` — получение всех городов из базы;
- ``GET /city/city_id/`` — получение города по id;
- ``GET /city/city_id/street/`` — получение всех улиц города; (city_id — идентификатор города)
- ``POST /shop/`` — создание магазина; Данный метод получает json c объектом магазина, в
  ответ возвращает id созданной записи.
    
     Передаем сюда следующие параметры:
    - ```title: (string)``` = название магазина (Ашан)
    - ```city:  (integer)``` = id города (1,5,8)
    - ```house: (string)``` = номер дома (1,2, 55a)
    - ```street: (integer)``` = id улица (1,5,8
    - ```time_open: (string)``` = время открытия магазина (hh:mm) (07:55)
    - ```time_closed: (string)``` = время закрытия магазина (hh:mm) (22:15)

- ``GET /shop/?street=&city=&open=0/1&time=10:00`` — получение списка магазинов:

  - I. Метод принимает параметры для фильтрации. Параметры не обязательны. В
    случае отсутствия параметров выводится все магазины, если хоть один параметр
    есть, то по нему выполнятся фильтрации.
  - II. Важно! В объекте каждого магазина выводится название города и улицы, а не id
    записей.
  - III. Параметр open: 0 - закрыт, 1 - открыт. Данный статус определяет исход из
    параметров «Врем открытия», «Врем закрытия» и текущего времени сервера.
  - IV. Добавлен параметр time (нету в т.з) для удобства дебага. Сюда нужно передать время типа ``HH:mm`` (Часы:минуты (00:59))

---

#### P.S (о базе данных)

Сейчас подключена реляционная база данных SQLite3, в ней уже есть данные для тестов.

Так же в контейнере установлена база данных PostgreSQL (которая рекомендована в т.з), она не используется по умолчанию так как в нее нужно дополнительно вносить обьекты (что не удобно) для этого используется SQLite3 чтобы сьекономить время для тестов.

Переключиться на PostgreSQL можно в настройках в папке ``/backend/guruproject/components/databases.py`` там нужно раскоментировать настройки для postgresql, и закоменитровать для sqlite3, и пересобрать контейнер, потом еще нужно сделать миграции ```docker exec -it infra_backend_1 python manage.py migrate``` и создать админа ```docker exec -it infra_backend_1 python manage.py createsuperuser```. Но в рамках тестового для экономии времени используем SQLite3.
