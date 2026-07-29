
# 🥈 Transform Dimension Tables into the Silver Layer

![Azure](<https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoftazure&logoColor=white>)
![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-FF3621?logo=databricks&logoColor=white)
![Unity Catalog](https://img.shields.io/badge/Unity-Catalog-orange)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)

---

⬅️ [Back to Silver Layer](README.md)

---

# 📚 Table of Contents

- Overview
- Learning Objectives
- Prerequisites
- Dimension Tables
- Notebook Overview
- Transformation Architecture
- Transformation Workflow
- Step 1 – Configure Notebook
- Step 2 – Read Bronze Dimension Tables
- Step 3 – Clean Dimension Data
- Step 4 – Validate Records
- Step 5 – Standardize Data
- Step 6 – Write Silver Delta Tables
- Step 7 – Verify Silver Tables
- Silver Dimension Tables
- Resource Hierarchy
- Data Flow
- Data Lineage
- Verification Checklist
- SQL Verification
- Benefits
- Best Practices
- Common Mistakes
- Interview Questions
- Summary
- Key Takeaways


---

# 📖 Overview

This notebook transforms raw **Dimension tables** from the Bronze layer into clean, validated, and standardized datasets in the Silver layer.

The transformation pipeline improves data quality by removing duplicate records, handling null values, enforcing business rules, standardizing column formats, and writing the processed data into managed Delta tables.

The resulting Silver Dimension tables become the trusted source for downstream fact table joins, reporting, and Gold layer business models.

---

# 🎯 Learning Objectives

After completing this notebook, you will be able to:

- Read Bronze Dimension tables.
- Clean invalid records.
- Remove duplicate rows.
- Standardize text values.
- Convert columns into appropriate data types.
- Apply business validation rules.
- Create managed Silver Delta tables.
- Verify transformed datasets.

---

# 📋 Prerequisites

Before executing this notebook, ensure that you have completed:

- Bronze Layer ingestion
- Unity Catalog configuration
- Azure Databricks workspace setup
- ADLS Gen2 configuration
- Bronze Delta tables successfully created

---

# 📂 Dimension Tables

This notebook processes the following dimension datasets:

| Bronze Table  | Silver Table  | Description        |
| ------------- | ------------- | ------------------ |
| brz_category  | slv_category  | Product Categories |
| brz_brands    | slv_brands    | Product Brands     |
| brz_products  | slv_products  | Product Master     |
| brz_customers | slv_customers | Customer Master    |
| brz_calendar  | slv_calendar  | Calendar Dimension |

---

# 📓 Notebook Overview

The notebook performs the following tasks:

1. Configure notebook parameters
2. Read Bronze Dimension tables
3. Remove duplicate records
4. Handle null values
5. Standardize text columns
6. Convert data types
7. Apply business validation rules
8. Write Silver Delta tables
9. Verify results

---

# 🏗 Transformation Architecture

```text
Bronze Dimension Tables
         │
         ▼
PySpark Notebook
         │
         ▼
Duplicate Removal
         │
         ▼
Null Handling
         │
         ▼
Data Standardization
         │
         ▼
Business Validation
         │
         ▼
Silver Delta Tables
```

---

# 🔄 Transformation Workflow

```text
Read Bronze Tables
        │
        ▼
Clean Records
        │
        ▼
Validate Data
        │
        ▼
Standardize Values
        │
        ▼
Write Silver Tables
        │
        ▼
Verify Results
```

---

# 🚀 Step 1 — Configure Notebook

Configure Unity Catalog and notebook parameters.

Example:

```python
catalog_name = "ecommerce"
silver_schema = "silver"
```

This ensures all tables are written into:

```
ecommerce.silver
```

---

# 🚀 Step 2 — Read Bronze Dimension Tables

Read managed Bronze Delta tables.

Example:

```python
df_products = spark.table(
    "ecommerce.bronze.brz_products"
)
```

Dimension tables include:

- Categories
- Brands
- Products
- Customers
- Calendar

---

# 🚀 Step 3 — Clean Dimension Data

Typical cleaning operations:

- Remove duplicate rows
- Handle null values
- Trim spaces
- Remove invalid records

Example:

```python
df = df.dropDuplicates()

df = df.na.drop()
```

---

# 🚀 Step 4 — Validate Records

Business validation examples:

- Product ID cannot be NULL
- Customer ID must exist
- Category ID should be valid
- Product Name cannot be blank

Invalid records are removed or quarantined.

---

# 🚀 Step 5 — Standardize Data

Standardization includes:

- Convert text to uppercase
- Trim whitespace
- Format dates
- Convert data types
- Rename columns

Example:

```python
from pyspark.sql.functions import upper, trim

df = df.withColumn(
    "brand_name",
    upper(trim("brand_name"))
)
```

---

# 🚀 Step 6 — Write Silver Delta Tables

Write the transformed dataset into managed Delta tables.

Example:

```python
df.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable(
        "ecommerce.silver.slv_products"
    )
```

---

# 🚀 Step 7 — Verify Silver Tables

Verify tables using Catalog Explorer.

Expected tables:

- slv_category
- slv_brands
- slv_products
- slv_customers
- slv_calendar

---

# 📂 Silver Dimension Tables

| Table         | Description              |
| ------------- | ------------------------ |
| slv_category  | Clean Product Categories |
| slv_brands    | Standardized Brands      |
| slv_products  | Validated Products       |
| slv_customers | Cleansed Customers       |
| slv_calendar  | Calendar Dimension       |

---

# 📂 Resource Hierarchy

```text
ecommerce
│
├── bronze
│
│   ├── brz_category
│   ├── brz_brands
│   ├── brz_products
│   ├── brz_customers
│   └── brz_calendar
│
└── silver
    │
    ├── slv_category
    ├── slv_brands
    ├── slv_products
    ├── slv_customers
    └── slv_calendar
```

---

# 🔄 Data Flow

```text
Bronze Delta Tables
        │
        ▼
PySpark Notebook
        │
        ▼
Cleaning
        │
        ▼
Validation
        │
        ▼
Standardization
        │
        ▼
Silver Delta Tables
```

---

# 📈 Data Lineage

```text
Raw CSV Files
      │
      ▼
Bronze Tables
      │
      ▼
Transform Dimension Notebook
      │
      ▼
Silver Dimension Tables
      │
      ▼
Gold Layer
```

---

# ✅ Verification Checklist

| Component                 | Status |
| ------------------------- | :----: |
| Bronze Tables Read        |   ✅   |
| Duplicate Records Removed |   ✅   |
| Null Values Handled       |   ✅   |
| Validation Completed      |   ✅   |
| Standardization Completed |   ✅   |
| Silver Tables Created     |   ✅   |
| Unity Catalog Updated     |   ✅   |

---

# 🔍 SQL Verification

```sql
SHOW TABLES IN silver;
```

```sql
SELECT *
FROM silver.slv_products
LIMIT 10;
```

```sql
SELECT COUNT(*)
FROM silver.slv_products;
```

---

# 📈 Benefits

- Improved data quality
- Trusted dimension tables
- Standardized datasets
- Better query performance
- Reliable downstream joins
- Analytics-ready data

---

# 💡 Best Practices

- Remove duplicates.
- Handle null values.
- Validate mandatory columns.
- Standardize text formats.
- Keep transformations deterministic.
- Store in Delta format.

---

# ⚠️ Common Mistakes

- Ignoring duplicates.
- Leaving invalid records.
- Mixing aggregation logic.
- Using inconsistent naming.
- Writing directly to Gold.

---

# 🎤 Interview Questions

### 1. Why transform Dimension tables?

Dimension tables are transformed in the Silver Layer to improve data quality and create trusted reference data for downstream analytics.

The transformation process helps to:

- Remove duplicate records.
- Handle null and missing values.
- Standardize text and data formats.
- Validate business rules.
- Improve consistency across datasets.
- Prepare dimensions for joining with fact tables.

Clean and consistent dimension tables improve the accuracy of reports, dashboards, and business metrics.

---

### 2. Why remove duplicate records?

Duplicate records can cause incorrect analytical results and inconsistent business reporting.

Removing duplicates helps to:

- Prevent duplicate dimension members.
- Improve data accuracy.
- Ensure unique business entities.
- Avoid incorrect joins with fact tables.
- Improve reporting reliability.

For example, duplicate customer or product records can lead to incorrect customer counts or product sales analysis.

---

### 3. What validations are applied?

The Silver Layer applies business validation rules to ensure that only valid records are promoted.

Typical validations include:

- Primary key must not be NULL.
- Mandatory columns must contain valid values.
- Product IDs and Customer IDs must be unique.
- Category IDs must exist.
- Dates must follow the expected format.
- Numeric values must be within valid ranges.

Invalid records may be corrected, filtered, or stored in a quarantine table based on business requirements.

---

### 4. Why standardize text values?

Text values often contain inconsistent formatting that can affect joins, filtering, and reporting.

Standardization improves consistency by:

- Converting text to uppercase or lowercase.
- Removing leading and trailing spaces.
- Normalizing categorical values.
- Correcting inconsistent spellings.
- Ensuring uniform formatting across datasets.

For example:

- `apple`
- `Apple`
- `APPLE`

can all be standardized to **APPLE** to ensure consistent reporting.

---

### 5. Why use Delta tables?

Delta Lake provides reliable and scalable storage for Silver datasets.

Key benefits include:

- ACID Transactions
- Schema Enforcement
- Schema Evolution
- Time Travel
- Data Versioning
- Efficient MERGE operations
- High Query Performance

Delta tables ensure that transformed data remains consistent, reliable, and easy to manage.

---

### 6. What is the difference between Bronze and Silver Dimension tables?

| Bronze Dimension Tables | Silver Dimension Tables |
|--------------------------|-------------------------|
| Raw source data | Clean and validated data |
| Minimal transformations | Standardized and enriched data |
| May contain duplicates | Duplicate records removed |
| Original data preserved | Business rules applied |
| Source for Silver | Trusted source for Gold |

Bronze dimension tables preserve the original source data, while Silver dimension tables contain high-quality reference data ready for downstream analytics.

---

### 7. Why use Unity Catalog?

Unity Catalog provides centralized governance and management for all Silver tables.

Its benefits include:

- Centralized metadata management.
- Fine-grained access control.
- Data lineage tracking.
- Auditing and monitoring.
- Secure data sharing.
- Consistent governance across catalogs and schemas.

Unity Catalog simplifies data management while improving security and compliance.

---

### 8. What is the purpose of business validation?

Business validation ensures that data satisfies predefined business rules before it is stored in the Silver Layer.

Its purpose is to:

- Improve data quality.
- Prevent invalid records from entering downstream systems.
- Ensure consistency across datasets.
- Reduce reporting errors.
- Increase trust in analytical data.

For example:

- Product price must be greater than zero.
- Customer ID must not be NULL.
- Product category must exist.

Only records that meet these business rules are promoted to the Silver layer.

---

### 9. Why are Dimension tables important?

Dimension tables provide descriptive information about business entities and are essential for analytical reporting.

Examples include:

- Products
- Customers
- Categories
- Brands
- Calendar

Dimension tables are used to:

- Filter reports.
- Group business metrics.
- Join with fact tables.
- Support star schema design.
- Improve reporting performance.

They provide the business context required to analyze transactional data stored in fact tables.

---

### 10. What is the output of this notebook?

The notebook produces **clean, validated, standardized, and trusted Silver Dimension Delta tables**.

The output tables:

- Remove duplicate records.
- Apply business validation rules.
- Standardize data formats.
- Convert columns to appropriate data types.
- Improve data quality.
- Store trusted reference data for downstream processing.

Typical output tables include:

- `slv_category`
- `slv_brands`
- `slv_products`
- `slv_customers`
- `slv_calendar`

These Silver Dimension tables serve as the trusted reference data for fact table joins, Gold layer transformations, dashboards, reporting, and business analytics.

---

# 📊 Summary

| Component       | Purpose                |
| --------------- | ---------------------- |
| Bronze Tables   | Source                 |
| Cleaning        | Remove invalid records |
| Validation      | Improve quality        |
| Standardization | Consistency            |
| Silver Tables   | Trusted dimensions     |

---

# 🎯 Key Takeaways

- Dimension tables are refined in the Silver layer through cleansing, validation, and standardization.
- Silver Dimension tables become the trusted reference data for downstream fact table joins and Gold layer analytics.
- Consistent transformation logic improves data quality, governance, and reporting accuracy.
- Managed Delta tables and Unity Catalog provide reliable storage, governance, and lineage.

