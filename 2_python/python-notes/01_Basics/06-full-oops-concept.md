
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


# 🧠 Core OOPs Concepts in Python

Object-Oriented Programming (OOPs) is a programming paradigm used to organize software using classes and objects.

OOPs helps developers create:

- ♻️ Reusable code
- 📂 Modular applications
- 🔒 Secure programs
- 🚀 Scalable systems

---

# 📚 Main OOPs Concepts

- 🏗 Class
- 👤 Object
- 🔒 Encapsulation
- 🧬 Inheritance
- 🎭 Polymorphism
- 🧩 Abstraction

---

# 🏗 Class

A **class** is a blueprint used to create objects.

It defines:

- 📌 Attributes (variables)
- ⚙️ Methods (functions)

```python
class User:

    def greet(self):
        print("Hello User")

print(User)

# Output
# <class '__main__.User'>
```

---

# 👤 Object

An **object** is an instance of a class.

Objects contain real data and can access class methods.

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

# 📌 Attributes (Properties)

Attributes store data related to an object.

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

# ⚙️ Methods

Methods define object behavior.

```python
class Car:

    def start(self):
        print("Car Started")

car1 = Car()

car1.start()

# Output
# Car Started
```

---

# 🔧 Constructor — `__init__()`

The constructor initializes object properties automatically.

```python
class Student:

    def __init__(self, name):

        self.name = name

student1 = Student("Alice")

print(student1.name)

# Output
# Alice
```

---

# 🔒 Encapsulation

Encapsulation restricts direct access to object data.

Private variables are created using `__`.

```python
class BankAccount:

    def __init__(self):

        self.__balance = 1000

    def show_balance(self):

        print(self.__balance)

account = BankAccount()

account.show_balance()

# Output
# 1000
```

---

# 🧬 Inheritance

Inheritance allows one class to acquire properties and methods from another class.

---

# 👨 Parent Class

```python
class Animal:

    def sound(self):

        print("Animal makes sound")
```

---

# 🐶 Child Class

```python
class Dog(Animal):

    def bark(self):

        print("Dog Barks")

dog = Dog()

dog.sound()
dog.bark()

# Output
# Animal makes sound
# Dog Barks
```

---

# 🎭 Polymorphism

Polymorphism allows the same method name to behave differently.

```python
class Cat:

    def sound(self):

        print("Cat Meows")

class Dog:

    def sound(self):

        print("Dog Barks")

animals = [Cat(), Dog()]

for animal in animals:

    animal.sound()

# Output
# Cat Meows
# Dog Barks
```

---

# 🧩 Abstraction

Abstraction hides implementation details and shows only essential features.

Python uses abstract classes for abstraction.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):

        print("Car Started")

car = Car()

car.start()

# Output
# Car Started
```

---

# ⚡ Method Overriding

Method overriding allows a child class to change parent class behavior.

```python
class Animal:

    def sound(self):

        print("Animal Sound")

class Dog(Animal):

    def sound(self):

        print("Dog Barking")

dog = Dog()

dog.sound()

# Output
# Dog Barking
```

---

# ➕ Method Overloading

Python does not support traditional method overloading directly.

Default arguments can achieve similar behavior.

```python
class Math:

    def add(self, a, b=0, c=0):

        return a + b + c

m = Math()

print(m.add(10))
print(m.add(10, 20))
print(m.add(10, 20, 30))

# Output
# 10
# 30
# 60
```

---

# 🏛 Types of Inheritance

---

# 🔹 Single Inheritance

```python
class A:
    pass

class B(A):
    pass
```

---

# 🔹 Multiple Inheritance

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

---

# 🔹 Multilevel Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

---

# 🔹 Hierarchical Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass
```

---

# 🔹 Hybrid Inheritance

Combination of multiple inheritance types.

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```

---

# 🎯 Key Points

- 🏗 Class → Blueprint
- 👤 Object → Instance of class
- 📌 Attributes → Store data
- ⚙️ Methods → Define behavior
- 🔒 Encapsulation → Data hiding
- 🧬 Inheritance → Code reusability
- 🎭 Polymorphism → Multiple behaviors
- 🧩 Abstraction → Hide complexity

---

# ✅ Advantages of OOPs

- ♻️ Code Reusability
- 📂 Better Project Structure
- 🔒 Improved Security
- 🛠 Easy Maintenance
- 🚀 Faster Development
- 📈 Scalable Applications


# 🚀 Additional OOPs Concepts in Python

---

# 🔑 Access Modifiers

Access modifiers control how variables and methods are accessed.

| Modifier | Syntax | Access |
|----------|--------|--------|
| Public | `name` | Accessible everywhere |
| Protected | `_name` | Accessible inside class and child class |
| Private | `__name` | Accessible only inside class |

---

# 🌍 Public Member

```python
class User:

    def __init__(self):
        self.name = "Rahul"

