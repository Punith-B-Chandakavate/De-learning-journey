# 🚀 Data Engineering Foundations (ETL & AWS)

This repository contains the fundamental concepts every Data Engineer should master before working with Big Data, Apache Spark, Airflow, Snowflake, or Cloud Data Platforms.

It covers **Data Storage**, **ETL/ELT**, **Data Warehousing**, and **AWS Services**, providing both theoretical knowledge and practical cloud implementation.

---

# 📚 Repository Structure

```text
3_DE_Foundations_ETL_AWS
│
├── 01_Data_Storage
│   ├── 01_OLAP_&_OLTP.md
│   └── 02_Data_Lake_Warehouse_Lakehouse.md
│
├── 02_Data_Transformation_File_Formats
│   ├── 01_ETL_&_ELT.md
│   ├── 02_Medallion_Arch.md
│   ├── 03_File_Formats_Fundamentals.md
│   └── 04_Parquet_Columnar_File_Format.md
│
├── 03_Data_Warehousing
│   ├── 01_Data_Normalization_Denormalization.md
│   ├── 02_Data_Modeling.md
│   ├── 03_Star_Schema_Snowflake_Schema.md
│   └── 04_SCD_modeling.md
│
├── 04_Data_Extraction_Storage
│   ├── 01_AWS_account_Setup
│   ├── 02_AWS_S3_Setup
│   ├── 03_AWS_EC2
│   ├── 04_AWS_Lambda
│   ├── 05_AWS_Glue
│   ├── 06_AWS_Athena
│   └── 07_AWS_Redshift
│
└── README.md
```

---

# 📖 Learning Modules

## 📦 1. Data Storage

Learn the core concepts of modern data storage systems.

* 📄 [OLTP &amp; OLAP](01_Data_Storage/01_OLAP_&_OLTP.md)
* 📄 [Data Lake, Data Warehouse &amp; Data Lakehouse](01_Data_Storage/02_Data_Lake_Warehouse_Lakehouse.md)

Topics Covered:

* OLTP vs OLAP
* Structured Data
* Semi-Structured Data
* Unstructured Data
* Data Lake
* Data Warehouse
* Data Lakehouse

---

## 🔄 2. Data Transformation & File Formats

Understand how data moves from raw sources into analytics-ready datasets.

* 📄 [ETL &amp; ELT](02_Data_Transformation_File_Formats/01_ETL_&_ELT.md)
* 📄 [Medallion Architecture](02_Data_Transformation_File_Formats/02_Medallion_Arch.md)
* 📄 [File Format Fundamentals](02_Data_Transformation_File_Formats/03_File_Formats_Fundamentals.md)
* 📄 [Parquet Columnar File Format](02_Data_Transformation_File_Formats/04_Parquet_Columnar_File_Format.md)

Topics Covered:

* ETL
* ELT
* Bronze Layer
* Silver Layer
* Gold Layer
* CSV
* JSON
* Parquet
* Row vs Columnar Storage

---

## 🏢 3. Data Warehousing

Learn how enterprise data warehouses are designed.

* 📄 [Data Normalization &amp; Denormalization](03_Data_Warehousing/01_Data_Normalization_Denormalization.md)
* 📄 [Data Modeling](03_Data_Warehousing/02_Data_Modeling.md)
* 📄 [Star Schema &amp; Snowflake Schema](03_Data_Warehousing/03_Star_Schema_Snowflake_Schema.md)
* 📄 [Slowly Changing Dimensions (SCD)](03_Data_Warehousing/04_SCD_modeling.md)

Topics Covered:

* Database Normalization
* Data Modeling
* Fact Tables
* Dimension Tables
* Star Schema
* Snowflake Schema
* SCD Type 1
* SCD Type 2

---

## ☁️ 4. AWS Data Engineering

Hands-on implementation of a modern AWS-based ETL pipeline.

### AWS Setup

* 📄 [AWS Account Setup](04_Data_Extraction_Storage/01_AWS_account_Setup/README.md)
* 📄 [Amazon S3 Setup](04_Data_Extraction_Storage/02_AWS_S3_Setup/README.md)
* 📄 [Amazon EC2](04_Data_Extraction_Storage/03_AWS_EC2/README.md)
* 📄 [AWS Lambda](04_Data_Extraction_Storage/04_AWS_Lambda/README.md)
* 📄 [AWS Glue](04_Data_Extraction_Storage/05_AWS_Glue/README.md)
* 📄 [AWS Athena](04_Data_Extraction_Storage/06_AWS_Athena/README.md)
* 📄 [Amazon Redshift](04_Data_Extraction_Storage/07_AWS_Redshift/README.md)

Topics Covered:

* IAM
* S3
* EC2
* Lambda
* Glue
* Athena
* Redshift

---

# 🛣️ Learning Roadmap

```text
                     Data Engineering Foundations
                                 │
     ┌───────────────────────────┼────────────────────────────┐
     │                           │                            │
     ▼                           ▼                            ▼
 Data Storage           Data Transformation          Data Warehousing
     │                           │                            │
 OLTP & OLAP                 ETL / ELT              Data Modeling
 Data Lake                   Medallion              Normalization
 Warehouse                   File Formats           Star Schema
 Lakehouse                   Parquet                Snowflake Schema
                                                          │
                                                          ▼
                                                 Slowly Changing
                                                   Dimensions
                                                          │
                                                          ▼
                                             AWS Data Engineering
                                                          │
      ┌───────────────┬──────────────┬──────────────┬──────────────┐
      ▼               ▼              ▼              ▼              ▼ 
     IAM             S3             EC2          Lambda           Glue
                                                                   │
                                                                   ▼
                                                                 Athena
                                                                   │
                                                                   ▼
                                                               Redshift
                                                                   │
                                                                   ▼
                                                                Power BI
```

---

# 🏗️ End-to-End AWS ETL Pipeline

```text
OLTP Database
      │
      ▼
Amazon S3
(Raw Data)
      │
      ▼
AWS Lambda
(Event Trigger)
      │
      ▼
AWS Glue ETL
      │
      ▼
Amazon S3
(Processed Data)
      │
      ▼
AWS Glue Catalog
      │
      ▼
Amazon Athena
      │
      ▼
Amazon Redshift
      │
      ▼
Power BI Dashboard
```

---

# 🎯 Learning Outcomes

By completing this repository, you will understand:

* ✅ Modern Data Storage Architectures
* ✅ ETL and ELT Pipelines
* ✅ Medallion Architecture
* ✅ Data Warehousing Concepts
* ✅ Data Modeling Techniques
* ✅ AWS Data Engineering Services
* ✅ Building Serverless ETL Pipelines
* ✅ Querying Data Lakes with Athena
* ✅ Data Warehousing with Amazon Redshift
* ✅ Dashboarding with Power BI

---

# 🛠️ Technologies Covered

| Category          | Technologies                                 |
| ----------------- | -------------------------------------------- |
| Database Concepts | OLTP, OLAP                                   |
| Storage           | Data Lake, Data Warehouse, Data Lakehouse    |
| Data Processing   | ETL, ELT, Medallion Architecture             |
| File Formats      | CSV, JSON, Parquet                           |
| Data Modeling     | Star Schema, Snowflake Schema, SCD           |
| AWS Cloud         | IAM, S3, EC2, Lambda, Glue, Athena, Redshift |
| Visualization     | Power BI                                     |

---

# 🚀 Next Module

➡️ [Spark &amp; Databricks Fundamentals](../4_Spark_Databricks/01_Spark&Databricks_Fundamentals.md)
