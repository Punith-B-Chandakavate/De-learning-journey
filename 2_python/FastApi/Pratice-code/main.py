from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample Database
users = {}

# Request Body Model
class User(BaseModel):
    name: str
    age: int


# =========================
# GET METHODS
# =========================

@app.get("/")
def home():
    return {"message": "Hello!"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id in users:
        return users[user_id]
    return {"error": "User not found"}


# =========================
# POST METHOD
# =========================

@app.post("/users")
def create_user(user_id: int, user: User):
    users[user_id] = user.dict()
    return {
        "message": "User created successfully",
        "data": users[user_id]
    }


# =========================
# PUT METHOD
# =========================

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users:
        return {"error": "User not found"}

    users[user_id] = user.dict()

    return {
        "message": "User updated successfully",
        "data": users[user_id]
    }


# =========================
# PATCH METHOD
# =========================

@app.patch("/users/{user_id}")
def patch_user(user_id: int, name: str = None, age: int = None):

    if user_id not in users:
        return {"error": "User not found"}

    if name:
        users[user_id]["name"] = name

    if age:
        users[user_id]["age"] = age

    return {
        "message": "User partially updated",
        "data": users[user_id]
    }


# =========================
# DELETE METHOD
# =========================

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    if user_id not in users:
        return {"error": "User not found"}

    deleted_user = users.pop(user_id)

    return {
        "message": "User deleted successfully",
        "data": deleted_user
    }