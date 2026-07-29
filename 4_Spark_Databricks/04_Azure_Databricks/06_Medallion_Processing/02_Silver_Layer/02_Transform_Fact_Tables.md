
# 🥈 Transform Fact Tables into the Silver Layer

![Azure](<https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoftazure&logoColor=white>)
![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-FF3621?logo=databricks&logoColor=white)
![Unity Catalog](https://img.shields.io/badge/Unity-Catalog-orange)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)
![Structured Streaming](<https://img.shields.io/badge/Spark-Structured%20Streaming-red>)

---

⬅️ [Back to Silver Layer](README.md)

---

# 📚 Table of Contents

- Overview
- Learning Objectives
- Prerequisites
- Fact Tables
- Notebook Overview
- Transformation Architecture
- Processing Workflow
- Step 1 – Configure Notebook Parameters
- Step 2 – Read Bronze Fact Tables
- Step 3 – Apply Data Quality Transformations
- Step 4 – Configure Checkpoint Location
- Step 5 – Create Upsert Function
- Step 6 – Incrementally Load Data into Silver
- Step 7 – Verify Silver Tables
- Silver Fact Tables
- Resource Hierarchy
- Data Flow
- Data Lineage
- Verification Checklist
- SQL Verification
- Benefits
- Why Structured Streaming?
- Why foreachBatch()?
- Why Delta MERGE?
- Best Practices
- Common Mistakes
- Interview Questions
- Summary
- Key Takeaways

---

# 📖 Overview

This notebook transforms raw transactional data from the Bronze layer into trusted Silver Delta tables using **Apache Spark Structured Streaming** and **Delta Lake**.

Unlike the Dimension transformation notebook, this implementation performs **incremental processing** by continuously reading newly available records from the Bronze Delta tables. Each micro-batch is cleaned, standardized, validated, and merged into the Silver layer using Delta MERGE operations.

The notebook ensures that existing records are updated, new records are inserted, and duplicate records are avoided, producing reliable fact datasets for downstream Gold layer analytics.

---

# 🎯 Learning Objectives

After completing this notebook, you will be able to:

- Read Bronze fact tables using Structured Streaming.
- Process incremental data using Spark.
- Clean and standardize transactional data.
- Configure checkpointing.
- Implement Delta MERGE (upsert).
- Enable Change Data Feed (CDF).
- Create trusted Silver fact tables.

---

# 📋 Prerequisites

Before running this notebook, ensure that you have completed:

- Azure Databricks Setup
- Unity Catalog Configuration
- Bronze Layer Data Ingestion
- Structured Streaming Fundamentals
- Delta Lake Fundamentals
- Bronze Fact Tables Successfully Created

---

# 📂 Fact Tables

The notebook processes the following transactional datasets.

| Bronze Table    | Silver Table    | Description         |
| --------------- | --------------- | ------------------- |
| brz_orders      | slv_orders      | Sales Orders        |
| brz_order_items | slv_order_items | Order Line Items    |
| brz_shipments   | slv_shipments   | Shipment Details    |
| brz_returns     | slv_returns     | Return Transactions |

---

# 📓 Notebook Overview

The notebook performs the following tasks:

1. Configure notebook parameters
2. Read Bronze streaming data
3. Apply cleansing transformations
4. Remove duplicate records
5. Convert data types
6. Configure checkpoint location
7. Process micro-batches using foreachBatch()
8. Execute Delta MERGE
9. Verify Silver tables

---

# 🏗 Transformation Architecture

```text
Bronze Fact Tables
         │
         ▼
Structured Streaming
         │
         ▼
Data Cleansing
         │
         ▼
Business Validation
         │
         ▼
foreachBatch()
         │
         ▼
Delta MERGE
         │
         ▼
Silver Delta Tables
```

---

# 🔄 Processing Workflow

```text
Read Bronze Stream
         │
         ▼
Remove Duplicates
         │
         ▼
Convert Data Types
         │
         ▼
Standardize Values
         │
         ▼
Add Metadata
         │
         ▼
foreachBatch()
         │
         ▼
Delta MERGE
         │
         ▼
Silver Tables
```

---

# 🚀 Step 1 — Configure Notebook Parameters

Configure notebook widgets and environment variables.

Typical parameters include:

- Catalog Name
- Storage Account
- Container Name

These parameters make the notebook reusable across Development, Test, and Production environments.

---

# 🚀 Step 2 — Read Bronze Fact Tables

Read incremental records from Bronze Delta tables.

Example:

```python
df = spark.readStream \
    .format("delta") \
    .table("ecommerce.bronze.brz_order_items")
```

---

# 🚀 Step 3 — Apply Data Quality Transformations

Typical transformations include:

- Remove duplicate records
- Convert numeric fields
- Normalize text values
- Handle null values
- Standardize categorical values
- Add processing timestamp

---

# 🚀 Step 4 — Configure Checkpoint Location

Checkpointing enables:

- Fault tolerance
- Exactly-once processing
- Recovery after failures
- Tracking processed batches

---

# 🚀 Step 5 — Create Upsert Function

The notebook defines a reusable function that:

- Creates the Silver table if it does not exist
- Enables Delta Change Data Feed
- Executes Delta MERGE
- Updates existing records
- Inserts new records

---

# 🚀 Step 6 — Incrementally Load Data into Silver

The notebook processes each streaming micro-batch using:

```python
.foreachBatch(upsert_to_silver)
```

Each micro-batch is merged into the Silver table using the business key.

---

# 🚀 Step 7 — Verify Silver Tables

Verify that the following Silver fact tables have been created:

- slv_orders
- slv_order_items
- slv_shipments
- slv_returns

---

# 📂 Silver Fact Tables

| Table           | Description          |
| --------------- | -------------------- |
| slv_orders      | Clean Sales Orders   |
| slv_order_items | Clean Order Items    |
| slv_shipments   | Shipment Information |
| slv_returns     | Return Information   |

---

# 📂 Resource Hierarchy

```text
ecommerce
│
├── bronze
│   ├── brz_orders
│   ├── brz_order_items
│   ├── brz_shipments
│   └── brz_returns
│
└── silver
    ├── slv_orders
    ├── slv_order_items
    ├── slv_shipments
    └── slv_returns
```

---

# 🔄 Data Flow

```text
Bronze Delta Tables
        │
        ▼
Structured Streaming
        │
        ▼
Data Quality Transformations
        │
        ▼
foreachBatch()
        │
        ▼
Delta MERGE
        │
        ▼
Silver Delta Tables
```

---

# 📈 Data Lineage

```text
Landing Files
      │
      ▼
Bronze Fact Tables
      │
      ▼
Transform Fact Notebook
      │
      ▼
Silver Fact Tables
      │
      ▼
Gold Layer
```

---

# ✅ Verification Checklist

| Component                      | Status |
| ------------------------------ | :----: |
| Notebook Parameters Configured |   ✅   |
| Bronze Stream Connected        |   ✅   |
| Data Cleansed                  |   ✅   |
| Duplicate Records Removed      |   ✅   |
| Data Standardized              |   ✅   |
| Checkpoint Created             |   ✅   |
| MERGE Executed                 |   ✅   |
| Silver Tables Updated          |   ✅   |
| Change Data Feed Enabled       |   ✅   |

---

# 🔍 SQL Verification

```sql
SHOW TABLES IN silver;
```

```sql
SELECT *
FROM silver.slv_order_items
LIMIT 10;
```

```sql
SELECT COUNT(*)
FROM silver.slv_order_items;
```

```sql
DESCRIBE EXTENDED silver.slv_order_items;
```

---

# 📈 Benefits

- Incremental Processing
- Exactly-once Processing
- Reliable MERGE Operations
- Better Data Quality
- Reduced Processing Time
- Fault Tolerance
- Analytics-ready Fact Tables

---

# 🏆 Why Structured Streaming?

Structured Streaming enables:

- Continuous ingestion
- Incremental processing
- Scalability
- Fault tolerance
- Efficient resource utilization

---

# 🏆 Why foreachBatch()?

The `foreachBatch()` API enables:

- Custom processing logic
- Delta MERGE operations
- Batch-level transformations
- Reusable ETL logic

---

# 🏆 Why Delta MERGE?

Delta MERGE provides:

- Upsert support
- Prevents duplicate records
- Efficient updates
- ACID transactions
- Reliable incremental loading

---

# 💡 Best Practices

- Use business keys for MERGE.
- Configure checkpoint locations.
- Enable Change Data Feed.
- Standardize data before loading.
- Monitor streaming jobs.
- Keep transformations deterministic.
- Validate record counts after loading.

---

# ⚠️ Common Mistakes

- Missing checkpoint configuration.
- Using append instead of MERGE.
- Ignoring duplicate records.
- Using incorrect business keys.
- Mixing Bronze and Silver logic.
- Skipping validation.

---

# 🎤 Interview Questions

### 1. What is Structured Streaming?

**Apache Spark Structured Streaming** is a scalable stream processing engine that processes data continuously as it arrives while using the same DataFrame and SQL APIs as batch processing.

Instead of processing an entire dataset repeatedly, Structured Streaming processes only newly available records, making it suitable for real-time and incremental ETL pipelines.

**Key Benefits:**

- Incremental data processing
- High scalability
- Fault tolerance
- Exactly-once processing
- Unified batch and streaming APIs

---

### 2. Why use `foreachBatch()`?

The `foreachBatch()` API allows developers to apply custom processing logic to every streaming micro-batch.

In this project, it is used because Delta Lake **MERGE (upsert)** operations cannot be performed directly with the standard streaming sink.

Using `foreachBatch()` enables:

- Delta MERGE operations
- Custom business logic
- Data validation
- Batch-level processing
- Reusable ETL functions

Each micro-batch is passed to a custom function where records are inserted or updated in the Silver table.

---

### 3. Why use Delta MERGE?

**Delta MERGE** performs an **upsert** operation by updating existing records and inserting new records in a single transaction.

Benefits include:

- Prevents duplicate records
- Updates changed records
- Inserts new records
- Supports ACID transactions
- Simplifies incremental loading
- Maintains data consistency

It is commonly used in the Silver Layer to synchronize transactional data with the latest changes from the Bronze layer.

---

### 4. What is checkpointing?

Checkpointing is a mechanism used by Spark Structured Streaming to store metadata about processed micro-batches.

Checkpoint data includes:

- Processed offsets
- Streaming progress
- Batch metadata
- Execution state

Checkpointing enables:

- Fault tolerance
- Recovery after failures
- Exactly-once processing
- Prevention of duplicate processing

If a streaming job fails, Spark resumes processing from the last successful checkpoint instead of starting from the beginning.

---

### 5. What is Change Data Feed (CDF)?

**Change Data Feed (CDF)** is a Delta Lake feature that records changes made to a Delta table.

It captures:

- Inserts
- Updates
- Deletes

Benefits of CDF include:

- Incremental downstream processing
- Efficient data synchronization
- Easier ETL pipelines
- Simplified CDC (Change Data Capture)

Instead of reading the entire table repeatedly, downstream processes can read only the changed records.

---

### 6. Why are business keys important?

A **business key** uniquely identifies a business record.

Examples include:

- `order_id`
- `customer_id`
- `product_id`
- `order_id + item_seq`

Business keys are used during MERGE operations to determine whether an incoming record already exists.

Benefits include:

- Prevent duplicate records
- Identify records to update
- Maintain data integrity
- Support incremental loading

Without business keys, MERGE operations cannot correctly match existing records.

---

### 7. What is incremental processing?

Incremental processing means processing **only newly added or modified data** instead of reprocessing the entire dataset.

Advantages include:

- Faster execution
- Lower compute cost
- Better scalability
- Reduced processing time
- Improved pipeline efficiency

In this notebook, Structured Streaming continuously processes only new records from the Bronze Delta table and loads them into the Silver layer.

---

### 8. What is the difference between Append and MERGE?

| Append | MERGE |
|---------|-------|
| Only inserts new records | Inserts and updates records |
| Cannot modify existing records | Updates matching records |
| May create duplicate records | Prevents duplicates |
| Suitable for immutable data | Suitable for changing transactional data |
| Faster but less flexible | More flexible and reliable |

Append is generally used for raw data ingestion, while MERGE is preferred in the Silver Layer for maintaining trusted datasets.

---

### 9. Why remove duplicates?

Duplicate records can lead to incorrect analytics and reporting.

Removing duplicates helps to:

- Improve data accuracy
- Prevent double counting
- Maintain data integrity
- Improve downstream joins
- Produce reliable business reports

For example, duplicate order records can inflate total sales values and produce inaccurate business metrics.

---

### 10. What is the output of this notebook?

The notebook produces **clean, validated, standardized, and incrementally updated Silver Delta tables**.

The output tables:

- Remove duplicate records
- Apply business validation rules
- Standardize data formats
- Convert columns to correct data types
- Include processing metadata
- Store trusted transactional data

Examples of output tables include:

- `slv_orders`
- `slv_order_items`
- `slv_shipments`
- `slv_returns`

These Silver Delta tables become the trusted source for downstream Gold layer aggregations, dashboards, reporting, and business analytics.

---

# 📊 Summary

| Component            | Purpose                  |
| -------------------- | ------------------------ |
| Bronze Fact Tables   | Source Data              |
| Structured Streaming | Incremental Processing   |
| Data Cleansing       | Improve Quality          |
| Delta MERGE          | Upsert Records           |
| Checkpointing        | Fault Tolerance          |
| Silver Fact Tables   | Trusted Transaction Data |

---

# 🎯 Key Takeaways

- Bronze fact tables are transformed incrementally using Spark Structured Streaming.
- Data quality improvements include cleansing, validation, and standardization.
- Delta MERGE ensures existing records are updated and new records are inserted without creating duplicates.
- Checkpointing and Change Data Feed provide reliable, fault-tolerant incremental processing.
- Silver fact tables become the trusted transactional datasets used by the Gold layer for business reporting and analytics.

