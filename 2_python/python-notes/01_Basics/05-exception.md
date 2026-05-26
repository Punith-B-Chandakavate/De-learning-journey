# 🐍 Python Object-Oriented Programming (OOPs), Exception Handling

# 🧠 Object-Oriented Programming (OOPs) in Python

Object-Oriented Programming (OOPs) is a programming paradigm used to organize and manage software efficiently.

It helps developers build:

- ♻️ Reusable code
- 📂 Well-structured applications
- 🛠 Easy-to-maintain projects
- 🚀 Scalable software systems

---

## 🏗 Core Concepts of OOPs

- 📦 Classes
- 👤 Objects
- 📌 Attributes
- ⚙️ Methods
- 🔧 Constructors

---

## 📦 Class

A **class** is a blueprint used to create objects.

```python
class User:
    pass
```

---

## 👤 Object

An **object** is an instance of a class.

```python
class User:
    pass

user1 = User()

print(type(user1))

# Output
# <class '__main__.User'>
```

---

## 📌 Attributes (Properties)

Attributes store object data.

```python
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User("Rahul", 21)

print(user1.name)
print(user1.age)

# Output
# Rahul
# 21
```

---

## ⚙️ Methods

Methods define object behavior.

```python
class User:

    def greet(self):
        print("Hello User")

user1 = User()

user1.greet()

# Output
# Hello User
```

---

## 🔧 Constructor — `__init__()`

The `__init__()` method initializes object attributes automatically when an object is created.

```python
class User:

    def __init__(self, name):
        self.name = name

user1 = User("Rahul")

print(user1.name)

# Output
# Rahul
```

---

## 🚀 Complete OOP Example

```python
class User:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating Object
user1 = User("Rahul", 21)

# Calling Method
user1.display()

# Output
# Name: Rahul
# Age: 21
```

---

## ⚡ Magic Methods (Dunder Methods)

Magic methods are special built-in methods surrounded by double underscores.

```python
__init__
__str__
__len__
```

They allow custom objects to behave like Python built-in objects.

---

## 🔧 Common Magic Methods

| Method | Description |
|--------|-------------|
| `__init__()` | Initialize object properties |
| `__str__()` | String representation |
| `__repr__()` | Official representation |
| `__len__()` | Return object length |
| `__del__()` | Called when object is deleted |
| `__eq__()` | Compare objects |
| `__add__()` | Add objects using `+` |

---

### 🖨 `__str__()` Method

Returns a readable string representation of an object.

```python
class User:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User Name: {self.name}"

user1 = User("Rahul")

print(user1)

# Output
# User Name: Rahul
```

---

### 📏 `__len__()` Method

Returns the length of an object.

```python
class Students:

    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)

obj = Students(["A", "B", "C"])

print(len(obj))

# Output
# 3
```

---

### ➕ `__add__()` Method

Defines behavior for the `+` operator.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

# Output
# 30
```

---

### ⚖️ `__eq__()` Method

Used to compare objects.

```python
class User:

    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

u1 = User(20)
u2 = User(20)

print(u1 == u2)

# Output
# True
```

---

### 🗑 `__del__()` Method

Called automatically when an object is deleted.

```python
class Test:

    def __del__(self):
        print("Object Deleted")

obj = Test()

del obj

# Output
# Object Deleted
```

---

## 🎯 Key Points

- 🏗 Class → Blueprint for objects
- 👤 Object → Instance of class
- 📌 Attributes → Store object data
- ⚙️ Methods → Define behavior
- 🔧 `__init__()` → Constructor
- ⚡ Magic Methods → Customize object behavior

---

## ✅ Advantages of OOPs

- ♻️ Code Reusability
- 📂 Better Code Organization
- 🔒 Data Security
- 🛠 Easy Maintenance
- 🚀 Faster Development
- 📈 Scalable Applications

# ⚠️ Exception Handling in Python

Exception Handling is used to handle runtime errors in a program without stopping the execution.

It helps developers:

- 🛡 Prevent program crashes
- 🧹 Write cleaner code
- 🔍 Handle errors properly
- 🚀 Improve application reliability

---

## 🧠 What is an Exception?

An **exception** is an error that occurs during program execution.

## Example

```python
print(10 / 0)

# Output
# ZeroDivisionError: division by zero
```

---

## 🔧 Basic Exception Handling

Python uses:

- `try`
- `except`

to handle exceptions.

### Example

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

# Output
# Cannot divide by zero
```

---

## 🛠 Try Block

The `try` block contains code that may cause an error.

```python
try:
    number = int("abc")

except:
    print("Error occurred")

# Output
# Error occurred
```

---

## 🚨 Except Block

The `except` block handles the error.

