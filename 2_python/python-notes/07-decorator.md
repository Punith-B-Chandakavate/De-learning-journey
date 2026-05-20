# 🎭 Decorators in Python

Decorators are used to modify or extend the behavior of functions or methods without changing their original code.

They are commonly used for:

- 📝 Logging
- ⏱ Timing functions
- 🔒 Authentication
- ✅ Validation
- 📊 Monitoring

---

# 🧠 What is a Decorator?

A decorator is a function that takes another function as an argument and returns a new function.

---

# 🔧 Basic Syntax

```python
@decorator_name
def function():
    pass
```

---

# 🚀 Simple Decorator Example

```python
def decorator_function(original_function):

    def wrapper_function():

        print("Before Function Call")

        original_function()

        print("After Function Call")

    return wrapper_function


@decorator_function
def display():

    print("Hello Python")


display()

# Output
# Before Function Call
# Hello Python
# After Function Call
```

---

# 🔍 How Decorators Work

This:

```python
@decorator_function
def display():
    print("Hello")
```

is internally equivalent to:

```python
def display():
    print("Hello")

display = decorator_function(display)
```

---

# ⚙️ Decorator Without `@` Symbol

```python
def decorator_function(func):

    def wrapper():

        print("Decorator Executed")

        func()

    return wrapper


def greet():

    print("Hello User")


decorated = decorator_function(greet)

decorated()

# Output
# Decorator Executed
# Hello User
```

---

# 📦 Decorator with Arguments

Decorators can also handle function arguments using `*args` and `**kwargs`.

```python
def decorator_function(func):

    def wrapper(*args, **kwargs):

        print("Function Started")

        func(*args, **kwargs)

        print("Function Ended")

    return wrapper


@decorator_function
def add(a, b):

    print(a + b)


add(10, 20)

# Output
# Function Started
# 30
# Function Ended
```

---

# ⏱ Timing Decorator Example

Used to measure function execution time.

```python
import time

def timer(func):

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print("Execution Time:", end - start)

    return wrapper


@timer
def process():

    time.sleep(2)

    print("Processing...")


process()

# Output
# Processing...
# Execution Time: 2.0
```

---

# 📝 Logging Decorator

Used to log function calls.

```python
def logger(func):

    def wrapper():

        print(f"Calling Function: {func.__name__}")

        func()

    return wrapper


@logger
def greet():

    print("Hello User")


greet()

# Output
# Calling Function: greet
# Hello User
```

---

# 🔒 Authentication Decorator Example

```python
def authenticate(func):

    def wrapper(user):

        if user == "admin":

            func(user)

        else:

            print("Access Denied")

    return wrapper


@authenticate
def dashboard(user):

    print("Welcome", user)


dashboard("admin")
dashboard("guest")

# Output
# Welcome admin
# Access Denied
```

---

# 🏛 Multiple Decorators

More than one decorator can be applied to a function.

```python
def bold(func):

    def wrapper():

        return "<b>" + func() + "</b>"

    return wrapper


def italic(func):

    def wrapper():

        return "<i>" + func() + "</i>"

    return wrapper


@bold
@italic
def text():

    return "Hello"


print(text())

# Output
# <b><i>Hello</i></b>
```

---

# 🧩 Built-in Decorators

Python provides built-in decorators.

| Decorator | Purpose |
|-----------|----------|
| `@staticmethod` | Static method |
| `@classmethod` | Class method |
| `@property` | Getter method |

---

# ⚡ `@staticmethod`

```python
class Math:

    @staticmethod
    def add(a, b):

        return a + b

print(Math.add(10, 20))

# Output
# 30
```

---

# 🏛 `@classmethod`

```python
class Student:

    school = "ABC School"

    @classmethod
    def get_school(cls):

        return cls.school

print(Student.get_school())

# Output
# ABC School
```

---

# 📌 `@property`

Used to access methods like attributes.

```python
class User:

    def __init__(self, name):

        self._name = name

    @property
    def name(self):

        return self._name


user = User("Rahul")

print(user.name)

# Output
# Rahul
```

---

# 🎯 Key Points

- 🎭 Decorators modify function behavior
- ⚙️ Functions are first-class objects in Python
- 📦 Decorators can accept arguments
- 🏛 Multiple decorators can be chained
- 🔒 Useful for logging, validation, authentication

---

# ✅ Advantages of Decorators

- ♻️ Code Reusability
- 🧹 Cleaner Code
- 🚀 Better Function Management
- 🔒 Easier Authentication and Validation
- 📊 Useful for Logging and Monitoring