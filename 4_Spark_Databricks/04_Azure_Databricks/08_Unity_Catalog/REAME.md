# 🏛️ Azure Databricks Unity Catalog

![Microsoft Azure](<https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoftazure&logoColor=white>)
![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-FF3621?logo=databricks&logoColor=white)
![Unity Catalog](https://img.shields.io/badge/Unity-Catalog-orange)
![Azure Data Lake Storage Gen2](https://img.shields.io/badge/ADLS-Gen2-0078D4)
![Managed Identity](https://img.shields.io/badge/Managed-Identity-green)

---

# Table of Contents

- Overview
- Learning Objectives
- What is Unity Catalog?
- Why Unity Catalog?
- Unity Catalog Architecture
- Unity Catalog Components
- Unity Catalog Hierarchy
- Benefits of Unity Catalog
- Data Governance Features
- Managed vs External Tables
- ShopVista Unity Catalog Organization
- Module Documentation
- End-to-End Data Flow
- Technologies Used
- Best Practices
- Common Challenges
- Interview Questions
- Summary
- Key Takeaways
- Related Documentation
- Completion Checklist
- Congratulations

---

# 📖 Overview

Unity Catalog is the centralized governance solution for Azure Databricks. It provides a unified way to organize data assets, manage metadata, secure cloud storage, enforce permissions, and track data lineage across an entire Databricks account.

Instead of managing permissions and metadata independently for each workspace, Unity Catalog provides a single governance layer that simplifies administration while improving security, collaboration, and compliance.

In this learning module, you will understand the core concepts of Unity Catalog, its architecture, governance model, and how it integrates with Azure Data Lake Storage Gen2 to support the Medallion Architecture.

---

# 🎯 Learning Objectives

After completing this module, you will be able to:

- Understand Unity Catalog
- Understand the Unity Catalog hierarchy
- Learn Catalogs and Schemas
- Understand Storage Credentials
- Learn External Locations
- Understand External Volumes
- Understand centralized governance
- Learn fine-grained permissions
- Understand metadata management
- Learn data lineage concepts

---

# 🏛️ What is Unity Catalog?

Unity Catalog is the centralized governance layer for Azure Databricks.

It provides:

- Centralized metadata management
- Fine-grained security
- Cloud storage integration
- Data lineage
- Auditing
- Data discovery
- Cross-workspace governance

Unity Catalog enables organizations to securely manage all their data assets from a single governance platform.

---

# 🚀 Why Unity Catalog?

Modern organizations manage data across multiple teams, workspaces, and storage accounts.

Unity Catalog simplifies this by providing:

- Centralized governance
- Secure cloud storage access
- Consistent metadata
- Simplified administration
- Better collaboration
- Regulatory compliance
- Enterprise security
- Improved data discovery

---

# 🏗️ Unity Catalog Architecture

```text
Azure Data Lake Storage Gen2
            │
            ▼
     Managed Identity
            │
            ▼
   Storage Credential
            │
            ▼
   External Location
            │
            ▼
    External Volume
            │
            ▼
     Unity Catalog
            │
            ▼
        Catalog
            │
            ▼
        Schema
            │
            ▼
Tables • Views • Volumes • Functions
```

---

# 🧩 Unity Catalog Components

| Component          | Purpose                                    |
| ------------------ | ------------------------------------------ |
| Metastore          | Stores metadata for the Databricks account |
| Catalog            | Top-level container for organizing data    |
| Schema             | Groups related database objects            |
| Tables             | Structured datasets                        |
| Views              | Virtual datasets                           |
| Volumes            | Storage for unstructured files             |
| Storage Credential | Secure authentication to cloud storage     |
| External Location  | Secure mapping to Azure Storage            |
| Managed Identity   | Authentication without storage keys        |

---

# 🏛️ Unity Catalog Hierarchy

```text
Metastore
     │
     ▼
 Catalog
     │
     ▼
 Schema
     │
     ├────────────┬────────────┬────────────┐
     ▼            ▼            ▼            ▼
 Tables       Views       Volumes     Functions
```

---

# ✅ Benefits of Unity Catalog

- Centralized Governance
- Fine-Grained Security
- Secure Cloud Storage Access
- Unified Metadata
- Data Lineage
- Cross-Workspace Sharing
- Auditing
- Regulatory Compliance

---

# 🛡️ Data Governance Features

Unity Catalog provides:

- Role-Based Access Control (RBAC)
- Catalog-level permissions
- Schema-level permissions
- Table-level permissions
- Metadata management
- Auditing
- Data lineage
- Ownership management

---

# 🗂️ Managed vs External Tables

| Managed Tables                | External Tables                 |
| ----------------------------- | ------------------------------- |
| Databricks manages storage    | External storage manages files  |
| Managed lifecycle             | External lifecycle              |
| Best for curated Delta tables | Best for existing cloud storage |

---

# 🏢 ShopVista Unity Catalog Organization

```text
Metastore
│
└── ecommerce
      │
      ├── raw
      ├── bronze
      ├── silver
      └── gold
```
---

# 🔄 End-to-End Data Flow

```text
Azure Data Lake Storage Gen2
            │
            ▼
Managed Identity
            │
            ▼
Storage Credential
            │
            ▼
External Location
            │
            ▼
External Volume
            │
            ▼
Unity Catalog
            │
            ▼
Catalog
            │
            ▼
Schemas
      │
      ├── Raw
      ├── Bronze
      ├── Silver
      └── Gold
            │
            ▼
Azure Databricks
            │
            ▼
Power BI
```

---

# 🛠️ Technologies Used

- Azure Databricks
- Unity Catalog
- Azure Data Lake Storage Gen2
- Azure Managed Identity
- Delta Lake
- Apache Spark
- PySpark
- Power BI

---

# 💡 Best Practices

- Use one Catalog per business domain.
- Organize Schemas based on the Medallion Architecture.
- Use Azure Managed Identity.
- Avoid Storage Account Keys.
- Use External Locations for storage access.
- Store raw files in External Volumes.
- Apply Role-Based Access Control (RBAC).
- Maintain metadata and descriptions.
- Enable data lineage.
- Follow consistent naming conventions.

---

# ⚠️ Common Challenges

| Challenge                | Solution                             |
| ------------------------ | ------------------------------------ |
| Permission issues        | Verify Unity Catalog privileges      |
| Storage access errors    | Validate Managed Identity and RBAC   |
| External Location errors | Verify Storage Credential            |
| Missing metadata         | Check Catalog and Schema permissions |
| Governance complexity    | Use consistent naming and RBAC       |

---

# 🎤 Interview Questions

---

## 1. What is Unity Catalog?

**Answer:**

Unity Catalog is the centralized data governance solution for Azure Databricks. It provides a unified way to manage metadata, permissions, security, data lineage, and access control across all Databricks workspaces within an organization.

---

## 2. Why use Unity Catalog?

**Answer:**

Unity Catalog is used to centralize data governance and simplify data management across the Lakehouse platform.

Key benefits include:

- Centralized metadata management
- Fine-grained access control
- Secure cloud storage integration
- Data lineage and auditing
- Cross-workspace data sharing
- Simplified administration
- Regulatory compliance

---

## 3. What is a Metastore?

**Answer:**

A Metastore is the top-level metadata repository in Unity Catalog. It stores information about catalogs, schemas, tables, views, functions, volumes, permissions, and metadata for an entire Databricks account.

Hierarchy:

```text
Metastore
    │
    ▼
Catalog
    │
    ▼
Schema
```

---

## 4. What is a Catalog?

**Answer:**

A Catalog is the highest-level logical container inside a Metastore. It groups related schemas and organizes data according to business domains or projects.

Example:

```text
Metastore
    │
    ▼
ecommerce
```

---

## 5. What is a Schema?

**Answer:**

A Schema is a logical container within a Catalog that organizes related database objects such as tables, views, functions, and volumes.

Example:

```text
ecommerce
│
├── raw
├── bronze
├── silver
└── gold
```

Schemas help separate data into logical layers and simplify data management.

---

## 6. What is a Storage Credential?

**Answer:**

A Storage Credential is a Unity Catalog object that securely authenticates Azure Databricks with cloud storage using **Azure Managed Identity**, instead of Storage Account Keys or SAS Tokens.

Benefits include:

- Secure authentication
- No hardcoded credentials
- Centralized credential management
- Azure-native security
- Easier credential rotation

---

## 7. What is an External Location?

**Answer:**

An External Location is a Unity Catalog object that securely maps an Azure Data Lake Storage path to a Storage Credential. It allows Databricks to access external storage while enforcing Unity Catalog permissions.

Example:

```text
Storage Credential
        │
        ▼
External Location
        │
        ▼
Azure Data Lake Storage Gen2
```

---

## 8. What is an External Volume?

**Answer:**

An External Volume is a Unity Catalog object that provides governed access to unstructured files stored in external cloud storage.

It is commonly used to store:

- CSV files
- JSON files
- Excel files
- Images
- PDFs
- Machine Learning datasets
- Configuration files

Unlike tables, Volumes are designed for file storage rather than structured data.

---

## 9. What is the difference between Managed Tables and External Tables?

| Managed Tables                       | External Tables                           |
| ------------------------------------ | ----------------------------------------- |
| Storage managed by Databricks        | Storage managed externally                |
| Data lifecycle managed by Databricks | Data lifecycle managed outside Databricks |
| Best for curated Delta tables        | Best for existing cloud storage           |
| Simplified management                | Greater storage flexibility               |

---

## 10. What is Data Lineage?

**Answer:**

Data Lineage is the ability to track how data moves through the data platform—from its source to its final destination.

It shows:

- Source files
- Transformation notebooks
- Tables created
- Downstream dependencies
- Data flow across Bronze, Silver, and Gold layers

Data Lineage helps with impact analysis, auditing, troubleshooting, and regulatory compliance.

---

## 11. How does Unity Catalog improve governance?

**Answer:**

Unity Catalog improves governance by providing centralized control over all data assets in Azure Databricks.

It enables:

- Centralized metadata management
- Fine-grained permissions
- Role-Based Access Control (RBAC)
- Data lineage tracking
- Auditing and monitoring
- Secure cloud storage access
- Consistent governance across multiple workspaces

This helps organizations maintain security, compliance, and data consistency.

---

## 12. Why use Managed Identity?

**Answer:**

Managed Identity is used to securely authenticate Azure Databricks with Azure Data Lake Storage without storing secrets, Storage Account Keys, or SAS Tokens.

Benefits include:

- Eliminates hardcoded credentials
- Improves security
- Supports Azure Role-Based Access Control (RBAC)
- Simplifies authentication management
- Automatic credential rotation
- Reduces the risk of credential exposure

Managed Identity is the recommended authentication method for production Azure Databricks environments.

---

# 📊 Summary

Unity Catalog provides centralized governance for Azure Databricks by managing metadata, permissions, cloud storage access, and data lineage. It forms the governance foundation of the ShopVista Lakehouse architecture and supports secure, scalable, and enterprise-ready data management.

---

# 🎯 Key Takeaways

- Centralized Governance
- Fine-Grained Security
- Metadata Management
- Data Lineage
- Azure Managed Identity
- External Locations
- External Volumes
- Enterprise Lakehouse Governance

---
# 📚 Next Topic

➡️ [Azure Databricks Role-Based Access Control (RBAC)](01_Role_Based_Access_Control.md)
