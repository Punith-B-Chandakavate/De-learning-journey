# PostgreSQL

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

# 📌 SQL Numerical Queries Cheat Sheet

## 🔹 Basic Numerical Operators

- Used to compare numeric values in SQL conditions

| Operator | Meaning                  | Example            |
| -------- | ------------------------ | ------------------ |
| `<`      | Less than                | imdb_rating < 9    |
| `<=`     | Less than or equal to    | imdb_rating <= 7   |
| `>`      | Greater than             | imdb_rating > 8    |
| `>=`     | Greater than or equal to | imdb_rating >= 8.5 |

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
| `<, >`   | Basic numerical comparisons    |
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


# 📌 SQL Joins – Notes & Examples

## 🔹 Why Multiple Tables?

Companies use multiple tables to store data because:

* Avoid repetition (data redundancy)
* Better organization
* Easier updates and maintenance

---

## 🔹 What is JOIN?

In SQL, a `JOIN` is used to combine data from multiple tables based on a related column.

---

## 🔹 INNER JOIN

Returns only matching records from both tables.

```sql
SELECT 
    m.movie_id, m.title, f.budget, f.revenue, f.currency, f.unit 
FROM movies m 
JOIN financials f 
    ON f.movie_id = m.movie_id;
```

✅ Output: Only common `movie_id` (1,2,3)

---

## 🔹 LEFT JOIN

Returns all records from **movies**, and matched records from financials.

```sql
SELECT 
    m.movie_id, m.title, f.budget, f.revenue, f.currency, f.unit 
FROM movies m 
LEFT JOIN financials f 
    ON f.movie_id = m.movie_id;
```

✅ Output:

* All movies included
* Missing financials → `NULL`

---

## 🔹 RIGHT JOIN

Returns all records from **financials**, and matched records from movies.

```sql
SELECT 
    f.movie_id, m.title, f.budget, f.revenue, f.currency, f.unit 
FROM movies m 
RIGHT JOIN financials f 
    ON f.movie_id = m.movie_id;
```

✅ Output:

* Includes movie_id = 5 (no movie data → NULL)

---

## 🔹 FULL JOIN (Using UNION)

Combines LEFT + RIGHT JOIN results.

```sql
SELECT 
    m.movie_id, m.title, f.budget, f.revenue, f.currency, f.unit 
FROM movies m 
LEFT JOIN financials f 
    ON f.movie_id = m.movie_id

UNION

SELECT 
    f.movie_id, m.title, f.budget, f.revenue, f.currency, f.unit 
FROM movies m 
RIGHT JOIN financials f 
    ON f.movie_id = m.movie_id;
```

---

## 🔹 FULL JOIN (Direct)

Returns all records from both tables.

```sql
SELECT 
    m.movie_id, m.title, f.budget, f.revenue, f.currency, f.unit 
FROM movies m 
FULL JOIN financials f 
    ON f.movie_id = m.movie_id;
```

---

## 🔹 JOIN USING Clause

Cleaner syntax when column names are same.

```sql
SELECT 
    movie_id, title, budget, revenue, currency, unit 
FROM movies m 
JOIN financials f 
USING (movie_id);
```

---

##  Summary

| JOIN Type  | Description                  |
| ---------- | ---------------------------- |
| INNER JOIN | Only matching records        |
| LEFT JOIN  | All from left + matches      |
| RIGHT JOIN | All from right + matches     |
| FULL JOIN  | All records from both tables |
| USING      | Simplified join syntax       |

---

# 📌 Window Functions

## 🔹 What are Window Functions?

Window functions perform calculations across a set of rows related to the current row **without collapsing rows (unlike GROUP BY)**.

-  Each row keeps its identity, but gets additional computed values.

---

## ⚙️ OVER() Clause (Core Concept)

Defines the “window” of rows used for calculation.

* `PARTITION BY` → splits data into groups
* `ORDER BY` → defines order within each group

```sql
SELECT 
    title,
    industry,
    imdb_rating,
    ROW_NUMBER() OVER (PARTITION BY industry ORDER BY imdb_rating DESC) AS rank_in_industry
FROM movies;
```

---

# 🔢 Ranking Functions

## 🔹 ROW_NUMBER()

Assigns a **unique number** to each row within a partition

