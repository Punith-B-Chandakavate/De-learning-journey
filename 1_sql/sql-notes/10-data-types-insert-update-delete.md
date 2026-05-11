Here's your content rewritten properly with better formatting, consistent structure, and fixed issues:

---

## 📝 SQL Data Types & CRUD Operations

Database data types are generally divided into the following categories:

- 🔢 **Numeric**
- 🔤 **Text/String**
- 📅 **Date & Time**
- 📦 **Other Types**

---

## 🔢 Numeric Data Types

### 🧮 Whole Numbers (Integers)

Used to store numbers without decimal points.

| Data Type | Size | Signed Range | Unsigned Range |
|-----------|------|--------------|----------------|
| `TINYINT` | 1 Byte | -128 to 127 | 0 to 255 |
| `SMALLINT` | 2 Bytes | -32,768 to 32,767 | 0 to 65,535 |
| `INT` | 4 Bytes | -2,147,483,648 to 2,147,483,647 | 0 to 4,294,967,295 |
| `BIGINT` | 8 Bytes | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | 0 to 18,446,744,073,709,551,615 |

---

### 🔹 Numbers with Decimal Points

Used to store fractional values.

| Data Type | Size | Description |
|-----------|------|-------------|
| `FLOAT` | 4 Bytes | Approximate floating-point number |
| `DOUBLE` | 8 Bytes | Double precision floating-point number |
| `DECIMAL(5,3)` | Depends on precision | Exact fixed-point number |

#### 📍 Example

```sql
DECIMAL(5,3)
```

Can store values like:

```
12.345
99.999
-7.123
```

---

## 🔤 String Data Types

| Data Type | Description |
|-----------|-------------|
| `CHAR(n)` | Stores a **fixed** number of characters. Automatically adds spaces to fill remaining length. (e.g., country codes like `'IN'`, `'US'`) |
| `VARCHAR(n)` | Stores a **variable** number of characters. Only uses required storage space. (e.g., names, emails, addresses) |

---

## 📅 Date & Time Data Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| `DATE` | Stores date values | `2026-05-08` |
| `TIME` | Stores time values | `14:30:00` |
| `DATETIME` | Stores both date and time | `2026-05-08 14:30:00` |
| `TIMESTAMP` | Stores timestamp for tracking record creation/updates | `2026-05-08 14:30:00+00` |

---

## 📦 Other Common Data Types

| Data Type | Description |
|-----------|-------------|
| `BOOLEAN` | Stores `TRUE` or `FALSE` values |
| `BLOB` | Stores binary large objects (images, audio, files) |
| `JSON` | Stores JSON formatted data: `{"name": "John", "age": 25}` |
| `ENUM` | Stores predefined values from a fixed list: `'small'`, `'medium'`, `'large'` |
| `GEOMETRY` | Stores spatial/geographic data (points, lines, polygons) |

---

### 🔍 JSON Operators

| Operator | Description |
|----------|-------------|
| `->` | Extracts a JSON object |
| `->>` | Extracts a text value from JSON data |

---

## 🔍 Filtering JSON Data by Database

### 🐘 PostgreSQL

```sql
SELECT * FROM items
WHERE properties ->> 'color' = 'red';
```

### 🐬 MySQL

```sql
SELECT * FROM items
WHERE properties->>'$.color' = 'red';
```

### 🟦 SQL Server

```sql
SELECT * FROM items
WHERE JSON_VALUE(properties, '$.color') = 'red';
```

### 🟧 SQLite

```sql
SELECT * FROM items
WHERE json_extract(properties, '$.color') = 'red';
```

---

# 🔑 Database Keys

## 🟢 Natural Key

A **Natural Key** is a key created from the original data itself.

**Examples:**
- Email Address
- National ID
- Username

> These values already exist in real-world data and can uniquely identify a record.

---

## 🟡 Surrogate Key

A **Surrogate Key** is an artificial key generated automatically by the database.

**Characteristics:**
- Numeric
- Auto-incremented
- Used as a Primary Key

**Example:**
```sql
id SERIAL PRIMARY KEY
```

---

## 🟣 Composite Key

A **Composite Key** is created by combining multiple columns to uniquely identify a record.

**Example:**
```sql
PRIMARY KEY (student_id, course_id)
```

> Both columns together form the primary key.

---

## 🔢 Auto Increment

Automatically generates incremental numeric values for new records.

**Example:**
```sql
id SERIAL
```

**Generated Values:**
```
1, 2, 3, 4, 5...
```

---

## 🔗 Foreign Key

Creates relationships between tables by referencing the primary key of another table.

**Example:**
```sql
customer_id INT REFERENCES customers(id)
```

---

## 🔄 Database Relationships

### 1️⃣ One-to-One (1:1)

One record in a table relates to only one record in another table.

**Example:** One user → One passport

---

### 2️⃣ One-to-Many (1:N)

One record in a table relates to multiple records in another table.

**Example:** One customer → Many orders

---

### 3️⃣ Many-to-Many (M:N)

Multiple records in one table relate to multiple records in another table.

**Example:** Students ↔ Courses (requires a **link table**)

---

## 🧩 Identifying vs Non-Identifying Relationships

| Type | Description |
|------|-------------|
| **Identifying** | Child table's primary key contains parent table's primary key (weak entity) |
| **Non-Identifying** | Child table has its own primary key and references parent with foreign key |

---

# ✍️ CRUD Operations

## ➕ INSERT

### Insert into All Columns

```sql
INSERT INTO table_name
VALUES (v1, v2, v3, v4);
```

### Insert into Specific Columns

```sql
INSERT INTO table_name (column1, column2)
VALUES (v1, v2);
```

### Insert Multiple Records

```sql
INSERT INTO table_name (column1, column2)
VALUES
    (v1, v2),
    (v1, v2),
    (v1, v2);
```

---

## ✏️ UPDATE

### Update Single Column

```sql
UPDATE table_name
SET column_name = value
WHERE condition;
```

### Update Multiple Columns

```sql
UPDATE table_name
SET
    column1 = value,
    column2 = value,
    column3 = value
WHERE condition;
```

---

## ❌ DELETE

Deletes specific records from a table.

```sql
DELETE FROM table_name
WHERE condition;
```

> ⚠️ **Warning:** Without a `WHERE` clause, all records will be deleted!

---

## 🗑️ DROP TABLE

Deletes the entire table including:

- Structure
- Data
- Constraints
- Indexes

```sql
DROP TABLE table_name;
```

> ⚠️ **Warning:** This action cannot be undone!

---

## ✅ CRUD Operations Summary

| Operation | SQL Command | Description |
|-----------|-------------|-------------|
| **C**reate | `INSERT` | Adds new records |
| **R**ead | `SELECT` | Retrieves records |
| **U**pdate | `UPDATE` | Modifies existing records |
| **D**elete | `DELETE` | Removes records |

---

## 📊 Quick Reference: Data Type Selection Guide

| Use Case | Recommended Type |
|----------|------------------|
| Age, count of items | `INT` or `SMALLINT` |
| Price, salary | `DECIMAL(10,2)` |
| Name, description | `VARCHAR(255)` |
| Fixed code (state, country) | `CHAR(2)` |
| Yes/No flag | `BOOLEAN` |
| Created/updated date | `TIMESTAMP` |
| Configuration, API responses | `JSON` |
| Predefined options (size, status) | `ENUM` |

---
