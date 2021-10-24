# moscow_books

Рекомендации книг. Команда Дальнее чтение

## Используемые данные:

- circulation_*.csv
- books_full.json


## Файлы и как запускать

- process_data
  - [data_to_db.ipynb](https://github.com/dkbrz/moscow_books/blob/main/process_data/data_to_db.ipynb) : информация из файлов складывается в SQLite базу, чтобы было удобно работать
  - [predictions.ipynb](https://github.com/dkbrz/moscow_books/blob/main/process_data/predictions.ipynb) : собственно предсказания и складывание их в другую базу для API
- demoapp : версия для PythonAnyWhere, который не поддерживает полную версию
- bookapp : основная версия API
  - 
