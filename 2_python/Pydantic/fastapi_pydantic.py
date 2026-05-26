from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None  # Optional field with default value None

@app.post("/add_user/")
def create_user(user: User):
    return {"message": "User created successfully", "user": user}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    # In a real application, you would fetch the user from a database
    # Here, we return a dummy user for demonstration purposes
    dummy_user = User(id=user_id, name="John Doe", email="john.doe@example.com", age=None)
    return {"user": dummy_user}