user = User()

print(user.name)

# Output
# Rahul
```

---

# 🔒 Protected Member

```python
class User:

    def __init__(self):
        self._salary = 50000

class Employee(User):

    def show(self):
        print(self._salary)

emp = Employee()

emp.show()

# Output
# 50000
```

---

# 🔐 Private Member

```python
class User:

    def __init__(self):
        self.__password = "1234"

    def show(self):
        print(self.__password)

user = User()

user.show()

# Output
# 1234
```

---

# ⚡ Static Method

Static methods belong to the class rather than objects.

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

# 🏛 Class Method

Class methods work with class variables using `cls`.

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

# 📌 Instance Method

Instance methods work with object variables using `self`.

```python
class User:

    def greet(self):

        print("Hello User")

user = User()

user.greet()

# Output
# Hello User
```

---

# 🧾 Class Variables vs Instance Variables

---

# 🌍 Class Variable

Shared among all objects.

```python
class Student:

    school = "ABC School"

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)

# Output
# ABC School
# ABC School
```

---

# 👤 Instance Variable

Unique for every object.

```python
class Student:

    def __init__(self, name):

        self.name = name

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.name)
print(s2.name)

# Output
# Alice
# Bob
```

---

# 🧱 Composition

Composition means one class contains another class object.

```python
class Engine:

    def start(self):

        print("Engine Started")

class Car:

    def __init__(self):

        self.engine = Engine()

car = Car()

car.engine.start()

# Output
# Engine Started
```

---

# 🔗 Association

Association represents a relationship between two independent classes.

```python
class Teacher:

    def __init__(self, name):

        self.name = name

class Student:

    def __init__(self, teacher):

        self.teacher = teacher

teacher = Teacher("John")

student = Student(teacher)

print(student.teacher.name)

# Output
# John
```

---

# 🧩 Aggregation

Aggregation is a weak relationship where objects can exist independently.

```python
class Department:

    def __init__(self, name):

        self.name = name

class Employee:

    def __init__(self, department):

        self.department = department

dept = Department("IT")

emp = Employee(dept)

print(emp.department.name)

# Output
# IT
```

---

# 🧠 Abstract Class

Abstract classes cannot be instantiated directly.

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):

        print("Dog Barks")

dog = Dog()

dog.sound()

# Output
# Dog Barks
```

---

# ⚡ Operator Overloading

Operator behavior can be customized.

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

# 🔄 Iterator Protocol

Custom objects can behave like iterators.

```python
class Counter:

    def __init__(self):

        self.num = 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.num <= 3:

            value = self.num
            self.num += 1

            return value

        raise StopIteration

c = Counter()

for i in c:

    print(i)

# Output
# 1
# 2
# 3
```

---

# 🎯 SOLID Principles

SOLID principles improve software design.

| Principle | Meaning |
|-----------|----------|
| S | Single Responsibility Principle |
| O | Open/Closed Principle |
| L | Liskov Substitution Principle |
| I | Interface Segregation Principle |
| D | Dependency Inversion Principle |

---

# 🏆 Final OOPs Concepts List

- 🏗 Class
- 👤 Object
- 📌 Attributes
- ⚙️ Methods
- 🔧 Constructor
- 🔒 Encapsulation
- 🧬 Inheritance
- 🎭 Polymorphism
- 🧩 Abstraction
- 🔄 Method Overriding
- ➕ Method Overloading
- 🔑 Access Modifiers
- ⚡ Static Methods
- 🏛 Class Methods
- 📌 Instance Methods
- 🧾 Class Variables
- 👤 Instance Variables
- 🧱 Composition
- 🔗 Association
- 🧩 Aggregation
- ⚡ Operator Overloading
- 🔄 Iterator Protocol
- 🎯 SOLID Principles