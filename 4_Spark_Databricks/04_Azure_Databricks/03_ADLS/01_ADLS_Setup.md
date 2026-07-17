# 📦 Azure Data Lake Storage Gen2 (ADLS Gen2) Setup Guide

![Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoftazure&logoColor=white)
![ADLS Gen2](https://img.shields.io/badge/Azure%20Data%20Lake%20Gen2-0078D4?logo=microsoftazure&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

⬅️ [Back to Azure Data Lake Storage](READM.md)

---

# 📖 Overview

Azure Data Lake Storage Gen2 (ADLS Gen2) is Microsoft's enterprise-grade cloud storage solution designed for Big Data Analytics workloads.

This guide demonstrates how to:

- Create an Azure Storage Account
- Enable Data Lake Storage Gen2
- Deploy the Storage Account
- Create Containers
- Upload Data
- Organize Data Lake Structure
- Verify Uploaded Data
- Prepare ADLS for Azure Databricks

---

# 🏗 Architecture

```text
Azure Portal
      │
      ▼
Storage Account
      │
      ▼
Azure Data Lake Storage Gen2
      │
      ▼
Containers
      │
      ▼
CSV / JSON / Parquet Files
      │
      ▼
Azure Databricks
      │
      ▼
Delta Lake
```

---

# 🚀 Step 1 — Create Azure Storage Account

Create a Storage Account from the Azure Portal.

<div align="center">

![Step 1](images/step1-storage-account.png)

</div>

---

# 🚀 Step 2 — Enable Azure Data Lake Storage Gen2

Enable the **Hierarchical Namespace** to convert Blob Storage into Azure Data Lake Storage Gen2.

<div align="center">

![Step 2](images/step2-enable-hns.png)

</div>

---

# 🚀 Step 3 — Deploy Storage Account

Review the configuration and deploy the Storage Account.

<div align="center">

![Step 3](images/step3-deployment.png)

</div>

---

# 🚀 Step 4 — Create Azure Data Lake Container

Inside the Storage Account,

<div align="center">

![Step 4](images/step4-container.png)

</div>

---

# 🚀 Step 5 — Upload Files

Open the container and upload the source files.

<div align="center">

![Step 5](images/step5-upload-files.png)

</div>

---

# 🚀 Step 6 — Verify Uploaded Data

Verify that all files are successfully uploaded.

<div align="center">

![Step 6](images/step6-verify-files.png)

</div>

---

# 🚀 Step 7 — Organize Data Lake Structure

A recommended enterprise folder structure

<div align="center">

![Step 7](images/step7-folder-structure.png)

</div>

---

# 🚀 Step 8 — Azure Data Lake Ready

Your Azure Data Lake is now ready for Data Engineering workloads.

<div align="center">

![Step 8](images/step8-final-architecture.png)

</div>

---

# 📋 Best Practices

- ✅ Enable Hierarchical Namespace
- ✅ Use meaningful Storage Account names
- ✅ Create separate Containers for environments
- ✅ Organize Bronze / Silver / Gold folders
- ✅ Enable RBAC
- ✅ Use Microsoft Entra ID authentication
- ✅ Enable Lifecycle Management
- ✅ Enable Soft Delete
- ✅ Monitor Storage usage
- ✅ Enable Diagnostic Logs

---

# 🎯 Benefits of ADLS Gen2

| Feature | Description |
|----------|-------------|
| 🚀 High Performance | Optimized for Big Data workloads |
| 📂 Hierarchical Namespace | Native folder support |
| 🔒 Secure | Microsoft Entra ID, RBAC, Private Endpoints |
| 📈 Scalable | Petabyte-scale storage |
| 💰 Cost Optimized | Hot, Cool, Cold tiers |
| ⚡ Analytics Ready | Works with Databricks, Synapse, Fabric |


