# PostgreSQL

# 📌SQL Basic Cheat Sheet

## 🔹 Basic SQL Clauses

- `SELECT`, `FROM`, and `WHERE` are the core SQL statements.

---

## 🔹 Select All Columns

- `*` means select all columns from a table

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

# 📌 SQL Numerical Queries Cheat Sheet

## 🔹 Basic Numerical Operators

- Used to compare numeric values in SQL conditions

| Operator | Meaning                  | Example            |
| -------- | ------------------------ | ------------------ |
| `<`    | Less than                | imdb_rating < 9    |
| `<=`   | Less than or equal to    | imdb_rating <= 7   |
| `>`    | Greater than             | imdb_rating > 8    |
| `>=`   | Greater than or equal to | imdb_rating >= 8.5 |

```sql
SELECT * FROM movies
WHERE imdb_rating > 9;
```

---

## 🔹 Logical Operators

- Combine multiple conditions in a query

### AND

- Returns rows where **all conditions are true**

```sql
SELECT * FROM movies
WHERE imdb_rating > 8 AND imdb_rating < 9;
```

### OR

- Returns rows where **at least one condition is true**

```sql
SELECT * FROM movies
WHERE imdb_rating > 8.5 OR imdb_rating < 9;
```

---

## 🔹 BETWEEN Operator

- Returns values within a given range (inclusive)

```sql
SELECT * FROM movies
WHERE imdb_rating BETWEEN 7 AND 9.5;
```

---

## 🔹 IN Operator

- Matches values from a list (alternative to multiple OR)

```sql
SELECT * FROM movies
WHERE imdb_rating IN (8.2, 8.5, 9);
```

---

## 🔹 ORDER BY Clause

- Sorts the result set (default is ascending)

```sql
SELECT * FROM movies
ORDER BY imdb_rating ASC;
```

```sql
SELECT * FROM movies
ORDER BY imdb_rating DESC;
```

---

## 🔹 LIMIT Clause

- Limits the number of rows returned

```sql
SELECT * FROM movies
LIMIT 5;
```

---

## 🔹 OFFSET Clause

- Skips a specified number of rows

```sql
SELECT * FROM movies
LIMIT 5 OFFSET 10;
```

---

## ✅ Summary

| Concept  | Description                    |
| -------- | ------------------------------ |
| `<, >` | Basic numerical comparisons    |
| AND      | All conditions must be true    |
| OR       | At least one condition is true |
| BETWEEN  | Range filter (inclusive)       |
| IN       | Match multiple values          |
| ORDER BY | Sort results                   |
| LIMIT    | Restr number of rows           |
| OFFSET   | Skip rows                      |

---

# 📌 SQL Summary Analytics Cheat Sheet

## 🔹 Aggregate Functions

- Used to summarize data for analysis

| Function | Meaning       | Example          |
| -------- | ------------- | ---------------- |
| MAX()    | Highest value | MAX(imdb_rating) |
| MIN()    | Lowest value  | MIN(imdb_rating) |
| AVG()    | Average value | AVG(imdb_rating) |

```sql
SELECT
    MAX(imdb_rating) AS highest_rating,
    MIN(imdb_rating) AS lowest_rating,
    AVG(imdb_rating) AS average_rating
FROM movies;
```

---

## 🔹 AS (Alias)

- Used to rename columns in the output

```sql
SELECT
    AVG(imdb_rating) AS avg_rating
FROM movies;
```

---

## 🔹 GROUP BY Clause

- Groups rows and applies aggregate functions on each group

```sql
SELECT
    studio,
    AVG(imdb_rating) AS avg_rating
FROM movies
GROUP BY studio;
```

---

## 🔹 COUNT with GROUP BY

- Counts number of rows in each group

```sql
SELECT
    industry,
    COUNT(*) AS industry_count
FROM movies
GROUP BY industry;
```

---

## 🔹 Multiple Aggregations

- Apply multiple summary functions together

```sql
SELECT
    industry,
    MAX(imdb_rating) AS highest_rating,
    MIN(imdb_rating) AS lowest_rating,
    AVG(imdb_rating) AS average_rating
FROM movies;
GROUP BY industry;
```

---

## ✅ Summary

| Concept  | Description                |
| -------- | -------------------------- |
| MAX()    | Returns highest value      |
| MIN()    | Returns lowest value       |
| AVG()    | Returns average value      |
| AS       | Rename column              |
| GROUP BY | Group data for aggregation |
| COUNT()  | Count rows in each group   |

---

# 📌 SQL Takeaways

## 🔹Order of Query Execution

```sql
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```

SQL does **not execute queries in the written order**. Instead:

- `FROM`: selects the table
- `WHERE`: filters rows
- `GROUP BY`: groups data
- `HAVING`: filters grouped data
- `SELECT`: chooses columns
- `ORDER BY`: sorts the result

```sql
SELECT release_year, COUNT(*) AS movies_count
FROM movies
WHERE imdb_rating > 2
GROUP BY department
HAVING movies_count > 3
ORDER BY movies_count DESC;
```

---

## 🔹GROUP BY and HAVING Together

- `GROUP BY` groups rows based on a column
- `HAVING` filters those groups (like `WHERE`, but for groups)

```sql
SELECT release_year,  AVG(imdb_rating) AS avg_rating
FROM movies
GROUP BY release_year
HAVING avg_rating > 3;
```

👉 This shows only release_year where the average imdb_rating is greater than 3.

---

## 🔹HAVING vs WHERE

- `WHERE`: filters rows **before grouping**
- `HAVING`: filters results **after grouping**

### Rule

- Columns in `HAVING` should usually be in `SELECT` or aggregated
- `WHERE` can use columns not in `SELECT`

```sql
-- WHERE example
SELECT title
FROM movies
WHERE imdb_rating > 5;

-- HAVING example
SELECT studio, COUNT(*) AS total
FROM movies
GROUP BY studio
HAVING COUNT(*) > 3;
```

---

## 🔹Derived Columns

Create new columns using existing data.

```sql
select *, year(curdate()) - birth_year as age from actors;
```

---

## 🔹Profit

```sql
select *,
    (revenue - budget) as profit
from financials;
```

---

## 🔹Currency / Unit Conversion

Used for business transformations like currency or unit conversion.

```sql
SELECT revenue,
       revenue * 83 AS price_in_inr
FROM financials;
```

---

## 🔹IF Function

Used for simple conditions (mostly MySQL).

```sql
select *,
     if (currency = 'USD', revenue * 77, revenue) as revenue_inr
from financials;
```

---

## 🔹CASE WHEN (Multiple Conditions)

Use when handling multiple conditions.

```sql
select *,
	case
	    when unit='thosands' then revenue/1000
	    when unit='billinos' then revenue*1000
            else revenue
	END AS revenue_mln
from financials;
```

---

## ✅ Summary

| Concept          | Purpose             |
| ---------------- | ------------------- |
| WHERE            | Filter rows         |
| GROUP BY         | Group data          |
| HAVING           | Filter groups       |
| Derived Columns  | Create new values   |
| Revenue / Profit | Business metrics    |
| Conversion       | Transform data      |
| IF               | Simple condition    |
| CASE             | Multiple conditions |

---
