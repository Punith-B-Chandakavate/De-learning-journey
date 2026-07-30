
# 📘 Build Dimension Tables in the Gold Layer

![Azure](<https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoftazure&logoColor=white>)
![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-FF3621?logo=databricks&logoColor=white)
![Unity Catalog](https://img.shields.io/badge/Unity-Catalog-orange)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)

---

⬅️ [Back to Gold Layer Overview](README.md)

---

# 📚 Table of Contents

- Overview
- Learning Objectives
- Prerequisites
- Source Silver Dimension Tables
- Target Gold Dimension Tables
- Gold Dimension Architecture
- Notebook Workflow
- Configure Unity Catalog
- Read Silver Dimension Tables
- Build Gold Dimension Tables
- Apply Business Transformations
- Write Gold Dimension Tables
- Gold Dimension Tables Created
- Verify Gold Dimension Tables
- Validate Table Contents
- Resource Hierarchy
- Data Flow
- Delta Optimization
- Best Practices
- Common Mistakes
- Interview Questions
- Summary
- Key Takeaways

---

# 📖 Overview

This notebook builds the **Gold Dimension Tables** by transforming trusted Silver Dimension datasets into business-ready analytical dimensions.

The resulting Gold Dimension tables provide descriptive business information that is used to analyze Fact tables within a **Star Schema**.

Unlike the Silver Layer, which focuses on cleansing and validation, the Gold Layer enriches and organizes data for business intelligence, reporting, and analytics.

After completing this notebook, the Gold schema contains optimized Dimension tables ready for Power BI dashboards and downstream analytical workloads.

---

# 🎯 Learning Objectives

After completing this notebook, you will be able to:

- Read trusted Silver Dimension tables.
- Create business-ready Gold Dimension tables.
- Apply business-friendly transformations.
- Organize Dimension tables using Star Schema principles.
- Write managed Delta tables into the Gold schema.
- Validate the Gold Dimension tables in Unity Catalog.

---

# 📋 Prerequisites

Before executing this notebook, ensure that the following components are available:

- Azure Databricks Workspace
- Unity Catalog configured
- Gold schema created
- Silver Layer completed successfully
- Silver Dimension tables available
- PySpark runtime installed
- Delta Lake enabled

---

# 📂 Source Silver Dimension Tables

The notebook reads trusted Dimension tables from the **Silver** schema.

```text
silver
│
├── slv_products
├── slv_customers
├── slv_category
├── slv_brands
└── slv_calendar
```

These datasets have already been cleaned, validated, standardized, and enriched during the Silver Layer transformations.

---

# 📂 Target Gold Dimension Tables

The notebook creates the following analytical Dimension tables.

```text
gold
│
├── dim_product
├── dim_customer
├── dim_category
├── dim_brand
└── dim_calendar
```

These tables become the descriptive dimensions used by the Gold Fact tables.

---

# 🏗 Notebook Architecture

```text
Silver Dimension Tables
          │
          ▼
Read Delta Tables
          │
          ▼
Business Transformations
          │
          ▼
Dimension Modeling
          │
          ▼
Create Gold Dimension Tables
          │
          ▼
Write Delta Tables
          │
          ▼
Unity Catalog
```

---

# 🔄 Notebook Workflow

```text
Read Silver Tables
        │
        ▼
Select Required Columns
        │
        ▼
Rename Business Columns
        │
        ▼
Apply Business Transformations
        │
        ▼
Create Dimension Tables
        │
        ▼
Write Gold Delta Tables
```

---

# ⚙️ Configure Unity Catalog

The notebook first selects the appropriate catalog and schema.

Example:

```python
spark.sql("USE CATALOG ecommerce")

spark.sql("USE SCHEMA gold")
```

This ensures that all Dimension tables are written into the Gold schema managed by Unity Catalog.

---

# 📥 Read Silver Dimension Tables

The notebook reads each trusted Silver Dimension table using Spark.

Example:

```python
df_products = spark.table("ecommerce.silver.slv_products")

df_customers = spark.table("ecommerce.silver.slv_customers")

df_category = spark.table("ecommerce.silver.slv_category")

df_brands = spark.table("ecommerce.silver.slv_brands")

df_calendar = spark.table("ecommerce.silver.slv_calendar")
```

These tables serve as the source datasets for building analytical dimensions.

---

# 🏷 Build Gold Dimension Tables

Each Silver dataset is transformed into a business-friendly Gold Dimension table.

Typical operations include:

- Selecting analytical columns
- Renaming business fields
- Removing technical metadata
- Organizing descriptive attributes
- Preparing reporting dimensions

Example workflow:

```text
Silver Product
        │
        ▼
Select Business Columns
        │
        ▼
Rename Columns
        │
        ▼
Build Product Dimension
        │
        ▼
Gold Product Dimension
```

The same approach is applied to all Dimension datasets.

---

# 🔄 Apply Business Transformations

The Gold Layer applies transformations that improve usability for reporting and analytics.

Typical transformations include:

- Rename technical column names
- Create business-friendly attributes
- Remove unnecessary metadata columns
- Standardize naming conventions
- Reorder columns for reporting
- Prepare dimensions for Star Schema relationships

Unlike the Silver Layer, no data cleansing is performed here because the data has already been validated.

The focus is on creating analytical Dimension tables that provide descriptive context for business reporting.

---

# 💾 Write Gold Dimension Tables

After applying the required business transformations, the Dimension DataFrames are written as managed Delta tables in the **Gold** schema.

Each table is stored in **Delta Lake** format, providing ACID transactions, schema enforcement, and high-performance analytical queries.

Typical write operations include:

- Overwrite existing Dimension tables
- Store data in Delta format
- Register tables in Unity Catalog
- Preserve schema consistency

Example:

```python
df_dim_product.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("ecommerce.gold.dim_product")

df_dim_customer.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("ecommerce.gold.dim_customer")

df_dim_category.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("ecommerce.gold.dim_category")

df_dim_brand.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("ecommerce.gold.dim_brand")

df_dim_calendar.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("ecommerce.gold.dim_calendar")
```

---

# 📊 Gold Dimension Tables Created

After successful execution, the following analytical Dimension tables are available.

| Gold Table | Description |
|------------|-------------|
| dim_product | Product Dimension |
| dim_customer | Customer Dimension |
| dim_category | Category Dimension |
| dim_brand | Brand Dimension |
| dim_calendar | Calendar Dimension |

These tables provide descriptive business information for analytical reporting and are referenced by the Gold Fact tables.

---

# ✅ Verify Gold Dimension Tables

After executing the notebook, verify that the Gold Dimension tables are successfully created in Unity Catalog.

Expected tables:

```text
gold
│
├── dim_product
├── dim_customer
├── dim_category
├── dim_brand
└── dim_calendar
```

---

# 📸 Verify Tables in Unity Catalog

Open **Catalog Explorer** in Azure Databricks and navigate to:

```text
Catalog
│
└── ecommerce
     │
     └── gold
          │
          ├── dim_product
          ├── dim_customer
          ├── dim_category
          ├── dim_brand
          └── dim_calendar
```

Example screenshot:

```text
📷 images/01_verify_gold_dimension_tables.png
```

---

# 🔍 Validate Table Contents

Run SQL queries to confirm that the Dimension tables contain the expected data.

Example:

```sql
SELECT *
FROM ecommerce.gold.dim_product
LIMIT 10;
```

```sql
SELECT *
FROM ecommerce.gold.dim_customer
LIMIT 10;
```

```sql
SELECT *
FROM ecommerce.gold.dim_category
LIMIT 10;
```

Verify:

- Column names
- Data types
- Business attributes
- Record counts
- No unexpected NULL values

---

# 📂 Resource Hierarchy

```text
03_Gold_Layer/
│
├── README.md
│
├── 01_Build_Dimension_Tables.md
│
├── 02_Build_Fact_Tables.md
│
└── images/
      ├── 01_Gold_Dimension_Architecture.png
      ├── 02_Verify_Gold_Dimension_Tables.png
      └── 03_Dimension_DataFlow.png
```

---

# 🔄 Data Flow

```text
             Silver Layer
                    │
                    ▼
      Silver Dimension Tables
                    │
                    ▼
          Read Delta Tables
                    │
                    ▼
      Apply Business Transformations
                    │
                    ▼
      Create Gold Dimension Tables
                    │
                    ▼
        Write Delta Tables
                    │
                    ▼
         Unity Catalog (Gold)
                    │
                    ▼
     Used by Gold Fact Tables
                    │
                    ▼
      Power BI Dashboards
```

---

# ⚡ Delta Optimization

After creating the Gold Dimension tables, Delta Lake optimization can be performed to improve query performance.

Example:

```sql
OPTIMIZE ecommerce.gold.dim_product;
```

```sql
OPTIMIZE ecommerce.gold.dim_customer;
```

Benefits include:

- Faster reads
- Improved file compaction
- Better query planning
- Reduced I/O operations

---

# 💡 Best Practices

- Read only validated Silver Dimension tables.
- Keep Dimension tables descriptive.
- Use meaningful business column names.
- Remove technical metadata not required for analytics.
- Store Dimension tables as managed Delta tables.
- Maintain consistent naming conventions.
- Validate schema before publishing.
- Optimize Delta tables after loading.
- Register all tables in Unity Catalog.
- Document business definitions for each Dimension.

---

# ⚠️ Common Mistakes

Avoid the following while building Gold Dimension tables:

- Reading directly from Bronze tables.
- Including transactional measures in Dimension tables.
- Keeping unnecessary technical columns.
- Mixing Fact and Dimension logic.
- Using inconsistent business names.
- Ignoring schema validation.
- Creating duplicate Dimension records.
- Not validating relationships with Fact tables.
- Skipping Delta optimization.
- Writing tables outside the Gold schema.

---
# 🎤 Interview Questions

### 1. Why are Dimension tables created in the Gold Layer?

Dimension tables provide descriptive business information that helps users analyze transactional data stored in Fact tables.

Examples include:

- Product
- Customer
- Category
- Brand
- Calendar

They provide business context for reporting, dashboards, and analytical queries.

---

### 2. What is the purpose of a Product Dimension?

The Product Dimension contains descriptive information about products.

Typical attributes include:

- Product ID
- Product Name
- Brand
- Category
- Product Type
- Price
- Status

Business users use this table to analyze sales by product, category, and brand.

---

### 3. Why are Dimension tables separated from Fact tables?

Separating Dimension and Fact tables is a fundamental principle of **Star Schema** design.

Benefits include:

- Reduced data redundancy
- Simpler joins
- Better query performance
- Easier maintenance
- Improved reporting flexibility

Dimension tables describe business entities, while Fact tables store measurable business events.

---

### 4. What transformations are applied while building Gold Dimension tables?

Typical transformations include:

- Selecting analytical columns
- Renaming technical fields
- Removing unnecessary metadata
- Creating business-friendly column names
- Organizing descriptive attributes
- Preparing tables for analytical reporting

Unlike the Silver Layer, the Gold Layer does **not** perform data cleansing. It focuses on analytical modeling.

---

### 5. Why are Gold Dimension tables stored as Delta tables?

Delta Lake provides enterprise-grade storage features such as:

- ACID Transactions
- Schema Enforcement
- Schema Evolution
- Time Travel
- Version Control
- High Performance Reads

These capabilities ensure reliable and efficient analytical queries.

---

### 6. Why is Unity Catalog used for Gold tables?

Unity Catalog provides centralized governance for business-ready datasets.

Benefits include:

- Metadata management
- Fine-grained permissions
- Data lineage
- Auditing
- Secure access control
- Centralized catalog management

It enables organizations to manage analytical datasets securely and consistently.

---

### 7. What is the relationship between Dimension and Fact tables?

Dimension tables provide descriptive attributes, while Fact tables contain measurable business events.

Example:

```text
dim_customer
        │
        │ Customer Key
        ▼
fact_orders
        ▲
        │ Product Key
        │
dim_product
```

The Fact table references Dimension tables through surrogate or business keys to support analytical queries.

---

### 8. Why is the Calendar Dimension important?

The Calendar Dimension simplifies time-based analysis.

It enables reporting such as:

- Daily Sales
- Monthly Revenue
- Quarterly Performance
- Yearly Growth
- Weekend vs Weekday Sales

Using a dedicated Calendar Dimension improves reporting consistency and simplifies date-based calculations.

---

### 9. How do Gold Dimension tables improve reporting?

Gold Dimension tables provide clean and descriptive business information that allows users to:

- Slice and filter reports
- Group business metrics
- Create drill-down dashboards
- Analyze trends
- Improve visualization performance

They simplify reporting by reducing complex joins and exposing business-friendly attributes.

---

### 10. What is the output of this notebook?

After successfully executing this notebook, the following Gold Dimension tables are created:

- dim_product
- dim_customer
- dim_category
- dim_brand
- dim_calendar

These tables are stored as managed Delta tables in the **Gold** schema and are used by Fact tables, Power BI dashboards, SQL analytics, and downstream business intelligence applications.

---

# 📊 Summary

| Component | Purpose |
|-----------|---------|
| Silver Dimension Tables | Trusted Source Data |
| Business Transformations | Improve Analytical Usability |
| Gold Dimension Tables | Business Context |
| Delta Lake | Reliable Storage |
| Unity Catalog | Governance & Metadata |
| Star Schema | Analytical Data Modeling |
| Power BI | Business Reporting |

---

# 🎯 Key Takeaways

- Gold Dimension tables are built from trusted Silver Dimension datasets.
- They provide descriptive business information for analytical reporting.
- Star Schema modeling separates descriptive attributes from measurable business facts.
- Delta Lake ensures reliable and scalable storage.
- Unity Catalog provides governance, lineage, and access control.
- Gold Dimension tables become the foundation for Fact tables and business intelligence.


