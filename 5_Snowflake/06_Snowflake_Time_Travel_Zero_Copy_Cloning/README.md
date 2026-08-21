# ❄️ Snowflake Time Travel & Zero-Copy Cloning

![Snowflake](<https://img.shields.io/badge/Snowflake-Data%20Cloud-29B5E8?logo=snowflake&logoColor=white>)
![SQL](<https://img.shields.io/badge/SQL-Snowflake%20SQL-29B5E8?logo=snowflake&logoColor=white>)
![Status](<https://img.shields.io/badge/Status-Learning%20Module-brightgreen>)

> This module covers two important Snowflake capabilities: **Time Travel** for querying/recovering historical data and **Zero-Copy Cloning** for creating fast logical copies for testing, backup, and analysis.

---

# 📌 Table of Contents

- 📖 Overview
- 🎯 Objectives
- ⏳ Time Travel
- 🕐 Timestamp
- ⏪ Offset
- 🔎 Before Statement
- 🗑️ Undrop Dropped Tables
- 🧬 Zero-Copy Cloning
- 🧪 Development and Testing
- 🛡️ Backup Before Risky Operations
- 📊 Data Science and Analysis
- ⚙️ How Cloning Works
- 💡 Best Practices
- 🎤 Interview Questions
- 📋 SQL Reference
- ✅ Completion Checklist

---

# 📖 Overview

Data engineering environments frequently need historical recovery and isolated environments for experimentation.

```text
❄️ SNOWFLAKE
     │
     ├── ⏳ TIME TRAVEL
     │      ├── Historical queries
     │      ├── Changed-data recovery
     │      └── Dropped-object recovery
     │
     └── 🧬 ZERO-COPY CLONING
            ├── Development / Testing
            ├── Backup
            └── Data Analysis
```

---

# 🎯 Objectives

- ⏳ Understand Snowflake Time Travel.
- 🕐 Query historical data using a timestamp.
- ⏪ Query historical data using an offset.
- 🔎 Query data before a specific statement.
- 🗑️ Restore dropped tables with `UNDROP`.
- 🧬 Understand Zero-Copy Cloning.
- 🧪 Clone production data for testing.
- 🛡️ Create a backup before risky operations.
- 📊 Create isolated data-analysis copies.
- 💰 Understand how cloning can reduce unnecessary initial data duplication.

---

# ⏳ Time Travel

**Time Travel** allows historical versions of data to be queried and recovered within the configured retention period.

Typical scenarios:

- Accidental `UPDATE`
- Accidental `DELETE`
- Inspecting an earlier table state
- Recovering data after an unwanted change
- Restoring a dropped table when recovery is available

```text
Current Data
     │
     ▼
Historical State
     │
 ┌───┼─────────────┐
 ▼   ▼             ▼
🕐   ⏪             🔎
Time Offset       Statement
```

> 📝 The learning notes for this module describe a 90-day Time Travel period. In practice, retention depends on the Snowflake environment/configuration, so verify the configured retention for your account and object.

---

## 🕐 Query Data at a Specific Timestamp

```sql
SELECT *
FROM CUSTOMERS
AT (
    TIMESTAMP => '2024-10-25 14:20:00'::TIMESTAMP
);
```

Use this when the exact historical date and time are known.

```text
CUSTOMERS
    │
    ▼
2024-10-25 14:20:00
    │
    ▼
Historical CUSTOMER state
```

---

## ⏪ Query Data Using an Offset

```sql
SELECT *
FROM CUSTOMERS
AT (
    OFFSET => -300
);
```

The negative offset queries a historical state relative to the current time.

```text
Current Time
     │
     │  -300 seconds
     ▼
Historical Data
```

---

## 🔎 Query Data Before a Specific Statement

When an `UPDATE` or `DELETE` causes an unwanted change, first find its query ID.

## 1️⃣ Find the Query ID

```sql
SELECT
    query_id,
    query_text,
    start_time
FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY())
WHERE query_text ILIKE '%UPDATE customers%'
ORDER BY start_time DESC
LIMIT 5;
```

Copy the required `query_id`.

### 2️⃣ Query Data Before That Statement

```sql
SELECT *
FROM customers
BEFORE (
    STATEMENT => '<QUERY_ID>'
);
```

#### 🔄 Flow

```text
UPDATE customers
      │
      ▼
Query History
      │
      ▼
query_id
      │
      ▼
BEFORE (STATEMENT => query_id)
      │
      ▼
Previous Data State
```

---

## 🗑️ Undrop Dropped Tables

If a table is accidentally dropped, `UNDROP` can be used when the object is still recoverable.

### 1️⃣ Drop the Table

```sql
DROP TABLE employees;
```

### 2️⃣ Query the Dropped Table

```sql
SELECT *
FROM employees;
```

The query fails because the object has been dropped.

### 3️⃣ Restore the Table

```sql
UNDROP TABLE employees;
```

### 4️⃣ Verify

```sql
SELECT *
FROM employees;
```

#### 🔄 Recovery Flow

```text
📊 EMPLOYEES
     ↓
🗑️ DROP TABLE
     ↓
❌ Object unavailable
     ↓
↩️ UNDROP TABLE
     ↓
✅ Object restored
```

> 📝 The original notes mixed `employee` and `employees`; this README uses `employees` consistently.

---

## 🔄 Time Travel Recovery Methods

| Method       | Example                       | Purpose                                   |
| ------------ | ----------------------------- | ----------------------------------------- |
| 🕐 Timestamp | `AT (TIMESTAMP => ...)`     | Historical state at a known time          |
| ⏪ Offset    | `AT (OFFSET => ...)`        | Historical state relative to current time |
| 🔎 Statement | `BEFORE (STATEMENT => ...)` | State before a specific SQL statement     |
| 🗑️ Undrop  | `UNDROP TABLE ...`          | Restore a dropped table                   |

### 🧠 Easy Memory Trick

```text
TIMESTAMP → "I know the exact time."
OFFSET    → "I know how far back."
STATEMENT → "I know which SQL caused it."
UNDROP    → "I dropped the object."
```

---

# 🧬 Zero-Copy Cloning

Zero-Copy Cloning allows you to create a logical copy of a Snowflake database, schema, or table without initially duplicating the complete underlying data files.

```text
Original Data
      │
      ▼
Metadata References
      │
      ▼
Clone
```

This is useful for:

- 🧪 Development and testing
- 🛡️ Backup before risky operations
- 📊 Data science
- 📈 Data analysis

---

## 🧪 Use Case 1 — Development & Testing

### Clone Production Database

```sql
CREATE DATABASE SALES_DB_TEST
CLONE SALES_DB_PROD;
```

### Switch to the Test Database

```sql
USE DATABASE SALES_DB_TEST;
```

### Experiment Safely

```sql
UPDATE customers
SET status = 'TEST'
WHERE customer_id = 1;
```

Production remains isolated from these test changes.

### Drop the Test Database

```sql
DROP DATABASE SALES_DB_TEST;
```

#### 🔄 Flow

```text
🏭 SALES_DB_PROD
       │
       │ CLONE
       ▼
🧪 SALES_DB_TEST
       │
       ├── Test queries
       ├── UPDATE data
       ├── Experiment
       └── Validate transformations
```

---

## 🛡️ Use Case 2 — Backup Before Risky Operations

Create a quick table clone before an `UPDATE` or `DELETE`.

### 1️⃣ Create Backup

```sql
CREATE TABLE order_backup
CLONE orders;
```

### 2️⃣ Run Risky Operation

```sql
DELETE FROM orders
WHERE order_date < '2020-01-01';
```

### 3️⃣ Restore if Required

```sql
CREATE OR REPLACE TABLE orders
CLONE order_backup;
```

### 4️⃣ Remove Backup

```sql
DROP TABLE order_backup;
```

#### 🔄 Flow

```text
orders
  │
  ├── CLONE ──→ order_backup
  │
  ▼
Risky DELETE / UPDATE
  │
  ├── Success → DROP backup
  │
  └── Problem → Restore from clone
```

---

## 📊 Use Case 3 — Data Science & Data Analysis

Create a dedicated analysis copy.

### 1️⃣ Clone the Table

```sql
CREATE TABLE customers_analysis
CLONE customers;
```

### 2️⃣ Add Analysis Column

```sql
ALTER TABLE customers_analysis
ADD COLUMN segment VARCHAR(50);
```

### 3️⃣ Experiment With the Clone

```sql
UPDATE customers_analysis
SET segment = 'HIGH_VALUE'
WHERE total_spent > 10000;
```

Analysts can modify the clone without directly changing the original table.

```text
📊 customers
      │
      │ CLONE
      ▼
🔬 customers_analysis
      │
      ├── Add columns
      ├── Aggregate
      ├── Experiment
      └── Analyze
```

---

# ⚙️ How Zero-Copy Cloning Works

The initial clone uses metadata references to the existing data rather than requiring a complete physical copy.

```text
Original
   │
   ▼
Metadata
  ↙ ↘
 ↙   ↘
▼     ▼
Data  Clone
       │
       ▼
   Shared existing
   data references
```

When changes occur, new storage can be required for changed data.

```text
Clone Created
     ↓
Metadata Reference
     ↓
Fast Initial Clone
     ↓
Clone Modified
     ↓
New / Changed Data
     ↓
Additional Storage
```

### 💰 Storage Concept

Traditional copy:

```text
Original Data
     +
Full Duplicate
     =
More Storage
```

Zero-copy clone:

```text
Original Data
     +
Metadata References
     =
Fast Initial Clone
```

---

# 🔎 Verification Queries

## Current Data

```sql
SELECT *
FROM CUSTOMERS;
```

## Historical Timestamp

```sql
SELECT *
FROM CUSTOMERS
AT (
    TIMESTAMP => '2024-10-25 14:20:00'::TIMESTAMP
);
```

## Historical Offset

```sql
SELECT *
FROM CUSTOMERS
AT (
    OFFSET => -300
);
```

## Find Query ID

```sql
SELECT
    query_id,
    query_text,
    start_time
FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY())
WHERE query_text ILIKE '%UPDATE customers%'
ORDER BY start_time DESC
LIMIT 5;
```

## Before Statement

```sql
SELECT *
FROM CUSTOMERS
BEFORE (
    STATEMENT => '<QUERY_ID>'
);
```

## Restore Table

```sql
UNDROP TABLE employees;
```

## Clone Database

```sql
CREATE DATABASE SALES_DB_TEST
CLONE SALES_DB_PROD;
```

## Clone Table

```sql
CREATE TABLE order_backup
CLONE orders;
```

---

# 💡 Best Practices

## ⏳ Time Travel

- ✅ Use timestamp queries when the exact time is known.
- ✅ Use offsets for relative historical queries.
- ✅ Use query history when the problematic statement is known.
- ✅ Use `UNDROP` for recoverable dropped objects.
- ✅ Understand the configured retention period.
- ✅ Test recovery procedures before relying on them in production.

## 🧬 Zero-Copy Cloning

- ✅ Use clones for development and testing.
- ✅ Create a backup clone before risky operations.
- ✅ Give analysts isolated environments.
- ✅ Use clear names such as `_TEST`, `_BACKUP`, and `_ANALYSIS`.
- ✅ Drop temporary clones when they are no longer required.
- ✅ Remember that changes to clones can require additional storage.

---

# ⚠️ Important Notes

### ⏳ Time Travel Retention

The learning notes for this module reference **90 days** as the Time Travel period.

For a real implementation, always verify the retention configured for the relevant Snowflake environment and object.

### 🧬 Zero-Copy Clone

Zero-copy means the initial clone does not require a complete duplicate of the existing underlying data.

As data changes, additional storage can be used for changed/new data.

### 🗑️ UNDROP

`UNDROP` restores a dropped object when it remains recoverable under the applicable Snowflake recovery rules. Object naming and subsequent object creation can affect restoration.

---

# 🎤 Interview Questions

### 1. What is Snowflake Time Travel?

Time Travel allows historical versions of data to be queried and recovered within the configured retention period.

### 2. What are the main Time Travel methods?

```text
TIMESTAMP
OFFSET
BEFORE STATEMENT
UNDROP
```

### 3. When do you use `AT (TIMESTAMP => ...)`?

When the exact historical timestamp is known.

### 4. What does `OFFSET => -300` do?

It queries a historical state relative to the current time using a negative offset.

### 5. How do you query data before an UPDATE?

Find the statement's query ID and use:

```sql
SELECT *
FROM customers
BEFORE (
    STATEMENT => '<QUERY_ID>'
);
```

### 6. How do you restore a dropped table?

```sql
UNDROP TABLE employees;
```

### 7. What is Zero-Copy Cloning?

It creates a logical copy of a database, schema, or table without initially duplicating the complete underlying data files.

### 8. Why use Zero-Copy Cloning?

For:

- Development
- Testing
- Backup
- Data science
- Data analysis

### 9. How do you clone a database?

```sql
CREATE DATABASE SALES_DB_TEST
CLONE SALES_DB_PROD;
```

### 10. How do you clone a table?

```sql
CREATE TABLE order_backup
CLONE orders;
```

### 11. Does a clone always consume zero storage?

No. The initial clone can avoid full duplication, but changes can require additional storage.

### 12. Time Travel vs Zero-Copy Clone?

```text
⏳ Time Travel
→ Historical data access and recovery

🧬 Zero-Copy Clone
→ Fast isolated copies for testing, backup and analysis
```

---

# 📋 SQL Reference

## ⏳ Time Travel — Timestamp

```sql
SELECT *
FROM CUSTOMERS
AT (
    TIMESTAMP => '2024-10-25 14:20:00'::TIMESTAMP
);
```

## ⏪ Time Travel — Offset

```sql
SELECT *
FROM CUSTOMERS
AT (
    OFFSET => -300
);
```

## 🔎 Query History

```sql
SELECT
    query_id,
    query_text,
    start_time
FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY())
WHERE query_text ILIKE '%UPDATE customers%'
ORDER BY start_time DESC
LIMIT 5;
```

## 🔎 Before Statement

```sql
SELECT *
FROM CUSTOMERS
BEFORE (
    STATEMENT => '<QUERY_ID>'
);
```

## 🗑️ Undrop

```sql
UNDROP TABLE employees;
```

## 🧬 Clone Database

```sql
CREATE DATABASE SALES_DB_TEST
CLONE SALES_DB_PROD;
```

## 🧪 Clone Table

```sql
CREATE TABLE order_backup
CLONE orders;
```

## 🔄 Restore From Clone

```sql
CREATE OR REPLACE TABLE orders
CLONE order_backup;
```

## 🗑️ Drop Clone

```sql
DROP DATABASE SALES_DB_TEST;
```

```sql
DROP TABLE order_backup;
```

---

# 🏆 Final Takeaway

```text
                 ❄️ SNOWFLAKE
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
     ⏳ TIME TRAVEL         🧬 ZERO-COPY CLONE
          │                       │
     ┌────┼────┐             ┌────┼────┐
     │    │    │             │    │    │
     ▼    ▼    ▼             ▼    ▼    ▼
   TIME OFFSET STMT         TEST BACKUP ANALYSIS
     │    │    │             │    │    │
     └────┴────┘             └────┴────┘
          │                       │
          ▼                       ▼
   Historical Recovery       Isolated Copies
```
