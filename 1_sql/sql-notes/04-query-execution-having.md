# 📊 SQL Aggregate Functions & GROUP BY

## 🔹 Aggregate Functions

| Function | Meaning | Example |
|----------|---------|---------|
| MAX() | Highest value | `MAX(imdb_rating)` |
| MIN() | Lowest value | `MIN(imdb_rating)` |
| AVG() | Average value | `AVG(imdb_rating)` |

```sql
SELECT
    MAX(imdb_rating) AS highest_rating,
    MIN(imdb_rating) AS lowest_rating,
    AVG(imdb_rating) AS average_rating
FROM movies;
```

---

## 🔹 AS (Alias)

```sql
SELECT AVG(imdb_rating) AS avg_rating FROM movies;
```

---

## 🔹 GROUP BY Clause

```sql
SELECT studio, AVG(imdb_rating) AS avg_rating
FROM movies
GROUP BY studio;
```

---

## 🔹 COUNT with GROUP BY

```sql
SELECT industry, COUNT(*) AS industry_count
FROM movies
GROUP BY industry;
```

---

## 🔹 Multiple Aggregations

```sql
SELECT
    industry,
    MAX(imdb_rating) AS highest_rating,
    MIN(imdb_rating) AS lowest_rating,
    AVG(imdb_rating) AS average_rating
FROM movies
GROUP BY industry;
```

---

## ✅ Summary Table

| Concept | Description |
|---------|-------------|
| MAX() | Returns highest value |
| MIN() | Returns lowest value |
| AVG() | Returns average value |
| AS | Rename column |
| GROUP BY | Group data for aggregation |
| COUNT() | Count rows in each group |
```