```sql
SELECT 
    title,
    industry,
    ROW_NUMBER() OVER (PARTITION BY industry ORDER BY imdb_rating DESC) AS row_num
FROM movies;
```

✅ No duplicates, always unique

---

## 🔹 RANK() vs DENSE_RANK()

* `RANK()` → Skips numbers (gaps)
* `DENSE_RANK()` → No gaps

```sql
SELECT 
    title,
    imdb_rating,
    RANK() OVER (ORDER BY imdb_rating DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY imdb_rating DESC) AS dense_rank
FROM movies;
```

📌 Example:

| Rating | RANK | DENSE_RANK |
| ------ | ---- | ---------- |
| 9.0    | 1    | 1          |
| 8.5    | 2    | 2          |
| 8.5    | 2    | 2          |
| 8.0    | 4 ❌  | 3 ✅        |

---

# ⏪ Value Comparison Functions

## 🔹 LAG() and LEAD()

Access previous or next row values

* `LAG()` → Previous row
* `LEAD()` → Next row

```sql
SELECT 
    title,
    release_year,
    imdb_rating,
    LAG(imdb_rating) OVER (ORDER BY release_year) AS prev_rating,
    LEAD(imdb_rating) OVER (ORDER BY release_year) AS next_rating
FROM movies;
```

---

## 📈 Real Use Case (Growth Calculation)

```sql
SELECT 
    movie_id,
    revenue,
    LAG(revenue) OVER (ORDER BY movie_id) AS prev_revenue,
    revenue - LAG(revenue) OVER (ORDER BY movie_id) AS growth
FROM financials;
```

---

# 📊 Aggregate Window Functions

## 🔹 SUM() OVER() — Running Total

```sql
SELECT 
    movie_id,
    revenue,
    SUM(revenue) OVER (ORDER BY movie_id) AS running_revenue
FROM financials;
```

✅  cumulative revenue, sales trends

---

## 🔹 AVG() OVER() — Moving Average

```sql
SELECT 
    movie_id,
    revenue,
    AVG(revenue) OVER (
        ORDER BY movie_id 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg
FROM financials;
```

✅  rolling average (trend smoothing)

---

## 🔹 COUNT() OVER()

```sql
SELECT 
    industry,
    title,
    COUNT(*) OVER (PARTITION BY industry) AS total_movies_in_industry
FROM movies;
```

✅ Adds aggregated info without GROUP BY

---

# 🧠 Value Extraction Functions

## 🔹 FIRST_VALUE() / LAST_VALUE()

```sql
SELECT 
    industry,
    title,
    imdb_rating,
    FIRST_VALUE(title) OVER (PARTITION BY industry ORDER BY imdb_rating DESC) AS top_movie
FROM movies;
```

✅  top performer per group

---

# 📊 Distribution Functions

## 🔹 NTILE() — Bucketing

```sql
SELECT 
    title,
    imdb_rating,
    NTILE(4) OVER (ORDER BY imdb_rating DESC) AS quartile
FROM movies;
```

✅ Divides data into equal groups (e.g., top 25%)

---

## 🔹 CUME_DIST()

```sql
SELECT 
    title,
    imdb_rating,
    CUME_DIST() OVER (ORDER BY imdb_rating DESC) AS distribution
FROM movies;
```

✅ Shows cumulative distribution (percentile-like)

---

## 🔹 PERCENT_RANK()

```sql
SELECT 
    title,
    imdb_rating,
    PERCENT_RANK() OVER (ORDER BY imdb_rating DESC) AS percent_rank
FROM movies;
```

✅ Normalized ranking (0 → 1)

---

# 🔥 Window Frame (Very Important)

Controls which rows are included in calculation

```sql
SELECT 
    movie_id,
    revenue,
    SUM(revenue) OVER (
        ORDER BY movie_id 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_sum
FROM financials;
```

-  Example:

* Current row + previous 2 rows

---


## ✅ Window Functions — Quick Table

| Function       | Description                      |
| -------------- | -------------------------------- |
| ROW_NUMBER()   | Unique row number per partition  |
| RANK()         | Ranking with gaps                |
| DENSE_RANK()   | Ranking without gaps             |
| LAG()          | Previous row value               |
| LEAD()         | Next row value                   |
| SUM() OVER     | Running / cumulative total       |
| AVG() OVER     | Moving / rolling average         |
| COUNT() OVER   | Count without grouping rows      |
| FIRST_VALUE()  | First value in partition         |
| LAST_VALUE()   | Last value in partition          |
| NTILE(n)       | Divide data into n equal buckets |
| CUME_DIST()    | Cumulative distribution (0–1)    |
| PERCENT_RANK() | Relative rank (0–1)              |

