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

## Summary

| JOIN Type  | Description                  |
| ---------- | ---------------------------- |
| INNER JOIN | Only matching records        |
| LEFT JOIN  | All from left + matches      |
| RIGHT JOIN | All from right + matches     |
| FULL JOIN  | All records from both tables |
| USING      | Simplified join syntax       |
