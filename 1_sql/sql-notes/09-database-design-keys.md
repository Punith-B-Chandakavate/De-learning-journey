# 🗄️ Database Design & Updates

Database design is a critical step in creating a database. It usually consists of three stages:

### 1. Conceptual Model

Defines the overall structure and requirements of the database.

### 2. Entity Relationship Diagram (ERD)

Visually represents entities, attributes, and relationships between tables.

### 3. Database Schema

Defines the actual database structure, including:

- Tables
- Columns
- Data Types
- Constraints
- Relationships

---

## 🔄 Database Normalization

Database normalization is the process of organizing data in a database to:

- Reduce data duplication
- Improve data integrity
- Maintain consistency

## ✅ Data Integrity

Data integrity refers to the accuracy and consistency of data throughout its lifecycle.

---

## 🔗 Link Table

A **Link Table** (also called a **Junction Table**) is used to create relationships between two tables, especially in **many-to-many relationships**.

### 📍 Example

A `students` table and a `courses` table can be connected using a `student_courses` link table.

---

## 🏗️ Creating a Database from an ERD

### ▶️ Forward Engineering

Creating a database from a data model or ERD.

```
ERD / Data Model → Database
```

### ◀️ Reverse Engineering

Creating a data model or ERD from an existing database.

```
Database → ERD / Data Model
```

---

## 🛠️ Tools for Creating ERD Diagrams

Some popular tools for designing ERD diagrams are:

- 🐬 MySQL Workbench
- 🎨 Lucidchart
- ✏️ Draw.io
- 📊 dbdiagram.io
- 📘 Microsoft Visio

---