---

## ⚙️ OVER() Components

| Clause       | Purpose                     |
| ------------ | --------------------------- |
| PARTITION BY | Divide data into groups     |
| ORDER BY     | Define order within group   |
| ROWS BETWEEN | Define window frame (range) |

---

Here’s a **clean, practical Markdown section based on your movie database** with examples + 1-line explanations + summary 👇

---

# 📌 CTE, Functions & Procedures

## 🔹 CTE (Common Table Expression)

-  *Used to simplify complex queries by breaking them into readable steps*

```sql
WITH high_rated_movies AS (
    SELECT title, imdb_rating
    FROM movies
    WHERE imdb_rating > 8
)
SELECT * FROM high_rated_movies;
```


-  CTE makes queries **clean, readable, and reusable**

---

## 🔹 Multiple CTEs (Chaining)

-  *Used to build step-by-step transformations*

```sql
WITH high_rated AS (
    SELECT * FROM movies WHERE imdb_rating > 8
),
hollywood_movies AS (
    SELECT * FROM high_rated WHERE industry = 'Hollywood'
),
final_output AS (
    SELECT title, imdb_rating FROM hollywood_movies
)
SELECT * FROM final_output;
```

- Multiple CTEs help you **break complex logic into steps**

---

## 🔹 Recursive CTE

- *Used for hierarchical or iterative data*

```sql
WITH RECURSIVE movie_ids AS (
    
    -- Base case (start with smallest movie_id)
    SELECT MIN(movie_id) AS movie_id
    FROM movies

    UNION ALL

    -- Recursive step (next movie_id)
    SELECT movie_id + 1
    FROM movie_ids
    WHERE movie_id < (
        SELECT MIN(movie_id) + 4 FROM movies
    )
)

SELECT * FROM movie_ids;
```


- Recursive CTE is used for **loops and hierarchical data**

---

## 🔹 User-Defined Function (UDF)

- *Used to reuse logic like calculations*

```sql
CREATE OR REPLACE FUNCTION profit(budget INT, revenue REAL)
RETURNS REAL AS $$
BEGIN
    RETURN revenue - budget;
END;
$$ LANGUAGE plpgsql;
```

### Usage:

```sql
SELECT 
    movie_id,
    profit(budget, revenue) AS movie_profit
FROM financials;
```

-  UDF helps you **reuse logic instead of repeating calculations**

---

## 🔹 Stored Procedure

- *Used to execute a set of operations with parameters*

```sql
CREATE OR REPLACE PROCEDURE update_movie_language(
    movie_id INT,
    new_lang INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE movies
    SET language_id = new_lang
    WHERE id = movie_id;
END;
$$;
```

### Call:

```sql
CALL update_movie_language(10, 2);
```

## 🧠 When to Use What

### Use FUNCTION when:

* You need data output
* You want to use it inside queries
* Example:

  * filtering
  * reporting
  * calculations

---

### Use PROCEDURE when:

* You need transactions
* Multiple steps (insert/update/delete)
* Business workflows
* Example:

  * money transfer
  * batch processing

---

## 🚀 Final Verdict

👉 If your goal is:

* “Get movies by language” → ✅ **FUNCTION**

👉 If your goal is:

* “Update/insert/delete with logic” → ✅ **PROCEDURE**

---

# ✅ Summary Table

| Concept          | Example Use Case              | One-line Summary         |
| ---------------- | ----------------------------- | ------------------------ |
| CTE              | Filter high-rated movies      | Makes query readable     |
| Multiple CTE     | Step-by-step filtering        | Breaks complex logic     |
| Recursive CTE    | Generate sequence / hierarchy | Handles loops            |
| UDF              | Profit calculation            | Reusable logic           |
| Stored Procedure | Filter movies by language     | Reusable execution block |

---

# 🚀 Real Data Engineering Usage

* CTE → Data transformations in ETL
* Recursive CTE → Hierarchy (org, categories)
* UDF → Business logic (profit, scoring)
* Stored Procedure → Batch jobs / pipelines

---