```python
try:
    num = 5 / 0

except ZeroDivisionError:
    print("Division by zero is not allowed")

# Output
# Division by zero is not allowed
```

---

## 🎯 Handling Multiple Exceptions

You can handle multiple exceptions separately.

```python
try:
    number = int("abc")
    print(10 / 0)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

# Output
# Invalid number
```

---

## 🧾 Using `else`

The `else` block runs if no exception occurs.

```python
try:
    number = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Division Successful")

# Output
# Division Successful
```

---

## 🧹 Using `finally`

The `finally` block always executes whether an exception occurs or not.

```python
try:
    file = open("sample.txt", "r")

except FileNotFoundError:
    print("File not found")

finally:
    print("Execution Completed")

# Output
# File not found
# Execution Completed
```

---

## 🚀 Complete Example

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program Finished")
```

---

## ⚡ Raising Exceptions

You can manually raise exceptions using `raise`.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")

# Output
# ValueError: Age cannot be negative
```

---

## 🏗 Custom Exception

You can create your own exception class.

```python
class InvalidAgeError(Exception):
    pass

age = -1

try:

    if age < 0:
        raise InvalidAgeError("Invalid Age")

except InvalidAgeError as error:
    print(error)

# Output
# Invalid Age
```

---

## 🔧 Common Built-in Exceptions

| Exception | Description |
|-----------|-------------|
| `ZeroDivisionError` | Division by zero |
| `ValueError` | Invalid value |
| `TypeError` | Invalid data type |
| `IndexError` | Invalid index |
| `KeyError` | Invalid dictionary key |
| `FileNotFoundError` | File not found |
| `NameError` | Variable not defined |

---

## 🎯 Key Points

- 🛡 Exceptions prevent program crashes
- 🔧 `try` → Contains risky code
- 🚨 `except` → Handles errors
- 🧾 `else` → Runs if no error occurs
- 🧹 `finally` → Always executes
- ⚡ `raise` → Manually raise exceptions

---

## ✅ Advantages of Exception Handling

- 🚀 Better user experience
- 🛡 Prevents unexpected crashes
- 🧹 Cleaner and readable code
- 🔍 Easier debugging
- ⚙️ Reliable applications
---

# 🚀 `__main__` in Python

In Python, `__main__` is a special built-in variable.

It is mainly used to control the execution of code.

---

## 🧠 What is `__main__`?

When a Python file runs directly, Python automatically sets:

```python
__name__ = "__main__"
```

This helps Python identify whether the file is:

- ▶️ Run directly
- 📦 Imported as a module

---

## 🔧 Basic Syntax

```python
if __name__ == "__main__":
    # code
```

---

## ✅ Example 1 — Running File Directly

```python
print(__name__)

# Output
# __main__
```

When the file is executed directly, the output becomes:

```python
__main__
```

---

## 🚀 Example 2 — Using `__main__`

```python
def greet():
    print("Hello Python")

if __name__ == "__main__":
    greet()

# Output
# Hello Python
```

The `greet()` function runs only when the file is executed directly.

---

## 📦 Why Use `__main__`?

Using `__main__` prevents certain code from executing when the file is imported into another file.

---

## 🛠 Example Without `__main__`

### 📄 file1.py

```python
print("File1 Executed")
```

### 📄 file2.py

```python
import file1

# Output
# File1 Executed
```

When importing `file1`, all code executes automatically.

---

## ✅ Example With `__main__`

### 📄 file1.py

```python
def greet():
    print("Hello User")

if __name__ == "__main__":
    greet()
```

### 📄 file2.py

```python
import file1

print("File Imported Successfully")

# Output
# File Imported Successfully
```

Now the `greet()` function does not execute automatically during import.

---

## 🎯 Real-World Use Cases

- 🚀 Running application entry point
- 🧪 Testing functions
- 📦 Creating reusable modules
- 🔒 Preventing unwanted execution
- ⚙️ Organizing large projects

---

## 🧾 Complete Example

```python
def add(a, b):
    return a + b

def main():

    result = add(10, 20)

    print("Result:", result)

if __name__ == "__main__":
    main()

# Output
# Result: 30
```

---

## 🔥 How It Works

| Situation | Value of `__name__` |
|-----------|--------------------|
| File runs directly | `"__main__"` |
| File imported | Module name |

---

## 🎯 Key Points

- `__main__` is a special built-in variable
- `if __name__ == "__main__"` checks how the file is executed
- Prevents automatic execution during import
- Helps create reusable Python modules

---

## ✅ Advantages of Using `__main__`

- 📦 Reusable code
- 🛡 Better project structure
- 🚀 Cleaner execution flow
- ⚙️ Easier testing
- 🔒 Prevents unwanted code execution