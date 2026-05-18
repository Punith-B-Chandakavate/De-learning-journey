# 🐍 Python Functions, Modules, PIP and File Handling

Functions are one of the most important building blocks in Python.
They help organize code, improve reusability, and make programs easier to maintain.

# 🚀 Python Functions

Functions help organize code into reusable blocks, making programs cleaner and easier to maintain.

---

## 📌 Defining a Function

Functions are created using the `def` keyword.

```python
def greet():
    print("Hello, World!")

greet()
```

💡 Useful when repeating the same task multiple times.

---

## 📥 Function Parameters

Parameters allow functions to receive input values.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("John")
```

💡 Helpful for working with dynamic data like usernames, prices, or scores.

---

## 🔁 Return Statement

The `return` statement sends data back to the caller.

```python
def add(a, b):
    return a + b

result = add(5, 3)

print(result)
```

💡 Commonly used in calculations and data processing.

---

## ⚙️ Default Parameters

Default values are used when no argument is provided.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Alice")
```

💡 Useful for optional inputs and default settings.

---

## 🎯 Positional & Keyword Arguments

Python supports both positional and keyword arguments.

### ✅ Positional Argument

```python
def student(name, age):
    print(name, age)

student("John", 20)
```

### ✅ Keyword Argument

```python
def student(name, age):
    print(name, age)

student(age=20, name="John")
```

💡 Keyword arguments improve readability.

---

## ⚡ Lambda Functions

Lambda functions are short one-line anonymous functions.

```python
square = lambda x: x * x

print(square(5))
```

💡 Often used in sorting, filtering, and quick operations.

---

## 🧠 Benefits of Functions

- ✅ Code Reusability
- ✅ Better Organization
- ✅ Easier Debugging
- ✅ Improved Readability
- ✅ Reduced Repetition

---

## 📚 Real-World Use Cases

| Scenario        | Usage                 |
| --------------- | --------------------- |
| Calculator App  | Perform calculations  |
| Login System    | Validate users        |
| E-commerce Site | Calculate discounts   |
| Data Analysis   | Process datasets      |
| Games           | Handle player actions |

---

# 🤖 Python Modules & PIP

Python modules and pip help developers write reusable code and install external libraries easily.

---

## 📦 Python Modules

Modules are Python files containing reusable functions, classes, and variables.

### ✅ Importing Modules

```python
import math

print(math.sqrt(25))
print(math.pi)
```

### ✅ Import Specific Functions

```python
from math import sqrt

print(sqrt(49))
```

### ✅ Using Aliases

```python
import numpy as np

numbers = np.array([1, 2, 3])

print(numbers)
```

### ✅ Creating Your Own Module

#### 📄 my_module.py

```python
def greet(name):
    return f"Hello, {name}"
```

#### 📄 main.py

```python
import my_module

print(my_module.greet("John"))
```

---

## 📚 Common Python Modules

| Module       | Purpose                |
| ------------ | ---------------------- |
| `math`     | Math operations        |
| `random`   | Random values          |
| `datetime` | Date & time            |
| `os`       | Operating system tasks |
| `sys`      | System functions       |
| `json`     | JSON handling          |

---

## 🚀 Module Use Cases

- 📊 Data Analysis
- 🌐 Web Development
- 🤖 Automation
- 🎮 Game Development
- 🔗 API Integration

---

## 📥 Python PIP

`pip` is Python’s package manager used to install and manage libraries.

#### ✅ Check Pip Version

```bash
pip --version
```

#### ✅ Install Packages

```bash
pip install numpy
```

```bash
pip install pandas matplotlib
```

#### ✅ Uninstall Packages

```bash
pip uninstall numpy
```

#### ✅ View Installed Packages

```bash
pip list
```

#### ✅ Upgrade Packages

```bash
pip install --upgrade numpy
```

---

### 📄 requirements.txt

#### ✅ Create requirements file

```bash
pip freeze > requirements.txt
```

#### ✅ Install from requirements file

```bash
pip install -r requirements.txt
```

---

### 🌐 Popular Python Packages

| Package        | Purpose             |
| -------------- | ------------------- |
| `numpy`      | Numerical computing |
| `pandas`     | Data analysis       |
| `matplotlib` | Data visualization  |
| `requests`   | API handling        |
| `flask`      | Web development     |
| `django`     | Backend framework   |

---

### 💡 Example

```bash
pip install requests
```

```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
```

---

# 📂 File Handling

File handling is used to create, read, update, and delete files in a program.

## ✨ Common File Operations

| Icon | Operation | Description |
|------|------------|-------------|
| 📖 | Read File | Open and read file content |
| ✍️ | Write File | Create or overwrite a file |
| ➕ | Append File | Add new content to existing file |
| ❌ | Delete File | Remove a file from the system |
| 📁 | Open File | Access a file using file path |
| 🔒 | Close File | Close the opened file safely |

---

## 🐍 Python File Handling Example


## 📌 File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read file |
| `"w"` | Write file (overwrite) |
| `"a"` | Append content |
| `"x"` | Create new file |
| `"t"` | Text mode |
| `"b"` | Binary mode |
| `"r+"` | Read & write |
| `"w+"` | Write & read |
| `"a+"` | Append & read |

---

### 📖 1. Read Mode (`"r"`)

```python
file = open("sample.txt", "r")
print(file.read())
file.close()
````

✅ Reads file content

---

### ✍️ 2. Write Mode (`"w"`)

```python
file = open("sample.txt", "w")
file.write("Hello World")
file.close()
```

⚠️ Overwrites existing content

---

### ➕ 3. Append Mode (`"a"`)

```python
file = open("sample.txt", "a")
file.write("\nNew Line Added")
file.close()
```

✅ Adds content without deleting old data

---

### 🆕 4. Create Mode (`"x"`)

```python
file = open("newfile.txt", "x")
file.write("New File Created")
file.close()
```

⚠️ Gives error if file already exists

---

### 🔄 5. Read & Write Mode (`"r+"`)

```python
file = open("sample.txt", "r+")
print(file.read())

file.write("\nAdded using r+")
file.close()
```

✅ Read and write both

---

### 📝 6. Write & Read Mode (`"w+"`)

```python
file = open("sample.txt", "w+")
file.write("New Content")

file.seek(0)
print(file.read())

file.close()
```

⚠️ Deletes old content first

---

### ➕📖 7. Append & Read Mode (`"a+"`)

```python
file = open("sample.txt", "a+")
file.write("\nAppended Text")

file.seek(0)
print(file.read())

file.close()
```

✅ Append and read together

---

### 📄 8. Text Mode (`"t"`)

```python
file = open("sample.txt", "rt")
print(file.read())
file.close()
```

✅ Default mode for text files

---

### 🖼 9. Binary Mode (`"b"`)

```python
file = open("image.png", "rb")
data = file.read()

print(data)
file.close()
```

✅ Used for images, videos, PDFs, etc.

---

## ✅ Best Practice (`with open`)

```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

✅ Automatically closes the file

---

## 🚀 Advantages of File Handling

* 📦 Permanent data storage
* ⚡ Easy file management
* 🔄 Read/update anytime
* 🛠 Useful for logs, reports, and backups

```
