from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()


@app.get("/")
async def main_page() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def admin_page() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def id_page(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=78)) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def info_page(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Lexar")],
                    age: int = Path(ge=18, le=120, description="Enter age", example=53)) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
