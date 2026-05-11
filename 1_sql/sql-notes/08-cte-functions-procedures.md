
# 📌 CTE, Functions & Procedures

## 🔹 CTE (Common Table Expression)

- *Used to simplify complex queries by breaking them into readable steps*

```sql
WITH high_rated_movies AS (
    SELECT title, imdb_rating
    FROM movies
    WHERE imdb_rating > 8
)
SELECT * FROM high_rated_movies;
```

- CTE makes queries **clean, readable, and reusable**

---

## 🔹 Multiple CTEs (Chaining)

- *Used to build step-by-step transformations*

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

- UDF helps you **reuse logic instead of repeating calculations**

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