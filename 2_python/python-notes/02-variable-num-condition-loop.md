# 🧮 Variables, Numbers, Condition and Loop in Python

---

# 📦 Variables in Python

A **variable** is a container used to store data in Python.

---

## 🧠 Python Data Types

Python provides several built-in data types to store different kinds of values.

---

## 📦 Main Categories of Data Types

| 📂 Category    | 📌 Data Types                            |
| -------------- | ---------------------------------------- |
| Numeric Types  | `int`, `float`, `complex`          |
| Sequence Types | `str`, `list`, `tuple`, `range`  |
| Mapping Type   | `dict`                                 |
| Set Types      | `set`, `frozenset`                   |
| Boolean Type   | `bool`                                 |
| Binary Types   | `bytes`, `bytearray`, `memoryview` |
| None Type      | `NoneType`                             |

---

## 🔢 Numeric Data Types

### 1️⃣ Integer (`int`)

Stores whole numbers.

```python
x = 10
y = -50
```

---

### 2️⃣ Float (`float`)

Stores decimal numbers.

```python
pi = 3.14
height = 5.9
```

---

### 3️⃣ Complex (`complex`)

Stores complex numbers.

```python
z = 2 + 3j
```

---

## 🔤 Sequence Data Types

### 1️⃣ String (`str`)

Stores text data.

```python
name = "Python"
```

---

### 2️⃣ List (`list`)

Ordered and mutable collection.

```python
numbers = [1, 2, 3, 4]
```

#### ✅ Features

* Ordered
* Changeable (mutable)
* Allows duplicate values

---

### 3️⃣ Tuple (`tuple`)

Ordered and immutable collection.

```python
colors = ("red", "green", "blue")
```

#### ✅ Features

* Ordered
* Cannot be changed (immutable)
* Allows duplicates

---

### 4️⃣ Range (`range`)

Represents a sequence of numbers.

```python
x = range(5)
```

---

## 🗂️ Mapping Data Type

### Dictionary (`dict`)

Stores data in key-value pairs.

```python
student = {
    "name": "John",
    "age": 20
}
```

#### ✅ Features

* Key-value format
* Mutable
* Keys must be unique

---

## 🧩 Set Data Types

### 1️⃣ Set (`set`)

Unordered collection of unique values.

```python
nums = {1, 2, 3, 4}
```

#### ✅ Features

* No duplicates
* Unordered
* Mutable

---

### 2️⃣ Frozen Set (`frozenset`)

Immutable version of a set.

```python
fset = frozenset([1, 2, 3])
```

---

## ✅ Boolean Data Type

### Boolean (`bool`)

Represents True or False values.

```python
is_logged_in = True
is_admin = False
```

---

## 💾 Binary Data Types

### 1️⃣ Bytes (`bytes`)

Immutable binary data.

```python
x = b"hello"
```

---

### 2️⃣ Bytearray (`bytearray`)

Mutable binary data.

```python
x = bytearray(5)
```

---

### 3️⃣ Memoryview (`memoryview`)

Accesses memory of binary objects.

```python
x = memoryview(bytes(5))
```

---

## 🚫 None Data Type

### NoneType (`None`)

Represents absence of value.

```python
x = None
```

---

## 🔍 Check Data Type

Use `type()` function.

```python
x = 10
print(type(x))
```

Output:

```python
<class 'int'>
```

---

## 📚 Summary Table

| 📌 Data Type   | ✅ Example               |
| -------------- | ------------------------ |
| `int`        | `10`                   |
| `float`      | `3.14`                 |
| `complex`    | `2 + 3j`               |
| `str`        | `"Hello"`              |
| `list`       | `[1, 2, 3]`            |
| `tuple`      | `(1, 2, 3)`            |
| `range`      | `range(5)`             |
| `dict`       | `{"name": "John"}`     |
| `set`        | `{1, 2, 3}`            |
| `frozenset`  | `frozenset([1,2])`     |
| `bool`       | `True`                 |
| `bytes`      | `b"hello"`             |
| `bytearray`  | `bytearray(5)`         |
| `memoryview` | `memoryview(bytes(5))` |
| `NoneType`   | `None`                 |

---

## 🔍 Checking Data Types

Use the `type()` function to check the datatype of a variable.

```python
age = 25
print(type(age))
```

Output:

```python
<class 'int'>
```

---

## 🆔 Memory ID of Variables

Every variable in Python has a unique memory location.

Use `id()` to check the memory ID.

```python
x = 10

print(id(x))
```

---

## 📛 Rules for Naming Variables

### ✅ Valid Rules

* Variable names must start with:

  * a letter (`a-z`, `A-Z`)
  * or an underscore (`_`)
* Variable names can contain:

  * letters
  * numbers
  * underscores (`_`)
* Underscore `_` is a valid character and can be used anywhere after the first character.

---

## ❌ Invalid Rules

### 1️⃣ Do Not Use Reserved Keywords

```python
# ❌ Invalid
def = 10
True = False
```

---

### 2️⃣ Variable Names Cannot Start With Numbers

```python
# ❌ Invalid
1name = "John"
```

---

### 3️⃣ No Spaces Allowed

```python
# ❌ Invalid
my name = "Python"
```

---

### 4️⃣ No Special Characters Allowed

```python
# ❌ Invalid
name@ = "John"
price# = 100
```

Special characters like:

```text
!, @, #, $, %, ^, &, *
```

are not allowed.

---

## ✅ Valid Variable Names

```python
name = "Python"
_age = 25
student_name = "John"
price_1 = 100
```

---

## ❌ Invalid Variable Names

```python
1name = "Python"
my-name = "John"
class = "Python"
student name = "Alex"
```

---

## 🎯 Best Practices for Variable Names

