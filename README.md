# moscow_books

Рекомендации книг. Команда Дальнее чтение

## Используемые данные:

- circulation_*.csv
- books_full.json


## Файлы и как запускать

- process_new
  - [prepare_data.ipynb](https://github.com/dkbrz/moscow_books/blob/main/process_new/prepare_data.ipynb) : информация из файлов складывается в SQLite базу, чтобы было удобно работать
  - [model_books_only.ipynb](https://github.com/dkbrz/moscow_books/blob/main/process_new/model_books_only.ipynb) : закономерности, когда какие-то книжки берут подряд (внутри автора или без автора)
  - [model_authors.ipynb](https://github.com/dkbrz/moscow_books/blob/main/process_new/model_authors.ipynb) : построение графа по авторам и их связям внутри рубрик 2 уровня
  - [predictions.ipynb](https://github.com/dkbrz/moscow_books/blob/main/process_new/predictions.ipynb) : построение предсказаний и складывание их в базу
  - contest_predictions.ipynb : специальная версия для формирования полной выборки в CSV для проверки
- demoapp : версия для PythonAnyWhere, который не поддерживает полную версию
- bookapp : основная версия API

**bookapp**

API, используещее Python FastAPI, достает готовые предсказания из базы и отдает пользователю

Запуск: 

1. положить в эту папку БД predictions.db, полученную в результате предсказаний (по ссылке в разделе результаты)
2. из корневой папки moscow_book запустить ```python3 bookapp.wsgi```

- На главной странице будет возвращаться проверка, что запущено.
- На странице /docs swagger для проверки
- /api/v0/recommend/full/{user_id} - результаты работы

requirements.txt - библиотеки для установки (в корне репозитория)

- database.py - подключение к базе
- default_recommendation.py - конфиг с рекомендацией по умолчанию
- main.py - основной код приложения
- models.py - модель БД
- schemas.py - схема, описывающая ответ
- services.py - функция обработки запроса к базе
- predictions.db : база результатов предсказаний (в корень demoapp)


**Модель**

1. [data_to_db.ipynb](https://github.com/dkbrz/moscow_books/blob/main/process_data/data_to_db.ipynb) - подготовка данных
2. [predictions.ipynb](https://github.com/dkbrz/moscow_books/blob/main/process_data/predictions.ipynb) - составление графа и прогон предсказаний, можно изменить финальную функцию под нужный формат выдачи

## Результаты для проверки CSV

**обновляется**
Вот [тут](https://drive.google.com/drive/folders/1qMSL5amDjwvLELGKPNZO8m2BRZ5YYvcF?usp=sharing) два файла: test_all - это те, кто попался в circulation как бравший книгу (173к человек), test_sample - пользователи из файла knigi_1

## Веб-интерфейс

- [Веб-интерфейс](http://dkbrz4.pythonanywhere.com/)
- 
