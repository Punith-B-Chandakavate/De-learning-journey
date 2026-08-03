# 🔐 Azure Databricks Role-Based Access Control (RBAC)

![Microsoft Azure](<https://img.shields.io/badge/Microsoft%20Azure-0078D4?logo=microsoftazure&logoColor=white>)
![Azure Databricks](https://img.shields.io/badge/Azure-Databricks-FF3621?logo=databricks&logoColor=white)
![Microsoft Entra ID](<https://img.shields.io/badge/Microsoft-Entra%20ID-0078D4>)
![Unity Catalog](https://img.shields.io/badge/Unity-Catalog-orange)
![RBAC](https://img.shields.io/badge/Security-RBAC-green)

---

# Table of Contents

- Overview
- Learning Objectives
- What is RBAC?
- Why RBAC?
- RBAC Architecture
- RBAC Components
- Authentication vs Authorization
- RBAC Permission Hierarchy
- Enterprise Access Flow
- Benefits of RBAC
- Best Practices
- Module Documentation
- Technologies Used
- Interview Questions
- Summary
- Key Takeaways
- Related Documentation
- Completion Checklist
- Congratulations

---

# 📖 Overview

Role-Based Access Control (RBAC) is a security model used to control access to resources based on a user's assigned role rather than assigning permissions directly to individual users.

Azure Databricks integrates with **Microsoft Entra ID**, **Security Groups**, and **Unity Catalog** to implement enterprise-grade access control.

Instead of granting permissions individually, users are assigned to security groups, and permissions are granted to those groups. This approach simplifies administration, improves security, and enables centralized governance.

This module introduces the concepts of Azure Databricks RBAC and explains how authentication, authorization, security groups, and Unity Catalog work together.

> **Note**
>
> The complete hands-on implementation is documented separately in **01_RBAC_Setup.md**.

---

# 🎯 Learning Objectives

After completing this module, you will be able to:

- Understand Role-Based Access Control
- Learn Authentication and Authorization
- Understand Microsoft Entra ID
- Learn Azure Databricks identity management
- Understand Security Groups
- Learn Unity Catalog permissions
- Understand enterprise access management
- Apply least privilege principles
- Design secure data platforms
- Implement enterprise governance

---

# 🔐 What is RBAC?

Role-Based Access Control (RBAC) is a security mechanism where permissions are assigned to roles instead of individual users.

Users receive permissions by becoming members of security groups.

Example:

```text
User
   │
   ▼
Security Group
   │
   ▼
Permissions
```

---

# 🚀 Why RBAC?

RBAC simplifies access management in enterprise environments.

Benefits include:

- Centralized permission management
- Reduced administrative effort
- Better security
- Easier auditing
- Simplified onboarding
- Consistent access policies
- Scalability
- Regulatory compliance

---

# 🏗 RBAC Architecture

```text
Microsoft Entra ID
        │
        ▼
 Enterprise Users
        │
        ▼
 Security Groups
        │
        ▼
 Azure Databricks
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
 Tables / Views / Volumes
```

---

# 🧩 RBAC Components

| Component          | Purpose                           |
| ------------------ | --------------------------------- |
| Microsoft Entra ID | Identity provider                 |
| Enterprise Users   | Authenticated users               |
| Security Groups    | Group-based permission management |
| Azure Databricks   | Compute platform                  |
| Unity Catalog      | Centralized governance            |
| SQL Warehouse      | Query execution                   |
| Catalog            | Top-level data container          |
| Schema             | Logical organization              |
| Tables             | Data storage                      |

---

# 🔑 Authentication vs Authorization

| Authentication                  | Authorization                       |
| ------------------------------- | ----------------------------------- |
| Verifies user identity          | Determines what the user can access |
| Performed by Microsoft Entra ID | Managed by Unity Catalog            |
| Login process                   | Permission enforcement              |
| "Who are you?"                  | "What can you do?"                  |

---

# 📂 RBAC Permission Hierarchy

Permissions are inherited through the Unity Catalog hierarchy.

```text
Catalog
     │
     ▼
Schema
     │
     ▼
Tables
     │
     ▼
Views
     │
     ▼
Volumes
```

---

# 🔄 Enterprise Access Flow

```text
Microsoft Entra ID
        │
        ▼
Authenticate User
        │
        ▼
Azure Databricks
        │
        ▼
Security Group
        │
        ▼
Unity Catalog
        │
        ▼
Permission Check
        │
        ▼
Grant / Deny Access
```

---

# ✅ Benefits of RBAC

- Centralized administration
- Group-based permissions
- Least privilege security
- Enterprise scalability
- Simplified auditing
- Better governance
- Improved compliance
- Easier user management

---

# 📂 Module Documentation

| Document                         | Description                                                                                                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [📘 RBAC Setup](01_RBAC_Setup.md) | Complete implementation guide covering Microsoft Entra ID, Azure Databricks users, Security Groups, Unity Catalog permissions, authentication, and permission validation. |

---

# 🛠 Technologies Used

- Microsoft Entra ID
- Azure Databricks
- Unity Catalog
- Azure RBAC
- SQL Warehouse
- Azure Data Lake Storage Gen2

---

# 💡 Best Practices

- Assign permissions to groups instead of users.
- Apply the Principle of Least Privilege.
- Separate Engineer, Analyst, and Admin roles.
- Audit permissions regularly.
- Use Microsoft Entra ID for authentication.
- Use Unity Catalog for authorization.
- Avoid granting unnecessary MODIFY permissions.
- Maintain consistent security group naming.

---

# 🎤 Interview Questions

---

## 1. What is RBAC?

**Answer:**

Role-Based Access Control (RBAC) is a security model that controls access to resources based on a user's assigned role rather than assigning permissions directly to individual users.

Users inherit permissions through roles or security groups, making access management simpler and more secure.

---

## 2. Why use RBAC?

**Answer:**

RBAC is used to simplify access management and improve security in enterprise environments.

Benefits include:

- Centralized permission management
- Improved security
- Simplified administration
- Scalable user management
- Easier onboarding and offboarding
- Better auditing and compliance
- Reduced risk of excessive permissions

---

## 3. Authentication vs Authorization?

| Authentication                    | Authorization                            |
| --------------------------------- | ---------------------------------------- |
| Verifies a user's identity        | Determines what the user can access      |
| Confirms**who the user is** | Determines**what the user can do** |
| Managed by Microsoft Entra ID     | Managed by Unity Catalog and RBAC        |
| Happens during login              | Happens after successful authentication  |

---

## 4. What is Microsoft Entra ID?

**Answer:**

Microsoft Entra ID (formerly Azure Active Directory) is Microsoft's cloud-based identity and access management service.

It is responsible for:

- User authentication
- User identity management
- Single Sign-On (SSO)
- Multi-Factor Authentication (MFA)
- Security Group management
- Enterprise identity governance

Azure Databricks uses Microsoft Entra ID to authenticate users before granting access to workspace resources.

---

## 5. What are Security Groups?

**Answer:**

Security Groups are collections of users that simplify permission management.

Instead of assigning permissions to each individual user, permissions are assigned to a group, and all members inherit those permissions.

Example:

```text
Data Engineers
├── User A
├── User B
└── User C
```

All members automatically receive the permissions granted to the **Data Engineers** group.

---

## 6. Why use Security Groups instead of individual users?

**Answer:**

Using Security Groups provides several advantages:

- Simplifies permission management
- Reduces administrative effort
- Ensures consistent access policies
- Makes onboarding and offboarding easier
- Supports enterprise scalability
- Minimizes permission errors
- Follows security best practices

Instead of updating permissions for every user, administrators only manage group membership.

---

## 7. What is Unity Catalog?

**Answer:**

Unity Catalog is the centralized data governance solution for Azure Databricks.

It manages:

- Metadata
- Permissions
- Catalogs
- Schemas
- Tables
- Views
- Volumes
- Data Lineage
- Auditing

Unity Catalog enforces authorization after a user has successfully authenticated through Microsoft Entra ID.

---

## 8. What is the Principle of Least Privilege?

**Answer:**

The Principle of Least Privilege (PoLP) is a security practice that grants users only the minimum permissions required to perform their job.

Benefits include:

- Reduces security risks
- Prevents accidental data modification
- Protects sensitive information
- Simplifies compliance
- Limits unauthorized access

For example, a Data Analyst may receive **SELECT** permission but not **MODIFY** permission on production tables.

---

## 9. How are permissions inherited?

**Answer:**

Permissions in Unity Catalog follow a hierarchical structure.

```text
Catalog
     │
     ▼
Schema
     │
     ▼
Tables
     │
     ▼
Views / Volumes
```

Permissions granted at a higher level can be inherited by lower-level objects, depending on the privilege model and configuration.

This hierarchy simplifies permission management across related data assets.

---

## 10. How does Azure Databricks integrate with Microsoft Entra ID?

**Answer:**

Azure Databricks integrates with Microsoft Entra ID for enterprise authentication and identity management.

The authentication and authorization flow is:

```text
Microsoft Entra ID
        │
        ▼
Authenticate User
        │
        ▼
Azure Databricks Workspace
        │
        ▼
Security Group Membership
        │
        ▼
Unity Catalog Permission Check
        │
        ▼
Access Granted / Access Denied
```

In this integration:

- **Microsoft Entra ID** authenticates the user.
- **Security Groups** determine role membership.
- **Unity Catalog** evaluates permissions.
- **Azure Databricks** grants or denies access to catalogs, schemas, tables, views, and volumes based on those permissions.

```

---

# 📊 Summary

RBAC provides secure, scalable, and centralized access management for Azure Databricks by integrating Microsoft Entra ID, Security Groups, and Unity Catalog. It simplifies administration while ensuring users receive only the permissions required for their roles.

---

# 🎯 Key Takeaways

- RBAC simplifies enterprise security.
- Authentication is handled by Microsoft Entra ID.
- Authorization is enforced by Unity Catalog.
- Security Groups simplify permission management.
- Unity Catalog provides centralized governance.
- Follow least privilege principles.
- Use group-based access control.
- Regularly review permissions.
```

---

# 📚 Next Topic

➡️ [Configure Unity Catalog and Role-Based Access Control (RBAC) in Azure Databricks](02_Unity_Catalog_and_RBAC_Setup.md)
