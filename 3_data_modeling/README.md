# 🏗️ Data Modeling & Data Warehouse Concepts (Movies Database)

## 📌 What is Data Modeling (ERD)?

👉 Data modeling is the process of designing how data is structured, stored, and related in a database.

![ERD Diagram](/diagrams/erd.png)

---

## 🎬 Your Database Mapping (Real Example)

This ERD represents your database:

* `movies` → main table (movie details)
* `actors` → actor information
* `movie_actor` → bridge table (many-to-many relationship)
* `financials` → budget & revenue
* `languages` → language details

---

## 🔗 Relationships

```text
movies --------< movie_actor >-------- actors
   |                                     
   |                                     
financials                         
   |
languages
```

---

## 🧠 One-line Understanding

👉 *“Data modeling = how tables connect and how data flows between them”*

---

# 📌 Table Breakdown

## 🎬 movies (Main Table)

```text
movie_id (PK)
title
industry
release_year
imdb_rating
studio
language_id (FK)
```

---

## 🎭 actors

```text
actor_id (PK)
name
birth_year
```

---

## 🔗 movie_actor (Bridge Table)

```text
movie_id (FK)
actor_id (FK)
```

👉 Handles **many-to-many relationship**
(one movie → many actors, one actor → many movies)

---

## 💰 financials

```text
movie_id (FK)
budget
revenue
unit
currency
```

👉 Contains **metrics (Fact-like table)**

---

## 🌐 languages

```text
language_id (PK)
name
```

---

# ⭐ Fact vs Dimension (Your Database)

## 📊 Fact Table

```text
financials
```

👉 Stores measurable data (budget, revenue)

---

## 📂 Dimension Tables

```text
movies
actors
languages
```

👉 Stores descriptive information

---

🧠 One-line:
👉 *“Fact = numbers, Dimension = context”*

---

# ⭐ Star Schema (Your DB Conversion)

If converted to Data Warehouse:

```text
              dim_language
                    |
dim_actor — fact_movie_performance — dim_movie
```

---

## 📊 Fact Table (Warehouse)

```text
fact_movie_performance
----------------------
movie_id
budget
revenue
```

---

## 📂 Dimensions

```text
dim_movie
dim_actor
dim_language
```

---

🧠 One-line:
👉 *“Star schema = optimized for analytics queries”*

---

# ❄️ Snowflake Schema (Your DB)

If normalized further:

```text
dim_movie → dim_language
```

👉 Already partially normalized in your DB

---

🧠 One-line:
👉 *“Snowflake = normalized dimensions, more joins”*

---

# 📊 ERD (Your Database)

```text
movies ----< movie_actor >---- actors
   |
financials
   |
languages
```

---

🧠 One-line:
👉 *“ERD = visual representation of table relationships”*

---

# 🔄 SCD Example (Using Your Data)

## 🔹 Type 1

```text
Movie studio updated → old value lost
```

---

## 🔹 Type 2

```text
movie_id | studio        | start_date | end_date
101      | Old Studio    | 2020       | 2023
101      | New Studio    | 2023       | NULL
```

---

🧠 One-line:
👉 *“Type 2 keeps history of changes”*

---

# 🧠 Final Summary

| Concept          | Your DB Example                |
| ---------------- | ------------------------------ |
| Fact Table       | financials                     |
| Dimension Tables | movies, actors, languages      |
| Bridge Table     | movie_actor                    |
| Relationship     | Many-to-many (movies ↔ actors) |
| ERD              | Table connections              |
| Star Schema      | Analytics optimized            |
| Snowflake        | Normalized structure           |

---

# ⚡ Final Insight

👉 *“Your current DB is OLTP-style → can be converted to Star Schema for analytics”*

---