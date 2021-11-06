import fastapi as _fastapi
import uvicorn

import bookapp.services as _services
import bookapp.schemas as _schemas
from bookapp.database import async_session

description = """
Тестовый стенд API рекомендаций для московских библиотек команды ```Дальнее чтение```

# Как попробовать?

## ID из полной базы

1. Выберите ниже ```/api/v0/recommend/full/{user_id}```
2. Нажмите ```try it out```
3. Введите ID пользователя
4. ```Execute```

На сайте доступны ID до 400 000, так как место на хостинге ограничено.


```
{
    "id": 0,
    "history": [
        {"id": 462667, "title": "Приключения капитана Врунгеля", "author": "Некрасов Андрей Сергеевич"}
    ],
    "recommendations": [
        {"id": 38125, "title": "Выстрел : повесть", "author": "Рыбаков Анатолий Наумович"}, 
        {"id": 152525, "title": "Похищение чародея : фантастические повести", "author": "Булычев Кир"}
    ]
}
```

"""

app = _fastapi.FastAPI(
    title="Рекомендации для библиотек. Команда Дальнее чтение",
    # docs_url="/",
    description=description
)


@app.get("/")
def index():
    return {"Moscow books": "OK"}


@app.get(
    "/api/v0/recommend/full/{user_id}",
    response_model=_schemas.Recommendation,
    status_code=200)
async def recommend_full(user_id: int):
    """
    Return recommendations from DB
    :param user_id: user_id from big dataset
    :return: json
    """
    async with async_session() as session:
        async with session.begin():
            result = await _services.get_basic(userid=user_id, db=session)
            print(result)
            return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
