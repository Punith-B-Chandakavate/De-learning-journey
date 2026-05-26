# 🚀 FastAPI - Detailed Notes for README.md

---

# 🔥 What is FastAPI?

**FastAPI** is a modern Python web framework used for building APIs quickly and efficiently.

It is built on:

* ⭐ **Starlette** → For web handling
* ⭐ **Pydantic** → For data validation

FastAPI is mainly used for:

* REST APIs
* Backend services
* Microservices
* AI/ML APIs
* Authentication systems

---

# ✅ Advantages of FastAPI

| Feature             | Description                        |
| ------------------- | ---------------------------------- |
| ⚡ High Performance  | Very fast like NodeJS & Go         |
| 📘 Automatic Docs   | Swagger UI generated automatically |
| ✅ Data Validation   | Uses Pydantic models               |
| 🔥 Async Support    | Supports asynchronous programming  |
| 🧠 Easy to Learn    | Simple syntax                      |
| 🔒 Type Hints       | Better coding & validation         |
| 🚀 Production Ready | Used in real-world applications    |

---

# 📦 Installation

## Install FastAPI

```bash
pip install fastapi
```

## Install ASGI Server (Uvicorn)

```bash
pip install uvicorn
```

---

# ▶️ First FastAPI Application

## 📄 main.py

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
```

---

# ▶️ Run the Server

```bash
uvicorn main:app --reload
```

---

# 🌐 Open in Browser

| URL                           | Purpose             |
| ----------------------------- | ------------------- |
| `http://127.0.0.1:8000`       | API                 |
| `http://127.0.0.1:8000/docs`  | Swagger UI          |
| `http://127.0.0.1:8000/redoc` | ReDoc Documentation |

---

# ✅ Output

```json
{
  "message": "Welcome to FastAPI"
}
```

---

# 🔥 FastAPI Project Structure

```text
project/
│
├── main.py
├── models.py
├── routers/
├── database.py
├── schemas.py
├── requirements.txt
```

---

# 🌐 HTTP Methods in FastAPI

| Method | Purpose             |
| ------ | ------------------- |
| GET    | Fetch Data          |
| POST   | Create Data         |
| PUT    | Update Full Data    |
| PATCH  | Update Partial Data |
| DELETE | Delete Data         |

---

# 📘 GET API Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return {
        "users": ["Punith", "Ravi", "Kiran"]
    }
```

---

# ✅ Output

```json
{
  "users": ["Punith", "Ravi", "Kiran"]
}
```

---

# 📘 POST API Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/create-user")
def create_user():
    return {
        "message": "User Created Successfully"
    }
```

---

# ✅ Output

```json
{
  "message": "User Created Successfully"
}
```

---

# 📘 Path Parameters

Used to send values in URL.

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{id}")
def get_user(id: int):
    return {"user_id": id}
```

---

# ✅ URL

```text
/users/10
```

## ✅ Output

```json
{
  "user_id": 10
}
```

---

# 📘 Query Parameters

Used after `?` in URL.

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def get_item(name: str):
    return {"item": name}
```

---

# ✅ URL

```text
/items/?name=Laptop
```

## ✅ Output

```json
{
  "item": "Laptop"
}
```

---

# 📘 Request Body Using Pydantic

Pydantic validates request data automatically.

## Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age
    }
```

---

# ✅ Input JSON

```json
{
  "name": "Punith",
  "age": 25
}
```

---

# ✅ Output

```json
{
  "name": "Punith",
  "age": 25
}
```

---

# 🔒 Data Validation Example

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
```

If invalid email is passed:

* FastAPI automatically returns validation error.

---

# ⚡ Async API Example

FastAPI supports asynchronous programming.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Async FastAPI"}
```

---

# 🔥 Difference Between def and async def

| def                   | async def             |
| --------------------- | --------------------- |
| Normal function       | Asynchronous function |
| Blocking              | Non-blocking          |
| Slower for large APIs | Better performance    |

---

# 📘 Status Codes

| Status Code | Meaning               |
| ----------- | --------------------- |
| 200         | Success               |
| 201         | Created               |
| 400         | Bad Request           |
| 401         | Unauthorized          |
| 404         | Not Found             |
| 500         | Internal Server Error |

---

# 📘 Returning Custom Status Code

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/create", status_code=status.HTTP_201_CREATED)
def create():
    return {"message": "Created"}
```

---

# 🔥 FastAPI Features

| Feature              | Usage                    |
| -------------------- | ------------------------ |
| Dependency Injection | Reusable logic           |
| Middleware           | Process request/response |
| Authentication       | JWT/OAuth2               |
| File Upload          | Upload files/images      |
| CORS                 | Frontend connection      |
| Background Tasks     | Run tasks in background  |
| WebSockets           | Real-time communication  |

---

# 📘 CORS Example

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
```

---

# 📘 JWT Authentication Flow

```text
User Login → Generate JWT Token → Send Token → Verify Token → Access API
```

---

# 📘 File Upload Example

```python
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

---

# 📘 Dependency Injection Example

```python
from fastapi import Depends

def common():
    return {"message": "Common Function"}

@app.get("/")
def home(data: dict = Depends(common)):
    return data
```

---

# 📘 Swagger UI

FastAPI automatically creates API documentation.

## Swagger URL

```text
/docs
```

---

# 📘 ReDoc Documentation

Alternative API documentation.

## ReDoc URL

```text
/redoc
```

---

# 🚀 FastAPI with Database

FastAPI commonly works with:

* PostgreSQL
* MySQL
* SQLite
* MongoDB

Using:

* SQLAlchemy
* Tortoise ORM
* Prisma

---

# 📘 FastAPI + SQLAlchemy Example

```python
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
```

---

# 📘 Install Requirements

```bash
pip install sqlalchemy psycopg2
```

---

# 🔥 FastAPI vs Django vs Flask

| Feature           | FastAPI   | Flask      | Django        |
| ----------------- | --------- | ---------- | ------------- |
| Performance       | Very Fast | Fast       | Moderate      |
| Built-in Features | Medium    | Minimal    | Many          |
| Async Support     | Excellent | Limited    | Good          |
| Best For          | APIs      | Small Apps | Full Projects |

---

# 📘 Interview Questions

## ❓ Why FastAPI is Fast?

✅ ASGI support
✅ Async programming
✅ Starlette backend

---

## ❓ What is Pydantic?

Used for:

* Data validation
* Serialization
* Type checking

---

## ❓ Difference Between WSGI and ASGI

| WSGI         | ASGI         |
| ------------ | ------------ |
| Synchronous  | Asynchronous |
| Django/Flask | FastAPI      |
| Slower       | Faster       |

---

# 🎯 Real-Time Use Cases

| Use Case            | Example              |
| ------------------- | -------------------- |
| Authentication APIs | Login System         |
| E-commerce APIs     | Product APIs         |
| AI APIs             | ChatGPT Integrations |
| Mobile Backend      | Android/iOS APIs     |
| Microservices       | Internal services    |

---

# 🏁 Summary

| Topic    | Description          |
| -------- | -------------------- |
| FastAPI  | Python API Framework |
| Pydantic | Validation           |
| Uvicorn  | ASGI Server          |
| Swagger  | API Documentation    |
| Async    | High Performance     |
| JWT      | Authentication       |
