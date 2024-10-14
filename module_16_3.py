from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")                             # получить всех пользователуй
async def get_all_users() -> dict:
    return users


@app.post("/user/{username}/{age}")             # создать пользователя
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                    example="Lexar")],
                      age: int = Path(ge=1, le=100, description="Enter User ID", example=78)) -> str:
    user_id = str(int(max(users, key=int))+1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")    # обновление пользователя
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=78)],
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                    example="Lexar")],
                      age: int = Path(ge=18, le=120, description="Enter age", example=53)) -> str:
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")                   # удалить пользователя
async def delete_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=78)) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"
"""1. GET '/users'
{
"1": "Имя: Example, возраст: 18"
}
2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
"User 2 is registered"
3. POST '/user/{username}/{age}' # username - NewUser, age - 22
"User 3 is registered"
4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
"User 1 has been updated"
5. DELETE '/user/{user_id}' # user_id - 2
"User 2 has been deleted"
6. GET '/users'
{
"1": "Имя: UrbanProfi, возраст: 28",
"3": "Имя: NewUser, возраст: 22"
}"""
