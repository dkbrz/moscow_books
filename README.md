# moscow_books

Рекомендации книг. Команда Дальнее чтение

## Используемые данные:

- circulation_*.csv
- books_full.json

## Результаты предсказаний (result.csv)

[тут](https://drive.google.com/drive/folders/1LPgGO22ddP6JJMzngKchXY8uiixvf8Kz?usp=sharing)

## Файлы и как запускать

- data ([скачать тут](https://drive.google.com/file/d/1W8DjwpaiJOQYS2nO2t5lYsrrq7ossO-d/view?usp=sharing))
  - books.jsonlines
  - books_full.jsonlines
  - circulation[].csv
  - rubrics.csv
- process_new (запускать по очереди)
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

## Веб-интерфейс

- [Веб-интерфейс](http://dkbrz4.pythonanywhere.com/)
