# 🥈 Silver Layer

![Azure](<https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoftazure&logoColor=white>)
![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-FF3621?logo=databricks&logoColor=white)
![Unity Catalog](https://img.shields.io/badge/Unity-Catalog-orange)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)

---

⬅️ [Back to Bronze Layer – Ingest Raw Dimension Data](../01_Bronze_Layer/README.md)

---

# 📚 Table of Contents

- Overview
- Learning Objectives
- Prerequisites
- What is the Silver Layer?
- Why Do We Need the Silver Layer?
- Silver Layer Responsibilities
- Medallion Architecture
- Silver Layer Architecture
- Silver Layer Characteristics
- Data Sources
- Typical Transformations
- Data Quality Framework
- Delta Lake in the Silver Layer
- Unity Catalog in the Silver Layer
- Silver Layer Workflow
- Bronze vs Silver
- Silver vs Gold
- Benefits
- Best Practices
- Common Mistakes
- Interview Questions
- Summary
- Key Takeaways
- Notebook Modules

---

# 📖 Overview

The **Silver Layer** is the second layer of the **Medallion Architecture** and serves as the **data refinement layer** within the Lakehouse. It receives raw datasets from the Bronze layer and transforms them into clean, validated, standardized, and trusted datasets.

Unlike the Bronze layer, which preserves data exactly as received, the Silver layer focuses on improving data quality through cleansing, validation, standardization, and business rule enforcement.

The datasets produced in the Silver layer become the trusted source for downstream Gold layer aggregations, dashboards, machine learning, and business reporting.

---

# 🎯 Learning Objectives

After completing this module, you will be able to:

- Understand the purpose of the Silver Layer.
- Explain the responsibilities of the Silver Layer.
- Understand common data quality transformations.
- Learn how Bronze data becomes trusted datasets.
- Understand incremental processing.
- Learn the role of Delta Lake and Unity Catalog.
- Prepare data for Gold layer analytics.

---

# 📋 Prerequisites

Before starting this module, you should have completed:

- Azure Databricks Workspace Setup
- Azure Data Lake Storage Gen2 Setup
- Unity Catalog Configuration
- Bronze Layer Data Ingestion
- PySpark Fundamentals
- Delta Lake Basics

---

# 🥈 What is the Silver Layer?

The **Silver Layer** is responsible for transforming raw Bronze data into clean and reliable datasets.

The main objective is to improve data quality before it is consumed by business users or analytical applications.

Typical processing includes:

- Data cleansing
- Duplicate removal
- Data validation
- Standardization
- Type conversion
- Null handling
- Business rule validation
- Metadata enrichment

The Silver layer produces **trusted datasets** that are ready for downstream analytics.

---

# ⭐ Why Do We Need the Silver Layer?

Raw data often contains inconsistencies that can affect analytics.

The Silver Layer addresses these issues by:

- Removing duplicate records
- Correcting invalid values
- Standardizing formats
- Handling missing data
- Applying business validations
- Improving consistency
- Creating trusted datasets

---

# 📌 Silver Layer Responsibilities

The Silver Layer is responsible for:

- Reading Bronze tables
- Cleansing raw data
- Removing duplicate records
- Handling null values
- Standardizing text and dates
- Converting data types
- Applying business rules
- Creating trusted Delta tables
- Preparing data for Gold

---

# 🏛 Medallion Architecture

```text
           Source Systems
                  │
                  ▼
          🥉 Bronze Layer
        Raw Source Data
                  │
                  ▼
          🥈 Silver Layer
 Cleaned & Validated Data
                  │
                  ▼
           🥇 Gold Layer
 Business Ready Data
```

---

# 🏗 Silver Layer Architecture

![Silver Layer Architecture](images/01_Silver_Layer_Architecture.png)

```text
Bronze Delta Tables
         │
         ▼
PySpark Transformations
         │
         ▼
Data Cleansing
         │
         ▼
Validation
         │
         ▼
Standardization
         │
         ▼
Business Rules
         │
         ▼
Silver Delta Tables
```

---

# 📌 Silver Layer Characteristics

- Clean Data
- Trusted Data
- Standardized
- Validated
- Deduplicated
- Incremental Processing
- Delta Lake Storage
- Analytics Ready

---

# 📂 Data Sources

The Silver Layer receives data from the Bronze Layer.

### Dimension Tables

- Categories
- Brands
- Products
- Customers
- Calendar

### Fact Tables

- Orders
- Order Items
- Shipments
- Returns

---

# 🔄 Typical Transformations

Typical transformations include:

- Remove duplicates
- Handle null values
- Standardize text
- Convert data types
- Normalize categorical values
- Apply business validations
- Filter invalid records
- Add processing metadata

---

# ✅ Data Quality Framework

The Silver Layer improves data quality through:

- Completeness
- Accuracy
- Consistency
- Validity
- Uniqueness
- Timeliness

These quality checks ensure reliable downstream analytics.

---

# 🏆 Delta Lake in the Silver Layer

Delta Lake provides enterprise-grade capabilities such as:

- ACID Transactions
- MERGE Operations
- Schema Enforcement
- Schema Evolution
- Time Travel
- Data Versioning
- High Performance
- Change Data Feed (CDF)

---

# 🔐 Unity Catalog in the Silver Layer

Unity Catalog provides:

- Centralized Governance
- Metadata Management
- Access Control
- Data Lineage
- Auditing
- Secure Data Sharing

---

# 🔄 Silver Layer Workflow

```text
Read Bronze Tables
        │
        ▼
Clean Data
        │
        ▼
Validate Records
        │
        ▼
Standardize Data
        │
        ▼
Apply Business Rules
        │
        ▼
Write Silver Tables
```

---

# ⚖️ Bronze vs Silver

| Bronze Layer            | Silver Layer             |
| ----------------------- | ------------------------ |
| Raw Data                | Clean Data               |
| Minimal Transformations | Business Transformations |
| Source Copy             | Trusted Dataset          |
| Append Only             | Update & Merge           |
| Data Ingestion          | Data Refinement          |

---

# ⚖️ Silver vs Gold

| Silver Layer     | Gold Layer        |
| ---------------- | ----------------- |
| Clean Data       | Business Data     |
| Standardized     | Aggregated        |
| Detailed Records | KPIs & Metrics    |
| Trusted Dataset  | Reporting Dataset |

---

# 📈 Benefits

- Improved Data Quality
- Trusted Datasets
- Better Analytics
- Standardized Data
- Easier Reporting
- Reliable Machine Learning
- Better Performance
- Centralized Governance

---

# ✅ Verify Silver Tables

After executing the Silver notebooks, verify that all Silver Delta tables are successfully created in Unity Catalog.

![Verify Silver Tables](images/02_verify_silver_tables.png)

You should see tables similar to:

- slv_category
- slv_brands
- slv_products
- slv_customers
- slv_calendar
- slv_orders
- slv_order_items
- slv_shipments
- slv_returns

---

# 💡 Best Practices

- Remove duplicate records.
- Validate mandatory fields.
- Standardize formats.
- Keep transformations deterministic.
- Store data in Delta format.
- Use MERGE for incremental processing.
- Maintain processing metadata.
- Document transformation rules.
- Monitor data quality.
- Separate Silver from Gold logic.

---

# ⚠️ Common Mistakes

- Leaving duplicate records.
- Ignoring null values.
- Mixing aggregation with cleansing.
- Not validating business rules.
- Using inconsistent formats.
- Writing directly to Gold.
- Ignoring metadata.
- Using inferred schemas in production.

---

# 🎤 Interview Questions

### 1. What is the Silver Layer?

The **Silver Layer** is the second layer of the **Medallion Architecture** that transforms raw Bronze data into clean, validated, standardized, and trusted datasets.

Unlike the Bronze layer, which preserves raw source data, the Silver layer focuses on improving data quality by applying cleansing, validation, standardization, and business rules. The resulting datasets become the trusted source for downstream Gold layer analytics, dashboards, and machine learning workloads.

---

### 2. Why is the Silver Layer important?

The Silver Layer improves the quality and reliability of data before it is consumed by business users.

Its importance includes:

- Removes duplicate records.
- Handles null and missing values.
- Standardizes text, dates, and numeric formats.
- Validates business rules.
- Produces trusted datasets.
- Improves reporting accuracy.
- Prepares data for Gold layer transformations.

Without the Silver Layer, poor-quality data from the Bronze layer could lead to inaccurate analytics and business decisions.

---

### 3. What transformations occur in the Silver Layer?

Typical transformations performed in the Silver Layer include:

- Removing duplicate records.
- Handling null or missing values.
- Standardizing text values.
- Converting data types.
- Formatting dates and timestamps.
- Validating business rules.
- Normalizing categorical values.
- Filtering invalid records.
- Adding processing metadata.
- Applying incremental MERGE operations for transactional data.

These transformations improve data consistency and quality while preserving the business meaning of the data.

---

### 4. Why remove duplicate records?

Duplicate records can negatively impact reporting and analytics by producing incorrect calculations and misleading insights.

Removing duplicates helps to:

- Maintain data accuracy.
- Prevent double counting.
- Improve reporting reliability.
- Ensure one unique business record.
- Improve downstream joins and aggregations.

For example, duplicate customer or order records can result in incorrect sales totals or customer counts.

---

### 5. What is data standardization?

**Data standardization** is the process of converting data into a consistent format so that it can be easily processed and analyzed.

Examples include:

- Converting text to uppercase or lowercase.
- Trimming leading and trailing spaces.
- Formatting dates into a standard format.
- Converting strings to numeric data types.
- Standardizing categorical values (e.g., `web` → `Website`, `app` → `Mobile`).

Standardization improves consistency across datasets and simplifies reporting and analytics.

---

### 6. What is business validation?

Business validation ensures that data complies with predefined business rules before it is promoted to the Silver Layer.

Examples of business validations include:

- Product ID must not be NULL.
- Customer ID must exist.
- Quantity must be greater than zero.
- Price must be a positive value.
- Order date must be valid.
- Category ID must exist in the Category dimension.

Records that fail validation may be corrected, filtered out, or stored in a quarantine table for further investigation.

---

### 7. What is the difference between the Bronze and Silver Layers?

| Bronze Layer               | Silver Layer                          |
| -------------------------- | ------------------------------------- |
| Stores raw source data     | Stores cleaned and validated data     |
| Minimal transformations    | Business transformations applied      |
| Preserves original records | Produces trusted datasets             |
| Raw ingestion layer        | Data refinement layer                 |
| Append-oriented            | Supports updates and MERGE operations |

The Bronze Layer focuses on preserving raw data, while the Silver Layer focuses on improving data quality.

---

### 8. Why use Delta Lake?

Delta Lake provides enterprise-grade reliability and performance for the Silver Layer.

Key benefits include:

- **ACID Transactions** for reliable data consistency.
- **Schema Enforcement** to prevent invalid data.
- **Schema Evolution** to support controlled schema changes.
- **MERGE Operations** for efficient upserts.
- **Time Travel** to access previous versions of data.
- **Data Versioning** for auditability.
- **Change Data Feed (CDF)** for downstream incremental processing.
- **High Performance** for large-scale analytics.

These features make Delta Lake ideal for managing trusted Silver datasets.

---

### 9. Why use Unity Catalog?

Unity Catalog provides centralized governance and management for data assets in the Lakehouse.

Its benefits include:

- Centralized metadata management.
- Fine-grained access control.
- Data lineage tracking.
- Auditing and monitoring.
- Secure data sharing.
- Consistent governance across catalogs, schemas, and tables.

Unity Catalog helps organizations manage data securely while maintaining compliance and traceability.

---

### 10. What is the output of the Silver Layer?

The output of the Silver Layer is a set of **clean, validated, standardized, and trusted Delta tables**.

These tables:

- Have duplicate records removed.
- Contain standardized data formats.
- Follow business validation rules.
- Include correct data types.
- Are stored as managed Delta tables.
- Serve as the trusted source for the Gold Layer.

Examples include:

- `slv_category`
- `slv_brands`
- `slv_products`
- `slv_customers`
- `slv_calendar`
- `slv_orders`
- `slv_order_items`
- `slv_shipments`
- `slv_returns`

These Silver tables provide a reliable foundation for business aggregations, dashboards, reporting, and advanced analytics in the Gold Layer.

# 📊 Summary

| Component       | Purpose          |
| --------------- | ---------------- |
| Bronze Tables   | Source Data      |
| Data Cleansing  | Improve Quality  |
| Validation      | Business Rules   |
| Standardization | Consistency      |
| Silver Tables   | Trusted Dataset  |
| Delta Lake      | Reliable Storage |
| Unity Catalog   | Governance       |

---

# 🎯 Key Takeaways

- The Silver Layer transforms raw Bronze data into trusted datasets.
- It focuses on data cleansing, validation, and standardization.
- Delta Lake provides reliable and scalable storage.
- Unity Catalog enables governance and lineage.
- Silver datasets are the foundation for Gold layer analytics.

---

# 📚 Notebook Modules

➡️ [Transform Dimension Tables into the Silver Layer](01_Transform_Dimensions.md)

➡️ [Transform Fact Tables into the Silver Layer](02_Transform_Fact_Tables.md)