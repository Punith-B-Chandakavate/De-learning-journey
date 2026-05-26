## 📋 Lists, String, Tuple and Dictionaries in Python

# 📋 Python Lists

- 🗂️ Lists are used to store multiple items in a single variable.
- 📍 Lists are **ordered**, meaning each element has a fixed position unless it is changed manually.
- 🔄 Lists are **mutable**, so elements can be added, removed, or modified after creation.
- 🎯 Python lists can store different data types in the same list, such as integers, floats, strings, booleans, and even other lists.

  Example:

```python
l = ["car", 4.5, True]
```

- ✂️ **List slicing** allows you to access a specific range of elements using the syntax:

```python
list[start:end:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[::2])   # [10, 30, 50]
```

---

## 📏 Rules of Python Lists

* ✅ Lists are created using square brackets `[]`
* ✅ Indexing starts from `0`
* ✅ Negative indexing is supported
* ✅ Duplicate values are allowed
* ✅ Lists can contain nested lists

Example:

```python
data = [1, 2, 2, "Python", [10, 20]]
```

---

## 🛠️ Python List Methods

| Method         | Description              | Example               |
| -------------- | ------------------------ | --------------------- |
| `.append()`  | Adds item at end         | `l.append(100)`     |
| `.clear()`   | Removes all items        | `l.clear()`         |
| `.copy()`    | Returns copy of list     | `l.copy()`          |
| `.count()`   | Counts occurrences       | `l.count(10)`       |
| `.extend()`  | Adds multiple items      | `l.extend([1,2])`   |
| `.index()`   | Returns item index       | `l.index(20)`       |
| `.insert()`  | Inserts item at position | `l.insert(1, "AI")` |
| `.pop()`     | Removes item using index | `l.pop(0)`          |
| `.remove()`  | Removes specific item    | `l.remove(20)`      |
| `.reverse()` | Reverses list            | `l.reverse()`       |
| `.sort()`    | Sorts list               | `l.sort()`          |

## 💡 Example

```python
fruits = ["apple", "banana"]

fruits.append("mango")
print(fruits)

fruits.remove("banana")
print(fruits)
```

---

# 🧵 Python Strings

- 🔒 Strings in Python are **immutable**, meaning they cannot be changed once they are created.
- 📝 Strings can be created using:

  - Single quotes → `'Python'`
  - Double quotes → `"Python"`
  - Triple quotes → `'''Python'''`
- 🔍 Access string characters using:

  - **Indexing** → `text[0]`
  - **Slicing** → `text[1:5]`
- ✨ Use **f-strings** for readable string formatting.

  Example:

  ```python
  name = "John"
  print(f"Hello {name}")
  ```

---

## 📏 Rules of Python Strings

- ✅ Strings are ordered sequences
- ✅ Strings support indexing and slicing
- ✅ Strings are immutable
- ✅ Strings allow duplicate characters
- ✅ Strings support negative indexing

---

## 🛠️ Python String Methods

| Method              | Description                               | Example                        |
| ------------------- | ----------------------------------------- | ------------------------------ |
| `.capitalize()`   | Capitalizes first letter                  | `"python".capitalize()`      |
| `.casefold()`     | Converts string to lowercase aggressively | `"PyThOn".casefold()`        |
| `.center(width)`  | Centers string                            | `"Hi".center(10)`            |
| `.count()`        | Counts occurrences                        | `"hello".count("l")`         |
| `.encode()`       | Encodes string                            | `"hello".encode()`           |
| `.endswith()`     | Checks ending                             | `"python".endswith("on")`    |
| `.expandtabs()`   | Expands tabs into spaces                  | `"H\ti".expandtabs(4)`       |
| `.find()`         | Finds substring position                  | `"python".find("t")`         |
| `.format()`       | Formats string                            | `"Hello {}".format("John")`  |
| `.format_map()`   | Formats using mapping                     | `"{x}".format_map({'x':10})` |
| `.index()`        | Finds substring index                     | `"python".index("t")`        |
| `.isalnum()`      | Checks alphanumeric                       | `"abc123".isalnum()`         |
| `.isalpha()`      | Checks alphabets only                     | `"Python".isalpha()`         |
| `.isascii()`      | Checks ASCII characters                   | `"abc".isascii()`            |
| `.isdecimal()`    | Checks decimal characters                 | `"123".isdecimal()`          |
| `.isdigit()`      | Checks digits                             | `"123".isdigit()`            |
| `.isidentifier()` | Checks valid identifier                   | `"var_1".isidentifier()`     |
| `.islower()`      | Checks lowercase                          | `"python".islower()`         |
| `.isnumeric()`    | Checks numeric characters                 | `"123".isnumeric()`          |
| `.isprintable()`  | Checks printable characters               | `"Hello".isprintable()`      |
| `.isspace()`      | Checks whitespace                         | `"   ".isspace()`            |
| `.istitle()`      | Checks title case                         | `"Hello World".istitle()`    |
| `.isupper()`      | Checks uppercase                          | `"PYTHON".isupper()`         |
| `.join()`         | Joins iterable items                      | `"-".join(["a","b"])`        |
| `.ljust()`        | Left aligns string                        | `"Hi".ljust(10)`             |
| `.lower()`        | Converts to lowercase                     | `"PYTHON".lower()`           |
| `.lstrip()`       | Removes left spaces                       | `"  hi".lstrip()`            |
| `.maketrans()`    | Creates translation table                 | `str.maketrans("a","b")`     |
| `.partition()`    | Splits into 3 parts                       | `"a-b".partition("-")`       |
| `.replace()`      | Replaces substring                        | `"Hello".replace("H","J")`   |
| `.rfind()`        | Finds from right side                     | `"hello".rfind("l")`         |
| `.rindex()`       | Finds index from right                    | `"hello".rindex("l")`        |
| `.rjust()`        | Right aligns string                       | `"Hi".rjust(10)`             |
| `.rpartition()`   | Splits from right                         | `"a-b-c".rpartition("-")`    |
| `.rsplit()`       | Splits from right                         | `"a,b,c".rsplit(",")`        |
| `.rstrip()`       | Removes right spaces                      | `"hi   ".rstrip()`           |
| `.split()`        | Splits string                             | `"a,b,c".split(",")`         |
| `.splitlines()`   | Splits lines                              | `"a\nb".splitlines()`        |
| `.startswith()`   | Checks starting                           | `"python".startswith("py")`  |
| `.strip()`        | Removes spaces                            | `"  hi  ".strip()`           |
| `.swapcase()`     | Swaps uppercase/lowercase                 | `"PyThOn".swapcase()`        |
| `.title()`        | Converts to title case                    | `"hello world".title()`      |
| `.translate()`    | Translates characters                     | `"abc".translate(table)`     |
| `.upper()`        | Converts to uppercase                     | `"python".upper()`           |
| `.zfill()`        | Adds leading zeros                        | `"5".zfill(3)`               |

