# 🥉 Bronze Layer

![Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoftazure&logoColor=white)
![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-FF3621?logo=databricks&logoColor=white)
![Unity Catalog](https://img.shields.io/badge/Unity-Catalog-orange)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)

---

⬅️ Back to Medallion Architecture

---

# 📚 Table of Contents

- Overview
- Learning Objectives
- What is the Bronze Layer?
- Why is the Bronze Layer Important?
- Medallion Architecture
- Bronze Layer Characteristics
- Bronze Layer Responsibilities
- Bronze Layer Architecture
- Bronze Layer Workflow
- Data Sources
- Bronze Layer vs Silver Layer
- Benefits
- Why Use Delta Lake?
- Best Practices
- Common Mistakes
- Interview Questions
- Summary
- Key Takeaways
- Next Modules

---

# 📖 Overview

The Bronze Layer is the first stage of the Medallion Architecture.

It is responsible for ingesting raw data from source systems into the Lakehouse while preserving the original data with minimal transformations.

The primary goal of the Bronze Layer is to establish a reliable and immutable foundation for downstream data processing.

---

# 🎯 Learning Objectives

After completing this guide, you will be able to:

- Understand the purpose of the Bronze Layer.
- Explain why raw data should be preserved.
- Understand the Bronze workflow.
- Identify the responsibilities of the Bronze Layer.
- Explain why Delta Lake is used.
- Understand how Bronze supports Silver and Gold layers.

---

# 🥉 What is the Bronze Layer?

The Bronze Layer is the raw ingestion layer of the Medallion Architecture.

Data from source systems is loaded exactly as received.

Only minimal processing is performed, such as:

- Schema validation
- Metadata enrichment
- Delta table creation

No business transformations are applied.

---

# ⭐ Why is the Bronze Layer Important?

The Bronze Layer provides:

- Raw data preservation
- Reliable source of truth
- Data lineage
- Auditability
- Reprocessing capability
- Scalable ingestion

---

# 🏛 Medallion Architecture

```text
Source Systems
      │
      ▼
🥉 Bronze
Raw Data
      │
      ▼
🥈 Silver
Clean & Validated Data
      │
      ▼
🥇 Gold
Business Ready Data
```

---

# 📌 Bronze Layer Characteristics

- Raw data ingestion
- Minimal transformations
- Append-oriented
- Immutable datasets
- Delta Lake storage
- Metadata enrichment
- Supports batch and streaming ingestion

---

# 📌 Bronze Layer Responsibilities

The Bronze Layer is responsible for:

- Reading source data
- Applying schemas
- Validating records
- Capturing ingestion metadata
- Writing Delta tables
- Maintaining data lineage

---

# 🏗 Bronze Layer Architecture

```text
Source Systems
       │
       ▼
Raw Files
       │
       ▼
Unity Catalog Volume
       │
       ▼
PySpark Notebook
       │
       ▼
Schema Validation
       │
       ▼
Delta Tables
```

---

# 🔄 Bronze Layer Workflow

```text
Read Data
      │
      ▼
Apply Schema
      │
      ▼
Validate
      │
      ▼
Add Metadata
      │
      ▼
Create Delta Tables
```

---

# 📂 Data Sources

Typical Bronze datasets include:

## Dimension Tables

- Categories
- Brands
- Products
- Customers
- Calendar

---

## Fact Tables

- Orders
- Shipments
- Returns

---

# ⚖ Bronze Layer vs Silver Layer

| Bronze | Silver |
|---------|---------|
| Raw Data | Clean Data |
| Minimal Transformations | Business Transformations |
| Immutable | Standardized |
| Source Copy | Analytics Ready |

---

# 📈 Benefits

- Preserves source data
- Supports data lineage
- Enables reprocessing
- Improves reliability
- Supports scalable ingestion
- Integrates with Unity Catalog

---

# 🏆 Why Use Delta Lake?

Delta Lake provides:

- ACID Transactions
- Schema Enforcement
- Schema Evolution
- Time Travel
- Data Versioning
- High Performance

---

# 💡 Best Practices

- Preserve raw data.
- Never apply business rules.
- Add ingestion metadata.
- Use predefined schemas.
- Store data in Delta format.
- Keep Bronze append-only.
- Separate Bronze from Silver transformations.

---

# ⚠️ Common Mistakes

- Applying business logic.
- Updating raw records.
- Ignoring metadata.
- Using inferred schemas in production.
- Mixing Bronze and Silver logic.

---

# 🎤 Interview Questions

### 1. What is the Bronze Layer?

The **Bronze Layer** is the first layer of the **Medallion Architecture**. It is responsible for ingesting raw data from source systems into the Lakehouse while preserving the original data with minimal transformations.

The primary goal of the Bronze Layer is to create a reliable and immutable foundation for downstream Silver and Gold layers.

---

### 2. Why should Bronze remain raw?

The Bronze Layer should remain raw because it acts as the organization's **single source of truth**.

Keeping data in its original form provides several benefits:

- Preserves original source data
- Enables data reprocessing
- Supports auditing and compliance
- Maintains complete data lineage
- Prevents accidental data loss

Business rules, cleansing, and transformations should be performed in the **Silver Layer**, not in Bronze.

---

### 3. Why use Delta Lake?

Delta Lake provides enterprise-grade storage and reliability for Bronze tables.

Its key features include:

- **ACID Transactions** – Ensures reliable reads and writes.
- **Schema Enforcement** – Prevents invalid data from being written.
- **Schema Evolution** – Supports controlled schema changes.
- **Time Travel** – Access previous versions of data.
- **Data Versioning** – Tracks changes over time.
- **High Performance** – Optimized for large-scale analytics.
- **Batch and Streaming Support** – Works seamlessly with both processing models.

---

### 4. What metadata is added?

During Bronze ingestion, operational metadata is added to improve traceability and auditing.

Common metadata columns include:

- **_ingested_at** – Timestamp when the record was ingested.
- **_ingest_time** – Processing time.
- **_source_file** – Source file name or path.
- **_batch_id** *(optional)* – Batch execution identifier.
- **_load_date** *(optional)* – Date the data was loaded.

This metadata helps with monitoring, troubleshooting, and data lineage.

---

### 5. What is data lineage?

**Data lineage** is the ability to trace the complete lifecycle of data, from its source to its final destination.

It shows:

- Where the data originated.
- How it was transformed.
- Which notebooks or jobs processed it.
- Which tables consume it.

Data lineage improves transparency, governance, auditing, and impact analysis.

---

### 6. Why are Bronze tables append-only?

Bronze tables are generally designed as **append-only** to preserve historical data exactly as it was received.

Benefits include:

- Maintains a complete history of ingested data.
- Supports auditing and compliance.
- Enables data recovery and reprocessing.
- Prevents accidental modification of raw records.
- Improves reliability for downstream transformations.

---

### 7. What is the difference between Bronze and Silver?

| Bronze Layer | Silver Layer |
|--------------|--------------|
| Stores raw data | Stores cleaned and validated data |
| Minimal transformations | Business transformations applied |
| Preserves original records | Standardizes and enriches data |
| Acts as the source of truth | Prepares data for analytics |
| Append-oriented | Quality-focused processing |

---

### 8. Why use Unity Catalog?

Unity Catalog is Databricks' centralized data governance solution.

It provides:

- Centralized metadata management
- Fine-grained access control
- Data lineage tracking
- Auditing
- Secure data sharing
- Consistent governance across the Lakehouse

This ensures that all data assets are managed securely and consistently.

---

### 9. What transformations occur in Bronze?

Only minimal transformations are performed in the Bronze Layer.

Typical operations include:

- Schema validation
- Data type enforcement
- Adding ingestion metadata
- Creating Delta tables

Business transformations such as data cleansing, joins, aggregations, and standardization are intentionally deferred to the Silver Layer.

---

### 10. Why preserve raw data?

Preserving raw data ensures that the organization always has an untouched copy of the original source data.

This enables:

- Reprocessing when business rules change.
- Troubleshooting data quality issues.
- Historical comparisons.
- Compliance and auditing.
- Reliable downstream processing.

By keeping the raw data intact, organizations can rebuild Silver and Gold layers whenever necessary without requesting the data again from source systems.

---

# 📊 Summary

| Component | Purpose |
|-----------|---------|
| Bronze Layer | Raw Data Ingestion |
| Delta Lake | Reliable Storage |
| Unity Catalog | Governance |
| Metadata | Auditing |
| Schema Validation | Data Quality |

---

# 🎯 Key Takeaways

- Bronze is the raw ingestion layer.
- Data is preserved without business transformations.
- Delta Lake provides reliable storage.
- Metadata supports auditing and lineage.
- Bronze is the foundation for Silver and Gold.

---

# 📚 Next Modules

➡️ [Ingest Raw Dimension Data into Bronze Layer](01_Ingest_Dimensions.md)

➡️ [Ingest Raw Fact Data into Bronze Layer](02_Ingest_Fact_Tables.md)