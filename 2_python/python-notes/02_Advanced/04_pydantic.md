# 📘 Pydantic

---

# 🔥 What is Pydantic?

**Pydantic** is a Python library used for:

* ✅ Data validation
* ✅ Data parsing
* ✅ Type checking
* ✅ Settings management

It uses Python type hints to validate data automatically.

---

# 🚀 Why Use Pydantic?

| Feature               | Description              |
| --------------------- | ------------------------ |
| ✅ Data Validation    | Validates input data     |
| ⚡ Fast Performance   | High-speed parsing       |
| 🧠 Type Safety        | Uses Python type hints   |
| 📘 Easy Serialization | Convert objects to JSON  |
| 🔥 FastAPI Support    | Mostly used with FastAPI |
| 🚀 Clean Code         | Better readability       |

---

# 📦 Install Pydantic

```bash
pip install pydantic
```

---

# 📘 Import Pydantic

```python
from pydantic import BaseModel
```

---

# 🔥 Basic Pydantic Model

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(
    name="Punith",
    age=25
)

print(user)

# Output:
# name='Punith' age=25
```

---

# 📘 Access Model Data

```python
print(user.name)
print(user.age)

# Output:
# Punith
# 25
```

---

# 🔥 Automatic Type Conversion

```python
from pydantic import BaseModel

class Employee(BaseModel):
    age: int

emp = Employee(age="30")

print(emp)

# Output:
# age=30
```

---

# 📘 Validation Error Example

```python
from pydantic import BaseModel

class User(BaseModel):
    age: int

user = User(age="abc")

# Output:
# ValidationError:
# value is not a valid integer
```

---

# 📘 Field Types

| Type      | Example |
| --------- | ------- |
| `str`   | Name    |
| `int`   | Age     |
| `float` | Salary  |
| `bool`  | Active  |
| `list`  | Skills  |
| `dict`  | Address |

---

# 🔥 Multiple Fields Example

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    marks: float
    active: bool

student = Student(
    name="Ravi",
    age=22,
    marks=88.5,
    active=True
)

print(student)

# Output:
# name='Ravi' age=22 marks=88.5 active=True
```

---

# 📘 Optional Fields

```python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    phone: Optional[str] = None

user = User(name="Punith")

print(user)

# Output:
# name='Punith' phone=None
```

---

# 📘 Default Values

```python
from pydantic import BaseModel

class Product(BaseModel):
    stock: int = 0

product = Product()

print(product)

# Output:
# stock=0
```

---

# 🔥 Convert Model to Dictionary

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(
    name="Punith",
    age=25
)

print(user.dict())

# Output:
# {
#     'name': 'Punith',
#     'age': 25
# }
```

---

# 📘 Convert Model to JSON

```python
print(user.json())

# Output:
# {
#   "name": "Punith",
#   "age": 25
# }
```

---

# 📘 Nested Models

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str

class User(BaseModel):
    name: str
    address: Address

user = User(
    name="Punith",
    address={
        "city": "Bangalore"
    }
)

print(user)

# Output:
# name='Punith' address=Address(city='Bangalore')
```

---

# 📘 List Validation

```python
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    skills: List[str]

user = User(
    skills=["Python", "Django"]
)

print(user)

# Output:
# skills=['Python', 'Django']
```

---

# 🔥 Email Validation

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr

user = User(
    email="test@gmail.com"
)

print(user)

# Output:
# email='test@gmail.com'
```

---

# 📘 Invalid Email Example

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr

user = User(
    email="invalid-email"
)

# Output:
# ValidationError:
# value is not a valid email address
```

---

# 📘 Field Validation Using validator

```python
from pydantic import BaseModel, validator

class User(BaseModel):
    age: int

    @validator("age")
    def validate_age(cls, value):

        if value < 18:
            raise ValueError(
                "Age must be above 18"
            )

        return value

user = User(age=20)

print(user)

# Output:
# age=20
```

---

# 📘 Validation Error Output

```python
user = User(age=10)

# Output:
# ValidationError:
# Age must be above 18
```

---

# 📘 Alias Fields

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    full_name: str = Field(alias="name")

user = User(name="Punith")

print(user)

# Output:
# full_name='Punith'
```

---

# 📘 Environment Variables with BaseSettings

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My App"

settings = Settings()

print(settings.app_name)

# Output:
# My App
```

---

# 🔥 Pydantic with FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user
```

---

# 📘 Input JSON

```json
{
  "name": "Punith",
  "age": 25
}
```

---

# ✅ API Response

```json
{
  "name": "Punith",
  "age": 25
}
```

---

# 🔥 Pydantic Features

| Feature         | Usage               |
| --------------- | ------------------- |
| BaseModel       | Create models       |
| Validation      | Validate data       |
| Serialization   | Convert to JSON     |
| Type Conversion | Auto conversion     |
| Nested Models   | Complex data        |
| Settings        | Environment configs |

---

# 📘 Real-Time Use Cases

| Use Case          | Example              |
| ----------------- | -------------------- |
| API Validation    | FastAPI requests     |
| Config Management | Environment settings |
| Data Parsing      | JSON validation      |
| Backend Systems   | User data validation |
| Form Validation   | Input checking       |

---

# 🔥 Interview Questions

## ❓ What is Pydantic?

Python library for data validation using type hints.

---

## ❓ Why use Pydantic?

✅ Automatic validation
✅ Cleaner code
✅ FastAPI integration

---

## ❓ What is BaseModel?

Base class used to create Pydantic models.

---

## ❓ What is ValidationError?

Raised when invalid data is passed.

---

## ❓ Difference Between dict() and json()

| dict()            | json()      |
| ----------------- | ----------- |
| Python dictionary | JSON string |

---

# 🏁 Summary

| Topic         | Description            |
| ------------- | ---------------------- |
| Pydantic      | Validation library     |
| BaseModel     | Model creation         |
| Validators    | Custom validation      |
| Serialization | JSON conversion        |
| EmailStr      | Email validation       |
| FastAPI       | API request validation |
