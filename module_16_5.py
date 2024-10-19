from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory='templates')
app = FastAPI()
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")                                   # получить главную страницу
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users/{user_id}'")                   # получить всех пользователуй
async def get_all_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})


@app.post("/user/{username}/{age}")             # создать пользователя
async def create_user(user: User, username: str, age: int):
    if len(users) == 0:
        user.id = 1
    else:
        user.id = users[len(users) - 1].id + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")    # обновление пользователя
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")                   # удалить пользователя
async def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            user = users[i]
            users.pop(i)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
