
# 📚 Setup Unity Catalog with Azure Managed Identity & External Location

⬅️ [Unity Catalog with Azure Connectors (ADLS Gen2)](../03_ADLS/READM.md)

---

# 📖 Overview

This guide demonstrates how to configure **Azure Databricks Unity Catalog** using **Azure Data Lake Storage Gen2** with **Managed Identity Authentication**.

The setup covers:

- ✅ Creating Azure Storage Container
- ✅ Creating Directory for Catalog
- ✅ Creating Azure Databricks Access Connector
- ✅ Assigning RBAC Permissions
- ✅ Creating Storage Credential
- ✅ Creating External Location
- ✅ Creating Unity Catalog backed by ADLS Gen2

---

# 🏗 Architecture

```text
                    Azure Subscription
                           │
                           ▼
               Azure Resource Group
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
Azure Databricks                    Storage Account
        │                                   │
        ▼                                   ▼
Access Connector                  ADLS Gen2 Container
(Managed Identity)                       │
        │                                ▼
        └──────────────RBAC──────────────►
                                  ecommerce_catalog
                                           │
                                           ▼
                               Storage Credential
                                           │
                                           ▼
                                  External Location
                                           │
                                           ▼
                                   Unity Catalog
```

---

# 📋 Prerequisites

Before starting, ensure you have:

- Azure Subscription
- Azure Databricks Workspace
- Unity Catalog Enabled
- Storage Account (ADLS Gen2)
- Owner or Contributor Access
- Permission to assign RBAC roles

---

# 🚀 Step-by-Step Configuration

---

# Step 1 — Open Unity Catalog

Open **Catalog Explorer** in your Azure Databricks workspace.

![01_open_unity_catalog](images/01_open_unity_catalog.png)


# Step 2 — Create a New Catalog

Click **Create → Create Catalog**.

![02_create_catalog](images/02_create_catalog.png)

---

# Step 3 — SQL Catalog Creation Error

![03_storage_location_required](images/03_storage_location_required.png)

---

# Step 4 — Create Azure Storage Container

📷 **Image:** `04_create_storage_container.png`

![04_create_storage_container](images/04_create_storage_container.png)

---

# Step 5 — Create Directory

![05_create_directory](images/05_create_directory.png)

---

# Step 6 — Open Resource Group

![06_resource_group](images/06_resource_group.png)

---

# Step 7 — Search Access Connector

📷 **Image:** `07_search_access_connector.png`

![07_search_access_connector](images/07_search_access_connector.png)

---

# Step 8 — Create Access Connector

![08_create_access_connector](images/08_create_access_connector.png)

---

# Step 9 — Deployment Successful

![09_connector_deployed](images/09_connector_deployed.png)

---

# Step 10 — Verify Azure Resources

![10_verify_resources](images/10_verify_resources.png)

---

# Step 11 — Assign IAM Permission

![11_assign_role](images/11_assign_role.png)

---

# Step 12 — Select Storage Blob Data Contributor

![12_storage_blob_contributor](images/12_storage_blob_contributor.png)

---

# Step 13 — Assign Managed Identity

![13_select_managed_identity](images/13_select_managed_identity.png)

---

# Step 14 — Copy Resource ID

![14_copy_resource_id](images/14_copy_resource_id.png)

---

# Step 15 — Create Storage Credential

![15_create_storage_credential](images/15_create_storage_credential.png)

---

# Step 16 — Create External Location

![16_create_external_location](images/16_create_external_location.png)

---

# Step 17 — Create Unity Catalog


![17_create_catalog_sql](images/17_create_catalog_sql.png)

---

# ✅ Final Verification Checklist

| Task                                   | Status |
| -------------------------------------- | ------ |
| Storage Account Created                | ✅     |
| Container Created                      | ✅     |
| Directory Created                      | ✅     |
| Access Connector Created               | ✅     |
| Managed Identity Assigned              | ✅     |
| Storage Blob Data Contributor Assigned | ✅     |
| Storage Credential Created             | ✅     |
| External Location Created              | ✅     |
| Unity Catalog Created                  | ✅     |

---

# 📚 Technologies Used

| Technology                   | Purpose                     |
| ---------------------------- | --------------------------- |
| Azure Databricks             | Data Engineering Platform   |
| Unity Catalog                | Centralized Data Governance |
| Azure Data Lake Storage Gen2 | Managed Storage             |
| Azure Managed Identity       | Secure Authentication       |
| Azure RBAC                   | Authorization               |
| Azure Resource Manager       | Resource Management         |
| SQL                          | Catalog Creation            |

---

# 📖 Learn More

- Azure Databricks
- Unity Catalog
- Azure Data Lake Storage Gen2
- Azure Managed Identity
- Azure RBAC
- External Locations
- Storage Credentials

---

