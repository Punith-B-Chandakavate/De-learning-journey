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

