# ⚙️ SQL Query Execution Order & HAVING

## 🔹 Order of Query Execution

```sql
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```

SQL does **not execute queries in the written order**:

| Step | Clause | Purpose |
|------|--------|---------|
| 1 | FROM | Selects the table |
| 2 | WHERE | Filters rows |
| 3 | GROUP BY | Groups data |
| 4 | HAVING | Filters grouped data |
| 5 | SELECT | Chooses columns |
| 6 | ORDER BY | Sorts the result |

---

## 🔹 Example

```sql
SELECT release_year, COUNT(*) AS movies_count
FROM movies
WHERE imdb_rating > 2
GROUP BY release_year
HAVING COUNT(*) > 3
ORDER BY movies_count DESC;
```

---

## 🔹 HAVING vs WHERE

| Clause | When it filters |
|--------|-----------------|
| WHERE | Before grouping |
| HAVING | After grouping |

### Rules:
- Columns in `HAVING` should be in `SELECT` or aggregated
- `WHERE` can use columns not in `SELECT`

```sql
-- WHERE example
SELECT title FROM movies WHERE imdb_rating > 5;

-- HAVING example
SELECT studio, COUNT(*) AS total
FROM movies
GROUP BY studio
HAVING COUNT(*) > 3;
```

---

## ✅ Summary

| Concept | Purpose |
|---------|---------|
| WHERE | Filter rows |
| GROUP BY | Group data |
| HAVING | Filter groups |
| ORDER BY | Sort results |
```