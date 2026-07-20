# 🔗 Unity Catalog with Azure Connectors (ADLS Gen2)

⬅️ [Back to Azure Data Lake Storage (ADLS)](../03_ADLS/READM.md)

---

# 📚 Table of Contents

- Overview
- Learning Objectives
- Why Connect Unity Catalog with ADLS?
- Architecture
- Core Components
- Authentication Flow
- Governance Objects
- Benefits
- Unity Catalog vs Storage Mounts
- Best Practices
- Interview Questions
- Summary
- Key Takeaways
- Related Guides

---

# 📖 Overview

Unity Catalog is Databricks' unified governance solution for managing data, AI assets, and external storage across workspaces.

When integrated with **Azure Data Lake Storage Gen2 (ADLS Gen2)**, Unity Catalog enables secure, centralized access to cloud storage using **Microsoft Entra ID (Azure Active Directory)** instead of storage account keys.

Rather than directly accessing storage, Databricks authenticates using **Storage Credentials** and **External Locations**, providing fine-grained access control, auditing, and governance.

---

# 🎯 Learning Objectives

After completing this guide, you will understand:

- Why Unity Catalog integrates with ADLS
- Core governance components
- Authentication flow
- Storage Credentials
- External Locations
- Catalog hierarchy
- Benefits of centralized governance
- Best practices
- Interview concepts

---

# ❓ Why Connect Unity Catalog with ADLS?

Using Unity Catalog together with ADLS Gen2 provides a secure and governed way to access cloud storage.

Instead of embedding:

- Storage Account Keys
- SAS Tokens

Databricks authenticates using **Microsoft Entra ID**, allowing organizations to centrally manage permissions and security.

This approach improves:

- Security
- Governance
- Auditing
- Scalability
- Collaboration

---

# 🏗️ Architecture

![Unity Catalog Azure Architecture](images/Unity_Catalog_Azure_Architecture.png)

Unity Catalog sits between Databricks and Azure Storage.

It authenticates using Microsoft Entra ID and authorizes access through Storage Credentials and External Locations before data is accessed from ADLS Gen2.

---

# 🧩 Core Components

| Component | Description |
|-----------|-------------|
| Microsoft Entra ID | Authenticates Databricks to Azure |
| Storage Credential | Stores secure authentication information |
| External Location | Maps ADLS paths to Unity Catalog |
| Catalog | Top-level governance container |
| Schema | Database inside a catalog |
| Tables / Views | Managed data objects |
| RBAC | Azure role-based access control |
| ADLS Gen2 | Cloud storage layer |

---

# 🔐 Authentication Flow

![Unity Catalog Authentication Flow](images/Unity_Catalog_Authentication_Flow.png)

Authentication process:

1. User accesses a Unity Catalog object.
2. Unity Catalog validates permissions.
3. Storage Credential authenticates with Microsoft Entra ID.
4. Azure authorizes the request.
5. Data is securely read from ADLS Gen2.

---

# 🗂️ Governance Objects

Unity Catalog organizes data into a hierarchical structure.

```text
Catalog
   │
   └── Schema
          │
          ├── Tables
          ├── Views
          ├── Functions
          └── Volumes
```

External cloud storage is connected using:

```text
Storage Credential
        │
        ▼
External Location
        │
        ▼
Catalog
        │
        ▼
Schema
        │
        ▼
Tables
```

---

# ⭐ Benefits

- 🔒 Secure authentication using Microsoft Entra ID
- 🛡 Fine-grained access control
- 📊 Centralized governance
- 📜 Built-in auditing
- 🔄 Cross-workspace data sharing
- ☁️ Secure access to ADLS Gen2
- 🚀 Simplified Lakehouse architecture
- 📈 Enterprise scalability

---

# ⚖️ Unity Catalog vs Storage Mounts

| Feature | Unity Catalog | Storage Mounts |
|----------|---------------|----------------|
| Authentication | Microsoft Entra ID | Storage Keys / Secrets |
| Governance | Centralized | Limited |
| Fine-Grained Permissions | ✅ | ❌ |
| Auditing | ✅ | ❌ |
| External Locations | ✅ | ❌ |
| Recommended by Databricks | ✅ | ❌ (Legacy) |

---

# 💡 Best Practices

- ✅ Use Microsoft Entra ID instead of storage account keys.
- ✅ Use **Storage Credentials** to securely authenticate with ADLS Gen2.
- ✅ Use **External Locations** instead of legacy storage mounts.
- ✅ Apply the principle of least privilege using Azure RBAC and Unity Catalog permissions.
- ✅ Grant permissions to groups rather than individual users.
- ✅ Organize data using separate catalogs for Development, Testing, and Production.
- ✅ Follow the Bronze → Silver → Gold architecture for data organization.
- ✅ Store secrets securely in Azure Key Vault.
- ✅ Enable auditing and monitor access regularly.
- ✅ Regularly review permissions and rotate credentials.

---

# 🎤 Interview Questions

### 1. What is Unity Catalog?

Unity Catalog is Databricks' centralized governance solution for managing data, AI assets, permissions, and auditing.

---

### 2. Why integrate Unity Catalog with ADLS Gen2?

To securely access cloud storage using Microsoft Entra ID while providing centralized governance and fine-grained permissions.

---

### 3. What is a Storage Credential?

A Unity Catalog object that securely stores authentication information for accessing cloud storage.

---

### 4. What is an External Location?

A Unity Catalog object that maps a cloud storage path to governed access.

---

### 5. What authentication method is recommended?

Microsoft Entra ID (Azure Active Directory).

---

### 6. Why are storage mounts no longer recommended?

Because they provide limited governance, auditing, and access control compared to Unity Catalog.

---

### 7. What is the hierarchy of Unity Catalog?

Catalog → Schema → Tables / Views / Functions / Volumes.

---

### 8. What Azure role is commonly assigned?

Storage Blob Data Contributor.

---

### 9. Where should secrets be stored?

Azure Key Vault.

---

### 10. Which protocol is used to access ADLS Gen2?

`abfss://`

---

# 📊 Summary

| Component | Purpose |
|-----------|---------|
| Microsoft Entra ID | Authentication |
| Storage Credential | Secure cloud authentication |
| External Location | Maps cloud storage paths |
| Catalog | Governance layer |
| Schema | Logical database |
| Tables & Views | Data objects |
| ADLS Gen2 | Storage layer |

---

# 🎯 Key Takeaways

- Unity Catalog provides centralized governance for Azure Data Lake Storage Gen2.
- Microsoft Entra ID enables secure, keyless authentication to cloud storage.
- Storage Credentials and External Locations replace legacy storage mounts.
- Fine-grained permissions improve security and simplify data governance.
- Unity Catalog supports cross-workspace collaboration and enterprise-scale data management.
- Integrating Unity Catalog with ADLS Gen2 is the recommended approach for building secure, production-ready Lakehouse architectures.

---

# 📚 Related Guides

- 📖 Azure Data Lake Storage (ADLS)
- 📖 Unity Catalog
- 📖 Delta Lake
- 📖 Databricks Workspace Setup *(Implementation Guide)*
- 📖 Unity Catalog Setup with Azure Connectors *(Step-by-Step Guide)*

---

# 📚 Next Topic

➡️ [Setup Unity Catalog with Azure Managed Identity & External Location](01_Setup_Azure_Catalog_and_Connectors.md)

➡️ [Setup Azure Catalog and Connectors](../04_Setup_Azure_Catalog_and_Connectors/README.md)