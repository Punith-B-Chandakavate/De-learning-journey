# ❄️ Snowflake Data Loading Fundamentals

![Snowflake](<https://img.shields.io/badge/Snowflake-Data%20Loading-29B5E8?logo=snowflake\&logoColor=white>)
![Stages](https://img.shields.io/badge/Snowflake-Stages-blue)
![File Formats](<https://img.shields.io/badge/Data-File%20Formats-orange>)
![COPY INTO](<https://img.shields.io/badge/SQL-COPY%20INTO-green>)
![Data Engineering](<https://img.shields.io/badge/Data%20Engineering-Snowflake-purple>)

---

# 📚 Table of Contents

- ❄️ Snowflake Data Loading Fundamentals
- 📚 Table of Contents
- 📖 Overview
- 🎯 Learning Objectives
- 📦 Section 1 — Snowflake Stages
  - 📖 What is a Stage?
  - 🏗️ Stage Architecture
  - 🏠 Internal Stage
    - Create Internal Stage
    - Show Stages
    - List Files
  - ☁️ External Stage
    - Create External Stage
  - 📊 Internal vs External Stage
  - 🏠 Create Internal Stage
  - ☁️ Create External Stage
  - 🔎 List Stage Files
    - Internal Stage
    - External Stage
- 🔎 Section 2 — File Patterns
  - 📖 What is a File Pattern?
  - 🔤 Regular Expressions
  - 📂 File Pattern Example
  - 🔎 Using Patterns with LIST
  - 📥 Using Patterns with COPY INTO
  - 🔄 File Pattern vs File Format
- 📄 Section 3 — File Formats
  - 📖 What is a File Format?
  - 📋 Common File Formats
  - 📝 Create CSV File Format
  - 🔍 Describe File Format
- 📥 Section 4 — COPY Comman
  - 📖 What is COPY INTO?
  - 🚀 COPY INTO Workflow
  - 📦 Bulk Loading
  - 🗃️ Create Target Table
  - 📄 COPY INTO with File Format
  - 🔎 COPY INTO with File Pattern
  - 🔄 Transformation During Loading
  - ⚠️ Error Handling
  - 🧪 Validate Loaded Data
- 🏗️ Complete Data Loading Architecture
- 🔄 How the Four Concepts Work Together
- 💡 Best Practices
  - 📦 Stage Best Practices
  - 🔎 File Pattern Best Practices
  - 📄 File Format Best Practices
  - 📥 COPY INTO Best Practices
- 📋 Important SQL Commands
- 🎤 Interview Questions
  - 1. What is a Snowflake Stage?
  - 2. What are the types of stages?
  - 3. What is the difference between an internal and external stage?
  - 4. What is a File Pattern?
  - 5. What is a File Format?
  - 6. What is the difference between File Pattern and File Format?
  - 7. What is COPY INTO?
  - 8. Can COPY INTO filter files?
  - 9. Can COPY INTO perform transformations?
  - 10. How can COPY INTO handle errors?
- 🎯 Key Takeaways
- 📖 Summary

---

# 📖 Overview

Snowflake provides several features for loading data from files into tables.

The four important concepts covered in this module are:

```text
📦 Stage
   │
   ▼
Where are the files stored?

🔎 File Pattern
   │
   ▼
Which files should be processed?

📄 File Format
   │
   ▼
How should the files be interpreted?

📥 COPY INTO
   │
   ▼
How are the files loaded into tables?
```

Together, these components form the foundation of file-based data ingestion in Snowflake.

---

# 🎯 Learning Objectives

After completing this module, you will be able to:

* Understand Snowflake stages
* Understand internal and external stages
* Create and use stages
* Understand file patterns
* Use regular expressions to filter files
* Understand Snowflake file formats
* Create reusable file format objects
* Understand the `COPY INTO` command
* Perform bulk data loading
* Apply file patterns during loading
* Apply file formats during loading
* Perform supported transformations during loading
* Handle loading errors
* Understand the complete Snowflake file-ingestion workflow

---

# 📦 Section 1 — Snowflake Stages

## 📖 What is a Stage?

A **stage** is a Snowflake location where data files are stored before they are loaded into Snowflake tables or after data is unloaded from tables.

There are two main types of stages:

```text
                    📦 Snowflake Stages
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       🏠 Internal Stage          ☁️ External Stage
              │                         │
              ▼                         ▼
     Snowflake Storage           Cloud Storage
                                        │
                                        ▼
                                    Amazon S3
```

---

## 🏗️ Stage Architecture

A typical file-loading workflow looks like:

```text
Source Files
     │
     ▼
📦 Stage
     │
     ▼
🔎 File Pattern
     │
     ▼
📄 File Format
     │
     ▼
📥 COPY INTO
     │
     ▼
❄️ Snowflake Table
```

The stage provides the location of the files, while the file pattern determines which files are processed and the file format defines how those files should be interpreted.

---

## 🏠 Internal Stage

An **Internal Stage** stores files within Snowflake-managed storage.

An external cloud-storage URL such as an S3 URL is not required.

```text
File
 │
 ▼
🏠 Internal Stage
 │
 ▼
Snowflake-managed Storage
```

### Create Internal Stage

```sql
CREATE OR REPLACE STAGE SALES_INTERNAL_STAGE;
```

### Show Stages

```sql
SHOW STAGES;
```

### List Files

```sql
LIST @SALES_INTERNAL_STAGE;
```

---

## ☁️ External Stage

An **External Stage** points to storage outside Snowflake.

For example:

```text
Amazon S3
    │
    ▼
s3://company-data/raw/
    │
    ▼
☁️ External Stage
    │
    ▼
❄️ Snowflake
```

### Create External Stage

```sql
CREATE OR REPLACE STAGE SALES_S3_STAGE
URL = 's3://company-data/raw/';
```

For secure cloud-storage access, a Storage Integration can be used:

```sql
CREATE OR REPLACE STAGE SALES_S3_STAGE
URL = 's3://company-data/raw/'
STORAGE_INTEGRATION = S3_STORAGE_INT;
```

---

## 📊 Internal vs External Stage

| Feature        | 🏠 Internal Stage   | ☁️ External Stage                       |
| -------------- | ------------------- | ----------------------------------------- |
| Storage        | Snowflake-managed   | External cloud storage                    |
| External URL   | Not required        | Required                                  |
| Example        | Snowflake storage   | Amazon S3                                 |
| Typical Usage  | Direct file staging | Cloud data lake ingestion                 |
| Authentication | Snowflake-managed   | Storage Integration / cloud configuration |

---

## 🏠 Create Internal Stage

```sql
CREATE OR REPLACE STAGE SALES_INTERNAL_STAGE;
```

Verify:

```sql
SHOW STAGES;
```

List staged files:

```sql
LIST @SALES_INTERNAL_STAGE;
```

---

## ☁️ Create External Stage

Example using Amazon S3:

```sql
CREATE OR REPLACE STAGE SALES_S3_STAGE
URL = 's3://company-data/raw/';
```

With Storage Integration:

```sql
CREATE OR REPLACE STAGE SALES_S3_STAGE
URL = 's3://company-data/raw/'
STORAGE_INTEGRATION = S3_STORAGE_INT;
```

---

## 🔎 List Stage Files

Use the `LIST` command to inspect files available in a stage.

### Internal Stage

```sql
LIST @SALES_INTERNAL_STAGE;
```

### External Stage

```sql
LIST @SALES_S3_STAGE;
```

Example:

```text
@SALES_S3_STAGE/
│
├── orders_2025.csv
├── orders_2026.csv
├── customers_2026.csv
└── products_2026.csv
```

---

# 🔎 Section 2 — File Patterns

## 📖 What is a File Pattern?

A **file pattern** is a regular-expression-based filter that tells Snowflake which files should be included or excluded during file operations.

File patterns can be used with operations such as:

```text
LIST
COPY INTO
REMOVE
```

The main question answered by a file pattern is:

> **Which files should Snowflake process?**

---

## 🔤 Regular Expressions

Snowflake file patterns use regular expressions.

| Pattern    | Meaning                        |
| ---------- | ------------------------------ |
| `.*`     | Match any number of characters |
| `orders` | Match the text`orders`       |
| `2026`   | Match the text`2026`         |
| `\.csv`  | Match`.csv`                  |
| `^`      | Beginning of string            |
| `$`      | End of string                  |

Example:

```regex
.*orders_2026.*\.csv
```

---

## 📂 File Pattern Example

Suppose a stage contains:

```text
orders_2025.csv
orders_2026.csv
customers_2026.csv
products_2026.csv
orders_2026_backup.csv
```

Pattern:

```regex
.*orders_2026.*\.csv
```

The matching files would be:

```text
orders_2026.csv          ✅
orders_2026_backup.csv   ✅
```

The following files would not match:

```text
orders_2025.csv          ❌
customers_2026.csv       ❌
products_2026.csv        ❌
```

---

## 🔎 Using Patterns with LIST

A pattern can be used to identify matching files:

```sql
LIST @SALES_S3_STAGE
PATTERN = '.*orders_2026.*\.csv';
```

This helps identify files that match the specified regular expression.

---

## 📥 Using Patterns with COPY INTO

A common use case is filtering files during data loading:

```sql
COPY INTO SALES_RAW
FROM @SALES_S3_STAGE
PATTERN = '.*orders_2026.*\.csv';
```

The `PATTERN` determines **which files are loaded**.

---

## 🔄 File Pattern vs File Format

These two concepts have different responsibilities:

| Concept         | Purpose                                                   |
| --------------- | --------------------------------------------------------- |
| 🔎 File Pattern | Determines**which files** should be processed       |
| 📄 File Format  | Determines**how the selected files** should be read |

```text
Stage
  │
  ▼
🔎 File Pattern
  │
  ▼
Select Files
  │
  ▼
📄 File Format
  │
  ▼
Interpret Files
  │
  ▼
📥 COPY INTO
  │
  ▼
Table
```

---

# 📄 Section 3 — File Formats

## 📖 What is a File Format?

A **File Format** defines how Snowflake should interpret data files during loading and unloading.

For example, when loading a CSV file, Snowflake needs to understand:

* Column delimiter
* Header handling
* Quote characters
* NULL representation
* File type
* Encoding

Conceptually:

```text
📄 File Format
      │
      ├── File Type
      ├── Field Delimiter
      ├── Header Handling
      ├── Quote Handling
      ├── NULL Handling
      └── Encoding
```

---

## 📋 Common File Formats

| Format  | Description                       |
| ------- | --------------------------------- |
| CSV     | Delimited text data               |
| JSON    | Semi-structured JSON data         |
| Parquet | Columnar file format              |
| Avro    | Row-oriented serialization format |
| ORC     | Columnar file format              |

---

## 📝 Create CSV File Format

```sql
CREATE OR REPLACE FILE FORMAT SALES_CSV_FORMAT
TYPE = CSV
SKIP_HEADER = 1
FIELD_OPTIONALLY_ENCLOSED_BY = '"';
```

This configuration tells Snowflake:

```text
TYPE = CSV
      ↓
The source file is CSV

SKIP_HEADER = 1
      ↓
Skip the first row

FIELD_OPTIONALLY_ENCLOSED_BY = '"'
      ↓
Values may be enclosed in double quotes
```

---

## 🔍 Describe File Format

To inspect the configuration:

```sql
DESC FILE FORMAT SALES_CSV_FORMAT;
```

List available file formats:

```sql
SHOW FILE FORMATS;
```

---

# 📥 Section 4 — COPY Command

## 📖 What is COPY INTO?

`COPY INTO` is a Snowflake SQL command primarily used to **bulk load data from staged files into Snowflake tables**.

Basic workflow:

```text
Files
  │
  ▼
Stage
  │
  ▼
COPY INTO
  │
  ▼
Snowflake Table
```

---

## 🚀 COPY INTO Workflow

```text
             Source Files
                  │
                  ▼
               📦 Stage
                  │
                  ▼
             🔎 Pattern
                  │
                  ▼
            📄 File Format
                  │
                  ▼
             📥 COPY INTO
                  │
                  ▼
           Snowflake Table
```

---

## 📦 Bulk Loading

`COPY INTO` is designed to efficiently load large volumes of data from staged files.

Example:

```sql
COPY INTO SALES_RAW
FROM @SALES_S3_STAGE
FILE_FORMAT = SALES_CSV_FORMAT;
```

---

## 🗃️ Create Target Table

Create the destination table before loading the staged data:

```sql
CREATE OR REPLACE TABLE SALES_RAW (
    ORDER_ID INT,
    CUSTOMER_ID INT,
    PRODUCT STRING,
    QUANTITY INT,
    PRICE FLOAT,
    ORDER_DATE DATE
);
```

---

## 📄 COPY INTO with File Format

```sql
COPY INTO SALES_RAW
FROM @SALES_S3_STAGE
FILE_FORMAT = SALES_CSV_FORMAT;
```

Here:

```text
@SALES_S3_STAGE
        ↓
Source Stage

SALES_CSV_FORMAT
        ↓
How the file should be interpreted

SALES_RAW
        ↓
Target Table
```

---

## 🔎 COPY INTO with File Pattern

Load only specific files:

```sql
COPY INTO SALES_RAW
FROM @SALES_S3_STAGE
FILE_FORMAT = SALES_CSV_FORMAT
PATTERN = '.*orders_2026.*\.csv';
```

Responsibilities:

```text
🔎 PATTERN
    ↓
Select files

📄 FILE_FORMAT
    ↓
Read files correctly

📥 COPY INTO
    ↓
Load files
```

---

## 🔄 Transformation During Loading

`COPY INTO` can perform supported transformations while loading data.

Example:

```sql
COPY INTO SALES_RAW
FROM (
    SELECT
        $1::INT,
        $2::INT,
        $3::STRING,
        $4::INT,
        $5::FLOAT,
        $6::DATE
    FROM @SALES_S3_STAGE
)
FILE_FORMAT = SALES_CSV_FORMAT;
```

The staged file columns are referenced using positional notation:

```text
$1 → ORDER_ID
$2 → CUSTOMER_ID
$3 → PRODUCT
$4 → QUANTITY
$5 → PRICE
$6 → ORDER_DATE
```

---

## ⚠️ Error Handling

`COPY INTO` provides options for handling errors during loading.

Example:

```sql
COPY INTO SALES_RAW
FROM @SALES_S3_STAGE
FILE_FORMAT = SALES_CSV_FORMAT
ON_ERROR = 'CONTINUE';
```

This allows the loading process to continue when supported loading errors occur.

Error-handling behavior should be selected based on the data-quality and reliability requirements of the pipeline.

---

## 🧪 Validate Loaded Data

After loading, validate the target table:

```sql
SELECT *
FROM SALES_RAW;
```

Check the number of records:

```sql
SELECT COUNT(*)
FROM SALES_RAW;
```

---

# 🏗️ Complete Data Loading Architecture

```text
                         ☁️ Amazon S3
                              │
                              ▼
                    🔐 Storage Integration
                              │
                              ▼
                       📦 External Stage
                              │
                              ▼
                       🔎 File Pattern
                              │
                              ▼
                       📄 File Format
                              │
                              ▼
                        📥 COPY INTO
                              │
                              ▼
                         🥉 Raw Table
                              │
                              ▼
                       🥈 Silver Layer
                              │
                              ▼
                        🥇 Gold Layer
                              │
                              ▼
                         📊 Analytics
```

---

# 🔄 How the Four Concepts Work Together

```text
┌──────────────────────────────────────────────┐
│                  📦 STAGE                    │
│                                              │
│              Where are files?               │
│                                              │
│       Internal / External Storage            │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│              🔎 FILE PATTERN                 │
│                                              │
│        Which files should be processed?      │
│                                              │
│             Regular Expression               │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│              📄 FILE FORMAT                  │
│                                              │
│          How should files be read?           │
│                                              │
│       CSV / JSON / Parquet / etc.            │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│               📥 COPY INTO                   │
│                                              │
│       Load selected files into table         │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
                 ❄️ Snowflake Table
```

---

# 💡 Best Practices

## 📦 Stage Best Practices

* Use meaningful stage names.
* Use external stages for cloud data lake ingestion.
* Use Storage Integration for secure cloud authentication.
* Organize external storage paths logically.
* Separate raw, processed, and curated data locations.

## 🔎 File Pattern Best Practices

* Use precise regular expressions.
* Test patterns before production loading.
* Avoid overly broad patterns.
* Use consistent source-file naming conventions.
* Filter files using meaningful attributes such as date or source.

## 📄 File Format Best Practices

* Create reusable file format objects.
* Use the correct format for the source data.
* Explicitly configure delimiters and headers where required.
* Standardize file-format definitions across pipelines.

## 📥 COPY INTO Best Practices

* Validate the target table schema.
* Use appropriate file formats.
* Use file patterns when required.
* Configure error handling carefully.
* Validate record counts after loading.
* Monitor loading history.
* Avoid loading unrelated files from the same stage.

---

# 📋 Important SQL Commands

| Requirement           | SQL Command                    |
| --------------------- | ------------------------------ |
| Create internal stage | `CREATE STAGE`               |
| Create external stage | `CREATE STAGE ... URL = ...` |
| List stages           | `SHOW STAGES`                |
| List staged files     | `LIST @stage_name`           |
| Create file format    | `CREATE FILE FORMAT`         |
| Inspect file format   | `DESC FILE FORMAT`           |
| List file formats     | `SHOW FILE FORMATS`          |
| Load files            | `COPY INTO table`            |
| Filter files          | `PATTERN = 'regex'`          |
| Handle errors         | `ON_ERROR = ...`             |
| Query loaded data     | `SELECT ...`                 |

---

# 🎤 Interview Questions

### 1. What is a Snowflake Stage?

A stage is a location where files are stored before loading them into Snowflake tables or after unloading data from tables.

### 2. What are the types of stages?

```text
🏠 Internal Stage
☁️ External Stage
```

An internal stage uses Snowflake-managed storage, while an external stage points to external cloud storage such as Amazon S3.

### 3. What is the difference between an internal and external stage?

An internal stage uses Snowflake-managed storage, while an external stage points to external cloud storage.

### 4. What is a File Pattern?

A file pattern is a regular-expression-based filter used to select specific files for processing.

### 5. What is a File Format?

A file format defines how Snowflake should interpret the structure of a staged file.

### 6. What is the difference between File Pattern and File Format?

```text
File Pattern
     ↓
Which files?

File Format
     ↓
How should they be read?
```

### 7. What is COPY INTO?

`COPY INTO` is a Snowflake command primarily used to bulk load data from staged files into Snowflake tables.

### 8. Can COPY INTO filter files?

Yes. The `PATTERN` option can be used to select files using a regular expression.

### 9. Can COPY INTO perform transformations?

Yes. Supported transformations can be applied during the loading operation.

### 10. How can COPY INTO handle errors?

The `ON_ERROR` option can be used to configure how loading errors should be handled.

---

# 🎯 Key Takeaways

* 📦 A **Stage** is a location for staged data files.
* 🏠 **Internal stages** use Snowflake-managed storage.
* ☁️ **External stages** point to external cloud storage.
* 📄 **File formats** define how Snowflake reads files.
* 🔎 **File patterns** determine which files should be processed.
* 📥 **COPY INTO** performs bulk data loading.
* 🔄 `COPY INTO` can support supported transformations during loading.
* ⚠️ Error-handling behavior can be configured during loading.
* 🔐 Storage Integrations provide secure access to external cloud storage.
* 📈 Stages and `COPY INTO` form an important part of Snowflake data-ingestion pipelines.

