# 📗 Build Fact Tables in the Gold Layer

![Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoftazure&logoColor=white)
![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-FF3621?logo=databricks&logoColor=white)
![Unity Catalog](https://img.shields.io/badge/Unity-Catalog-orange)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)
![Power BI](https://img.shields.io/badge/Power-BI-F2C811?logo=powerbi&logoColor=black)

---

⬅️ [Back to Gold Layer Overview](README.md)

---

# 📚 Table of Contents

- Overview
- Learning Objectives
- Prerequisites
- Source Silver Fact Tables
- Source Gold Dimension Tables
- Target Gold Fact Tables
- Notebook Architecture
- Notebook Workflow
- Configure Unity Catalog
- Read Silver Fact Tables
- Read Gold Dimension Tables
- Join Fact & Dimension Tables
- Build Gold Fact Tables
- Calculate Business KPIs
- Create Summary Tables
- Write Gold Fact Tables
- Gold Fact Tables Created
- Verify Gold Fact Tables
- Validate Table Contents
- Resource Hierarchy
- Data Flow
- Delta Optimization
- Best Practices
- Common Mistakes
- Interview Questions
- Summary
- Key Takeaways
- 
---

# 📖 Overview

This notebook builds the **Gold Fact Tables** by combining trusted transactional data from the **Silver Layer** with descriptive business information from the **Gold Dimension Tables**.

The resulting Fact tables become the foundation for enterprise reporting, KPI calculations, Power BI dashboards, executive reporting, and advanced analytics.

Unlike the Silver Layer, which focuses on data cleansing and validation, the Gold Layer organizes data into analytical models that support fast and consistent business reporting.

---

# 🎯 Learning Objectives

After completing this notebook, you will be able to:

- Read trusted Silver Fact tables.
- Read Gold Dimension tables.
- Join Facts with Dimensions.
- Build analytical Fact tables.
- Calculate business KPIs.
- Create reporting-ready summary datasets.
- Write managed Delta tables into the Gold schema.
- Validate analytical tables in Unity Catalog.

---

# 📋 Prerequisites

Before executing this notebook, ensure that the following components are available:

- Azure Databricks Workspace
- Unity Catalog configured
- Gold schema created
- Gold Dimension tables created
- Silver Fact tables available
- PySpark Runtime installed
- Delta Lake enabled

---

# 📂 Source Silver Fact Tables

The notebook reads trusted transactional datasets from the **Silver** schema.

```text
silver
│
├── slv_orders
├── slv_order_items
├── slv_shipments
└── slv_returns
```

These datasets have already been cleansed, validated, standardized, and enriched during the Silver Layer transformations.

---

# 📂 Source Gold Dimension Tables

The notebook also reads the analytical Dimension tables created in the previous notebook.

```text
gold
│
├── dim_product
├── dim_customer
├── dim_category
├── dim_brand
└── dim_calendar
```

These tables provide descriptive business attributes used to enrich transactional data.

---

# 📂 Target Gold Fact Tables

After processing, the notebook creates the following analytical Fact and Summary tables.

```text
gold
│
├── fact_orders
├── fact_shipments
├── fact_returns
├── daily_sales_summary
└── monthly_sales_summary
```

These datasets are optimized for reporting, business intelligence, and dashboarding.

---

# 🏗 Notebook Architecture

```text
        Silver Fact Tables
                 │
                 ▼
      Read Delta Fact Tables
                 │
                 ▼
      Read Gold Dimension Tables
                 │
                 ▼
       Join Facts & Dimensions
                 │
                 ▼
      Business Transformations
                 │
                 ▼
      Calculate Business KPIs
                 │
                 ▼
      Create Summary Tables
                 │
                 ▼
        Gold Fact Tables
                 │
                 ▼
        Power BI Dashboards
```

---

# 🔄 Notebook Workflow

```text
Read Silver Fact Tables
          │
          ▼
Read Gold Dimension Tables
          │
          ▼
Join Fact & Dimension Tables
          │
          ▼
Apply Business Logic
          │
          ▼
Calculate KPIs
          │
          ▼
Create Summary Tables
          │
          ▼
Write Gold Delta Tables
```

---

# ⚙️ Configure Unity Catalog

The notebook first selects the appropriate catalog and schema before reading and writing tables.

Example:

```python
spark.sql("USE CATALOG ecommerce")

spark.sql("USE SCHEMA gold")
```

This ensures that all analytical Fact tables are created in the managed Gold schema.

---

# 📥 Read Silver Fact Tables

The notebook reads each trusted Silver Fact table using Spark.

Example:

```python
df_orders = spark.table("ecommerce.silver.slv_orders")

df_order_items = spark.table("ecommerce.silver.slv_order_items")

df_shipments = spark.table("ecommerce.silver.slv_shipments")

df_returns = spark.table("ecommerce.silver.slv_returns")
```

These tables contain validated transactional records that serve as the foundation for analytical modeling.

---

# 📥 Read Gold Dimension Tables

The notebook reads the Gold Dimension tables created in the previous notebook.

Example:

```python
df_products = spark.table("ecommerce.gold.dim_product")

df_customers = spark.table("ecommerce.gold.dim_customer")

df_categories = spark.table("ecommerce.gold.dim_category")

df_brands = spark.table("ecommerce.gold.dim_brand")

df_calendar = spark.table("ecommerce.gold.dim_calendar")
```

These tables enrich transactional data with descriptive business information.

---

# 🔗 Join Fact & Dimension Tables

The notebook joins transactional data with related Dimension tables to create a Star Schema.

Typical joins include:

- Orders → Customer
- Order Items → Product
- Product → Category
- Product → Brand
- Orders → Calendar

```text
dim_customer
        │
        ▼
    fact_orders
        ▲
        │
dim_product
        │
        ▼
dim_category

        │

dim_brand

        │

dim_calendar
```

This produces a business-friendly analytical model that supports reporting and dashboard queries.

---

# 📊 Build Gold Fact Tables

The Gold Fact tables are created by combining transactional measures with descriptive Dimension attributes.

Typical business measures include:

- Order Amount
- Quantity Sold
- Discount Amount
- Shipping Cost
- Return Amount
- Net Sales
- Total Revenue

The resulting Fact tables are optimized for analytical workloads and Power BI reporting.

---

# 📈 Calculate Business KPIs

Business Key Performance Indicators (KPIs) are calculated during the Fact table creation process.

Typical KPIs include:

- Total Sales
- Total Revenue
- Total Orders
- Average Order Value
- Total Returns
- Return Rate
- Shipment Success Rate
- Monthly Revenue
- Daily Sales
- Customer Purchase Count

These KPIs provide ready-to-use business metrics for dashboards and executive reporting.

---
# 📊 Create Summary Tables

In addition to detailed Fact tables, the Gold Layer creates summary tables that provide aggregated business metrics for reporting and dashboards.

These summary tables reduce query complexity and improve dashboard performance.

Typical summary datasets include:

- Daily Sales Summary
- Monthly Sales Summary
- Sales by Category
- Sales by Brand
- Customer Purchase Summary

Example workflow:

```text
Fact Orders
       │
       ▼
Aggregate Sales
       │
       ▼
Group by Business Dimensions
       │
       ▼
Create Summary Tables
```

---

# 💾 Write Gold Fact Tables

After applying business transformations and KPI calculations, the analytical Fact tables are written as managed Delta tables.

Example:

```python
df_fact_orders.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("ecommerce.gold.fact_orders")

df_fact_shipments.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("ecommerce.gold.fact_shipments")

df_fact_returns.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("ecommerce.gold.fact_returns")
```

Summary tables are also written into the Gold schema.

```python
df_daily_sales.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("ecommerce.gold.daily_sales_summary")

df_monthly_sales.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("ecommerce.gold.monthly_sales_summary")
```

All tables are stored in Delta format and registered automatically in Unity Catalog.

---

# 📊 Gold Fact Tables Created

After successful execution, the following analytical tables are available.

## Fact Tables

| Gold Table | Description |
|------------|-------------|
| fact_orders | Sales Transactions |
| fact_shipments | Shipment Analytics |
| fact_returns | Product Returns |

## Summary Tables

| Gold Table | Description |
|------------|-------------|
| daily_sales_summary | Daily Business KPIs |
| monthly_sales_summary | Monthly Business KPIs |

These datasets become the primary source for Power BI dashboards and business reporting.

---

# ✅ Verify Gold Fact Tables

After executing the notebook, verify that all Gold Fact tables are successfully created in Unity Catalog.

Expected tables:

```text
gold
│
├── fact_orders
├── fact_shipments
├── fact_returns
├── daily_sales_summary
└── monthly_sales_summary
```

---

# 📸 Verify Tables in Unity Catalog

Open **Catalog Explorer** in Azure Databricks.

Navigate to:

```text
Catalog
│
└── ecommerce
      │
      └── gold
            │
            ├── fact_orders
            ├── fact_shipments
            ├── fact_returns
            ├── daily_sales_summary
            └── monthly_sales_summary
```

Example screenshot:

```text
📷 images/01_verify_gold_fact_tables.png
```

---

# 🔍 Validate Table Contents

Run SQL queries to verify the generated analytical tables.

Example:

```sql
SELECT *
FROM ecommerce.gold.fact_orders
LIMIT 10;
```

```sql
SELECT *
FROM ecommerce.gold.fact_shipments
LIMIT 10;
```

```sql
SELECT *
FROM ecommerce.gold.fact_returns
LIMIT 10;
```

```sql
SELECT *
FROM ecommerce.gold.daily_sales_summary
LIMIT 10;
```

Verify:

- Record counts
- Business measures
- KPI calculations
- Dimension relationships
- Aggregated values
- Data completeness

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
      ├── 01_Gold_Fact_Architecture.png
      ├── 02_Verify_Gold_Fact_Tables.png
      ├── 03_Fact_DataFlow.png
      └── 04_PowerBI_Dashboard.png
```

---

# 🔄 Data Flow

```text
               Silver Fact Tables
                        │
                        ▼
          Read Transactional Data
                        │
                        ▼
          Read Gold Dimension Tables
                        │
                        ▼
          Join Facts & Dimensions
                        │
                        ▼
          Calculate Business KPIs
                        │
                        ▼
           Create Summary Tables
                        │
                        ▼
          Write Gold Delta Tables
                        │
                        ▼
            Unity Catalog (Gold)
                        │
                        ▼
              Power BI Dashboards
```

---

# ⚡ Delta Optimization

After creating the Gold Fact tables, optimize them to improve analytical query performance.

Example:

```sql
OPTIMIZE ecommerce.gold.fact_orders;
```

```sql
OPTIMIZE ecommerce.gold.fact_shipments;
```

```sql
OPTIMIZE ecommerce.gold.fact_returns;
```

For large Fact tables, clustering can further improve query performance.

Example:

```sql
OPTIMIZE ecommerce.gold.fact_orders
ZORDER BY (customer_id, product_id);
```

Benefits include:

- Faster analytical queries
- Reduced file fragmentation
- Improved dashboard performance
- Better data skipping
- Efficient storage utilization

---

# 💡 Best Practices

- Read only trusted Silver Fact tables.
- Use Gold Dimension tables for all joins.
- Follow Star Schema modeling principles.
- Calculate KPIs in the Gold Layer.
- Keep Fact tables focused on measurable events.
- Store tables in Delta format.
- Optimize large tables regularly.
- Validate KPI calculations before publishing.
- Maintain consistent business definitions.
- Register all analytical tables in Unity Catalog.

---

# ⚠️ Common Mistakes

Avoid the following when building Gold Fact tables:

- Reading directly from Bronze tables.
- Performing data cleansing in the Gold Layer.
- Mixing Dimension attributes into transactional tables unnecessarily.
- Creating duplicate Fact records.
- Recalculating KPIs in reporting tools.
- Ignoring business validation.
- Skipping Delta optimization.
- Using inconsistent KPI definitions.
- Allowing dashboards to query Silver tables directly.
- Publishing incomplete analytical datasets.

---
# 🎤 Interview Questions

### 1. What is a Fact Table?

A **Fact Table** stores measurable business events or transactions that can be analyzed and aggregated.

Typical business measures include:

- Sales Amount
- Quantity Sold
- Discount Amount
- Shipping Cost
- Return Amount
- Net Revenue

Fact tables are the central component of a **Star Schema** and reference Dimension tables using business keys.

---

### 2. Why are Fact Tables created in the Gold Layer?

The Gold Layer organizes trusted transactional data into analytical models optimized for business intelligence.

Creating Fact tables in the Gold Layer provides:

- Faster analytical queries
- Standardized business metrics
- Simplified reporting
- Optimized Power BI dashboards
- Consistent KPI calculations

---

### 3. What is the relationship between Fact and Dimension tables?

Fact tables store measurable business events, while Dimension tables provide descriptive information.

Example:

```text
dim_customer
        │
        ▼
   fact_orders
        ▲
        │
dim_product
        │
        ▼
dim_category
        │
        ▼
dim_brand

        │

dim_calendar
```

This structure enables efficient filtering, grouping, and reporting across multiple business dimensions.

---

### 4. What KPIs are calculated in this notebook?

Typical business KPIs include:

- Total Sales
- Total Revenue
- Total Orders
- Average Order Value
- Total Quantity Sold
- Total Returns
- Return Rate
- Shipment Success Rate
- Daily Sales
- Monthly Revenue

These KPIs are calculated once in the Gold Layer and reused by reporting tools.

---

### 5. Why create Summary Tables?

Summary tables store pre-aggregated business metrics.

Examples include:

- Daily Sales Summary
- Monthly Sales Summary
- Sales by Category
- Sales by Brand

Benefits include:

- Faster dashboard performance
- Reduced query complexity
- Lower compute costs
- Improved user experience

---

### 6. Why use Delta Lake for Fact Tables?

Delta Lake provides enterprise-grade reliability and performance.

Key features include:

- ACID Transactions
- Schema Enforcement
- Schema Evolution
- Time Travel
- Data Versioning
- Optimized Storage
- High Performance Reads

These features ensure that analytical datasets remain accurate and scalable.

---

### 7. Why use Unity Catalog?

Unity Catalog manages and governs analytical datasets.

Benefits include:

- Centralized metadata
- Fine-grained permissions
- Data lineage
- Auditing
- Secure data sharing
- Governance across catalogs and schemas

It ensures that Gold Fact tables are secure and discoverable across the organization.

---

### 8. Why optimize Fact Tables?

Fact tables are typically the largest tables in a data warehouse.

Optimization helps by:

- Improving query performance
- Reducing scan time
- Improving Power BI refresh speed
- Optimizing file layout
- Lowering storage and compute costs

Techniques include:

- OPTIMIZE
- ZORDER
- Proper partitioning
- File compaction

---

### 9. What is the output of this notebook?

After successful execution, the following analytical datasets are created.

### Fact Tables

- fact_orders
- fact_shipments
- fact_returns

### Summary Tables

- daily_sales_summary
- monthly_sales_summary

These datasets are optimized for Power BI dashboards, SQL analytics, executive reporting, and downstream analytical applications.

---

### 10. Why is the Gold Layer the preferred source for reporting?

The Gold Layer contains trusted, business-ready datasets that are already modeled and optimized for analytics.

Advantages include:

- Consistent KPI definitions
- Business-friendly schema
- High query performance
- Simplified reporting
- Centralized governance
- Reduced dashboard complexity

For this reason, BI tools should query the Gold Layer instead of Bronze or Silver datasets.

---

# 📊 Summary

| Component | Purpose |
|-----------|---------|
| Silver Fact Tables | Trusted Transactional Data |
| Gold Dimension Tables | Business Context |
| Fact Tables | Measurable Business Events |
| KPI Calculations | Business Metrics |
| Summary Tables | Aggregated Reporting |
| Delta Lake | Reliable Storage |
| Unity Catalog | Governance & Metadata |
| Power BI | Business Visualization |

---

# 🎯 Key Takeaways

- Gold Fact tables are built from trusted Silver transactional datasets.
- Gold Dimension tables enrich Facts with descriptive business information.
- Star Schema modeling improves analytical performance.
- Business KPIs are calculated once in the Gold Layer for consistency.
- Delta Lake provides scalable and reliable analytical storage.
- Unity Catalog enables governance, lineage, and secure access.
- Fact and Summary tables power enterprise reporting and Power BI dashboards.