---

## 💡 Example

```python
text = "  Python Programming  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python", "Java"))
print(text.split())
print(text.startswith(" "))
```

# 🧩 Python Tuples

- 🔒 Tuples in Python are **immutable**, meaning their values cannot be changed after creation.
- 📦 Tuples are used to store multiple items in a single variable.
- 📝 Tuples are created using parentheses `()`.

## ✅ Creating a Tuple

```python
numbers = (1, 2, 3, 4, 5)
print(numbers)
```

---

## 📏 Rules of Python Tuples

- ✅ Tuples are ordered collections
- ✅ Tuples are immutable
- ✅ Tuples allow duplicate values
- ✅ Tuples support indexing and slicing
- ✅ Tuples can store different data types

---

## 🔍 Accessing Tuple Elements

### ✅ Indexing

```python
colors = ("red", "green", "blue")

print(colors[0])
print(colors[-1])
```

### ✅ Slicing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

---

## 🛠️ Python Tuple Methods

| Method | Description | Example |
|--------|-------------|---------|
| `.count()` | Counts occurrences of a value | `(1,2,2,3).count(2)` |
| `.index()` | Finds index of value | `(10,20,30).index(20)` |

---

## 💡 Tuple Example

```python
student = ("John", 21, "Python")

print(student[0])
print(student.count("Python"))
print(student.index(21))
```

---

## 🚀 Tuple Use Cases

| Scenario | Usage |
|----------|------|
| Database Records | Store fixed data |
| Coordinates | Store x and y values |
| Configuration Settings | Store constant values |
| Returning Multiple Values | Return multiple results from functions |

---

# 📘 Python Dictionaries

- 📚 Dictionaries store data in **key-value pairs**.
- ⚡ Dictionaries are mutable, meaning they can be modified.
- 📝 Dictionaries are created using curly braces `{}`.

## ✅ Creating a Dictionary

```python
student = {
    "name": "John",
    "age": 21,
    "course": "Python"
}

print(student)
```

---

## 📏 Rules of Python Dictionaries

- ✅ Dictionaries store key-value pairs
- ✅ Keys must be unique
- ✅ Dictionaries are mutable
- ✅ Dictionaries are ordered (Python 3.7+)
- ✅ Values can be duplicated

---

## 🔍 Accessing Dictionary Values

```python
student = {
    "name": "Alice",
    "age": 22
}

print(student["name"])
print(student.get("age"))
```

---

## ➕ Adding & Updating Values

```python
student = {
    "name": "John"
}

student["age"] = 21

print(student)
```

---

## ❌ Removing Values

```python
student = {
    "name": "John",
    "age": 21
}

student.pop("age")

print(student)
```

---

## 🛠️ Python Dictionary Methods

| Method | Description | Example |
|--------|-------------|---------|
| `.get()` | Gets value by key | `dict.get("name")` |
| `.keys()` | Returns all keys | `dict.keys()` |
| `.values()` | Returns all values | `dict.values()` |
| `.items()` | Returns key-value pairs | `dict.items()` |
| `.pop()` | Removes specified key | `dict.pop("age")` |
| `.update()` | Updates dictionary | `dict.update({"age":21})` |
| `.clear()` | Removes all items | `dict.clear()` |
| `.copy()` | Creates copy of dictionary | `dict.copy()` |

---

## 💡 Dictionary Example

```python
employee = {
    "name": "David",
    "salary": 50000,
    "role": "Developer"
}

print(employee.keys())
print(employee.values())
print(employee.items())
```

---

## 🚀 Dictionary Use Cases

| Scenario | Usage |
|----------|------|
| User Profiles | Store user information |
| APIs | Store JSON data |
| Inventory Systems | Store product details |
| Student Records | Store marks and grades |

---

# 🎉 Conclusion

Lists, Strings, Tuples, and Dictionaries are essential Python data structures that help developers store, organize, and manage data efficiently.

- 📋 **Lists** are best for storing ordered and changeable collections of items.
- 🔤 **Strings** are used for handling and manipulating text data.
- 📦 **Tuples** are ideal for fixed and unchangeable data.
- 📚 **Dictionaries** are perfect for storing structured key-value data.
