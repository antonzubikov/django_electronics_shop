# Online electronics store


## Project description:
Это онлайн магазин электроники с использованием фреймворка Django.


## В магазине можно:
* Зарегистрироваться и войти в профиль;
* Посмотреть каталог всех товаров;
* Отсортировать товары по определённым критериям;
* Добавить в корзину и оплатить товар (или несколько товаров);
* Оставлять комментарии к товарам


## Used technologies:

* Python (3.10);
* Django (4.1.3);
* DRF (3.14.0);
* SQLite3 (database);
* requests (2.28.1);
* PyYAML (6.0);
* sorl–thumbnail (12.9.0);
* transliterate (1.10.2)


## Installation:

* Необходимо скопировать все содержимое репозитория в отдельный каталог;
* Установить все связи из `requirements.txt`;

```
python pip install -r requirements.txt
```

* Выполнить миграции:

```
python manage.py makemigrations
python manage.py migrate
```


## Для тестирования и наглядного представления работы сайта необходимо загрузить фикстуры:

```
python manage.py loaddata fixtures/data_fixture.json
```

* В фикстурах суперпользователь: 
**admin@admin.an** (пароль: **admin**)


## Launch:

* Для запуска сайта воспользуйтесь командой:

```
python manage.py runserver
```
