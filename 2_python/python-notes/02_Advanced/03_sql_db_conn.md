# 📘 SQL Connection & Operations with Python - README.md

---

# 🗄️ Python SQL Database Connection

Python can connect to SQL databases like:

* MySQL
* PostgreSQL
* SQLite
* Oracle

Using Python, we can:

* ✅ Create tables
* ✅ Insert records
* ✅ Fetch data
* ✅ Update records
* ✅ Delete records

---

# 🔥 Popular Python SQL Libraries

| Database   | Python Package           | Import Statement         | Connection Example                                                                                          |
| ---------- | ------------------------ | ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| MySQL      | `mysql-connector-python` | `import mysql.connector` | `mysql.connector.connect(host="localhost", user="root", password="password", database="company")`           |
| PostgreSQL | `psycopg2`               | `import psycopg2`        | `psycopg2.connect(database="company", user="postgres", password="password", host="localhost", port="5432")` |
| SQLite     | `sqlite3`                | `import sqlite3`         | `sqlite3.connect("company.db")`                                                                             |
| Oracle     | `cx_Oracle`              | `import cx_Oracle`       | `cx_Oracle.connect(user="system", password="password", dsn="localhost/orcl")`                               |


---

# 📦 Install MySQL Connector

```bash
pip install mysql-connector-python
```

---

# 📘 Import Package

```python
import mysql.connector
```

---

# 🔥 Connect to MySQL Database

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="company"
)

print("Database Connected")
```

---

# ✅ Output

```text
Database Connected
```

---

# 📘 Create Cursor Object

Cursor is used to execute SQL queries.

```python
cursor = conn.cursor()
```

---

# 🔥 Create Table

```python
query = """
CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary FLOAT
)
"""

cursor.execute(query)

print("Table Created")
```

---

# ✅ Output

```text
Table Created
```

---

# 📘 Insert Data

```python
query = """
INSERT INTO employee (id, name, salary)
VALUES (1, 'Punith', 50000)
"""

cursor.execute(query)

conn.commit()

print("Data Inserted")
```

---

# ✅ Output

```text
Data Inserted
```

---

# 📘 Insert Multiple Records

```python
query = """
INSERT INTO employee (id, name, salary)
VALUES (%s, %s, %s)
"""

data = [
    (2, "Ravi", 45000),
    (3, "Kiran", 60000)
]

cursor.executemany(query, data)

conn.commit()
```

---

# 📘 Fetch Data

```python
query = "SELECT * FROM employee"

cursor.execute(query)

result = cursor.fetchall()

for row in result:
    print(row)
```

---

# ✅ Output

```text
(1, 'Punith', 50000)
(2, 'Ravi', 45000)
(3, 'Kiran', 60000)
```

---

# 📘 Fetch One Record

```python
query = "SELECT * FROM employee"

cursor.execute(query)

row = cursor.fetchone()

print(row)
```

---

# 📘 Update Data

```python
query = """
UPDATE employee
SET salary = 70000
WHERE id = 1
"""

cursor.execute(query)

conn.commit()

print("Data Updated")
```

---

# ✅ Output

```text
Data Updated
```

---

# 📘 Delete Data

```python
query = """
DELETE FROM employee
WHERE id = 2
"""

cursor.execute(query)

conn.commit()

print("Data Deleted")
```

---

# ✅ Output

```text
Data Deleted
```

---

# 📘 Drop Table

```python
query = "DROP TABLE employee"

cursor.execute(query)

print("Table Dropped")
```

---

# 📘 Close Connection

```python
cursor.close()

conn.close()

print("Connection Closed")
```

---

# 🔥 SQL CRUD Operations

| Operation | SQL Command |
| --------- | ----------- |
| Create    | INSERT      |
| Read      | SELECT      |
| Update    | UPDATE      |
| Delete    | DELETE      |

---

# 📘 Parameterized Query

Used to avoid SQL Injection attacks.

```python
query = """
SELECT * FROM employee
WHERE id = %s
"""

value = (1,)

cursor.execute(query, value)

result = cursor.fetchall()

print(result)
```

---

# 🔒 Why Parameterized Queries?

✅ Prevent SQL Injection
✅ Safer queries
✅ Better security

---

# 📘 Exception Handling

```python
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="company"
    )

    print("Connected")

except mysql.connector.Error as err:
    print("Error:", err)
```

---

# 📘 SQLite Connection Example

SQLite comes built-in with Python.

```python
import sqlite3

conn = sqlite3.connect("company.db")

cursor = conn.cursor()

print("SQLite Connected")
```

---

# 📘 SQLite Create Table

```python
query = """
CREATE TABLE employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL
)
"""

cursor.execute(query)

conn.commit()
```

---

# 📘 PostgreSQL Connection

Install package:

```bash
pip install psycopg2
```

---

## Example

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="company",
    user="postgres",
    password="password"
)

print("PostgreSQL Connected")
```

---

# 🔥 SQL Transaction

Transaction ensures data consistency.

```python
try:
    cursor.execute(query1)
  
    cursor.execute(query2)

    conn.commit()

except:
    conn.rollback()
```

---

# 📘 SQL JOIN Example

## Employee Table

| id | name   |
| -- | ------ |
| 1  | Punith |

---

## Salary Table

| emp_id | salary |
| ------ | ------ |
| 1      | 50000  |

---

## SQL Query

```sql
SELECT e.name, s.salary
FROM employee e
JOIN salary s
ON e.id = s.emp_id;
```

---

# ✅ Output

```text
Punith | 50000
```

---

# 📘 Fetch Column Names

```python
cursor.execute("SELECT * FROM employee")

print(cursor.column_names)
```

---

# 📘 Row Count

```python
print(cursor.rowcount)
```

---

# 📘 Commit vs Rollback

| Method         | Purpose      |
| -------------- | ------------ |
| `commit()`   | Save changes |
| `rollback()` | Undo changes |

---

# 🔥 Best Practices

| Practice                  | Reason                |
| ------------------------- | --------------------- |
| Use parameterized queries | Prevent SQL injection |
| Close connections         | Free resources        |
| Use transactions          | Data consistency      |
| Handle exceptions         | Avoid crashes         |
| Use connection pooling    | Better performance    |

---

# 📘 Real-Time Use Cases

| Use Case            | Example          |
| ------------------- | ---------------- |
| User Authentication | Login System     |
| E-commerce          | Product database |
| Banking             | Transactions     |
| Employee Management | HR systems       |
| Analytics           | Reports          |

---

# 🔥 Interview Questions

## ❓ What is Cursor?

Cursor executes SQL queries.

---

## ❓ Why use commit()?

To save database changes permanently.

---

## ❓ Difference Between fetchone() and fetchall()

| fetchone()      | fetchall()       |
| --------------- | ---------------- |
| Returns one row | Returns all rows |

---

## ❓ What is SQL Injection?

A security attack using malicious SQL queries.

---

## ❓ Why use Parameterized Queries?

To prevent SQL injection attacks.

---

# 🏁 Summary

| Topic                 | Description             |
| --------------------- | ----------------------- |
| Connection            | Connect Python with SQL |
| Cursor                | Execute queries         |
| CRUD                  | Database operations     |
| commit()              | Save changes            |
| rollback()            | Undo changes            |
| Parameterized Queries | Secure queries          |