✅ Use meaningful names

```python
student_name = "John"
total_marks = 95
```

❌ Avoid unclear names

```python
a = "John"
x = 95
```

---

## Numbers

- 🔢 **Integer (`int`)** stores whole numbers without a decimal part.Example: `57`
- 🎯 **Float (`float`)** stores fractional numbers with both whole and decimal parts.Example: `57.23`
- 🕵️ `type(variable_name)` is used to detect the data type of a variable.
- ➗ `/` is the division operator and returns a float value.
- 📉 `//` is the floor division operator and returns only the integer part of the result.
- 🧮 `%` is the modulo operator and returns the remainder of a division.
- ⚡ `x ** y` means “x raised to the power of y”.
- 🔄 Type casting can be done using functions such as `float()`, `int()`, and `str()`.
- 🧷 `float("10.2")` converts the string `"10.2"` into the float value `10.2`.
- 📚 The `math` module provides useful mathematical functions such as:

  - `sqrt()` → square root
  - `floor()` → rounds down
  - `ceil()` → rounds up

---

# 🔀 Python Conditional Statements (`if`)

Conditional statements are used to make decisions in Python based on conditions.

Python supports:
- ✅ `if`
- 🔁 `if-else`
- 🔀 `if-elif-else`
- 🎯 Nested `if`
- ⚡ Short-hand conditions

---

## ✅ `if` Statement

The `if` statement executes a block of code only if the condition is `True`.

### 📌 Syntax

```python
if condition:
    # code block
```

### 💡 Example

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```

---

## 🔁 `if-else` Statement

The `else` block executes when the condition is `False`.

### 📌 Syntax

```python
if condition:
    # code block
else:
    # code block
```

### 💡 Example

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

---

## 🔀 `if-elif-else` Statement

Used when multiple conditions need to be checked.

### 📌 Syntax

```python
if condition1:
    # code block
elif condition2:
    # code block
else:
    # code block
```

### 💡 Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

## 🎯 Nested `if` Statement

An `if` statement inside another `if` statement is called a nested `if`.

### 💡 Example

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
```

---

## ⚡ Short-hand `if`

Python allows writing simple `if` statements in one line.

### 💡 Example

```python
age = 20

if age >= 18: print("Adult")
```

---

## ⚡ Short-hand `if-else` (Ternary Operator)

Used to write `if-else` in a single line.

### 💡 Example

```python
age = 17

print("Adult") if age >= 18 else print("Minor")
```

---

## 🧠 Logical Operators in Conditions

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Returns True if both conditions are True | `x > 5 and x < 10` |
| `or` | Returns True if one condition is True | `x > 5 or x < 3` |
| `not` | Reverses condition result | `not(x > 5)` |

---

## ⚖️ Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

## 💡 Example Using Logical Operators

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
```

---

## 🚨 Important Notes

- ✅ Indentation is mandatory in Python.
- ✅ Conditions must return `True` or `False`.
- ✅ Multiple conditions can be combined using logical operators.
- ✅ Nested conditions are supported.

---

## 🛠️ Useful Functions in Conditions

| Function | Description | Example |
|----------|-------------|---------|
| `len()` | Returns length | `len(name)` |
| `type()` | Returns data type | `type(x)` |
| `isinstance()` | Checks object type | `isinstance(x, int)` |

---

## 💡 Example Using `len()`

```python
password = "python123"

if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")
```

---

# 🔁 Python Loops

Loops are used to execute a block of code repeatedly.

Python mainly supports:
- 🔄 `for` loop
- ♾️ `while` loop
- 🎯 Nested loops
- ⚡ Loop control statements (`break`, `continue`, `pass`)

---

## 🔁 `for` Loop

A `for` loop is used to iterate through sequences like lists, tuples, strings, dictionaries, or ranges.

### ✅ Syntax

```python
for variable in sequence:
    # code block
```

### 💡 Example

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

---

## 🔢 `range()` Function in Loops

The `range()` function generates a sequence of numbers.

### 📌 Syntax

```python
range(start, stop, step)
```

### 💡 Examples

```python
for i in range(5):
    print(i)
```

```python
for i in range(1, 10, 2):
    print(i)
```

---

## ♾️ `while` Loop

A `while` loop runs as long as a condition is `True`.

### ✅ Syntax

```python
while condition:
    # code block
```

### 💡 Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## 🎯 Nested Loops

A loop inside another loop is called a nested loop.

### 💡 Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

## ⚡ Loop Control Statements

### 🛑 `break`

Stops the loop immediately.

#### Example

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

### ⏭️ `continue`

Skips the current iteration and moves to the next iteration.

#### Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

### 🔹 `pass`

Used as a placeholder when no code is written.

#### Example

```python
for i in range(5):
    pass
```

---

## 🔄 Looping Through Different Data Types

### 📋 List

```python
numbers = [1, 2, 3]

for n in numbers:
    print(n)
```

### 🧵 String

```python
for ch in "Python":
    print(ch)
```

### 📦 Tuple

```python
data = (10, 20, 30)

for item in data:
    print(item)
```

### 📘 Dictionary

```python
student = {"name": "John", "age": 21}

for key, value in student.items():
    print(key, value)
```

---

## 🛠️ Useful Functions with Loops

| Function | Description | Example |
|----------|-------------|---------|
| `range()` | Generates sequence of numbers | `range(5)` |
| `enumerate()` | Returns index and value | `enumerate(list)` |
| `zip()` | Combines multiple iterables | `zip(l1, l2)` |
| `len()` | Returns length | `len(list)` |

---

## 💡 Example Using `enumerate()`

```python
fruits = ["apple", "banana"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

## 💡 Example Using `zip()`

```python
names = ["John", "Sam"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)
```