from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None  # Optional field with default value None
    address: Optional[str] = None  # Optional field with default value None


# Example usage

user_data = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
}

user = User(**user_data)

print('User:', user)
print('User Name:', user.name)
print('User Email:', user.email)
print('User Age:', user.age)
print('User Address:', user.address)

