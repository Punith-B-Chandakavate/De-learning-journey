# Python Advanced: JSON & APIs

---

# 🔹 Working with JSON

## 📘 What is JSON?

**JSON (JavaScript Object Notation)** is a lightweight format used to store and exchange data between applications and APIs.

✅ Easy to read
✅ Human-friendly
✅ Mostly used in Web APIs

---

## 🧩 JSON Data Types

| Type    | Example                              |
| ------- | ------------------------------------ |
| String  | `"name": "Punith"`                 |
| Number  | `"age": 25`                        |
| Boolean | `"active": true`                   |
| Array   | `"skills": ["Python", "Django"]`   |
| Object  | `"address": {"city": "Bangalore"}` |
| Null    | `"data": null`                     |

---

## ⚙️ Python JSON Methods

| Method           | Description                   |
| ---------------- | ----------------------------- |
| `json.dumps()` | Convert Python → JSON string |
| `json.loads()` | Convert JSON string → Python |
| `json.dump()`  | Write JSON to file            |
| `json.load()`  | Read JSON from file           |

---

## 💻 Example: Python to JSON

```python
import json

data = {
    "name": "Punith",
    "age": 25
}

json_data = json.dumps(data)

print(json_data)
print(type(json_data))
```

### ✅ Output

```python
{"name": "Punith", "age": 25}
<class 'str'>
```

---

## 💻 Example: JSON to Python

```python
import json

json_text = '{"course":"Python","duration":3}'

data = json.loads(json_text)

print(data)
print(type(data))
```

### ✅ Output

```python
{'course': 'Python', 'duration': 3}
<class 'dict'>
```

---

# 🌐 What is API?

## 📘 Definition

**API (Application Programming Interface)** allows two applications to communicate with each other.

Example:

* Mobile App ↔ Server
* Frontend ↔ Backend
* Python ↔ Weather API

---

## 🔥 Types of APIs

| API Type      | Description                      |
| ------------- | -------------------------------- |
| REST API      | Most commonly used web API       |
| SOAP API      | XML-based secure API             |
| GraphQL API   | Client requests only needed data |
| WebSocket API | Real-time communication          |

---

## 📡 Common HTTP Methods

| Method | Purpose              |
| ------ | -------------------- |
| GET    | Fetch data           |
| POST   | Create data          |
| PUT    | Update complete data |
| PATCH  | Update partial data  |
| DELETE | Remove data          |

---

## 🧠 API Flow

```text
Client Request → Server → Database → Response(JSON)
```

---

# 🔹 Calling APIs with `requests` Package

## 📘 What is `requests`?

`requests` is a Python library used to send HTTP requests easily.

Install:

```bash
pip install requests
```

---

## ⚙️ Common Methods in requests

| Method                | Use         |
| --------------------- | ----------- |
| `requests.get()`    | Fetch data  |
| `requests.post()`   | Send data   |
| `requests.put()`    | Update data |
| `requests.delete()` | Delete data |

---

## 💻 Example: GET Request

```python
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print(response.status_code)
print(response.json())
```

### ✅ Output

```python
200

{
  'id': 1,
  'name': 'Leanne Graham',
  'username': 'Bret'
}
```

---

## 💻 Example: POST Request

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python API",
    "body": "Learning requests package",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
```

### ✅ Output

```python
201

{
  'title': 'Python API',
  'body': 'Learning requests package',
  'userId': 1,
  'id': 101
}
```

---

## 🔥 Important Response Methods

| Method                   | Description              |
| ------------------------ | ------------------------ |
| `response.status_code` | HTTP status              |
| `response.json()`      | Convert response to JSON |
| `response.text`        | Response as string       |
| `response.headers`     | Response headers         |

---

# 🎯 Quick Interview Questions

## ❓ Difference Between JSON and Dictionary

| JSON                   | Python Dictionary         |
| ---------------------- | ------------------------- |
| String format          | Python object             |
| Uses double quotes     | Uses single/double quotes |
| Used for data exchange | Used inside Python        |

---

## ❓ Why APIs Use JSON?

✅ Lightweight
✅ Easy to parse
✅ Language independent
✅ Faster data exchange

---

# 🏁 Summary

| Topic    | Key Point                  |
| -------- | -------------------------- |
| JSON     | Data exchange format       |
| API      | Communication between apps |
| requests | Call APIs in Python        |
| FastAPI  | Build APIs quickly         |
