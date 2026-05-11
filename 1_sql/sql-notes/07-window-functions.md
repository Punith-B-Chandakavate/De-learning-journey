
# 📌 Value Comparison Functions

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

- Example:

* Current row + previous 2 rows

---

# ✅ Window Functions — Quick Table

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
| CUME_DIST()    | Cumulative distribution (0–1)   |
| PERCENT_RANK() | Relative rank (0–1)             |

---

# ⚙️ OVER() Components

| Clause       | Purpose                     |
| ------------ | --------------------------- |
| PARTITION BY | Divide data into groups     |
| ORDER BY     | Define order within group   |
| ROWS BETWEEN | Define window frame (range) |

---
