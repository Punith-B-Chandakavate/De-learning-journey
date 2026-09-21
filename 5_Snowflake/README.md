# ❄️ Snowflake Complete Learning Repository

> A comprehensive learning repository covering **Snowflake Fundamentals**, **Account Setup**, **Snowflake Architecture**, **S3 Integration**, **Data Loading**, **Time Travel**, **Zero-Copy Cloning**, and practical **Data Engineering & Analytics** workflows using Snowflake.

![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Cloud-29B5E8?logo=snowflake\&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Analytics-CC2927?logo=postgresql\&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS-S3-FF9900?logo=amazons3\&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache-Airflow-017CEE?logo=apacheairflow\&logoColor=white)
![Power BI](https://img.shields.io/badge/Power-BI-F2C811?logo=powerbi\&logoColor=black)
![Data Engineering](https://img.shields.io/badge/Data-Engineering-4CAF50)

---

# 📚 Table of Contents

* About This Repository
* Features
* Repository Structure
* Learning Modules
* Snowflake Learning Roadmap
* Snowflake Architecture
* Data Engineering Project Architecture
* Technologies Covered
* Learning Outcomes
* Prerequisites
* Best Practices
* Repository Goal
* Recommended Learning Order

---

# 📖 About This Repository

This repository is a structured learning resource for understanding **Snowflake as a modern cloud data platform** and applying it to real-world Data Engineering workloads.

The learning path starts with **Snowflake fundamentals and account setup**, then progresses through database objects, integrations, AWS S3 connectivity, data loading, Time Travel, Zero-Copy Cloning, and practical analytics workflows.

The repository combines:

* 📘 Conceptual documentation
* 💻 SQL examples
* ☁️ Cloud integration
* 🔄 Data ingestion workflows
* 🏗️ Data warehouse design
* 📊 Analytics use cases
* 🎯 Interview preparation
* 🧪 Hands-on Snowflake exercises

---

# 🚀 Features

* ✅ Snowflake Fundamentals
* ✅ Snowflake Architecture
* ✅ Cloud Data Warehouse Concepts
* ✅ Storage, Compute & Services Layers
* ✅ Virtual Warehouses
* ✅ Databases & Schemas
* ✅ Tables & Views
* ✅ Roles & Users
* ✅ RBAC
* ✅ Snowflake Integrations
* ✅ Storage Integration
* ✅ AWS S3 Integration
* ✅ External Stages
* ✅ File Formats
* ✅ File Patterns
* ✅ COPY INTO
* ✅ Data Loading
* ✅ Time Travel
* ✅ Zero-Copy Cloning
* ✅ SQL Analytics
* ✅ Incremental Data Processing
* ✅ Airflow Integration
* ✅ Power BI Analytics
* ✅ Subject Area Development
* ✅ Hands-on SQL
* ✅ Interview Questions
* ✅ Data Engineering Project Implementation

---

# 📂 Repository Structure

```text
5_Snowflake/
│
├── 01_Fundamentals/
│   ├── images/
│   └── README.md
│
├── 02_Snowflake_Account_Setup/
│   ├── images/
│   └── README.md
│
├── 03_Snowflake_vs_databricks/
│   └── README.md
│
├── 04_Snowflake_Concepts/
│   └── README.md
│
├── 05_Snowflake_S3_integration/
│   ├── images/
│   └── README.md
│
├── 06_Snowflake_Data_Loading/
│   ├── images/
│   └── README.md
│
├── 06_Snowflake_Time_Travel_Zero_Copy_Cloning/
│   ├── images/
│   └── README.md
│
├── dataset/
│   └── ...
│
└── README.md
```

---

# 🗂️ Learning Modules

## 🔹 Module 1 — Snowflake Fundamentals

Learn the core concepts required to understand Snowflake and modern cloud data warehousing.

| Topic                  | Description                                          | File                                       |
| ---------------------- | ---------------------------------------------------- | ------------------------------------------ |
| Snowflake Fundamentals | Introduction to Snowflake and cloud data warehousing | [`README.md`](./01_Fundamentals/README.md) |

### Topics Covered

* Snowflake overview
* Cloud data warehouse
* Snowflake architecture
* Storage layer
* Compute layer
* Services layer
* Virtual warehouses
* Connectivity
* Snowflake vs traditional RDBMS
* Snowflake vs traditional data warehouse

---

## 🔹 Module 2 — Snowflake Account Setup

Learn how to create and configure a Snowflake environment for development and learning.

| Topic                   | Description                                             | File                                                  |
| ----------------------- | ------------------------------------------------------- | ----------------------------------------------------- |
| Snowflake Account Setup | Configure Snowflake account and development environment | [`README.md`](./02_Snowflake_Account_Setup/README.md) |

### Topics Covered

* Snowflake account creation
* Trial account
* Cloud platform selection
* Region selection
* Snowsight
* Virtual warehouse
* Database
* Schema
* Table
* View
* Basic SQL execution

---

## 🔹 Module 3 — Snowflake vs Databricks

Understand the differences between Snowflake and Databricks and where each platform fits into modern Data Engineering architectures.

| Topic                   | Description                                   | File                                                  |
| ----------------------- | --------------------------------------------- | ----------------------------------------------------- |
| Snowflake vs Databricks | Platform architecture and workload comparison | [`README.md`](./03_Snowflake_vs_databricks/README.md) |

### Comparison Areas

```text
Snowflake
    │
    ├── Cloud Data Warehouse
    ├── SQL Analytics
    ├── Structured Data
    ├── Virtual Warehouses
    └── BI / Analytics

Databricks
    │
    ├── Lakehouse Platform
    ├── Apache Spark
    ├── PySpark
    ├── Data Engineering
    ├── Streaming
    └── Machine Learning
```

---

## 🔹 Module 4 — Snowflake Concepts

Learn the core Snowflake objects and capabilities used in Data Engineering projects.

| Topic              | Description                                      | File                                             |
| ------------------ | ------------------------------------------------ | ------------------------------------------------ |
| Snowflake Concepts | Core Snowflake objects and platform capabilities | [`README.md`](./04_Snowflake_Concepts/README.md) |

### Topics Covered

* Databases
* Schemas
* Tables
* Views
* Virtual Warehouses
* Roles
* Users
* RBAC
* Integrations
* Stages
* File Formats
* File Patterns
* COPY INTO
* Time Travel
* Zero-Copy Cloning

---

## 🔹 Module 5 — Snowflake S3 Integration

Learn how Snowflake securely connects to Amazon S3 using AWS IAM and Snowflake Storage Integration.

| Topic                    | Description                                  | File                                                   |
| ------------------------ | -------------------------------------------- | ------------------------------------------------------ |
| Snowflake S3 Integration | Configure secure Snowflake → S3 connectivity | [`README.md`](./05_Snowflake_S3_integration/README.md) |

### Architecture

```text
                 Amazon S3
                    │
                    │
              IAM Role
                    │
                    ▼
          Snowflake Storage
             Integration
                    │
                    ▼
           External Stage
                    │
                    ▼
             Snowflake RAW
```

### Topics Covered

* AWS IAM Role
* IAM Policies
* Trust Relationship
* External ID
* Role ARN
* Snowflake Storage Integration
* Allowed Locations
* External Stage
* S3 access
* Connectivity validation

---

## 🔹 Module 6 — Snowflake Data Loading

Learn how files are loaded from external storage into Snowflake tables.

| Topic        | Description                                  | File                                                 |
| ------------ | -------------------------------------------- | ---------------------------------------------------- |
| Data Loading | Load files from stages into Snowflake tables | [`README.md`](./06_Snowflake_Data_Loading/README.md) |

### Data Loading Flow

```text
CSV / JSON / Parquet
        │
        ▼
     Amazon S3
        │
        ▼
 External Stage
        │
        ▼
     COPY INTO
        │
        ▼
   RAW Table
        │
        ▼
 Transformation
        │
        ▼
 Analytics Tables
```

### Topics Covered

* Internal stages
* External stages
* File formats
* CSV files
* JSON files
* Parquet files
* File patterns
* COPY INTO
* Validation
* Error handling
* Data loading

---

## 🔹 Module 7 — Time Travel & Zero-Copy Cloning

Learn Snowflake's data recovery and environment cloning capabilities.

| Topic                           | Description                                              | File                                                                  |
| ------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| Time Travel & Zero-Copy Cloning | Recover historical data and create metadata-based clones | [`README.md`](./06_Snowflake_Time_Travel_Zero_Copy_Cloning/README.md) |

### Time Travel

Time Travel allows querying historical versions of data within the configured retention period.

```text
Current Table
     │
     ├── Current Data
     │
     ├── Previous Version
     │
     ├── Earlier Version
     │
     └── Historical Version
```

### Zero-Copy Cloning

```text
Production Database
        │
        │ CLONE
        ▼
Development Database
        │
        ▼
Independent Testing
```

### Topics Covered

* Time Travel
* `AT`
* `BEFORE`
* Query history
* Data recovery
* `UNDROP`
* Database cloning
* Table cloning
* Development environments
* Testing environments
* Backup scenarios

---

# 📈 Snowflake Learning Roadmap

```text
                  Snowflake
                      │
                      ▼
             Cloud Data Warehouse
                      │
                      ▼
             Snowflake Architecture
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Storage      Compute     Services
          │           │           │
          └───────────┼───────────┘
                      ▼
             Virtual Warehouses
                      │
                      ▼
               Database & Schema
                      │
                      ▼
              Tables & Views
                      │
                      ▼
               Roles & RBAC
                      │
                      ▼
                Integrations
                      │
                      ▼
                 AWS S3
                      │
                      ▼
              External Stage
                      │
                      ▼
                 COPY INTO
                      │
                      ▼
                RAW Tables
                      │
                      ▼
             Data Transformation
                      │
                      ▼
              Analytics Layer
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
       Airflow                 Power BI
```

---

# 🏗️ Snowflake Architecture

```text
                 Snowflake Platform
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
   Storage Layer    Compute Layer     Cloud Services
       │                 │                 │
       ▼                 ▼                 ▼
 Micro-partitions   Virtual           Authentication
 Columnar Data      Warehouses        RBAC
 Compression        Scaling           Metadata
 Metadata            Multi-cluster     Query Management
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                    SQL Analytics
```

---

# 🏢 Data Engineering Architecture

The Snowflake modules in this repository are designed to support an end-to-end Data Engineering workflow.

```text
                    Source Systems
                         │
                         ▼
                   Massive API
                         │
                         ▼
                   Apache Airflow
                         │
                         ▼
                     Amazon S3
                         │
                         ▼
                Snowflake External Stage
                         │
                         ▼
                    RAW Layer
                         │
                         ▼
                   CORE Layer
                         │
                         ▼
              DIMENSION + FACT
                         │
                         ▼
                  Subject Area
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
          Power BI              Analytics
              │
              ▼
         Dashboards
```

---

# 🔄 Data Loading Architecture

```text
                  Amazon S3
                      │
                      ▼
              S3 Bronze Location
                      │
                      ▼
           Snowflake Storage Integration
                      │
                      ▼
              Snowflake Stage
                      │
                      ▼
                  COPY INTO
                      │
                      ▼
                  RAW Tables
                      │
                      ▼
              Transformation
                      │
                      ▼
                 CORE Tables
                      │
                      ▼
             Dimension / Fact
                      │
                      ▼
              Subject Area
                      │
                      ▼
                 Power BI
```

---

# ⚡ Snowflake Core Concepts

## 🗄️ Storage

Snowflake stores data using a managed storage layer based on compressed
columnar data and micro-partitions.

```text
Table
  │
  ▼
Micro-partitions
  │
  ├── Column Data
  ├── Metadata
  └── Compression
```

---

## ⚙️ Compute

Snowflake uses **Virtual Warehouses** to execute queries and data-processing workloads.

```text
Virtual Warehouse
       │
       ├── Compute Resources
       ├── Query Execution
       ├── Scaling
       └── Workload Isolation
```

Example:

```sql
CREATE WAREHOUSE IF NOT EXISTS ETL_DEV_WH
WITH
    WAREHOUSE_SIZE = 'XSMALL'
    AUTO_SUSPEND = 60
    AUTO_RESUME = TRUE;
```

---

## 🔐 Security & Access Control

Snowflake supports role-based access control for managing access to databases,
schemas, tables, views, and other objects.

```text
User
 │
 ▼
Role
 │
 ▼
Privileges
 │
 ▼
Snowflake Objects
```

---

# 🔗 Snowflake Integrations

Snowflake integrations provide controlled connections between Snowflake and
external services.

```text
Snowflake
    │
    ├── Storage Integration
    │        │
    │        └── Amazon S3
    │
    ├── API Integration
    │
    ├── Security Integration
    │
    └── Catalog Integration
```

---

# 📦 Stages & Data Loading

Stages provide locations for files before loading data into Snowflake or
during data unloading.

```text
External Source
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

Common loading components:

* 📦 Stage
* 📄 File Format
* 🔎 File Pattern
* 📥 COPY INTO

---

# ⏪ Time Travel

Time Travel provides access to historical versions of Snowflake data within
the configured retention period.

Example:

```sql
SELECT *
FROM CUSTOMERS
AT (
    TIMESTAMP => '2024-10-25 14:20:00'::TIMESTAMP
);
```

Offset example:

```sql
SELECT *
FROM CUSTOMERS
AT (
    OFFSET => -300
);
```

---

# 🧬 Zero-Copy Cloning

Zero-Copy Cloning creates a clone without immediately duplicating the
underlying data.

```text
Production
    │
    │ CLONE
    ▼
Development
    │
    ▼
Testing / Analysis
```

Example:

```sql
CREATE DATABASE SALES_DB_TEST
CLONE SALES_DB_PROD;
```

Common use cases:

* Development
* Testing
* Data analysis
* Backup before changes
* Experimentation

---

# 🔄 Snowflake + Airflow

Snowflake can be integrated with Apache Airflow to orchestrate ETL workflows.

```text
              Apache Airflow
                    │
                    ▼
              EOD Ingestion
                    │
                    ▼
                Amazon S3
                    │
                    ▼
             Snowflake RAW
                    │
                    ▼
             Snowflake CORE
                    │
                    ▼
           Dimension / Fact
                    │
                    ▼
             Analytics Layer
```

Example Airflow workflow:

```text
Extract
   │
   ▼
Transform
   │
   ▼
Load S3
   │
   ▼
Load Snowflake RAW
   │
   ▼
Merge CORE
   │
   ▼
Build Dimensions
   │
   ▼
Build Facts
```

---

# 📊 Snowflake + Power BI

Snowflake can serve as the analytical data platform for Power BI reporting.

```text
Snowflake
    │
    ▼
Subject Area
    │
    ▼
Power BI Connector
    │
    ▼
Power Query
    │
    ▼
Semantic Model
    │
    ▼
Power BI Dashboards
```

Typical analytics include:

* Market liquidity
* Security performance
* Trading volume
* ETF analysis
* Watchlist analysis
* Sector analysis
* Daily pricing

---

# 🛠️ Technologies Covered

| Technology        | Purpose                             |
| ----------------- | ----------------------------------- |
| ❄️ Snowflake      | Cloud data warehouse                |
| 🗄️ SQL           | Data querying and transformation    |
| ☁️ AWS S3         | Cloud object storage                |
| 🔐 AWS IAM        | Secure cloud access                 |
| 🔄 Apache Airflow | Workflow orchestration              |
| 📊 Power BI       | Business intelligence               |
| 🐍 Python         | Data engineering and API processing |
| 📈 Massive API    | Market data ingestion               |

---

# 🎯 Learning Outcomes

After completing this repository, you should be able to:

* Understand Snowflake architecture
* Create Snowflake databases and schemas
* Create and manage virtual warehouses
* Create tables and views
* Understand Snowflake storage and compute
* Implement RBAC
* Create Snowflake integrations
* Connect Snowflake with AWS S3
* Configure external stages
* Load data using `COPY INTO`
* Work with file formats and patterns
* Use Time Travel
* Recover historical data
* Create Zero-Copy Clones
* Build RAW and CORE data layers
* Design analytical Dimension and Fact tables
* Integrate Snowflake with Airflow
* Build analytical datasets for Power BI
* Develop an end-to-end Snowflake Data Engineering pipeline

---

# ▶️ Prerequisites

To get the most from this repository, you should have basic knowledge of:

* Python
* SQL
* Relational databases
* Data Engineering fundamentals
* ETL / ELT concepts
* Cloud fundamentals
* AWS S3 basics
* Git and GitHub

---

# 💡 Best Practices

## ❄️ Snowflake

* Use appropriately sized virtual warehouses.
* Enable `AUTO_SUSPEND`.
* Enable `AUTO_RESUME` where appropriate.
* Separate warehouses by workload.
* Avoid unnecessary long-running warehouses.
* Use clear database and schema naming conventions.

---

## 🗄️ Data Modeling

* Separate RAW and analytical layers.
* Use appropriate Dimension and Fact tables.
* Keep transformations modular.
* Maintain consistent naming conventions.
* Document important tables and views.

---

## 🔐 Security

* Follow the Principle of Least Privilege.
* Use roles instead of assigning privileges directly to users where appropriate.
* Avoid hardcoding credentials.
* Never commit passwords or access keys.
* Use secure cloud authentication mechanisms.
* Review permissions regularly.

---

## ☁️ AWS S3 Integration

* Restrict allowed S3 locations.
* Use IAM roles instead of hardcoded credentials where appropriate.
* Configure appropriate trust relationships.
* Keep S3 paths organized.
* Separate raw and processed data.

---

## 📥 Data Loading

* Define reusable file formats.
* Validate incoming files.
* Use appropriate file patterns.
* Monitor `COPY INTO` results.
* Handle rejected records appropriately.
* Validate row counts after loading.

---

## 🔄 ETL / ELT

* Keep ingestion and transformation stages separate.
* Design pipelines to support incremental processing.
* Use metadata and audit information where required.
* Make pipelines restartable.
* Validate data before downstream processing.

---

## 📊 Analytics

* Prepare curated datasets for BI tools.
* Keep business logic in reusable analytical views where appropriate.
* Avoid exposing unnecessary RAW tables to reporting users.
* Use Power BI semantic models for reporting.
* Validate analytical metrics against source data.

---

# 📋 Repository Progress

```text
01  Snowflake Fundamentals
 │
 ▼
02  Snowflake Account Setup
 │
 ▼
03  Snowflake vs Databricks
 │
 ▼
04  Snowflake Concepts
 │
 ▼
05  Snowflake S3 Integration
 │
 ▼
06  Snowflake Data Loading
 │
 ▼
07  Time Travel & Zero-Copy Cloning
 │
 ▼
08  Airflow Integration
 │
 ▼
09  Analytics / Power BI
 │
 ▼
10  End-to-End Data Engineering
```

---

# 🎯 Repository Goal

The goal of this repository is to build a strong understanding of **Snowflake
from fundamentals to practical Data Engineering implementation**.

The learning journey progresses from:

```text
Snowflake Fundamentals
        │
        ▼
Snowflake Architecture
        │
        ▼
Account & Warehouse Setup
        │
        ▼
Databases & Schemas
        │
        ▼
Security & RBAC
        │
        ▼
S3 Integration
        │
        ▼
Data Loading
        │
        ▼
RAW / CORE Processing
        │
        ▼
Dimension & Fact Models
        │
        ▼
Analytics
        │
        ▼
Power BI
```

The repository is intended to bridge the gap between **learning Snowflake
concepts** and building **practical cloud Data Engineering pipelines**.

---

# 📚 Recommended Learning Order

Follow the modules in this order:

```text
1. Snowflake Fundamentals
           │
           ▼
2. Snowflake Account Setup
           │
           ▼
3. Snowflake vs Databricks
           │
           ▼
4. Snowflake Concepts
           │
           ▼
5. Snowflake S3 Integration
           │
           ▼
6. Snowflake Data Loading
           │
           ▼
7. Time Travel & Zero-Copy Cloning
           │
           ▼
8. Airflow + Snowflake
           │
           ▼
9. Subject Area / Analytics
           │
           ▼
10. Power BI
           │
           ▼
End-to-End Data Engineering
```

---
