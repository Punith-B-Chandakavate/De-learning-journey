# 🗄️ Snowflake Databases, Schemas, Tables & Views

![Snowflake](<https://img.shields.io/badge/Snowflake-Database%20Objects-29B5E8?logo=snowflake&logoColor=white>)
![SQL](https://img.shields.io/badge/Language-SQL-orange)
![Database](https://img.shields.io/badge/Object-Database-blue)
![Schema](https://img.shields.io/badge/Object-Schema-green)
![Tables](https://img.shields.io/badge/Object-Tables-purple)
![Views](https://img.shields.io/badge/Object-Views-yellow)

---

# 📚 Table of Contents

- 📖 Overview
- 🎯 Learning Objectives
- 🏗️ Snowflake Object Hierarchy
- 🗄️ Databases
- 📂 Schemas
- 📊 Tables
- 👁️ Views
- 🔗 Fully Qualified Object Names
- ⚙️ Create Snowflake Database
- 📂 Create Schemas
- 📊 Create Tables
- 📝 Insert Data
- 🔍 Query Tables
- 👁️ Create Views
- 📈 Query Views
- 🔎 Explore Database Objects
- 🏗️ Complete SQL Workflow
- 📊 Example Data Model
- 💡 Best Practices
- 🎤 Interview Questions
- 🎯 Key Takeaways
- 📖 Summary
- ✅ Completion Checklist

---

# 📖 Overview

Snowflake organizes data using a hierarchical structure consisting of:

```text
Database
   │
   ├── Schema
   │      │
   │      ├── Tables
   │      │
   │      └── Views
   │
   └── Schema
          │
          ├── Tables
          └── Views
```

A **Snowflake Database** can contain multiple schemas.

Schemas are used to logically organize database objects such as tables and views.

For example, a database can contain separate schemas for raw data and analytics:

```text
SALES_DB
│
├── RAW_SCHEMA
│   └── ORDER_RAW
│
└── ANALYTICS_SCHEMA
    └── MONTHLY_SALES
```

This structure provides a clean way to organize data for different stages and workloads.

---

# 🎯 Learning Objectives

After completing this module, you will be able to:

* Understand Snowflake databases
* Understand schemas
* Understand tables
* Understand views
* Understand the Snowflake object hierarchy
* Create databases using SQL
* Create schemas using SQL
* Create tables using SQL
* Insert data into Snowflake tables
* Query Snowflake tables
* Create analytical views
* Query views
* Use fully qualified object names
* Inspect Snowflake database objects

---

# 🏗️ Snowflake Object Hierarchy

Snowflake organizes database objects using a hierarchical structure.

```text
                         ❄️ Snowflake
                              │
                              ▼
                         🗄️ Database
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
           📂 RAW_SCHEMA              📂 ANALYTICS_SCHEMA
                │                           │
                ▼                           ▼
          📊 ORDER_RAW                👁️ MONTHLY_SALES
```

In this example:

```text
Database
   │
   ▼
SALES_DB
   │
   ├── RAW_SCHEMA
   │      │
   │      └── ORDER_RAW
   │
   └── ANALYTICS_SCHEMA
          │
          └── MONTHLY_SALES
```

---

# 🗄️ Databases

A **Database** is a top-level logical container for organizing Snowflake data objects.

A database can contain multiple schemas.

Example:

```text
SALES_DB
│
├── RAW_SCHEMA
│
├── ANALYTICS_SCHEMA
│
└── other schemas...
```

In this project, the database is:

```text
SALES_DB
```

---

# 📂 Schemas

A **Schema** is a logical container inside a database.

Schemas help organize tables, views, and other database objects.

For this example, two schemas are created:

```text
SALES_DB
│
├── RAW_SCHEMA
│
└── ANALYTICS_SCHEMA
```

### 🧱 RAW_SCHEMA

Used for raw source data.

```text
RAW_SCHEMA
    │
    └── ORDER_RAW
```

### 📊 ANALYTICS_SCHEMA

Used for analytical objects.

```text
ANALYTICS_SCHEMA
    │
    └── MONTHLY_SALES
```

This separation makes it easier to organize raw and analytical data.

---

# 📊 Tables

A **Table** stores structured data in rows and columns.

The example creates:

```text
SALES_DB.RAW_SCHEMA.ORDER_RAW
```

The table contains:

| Column          | Data Type  | Description             |
| --------------- | ---------- | ----------------------- |
| `ORDER_ID`    | `INT`    | Unique order identifier |
| `CUSTOMER_ID` | `INT`    | Customer identifier     |
| `PRODUCT`     | `STRING` | Product name            |
| `QUANTITY`    | `INT`    | Quantity purchased      |
| `PRICE`       | `FLOAT`  | Product price           |
| `ORDER_DATE`  | `DATE`   | Order date              |

The resulting structure is:

```text
ORDER_RAW
│
├── ORDER_ID
├── CUSTOMER_ID
├── PRODUCT
├── QUANTITY
├── PRICE
└── ORDER_DATE
```

---

# 👁️ Views

A **View** is a logical representation of query results.

Instead of storing a separate copy of the result data, the view definition contains the SQL query used to retrieve the data.

In this example:

```text
SALES_DB.ANALYTICS_SCHEMA.MONTHLY_SALES
```

is created as a view based on the raw order table.

```text
ORDER_RAW
    │
    ▼
Aggregation
    │
    ▼
MONTHLY_SALES View
```

The view calculates monthly revenue using:

```text
QUANTITY × PRICE
```

and groups the results by month.

---

# 🔗 Fully Qualified Object Names

Snowflake objects can be referenced using a fully qualified name:

```text
DATABASE.SCHEMA.OBJECT
```

For example:

```text
SALES_DB.RAW_SCHEMA.ORDER_RAW
```

where:

```text
SALES_DB       → Database
RAW_SCHEMA     → Schema
ORDER_RAW      → Table
```

Another example:

```text
SALES_DB.ANALYTICS_SCHEMA.MONTHLY_SALES
```

where:

```text
SALES_DB            → Database
ANALYTICS_SCHEMA    → Schema
MONTHLY_SALES       → View
```

### Hierarchy

```text
Database
   │
   ▼
Schema
   │
   ▼
Object
```

---

# ⚙️ Create Snowflake Database

The first step is to select the compute warehouse.

```sql
USE WAREHOUSE ETL_DEV_WH;
```

Create the database:

```sql
CREATE DATABASE IF NOT EXISTS SALES_DB;
```

The `IF NOT EXISTS` clause prevents an error if the database already exists.

---

# 🔄 Use the Database

After creating the database, switch the current session to it:

```sql
USE DATABASE SALES_DB;
```

The active database is now:

```text
SALES_DB
```

---

# 📂 Create Schemas

Create the raw schema:

```sql
CREATE SCHEMA IF NOT EXISTS RAW_SCHEMA;
```

Create the analytics schema:

```sql
CREATE SCHEMA IF NOT EXISTS ANALYTICS_SCHEMA;
```

The resulting structure is:

```text
SALES_DB
│
├── RAW_SCHEMA
│
└── ANALYTICS_SCHEMA
```

---

# 🥉 Raw Schema

Switch to the raw schema:

```sql
USE SCHEMA RAW_SCHEMA;
```

The raw schema will contain the source order data.

```text
SALES_DB
    │
    └── RAW_SCHEMA
          │
          └── ORDER_RAW
```

---

# 📊 Create the Order Table

Create the `ORDER_RAW` table:

```sql
CREATE OR REPLACE TABLE ORDER_RAW (
    ORDER_ID INT,
    CUSTOMER_ID INT,
    PRODUCT STRING,
    QUANTITY INT,
    PRICE FLOAT,
    ORDER_DATE DATE
);
```

The table structure is:

```text
ORDER_RAW
│
├── ORDER_ID
├── CUSTOMER_ID
├── PRODUCT
├── QUANTITY
├── PRICE
└── ORDER_DATE
```

---

# 📝 Insert Data

Insert sample order records into the table:

```sql
INSERT INTO ORDER_RAW
(
    ORDER_ID,
    CUSTOMER_ID,
    PRODUCT,
    QUANTITY,
    PRICE,
    ORDER_DATE
)
VALUES
(1001, 501, 'Laptop',       1, 75000.00, '2026-01-05'),
(1002, 502, 'Mouse',        2,   850.00, '2026-01-07'),
(1003, 503, 'Keyboard',     1,  2500.00, '2026-01-10'),
(1004, 501, 'Monitor',      2, 15000.00, '2026-01-12'),
(1005, 504, 'Headphones',   1,  4500.00, '2026-01-15'),
(1006, 505, 'Laptop',       1, 68000.00, '2026-01-18'),
(1007, 502, 'Webcam',       1,  3200.00, '2026-01-20'),
(1008, 506, 'Keyboard',     2,  2200.00, '2026-01-22'),
(1009, 507, 'Mouse',        3,   750.00, '2026-01-25'),
(1010, 503, 'Monitor',      1, 12500.00, '2026-01-28'),
(1011, 508, 'Laptop',       1, 72000.00, '2026-02-02'),
(1012, 501, 'Headphones',   2,  4200.00, '2026-02-05'),
(1013, 504, 'Mouse',        1,   900.00, '2026-02-08'),
(1014, 509, 'Webcam',       2,  3000.00, '2026-02-10'),
(1015, 510, 'Monitor',      1, 14000.00, '2026-02-12'),
(1016, 505, 'Keyboard',     1,  2700.00, '2026-02-15'),
(1017, 506, 'Laptop',       2, 69000.00, '2026-02-18'),
(1018, 507, 'Headphones',   1,  4800.00, '2026-02-20'),
(1019, 508, 'Mouse',        4,   800.00, '2026-02-22'),
(1020, 509, 'Monitor',      2, 13500.00, '2026-02-25');
```

---

# 🔍 Query the Raw Table

Verify the inserted records:

```sql
SELECT *
FROM ORDER_RAW;
```

You can also reference the table using its fully qualified name:

```sql
SELECT *
FROM SALES_DB.RAW_SCHEMA.ORDER_RAW;
```

---

# 📊 Raw Data Flow

The raw data structure is:

```text
                 SALES_DB
                     │
                     ▼
                RAW_SCHEMA
                     │
                     ▼
                 ORDER_RAW
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Orders    Customers   Products
```

The `ORDER_RAW` table contains the source order information used by the analytical layer.

---

# 📈 Create Analytical View

Switch to the analytics schema:

```sql
USE SCHEMA SALES_DB.ANALYTICS_SCHEMA;
```

Create the monthly sales view:

```sql
CREATE OR REPLACE VIEW MONTHLY_SALES AS
SELECT
    DATE_TRUNC('month', ORDER_DATE) AS ORDER_MONTH,
    SUM(QUANTITY * PRICE) AS TOTAL_REVENUE
FROM SALES_DB.RAW_SCHEMA.ORDER_RAW
GROUP BY 1
ORDER BY 1;
```

This creates:

```text
SALES_DB.ANALYTICS_SCHEMA.MONTHLY_SALES
```

---

# 🧮 Monthly Revenue Calculation

The view calculates revenue using:

```text
QUANTITY × PRICE
```

For example:

```text
Quantity = 2
Price    = 850

Revenue = 2 × 850
        = 1700
```

The view then aggregates revenue by month.

```text
ORDER_RAW
     │
     ▼
QUANTITY × PRICE
     │
     ▼
DATE_TRUNC('month', ORDER_DATE)
     │
     ▼
GROUP BY MONTH
     │
     ▼
MONTHLY_SALES
```

---

# 👁️ Query the View

Query the analytical view:

```sql
SELECT *
FROM MONTHLY_SALES;
```

Or use the fully qualified name:

```sql
SELECT *
FROM SALES_DB.ANALYTICS_SCHEMA.MONTHLY_SALES;
```

---

# 📊 Example Analytics Layer

The final structure becomes:

```text
SALES_DB
│
├── RAW_SCHEMA
│   │
│   └── ORDER_RAW
│       ├── ORDER_ID
│       ├── CUSTOMER_ID
│       ├── PRODUCT
│       ├── QUANTITY
│       ├── PRICE
│       └── ORDER_DATE
│
└── ANALYTICS_SCHEMA
    │
    └── MONTHLY_SALES
        ├── ORDER_MONTH
        └── TOTAL_REVENUE
```

---

# 🔎 Explore Snowflake Objects

Snowflake provides `SHOW` commands to inspect database objects.

## 🗄️ Show Databases

```sql
SHOW DATABASES;
```

This displays available databases in the Snowflake environment.

---

## 📂 Show Schemas

```sql
SHOW SCHEMAS IN DATABASE SALES_DB;
```

This displays schemas available inside `SALES_DB`.

Expected schemas include:

```text
RAW_SCHEMA
ANALYTICS_SCHEMA
```

---

## 📊 Show Tables

```sql
SHOW TABLES IN SCHEMA SALES_DB.RAW_SCHEMA;
```

This displays tables inside the raw schema.

Example:

```text
ORDER_RAW
```

---

## 👁️ Show Views

```sql
SHOW VIEWS IN SCHEMA SALES_DB.ANALYTICS_SCHEMA;
```

This displays views inside the analytics schema.

Example:

```text
MONTHLY_SALES
```

---

# 🏗️ Complete SQL Workflow

The complete workflow can be represented as:

```text
                ⚙️ ETL_DEV_WH
                      │
                      ▼
                 🗄️ SALES_DB
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
     🥉 RAW_SCHEMA          📊 ANALYTICS_SCHEMA
          │                       │
          ▼                       ▼
     ORDER_RAW              MONTHLY_SALES
          │                       │
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
               Business Analytics
```

---

# 🔄 End-to-End SQL Flow

```text
USE WAREHOUSE
      │
      ▼
CREATE DATABASE
      │
      ▼
USE DATABASE
      │
      ▼
CREATE SCHEMAS
      │
      ▼
CREATE TABLE
      │
      ▼
INSERT DATA
      │
      ▼
QUERY TABLE
      │
      ▼
CREATE VIEW
      │
      ▼
QUERY VIEW
      │
      ▼
SHOW DATABASE / SCHEMA / TABLE / VIEW
```

---

# 📋 Complete SQL Script

The complete example can be executed in the following order:

```sql
-- Select compute warehouse
USE WAREHOUSE ETL_DEV_WH;

-- Create database
CREATE DATABASE IF NOT EXISTS SALES_DB;

-- Use database
USE DATABASE SALES_DB;

-- Create schemas
CREATE SCHEMA IF NOT EXISTS RAW_SCHEMA;
CREATE SCHEMA IF NOT EXISTS ANALYTICS_SCHEMA;

-- Use raw schema
USE SCHEMA RAW_SCHEMA;

-- Create raw order table
CREATE OR REPLACE TABLE ORDER_RAW (
    ORDER_ID INT,
    CUSTOMER_ID INT,
    PRODUCT STRING,
    QUANTITY INT,
    PRICE FLOAT,
    ORDER_DATE DATE
);

-- Insert sample data
INSERT INTO ORDER_RAW
(
    ORDER_ID,
    CUSTOMER_ID,
    PRODUCT,
    QUANTITY,
    PRICE,
    ORDER_DATE
)
VALUES
(1001, 501, 'Laptop',       1, 75000.00, '2026-01-05'),
(1002, 502, 'Mouse',        2,   850.00, '2026-01-07'),
(1003, 503, 'Keyboard',     1,  2500.00, '2026-01-10'),
(1004, 501, 'Monitor',      2, 15000.00, '2026-01-12'),
(1005, 504, 'Headphones',   1,  4500.00, '2026-01-15'),
(1006, 505, 'Laptop',       1, 68000.00, '2026-01-18'),
(1007, 502, 'Webcam',       1,  3200.00, '2026-01-20'),
(1008, 506, 'Keyboard',     2,  2200.00, '2026-01-22'),
(1009, 507, 'Mouse',        3,   750.00, '2026-01-25'),
(1010, 503, 'Monitor',      1, 12500.00, '2026-01-28'),
(1011, 508, 'Laptop',       1, 72000.00, '2026-02-02'),
(1012, 501, 'Headphones',   2,  4200.00, '2026-02-05'),
(1013, 504, 'Mouse',        1,   900.00, '2026-02-08'),
(1014, 509, 'Webcam',       2,  3000.00, '2026-02-10'),
(1015, 510, 'Monitor',      1, 14000.00, '2026-02-12'),
(1016, 505, 'Keyboard',     1,  2700.00, '2026-02-15'),
(1017, 506, 'Laptop',       2, 69000.00, '2026-02-18'),
(1018, 507, 'Headphones',   1,  4800.00, '2026-02-20'),
(1019, 508, 'Mouse',        4,   800.00, '2026-02-22'),
(1020, 509, 'Monitor',      2, 13500.00, '2026-02-25');

-- Verify raw table
SELECT *
FROM ORDER_RAW;

-- Use analytics schema
USE SCHEMA SALES_DB.ANALYTICS_SCHEMA;

-- Create analytical view
CREATE OR REPLACE VIEW MONTHLY_SALES AS
SELECT
    DATE_TRUNC('month', ORDER_DATE) AS ORDER_MONTH,
    SUM(QUANTITY * PRICE) AS TOTAL_REVENUE
FROM SALES_DB.RAW_SCHEMA.ORDER_RAW
GROUP BY 1
ORDER BY 1;

-- Query analytical view
SELECT *
FROM MONTHLY_SALES;

-- Inspect objects
SHOW DATABASES;

SHOW SCHEMAS IN DATABASE SALES_DB;

SHOW TABLES IN SCHEMA SALES_DB.RAW_SCHEMA;

SHOW VIEWS IN SCHEMA SALES_DB.ANALYTICS_SCHEMA;
```

---

# 💡 Best Practices

* 🗂️ Use databases to organize major data domains.
* 📂 Use schemas to logically separate different types of data.
* 🥉 Keep raw/source objects in a dedicated raw schema.
* 📊 Keep analytical objects in a dedicated analytics schema.
* 🏷️ Use meaningful database, schema, table, and view names.
* 🔗 Use fully qualified object names when working across schemas.
* 👁️ Use views to expose reusable analytical logic.
* 🔐 Apply appropriate permissions to databases, schemas, tables, and views.
* 🧹 Avoid unnecessary duplication of analytical data when a view is sufficient.
* 🔍 Use `SHOW` commands to inspect and validate Snowflake objects.

---

# 🎤 Interview Questions

### 1. What is a database in Snowflake?

A database is a top-level logical container that can contain multiple schemas and their database objects.

---

### 2. What is a schema?

A schema is a logical container inside a database used to organize objects such as tables and views.

---

### 3. What is a table?

A table stores structured data in rows and columns.

---

### 4. What is a view?

A view is a logical representation of query results based on a SQL definition.

---

### 5. What is the Snowflake object hierarchy?

```text
Database
   │
   ▼
Schema
   │
   ▼
Table / View
```

---

### 6. What is a fully qualified table name?

A fully qualified object name identifies the database, schema, and object:

```text
DATABASE.SCHEMA.TABLE
```

Example:

```text
SALES_DB.RAW_SCHEMA.ORDER_RAW
```

---

### 7. Why create separate RAW and ANALYTICS schemas?

They provide logical separation between source/raw data and analytical objects.

```text
RAW_SCHEMA
    │
    └── Raw Data

ANALYTICS_SCHEMA
    │
    └── Analytical Objects
```

---

### 8. How do you create a database?

```sql
CREATE DATABASE IF NOT EXISTS SALES_DB;
```

---

### 9. How do you create a schema?

```sql
CREATE SCHEMA IF NOT EXISTS RAW_SCHEMA;
```

---

### 10. How do you create a table?

```sql
CREATE OR REPLACE TABLE ORDER_RAW (
    ORDER_ID INT,
    CUSTOMER_ID INT,
    PRODUCT STRING,
    QUANTITY INT,
    PRICE FLOAT,
    ORDER_DATE DATE
);
```

---

### 11. How do you create a view?

```sql
CREATE OR REPLACE VIEW MONTHLY_SALES AS
SELECT
    DATE_TRUNC('month', ORDER_DATE) AS ORDER_MONTH,
    SUM(QUANTITY * PRICE) AS TOTAL_REVENUE
FROM SALES_DB.RAW_SCHEMA.ORDER_RAW
GROUP BY 1;
```

---

### 12. How do you list schemas in a database?

```sql
SHOW SCHEMAS IN DATABASE SALES_DB;
```

---

### 13. How do you list tables in a schema?

```sql
SHOW TABLES IN SCHEMA SALES_DB.RAW_SCHEMA;
```

---

### 14. How do you list views in a schema?

```sql
SHOW VIEWS IN SCHEMA SALES_DB.ANALYTICS_SCHEMA;
```

---

# 🎯 Key Takeaways

* 🗄️ A Snowflake **Database** is a top-level container.
* 📂 A **Schema** organizes database objects.
* 📊 A **Table** stores structured data.
* 👁️ A **View** provides a logical representation of query results.
* 🔗 Objects can be referenced using `DATABASE.SCHEMA.OBJECT`.
* 🥉 `RAW_SCHEMA` can be used for raw source data.
* 📈 `ANALYTICS_SCHEMA` can contain analytical views.
* ⚙️ A warehouse must be selected before executing compute operations.
* 📝 SQL commands can create databases, schemas, tables, and views.
* 🔍 `SHOW` commands can be used to inspect Snowflake objects.

---
