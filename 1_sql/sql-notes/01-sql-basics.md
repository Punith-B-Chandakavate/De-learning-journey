
# 📌SQL Basic Cheat Sheet

## 🔹 Basic SQL Clauses

- `SELECT`, `FROM`, and `WHERE` are the core SQL statements.

---

## 🔹 Select All Columns

- means select all columns from a table

```sql
SELECT * FROM movies;
```

---

## 🔹 Select a Database

- Use `USE` to choose a database (MySQL)

```sql
USE my_database;
```

> ⚠️ Note: PostgreSQL does not use `USE`

---

## 🔹 COUNT Function

- Returns the number of rows

```sql
SELECT COUNT(*) FROM movies;
```

---

## 🔹 DISTINCT Function

- Returns unique values from a column

```sql
SELECT DISTINCT genre FROM movies;
```

---

## 🔹 Wildcard `%`

- `%` represents any sequence of characters

Examples:

- `%thor%` → contains "thor"
- `thor%` → starts with "thor"
- `%thor` → ends with "thor"

---

## 🔹 LIKE Operator

- Used for pattern matching

```sql
SELECT * FROM movies WHERE title LIKE '%thor%';
```

---

## 🔹 Case-Insensitive Search (PostgreSQL)

- Use `ILIKE`

```sql
SELECT * FROM movies WHERE title ILIKE '%thor%';
```

---

## ⚠️ Important Notes

- Use `'single quotes'` for strings
- `"double quotes"` are for column/table names in PostgreSQL

---

## ✅ Summary

| Concept  | Description      |
| -------- | ---------------- |
| SELECT   | Choose columns   |
| FROM     | Choose table     |
| WHERE    | Filter rows      |
| LIKE     | Pattern matching |
| %        | Wildcard         |
| COUNT()  | Count rows       |
| DISTINCT | Unique values    |

---
