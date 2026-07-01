# 🔗 Joins in PySpar

![Spark](https://img.shields.io/badge/Apache-Spark-E25A1C?logo=apachespark&logoColor=white)
![Databricks](https://img.shields.io/badge/Platform-Databricks%20Free%20Edition-red)
![Python](https://img.shields.io/badge/PySpark-Python-yellow)

⬅️ [Back to Handle Missing Values](03_Handle_Missing_Values.md)

# 📚 Table of Contents

- Overview
- Learning Objectives
- Join Architecture
- Sample Customer Data
- Sample Orders Data
- Customer DataFrame
- Orders DataFrame
- Types of Joins in PySpark
- Aliasing DataFrames
- Inner Join
- Duplicate Column Names
- Selecting Required Columns
- Left Join
- Right Join
- Full Outer Join
- Left Semi Join
- Left Anti Join
- Multi-Column Join
- Sorting Joined Data
- Join Summary
- Join Performance Tips
- Interview Questions
- Best Practices
- Key Takeaways

---

# 📖 Overview

A **Join** in PySpark combines rows from two or more DataFrames based on one or more common columns.

Joins are one of the most frequently used operations in Data Engineering for combining data from multiple sources.

For example:

- Customers + Orders
- Employees + Departments
- Products + Sales
- Students + Courses

In this tutorial, we'll use **customer_id** as the common column between two DataFrames.

---

# 🎯 Learning Objectives

After completing this tutorial, you will learn:

- Create sample DataFrames
- Understand different join types
- Perform Inner Join
- Perform Left Join
- Perform Right Join
- Perform Full Outer Join
- Handle duplicate column names
- Clean joined DataFrames

---

# 🏗 Join Architecture

```text
Customers DataFrame              Orders DataFrame

customer_id                      customer_id
name                             order_id
country                          amount
vip                              country

        │
        │
        ▼

      Join on customer_id

        │
        ▼

Combined DataFrame
````

---

# 📂 Sample Customer Data

```python
from pyspark.sql import functions as F, types as T

rows_customers = [
    (1,"Asha","IN",True),
    (2,"Bob","US",False),
    (3,"Chen","CN",True),
    (4,"Diana","US",None),
    (None,"Ghost","UK",False)
]
```

---

# 📂 Sample Orders Data

```python
rows_orders = [
    (101,1,120.0,"IN"),
    (102,1,80.0,"IN"),
    (103,2,50.0,"US"),
    (104,5,30.0,"DE"),
    (105,3,200.0,"CN"),
    (106,None,15.0,"UK"),
    (107,3,40.0,"CN"),
    (108,2,75.0,"US"),
]
```

---

# 📋 Customer DataFrame

| customer_id | name  | country | vip   |
| ----------- | ----- | ------- | ----- |
| 1           | Asha  | IN      | True  |
| 2           | Bob   | US      | False |
| 3           | Chen  | CN      | True  |
| 4           | Diana | US      | NULL  |
| NULL        | Ghost | UK      | False |

---

# 📋 Orders DataFrame

| order_id | customer_id | amount | country |
| -------- | ----------: | -----: | ------- |
| 101      |           1 |    120 | IN      |
| 102      |           1 |     80 | IN      |
| 103      |           2 |     50 | US      |
| 104      |           5 |     30 | DE      |
| 105      |           3 |    200 | CN      |
| 106      |        NULL |     15 | UK      |
| 107      |           3 |     40 | CN      |
| 108      |           2 |     75 | US      |

---

# 🤝 Types of Joins in PySpark

PySpark supports multiple join types.

| Join Type       | Description                                                               |
| --------------- | ------------------------------------------------------------------------- |
| Inner Join      | Returns matching rows from both DataFrames                                |
| Left Join       | Returns all rows from the left DataFrame and matching rows from the right |
| Right Join      | Returns all rows from the right DataFrame and matching rows from the left |
| Full Outer Join | Returns all rows from both DataFrames                                     |
| Left Semi Join  | Returns matching rows from the left DataFrame only                        |
| Left Anti Join  | Returns non-matching rows from the left DataFrame                         |
| Cross Join      | Cartesian Product                                                         |

---

# 🔥 Aliasing DataFrames

Aliasing makes joins easier to read.

```python
o = df_orders.alias("o")
c = df_customers.alias("c")
```

---

# 🔹 Inner Join

## What is an Inner Join?

An **Inner Join** returns only the rows where the join key exists in **both** DataFrames.

```text
Customers      Orders

1  ✓            1 ✓
2  ✓            2 ✓
3  ✓            3 ✓
4              5

Result

1
2
3
```

---

## Syntax

```python
df_inner = o.join(
    c,
    on="customer_id",
    how="inner"
)

df_inner.show()
```

---

# 📊 Expected Output

| customer_id | order_id | amount | country | name | country | vip   |
| ----------- | -------- | -----: | ------- | ---- | ------- | ----- |
| 1           | 101      |    120 | IN      | Asha | IN      | True  |
| 1           | 102      |     80 | IN      | Asha | IN      | True  |
| 2           | 103      |     50 | US      | Bob  | US      | False |
| 3           | 105      |    200 | CN      | Chen | CN      | True  |
| 3           | 107      |     40 | CN      | Chen | CN      | True  |
| 2           | 108      |     75 | US      | Bob  | US      | False |

Only matching customer IDs are returned.

---

# ⚠ Duplicate Column Names

Notice both DataFrames contain a **country** column.

Output becomes

```text
country
country
```

which is confusing.

---

# ✅ Selecting Required Columns

Use aliases to avoid duplicate column names.

```python
df_inner_clean = (
    o.join(c, on="customer_id", how="inner")
     .select(
        "customer_id",
        "order_id",
        "amount",
        F.col("o.country").alias("ship_country"),
        "name",
        F.col("c.country").alias("cust_country"),
        "vip"
     )
)
```

---

# 📊 Expected Output

| customer_id | order_id | amount | ship_country | name | cust_country | vip   |
| ----------- | -------- | -----: | ------------ | ---- | ------------ | ----- |
| 1           | 101      |    120 | IN           | Asha | IN           | True  |
| 1           | 102      |     80 | IN           | Asha | IN           | True  |
| 2           | 103      |     50 | US           | Bob  | US           | False |
| 3           | 105      |    200 | CN           | Chen | CN           | True  |
| 3           | 107      |     40 | CN           | Chen | CN           | True  |
| 2           | 108      |     75 | US           | Bob  | US           | False |

---

# 🔹 Left Join

## What is a Left Join?

A **Left Join** returns:

* Every row from the **left DataFrame**
* Matching rows from the right DataFrame
* NULL where no match exists

```python
display(
    o.join(
        c,
        on="customer_id",
        how="left"
    )
)
```

---

# 📊 Expected Output

| customer_id | order_id | amount | country | name | country | vip   |
| ----------- | -------- | -----: | ------- | ---- | ------- | ----- |
| 1           | 101      |    120 | IN      | Asha | IN      | True  |
| 1           | 102      |     80 | IN      | Asha | IN      | True  |
| 2           | 103      |     50 | US      | Bob  | US      | False |
| 5           | 104      |     30 | DE      | NULL | NULL    | NULL  |
| 3           | 105      |    200 | CN      | Chen | CN      | True  |
| NULL        | 106      |     15 | UK      | NULL | NULL    | NULL  |
| 3           | 107      |     40 | CN      | Chen | CN      | True  |
| 2           | 108      |     75 | US      | Bob  | US      | False |

Notice:

* Customer **5** has no customer record.
* NULL customer_id does not match NULL.

---

# 🔹 Right Join

## What is a Right Join?

A **Right Join** returns:

* Every row from the **right DataFrame**
* Matching rows from the left DataFrame
* NULL when no matching order exists

```python
display(
    o.join(
        c,
        on="customer_id",
        how="right"
    )
)
```

---

# 📊 Expected Output

| customer_id | order_id | amount | country | name  | country | vip   |
| ----------- | -------- | -----: | ------- | ----- | ------- | ----- |
| 1           | 101      |    120 | IN      | Asha  | IN      | True  |
| 1           | 102      |     80 | IN      | Asha  | IN      | True  |
| 2           | 103      |     50 | US      | Bob   | US      | False |
| 2           | 108      |     75 | US      | Bob   | US      | False |
| 3           | 105      |    200 | CN      | Chen  | CN      | True  |
| 3           | 107      |     40 | CN      | Chen  | CN      | True  |
| 4           | NULL     |   NULL | NULL    | Diana | US      | NULL  |
| NULL        | NULL     |   NULL | NULL    | Ghost | UK      | False |

Notice:

Customer **4** has no orders.

---

# 🔹 Full Outer Join

## What is a Full Join?

A Full Join returns:

* All matching rows
* All unmatched rows from the left DataFrame
* All unmatched rows from the right DataFrame

```python
display(
    o.join(
        c,
        on="customer_id",
        how="full"
    )
)
```

---

# 📊 Expected Output

| customer_id | order_id | amount | country | name  | country | vip   |
| ----------- | -------- | -----: | ------- | ----- | ------- | ----- |
| 1           | 101      |    120 | IN      | Asha  | IN      | True  |
| 1           | 102      |     80 | IN      | Asha  | IN      | True  |
| 2           | 103      |     50 | US      | Bob   | US      | False |
| 2           | 108      |     75 | US      | Bob   | US      | False |
| 3           | 105      |    200 | CN      | Chen  | CN      | True  |
| 3           | 107      |     40 | CN      | Chen  | CN      | True  |
| 5           | 104      |     30 | DE      | NULL  | NULL    | NULL  |
| NULL        | 106      |     15 | UK      | NULL  | NULL    | NULL  |
| 4           | NULL     |   NULL | NULL    | Diana | US      | NULL  |
| NULL        | NULL     |   NULL | NULL    | Ghost | UK      | False |

---

# 🔹 Left Semi Join

## What is a Left Semi Join?

A **Left Semi Join** returns only the rows from the **left DataFrame** that have a matching row in the right DataFrame.

Unlike an Inner Join, it **does not return columns from the right DataFrame**.

### Use Cases

- Check whether records exist
- Filtering data
- Existence checks

---

## Syntax

```python
display(
    o.join(
        c,
        on="customer_id",
        how="left_semi"
    )
)
```

---

## Expected Output

| customer_id | order_id | amount | country |
|-------------|----------|-------:|---------|
|1|101|120|IN|
|1|102|80|IN|
|2|103|50|US|
|3|105|200|CN|
|3|107|40|CN|
|2|108|75|US|

Only matching rows from **Orders** are returned.

---

# 🔹 Left Anti Join

## What is a Left Anti Join?

A **Left Anti Join** returns only the rows from the **left DataFrame** that do **not** have a matching row in the right DataFrame.

### Use Cases

- Find unmatched records
- Data Quality Checks
- Missing Master Data

---

## Syntax

```python
display(
    o.join(
        c,
        on="customer_id",
        how="left_anti"
    )
)
```

---

## Expected Output

| customer_id | order_id | amount | country |
|-------------|----------|-------:|---------|
|5|104|30|DE|
|NULL|106|15|UK|

Customer **5** doesn't exist in Customers.

NULL keys never match.

---

# 🔹 Multi-Column Join

Sometimes a single column is not sufficient for joining datasets.

PySpark allows joining using multiple columns.

---

## Syntax

```python
df_multi = o.join(
    c,
    on=["customer_id", "country"],
    how="inner"
)

display(df_multi)
```

---

## Expected Output

| customer_id | country | order_id | amount | name | vip |
|-------------|----------|---------:|-------:|------|------|
|1|IN|101|120|Asha|True|
|1|IN|102|80|Asha|True|
|2|US|103|50|Bob|False|
|2|US|108|75|Bob|False|
|3|CN|105|200|Chen|True|
|3|CN|107|40|Chen|True|

Both **customer_id** and **country** must match.

---

# 🔹 Sorting Joined Data

Spark allows sorting after joining.

---

## Descending Order

```python
df_multi.orderBy(
    F.col("customer_id").desc()
)
```

---

## Expected Output

| customer_id | country | order_id |
|-------------|----------|---------:|
|3|CN|105|
|3|CN|107|
|2|US|103|
|2|US|108|
|1|IN|101|
|1|IN|102|

---

## Using ascending=False

```python
df_multi.orderBy(
    "customer_id",
    ascending=False
)
```

Produces the same result.

---

## Multiple Sorting Columns

```python
df_multi.orderBy(
    F.col("customer_id").desc(),
    F.col("country").asc()
)
```

---

## Expected Output

| customer_id | country | order_id |
|-------------|----------|---------:|
|3|CN|105|
|3|CN|107|
|2|US|103|
|2|US|108|
|1|IN|101|
|1|IN|102|

---

# 📊 Join Summary

| Join Type | Returns |
|------------|---------|
| Inner | Matching rows from both DataFrames |
| Left | All rows from left + matching rows from right |
| Right | All rows from right + matching rows from left |
| Full | All rows from both DataFrames |
| Left Semi | Matching rows from left only |
| Left Anti | Non-matching rows from left only |

---

# ⚡ Join Performance Tips

Large joins can be expensive because Spark performs **shuffle operations** across the cluster.

To improve performance:

### ✅ Filter Before Joining

Reduce the amount of data before performing joins.

```python
filtered_orders = df_orders.filter(
    F.col("amount") > 50
)
```

---

### ✅ Select Only Required Columns

Avoid joining unnecessary columns.

```python
customers = df_customers.select(
    "customer_id",
    "name"
)
```

---

### ✅ Broadcast Small Tables

Broadcast small lookup tables to avoid shuffle.

```python
from pyspark.sql.functions import broadcast

result = df_orders.join(
    broadcast(df_customers),
    "customer_id"
)
```

---

### ✅ Repartition Large DataFrames

```python
df_orders = df_orders.repartition(8)
```

Helps distribute data evenly across partitions.

---

### ✅ Cache Frequently Used DataFrames

```python
df_customers.cache()
```

---

### ✅ Inspect Execution Plan

```python
df_inner.explain(True)
```

Useful for identifying:

- Shuffle operations
- Broadcast joins
- Scan types
- Join strategy

---


---

# 💼 PySpark Join Interview Questions

## 1. What is a Join in PySpark?

A Join combines rows from two DataFrames based on one or more common columns.

---

## 2. What are the different join types?

- Inner
- Left
- Right
- Full
- Left Semi
- Left Anti
- Cross

---

## 3. What is an Inner Join?

Returns only matching rows from both DataFrames.

---

## 4. What is a Left Join?

Returns every row from the left DataFrame and matching rows from the right DataFrame.

---

## 5. What is a Right Join?

Returns every row from the right DataFrame and matching rows from the left DataFrame.

---

## 6. What is a Full Join?

Returns all rows from both DataFrames, whether matched or unmatched.

---

## 7. What is a Left Semi Join?

Returns only matching rows from the left DataFrame without including columns from the right DataFrame.

---

## 8. What is a Left Anti Join?

Returns rows from the left DataFrame that have no matching rows in the right DataFrame.

---

## 9. Can Spark join on multiple columns?

Yes.

Example:

```python
df1.join(
    df2,
    ["customer_id", "country"],
    "inner"
)
```

---

## 10. Why use aliases?

Aliases prevent ambiguity when DataFrames contain columns with the same name.

Example:

```python
o = df_orders.alias("o")
c = df_customers.alias("c")
```

---

## 11. Why do NULL values not match in joins?

Spark follows SQL semantics where `NULL` represents an unknown value, so `NULL = NULL` evaluates to unknown rather than true.

---

## 12. What is a Broadcast Join?

A Broadcast Join sends a small DataFrame to all worker nodes to avoid expensive shuffle operations.

---

## 13. How can you improve join performance?

- Filter data early
- Broadcast small tables
- Repartition large DataFrames
- Cache reusable DataFrames
- Select only required columns

---

## 14. How do you analyze a join execution plan?

```python
df.explain(True)
```

---

## 15. Which join is commonly used in Data Engineering?

- Inner Join
- Left Join
- Left Anti Join
- Left Semi Join

These are the most common join types used in ETL pipelines.

---


# 🏆 Best Practices

Follow these best practices to write efficient, readable, and scalable join operations in PySpark.

- ✅ Choose the appropriate join type based on your business requirements.
- ✅ Filter data before joining to reduce the amount of data processed.
- ✅ Select only the required columns after performing a join.
- ✅ Use DataFrame aliases (`alias()`) to improve readability and avoid column ambiguity.
- ✅ Rename duplicate columns using `alias()` or `withColumnRenamed()`.
- ✅ Use meaningful column names in the final output.
- ✅ Broadcast small lookup tables to improve join performance and reduce shuffling.
- ✅ Avoid joining on `NULL` keys, as `NULL` values do not match in standard Spark joins.
- ✅ Use multi-column joins only when a single key is insufficient.
- ✅ Cache frequently reused DataFrames to avoid repeated computations.
- ✅ Analyze query execution plans using `explain()` to identify performance bottlenecks.
- ✅ Repartition large DataFrames when necessary to balance data distribution across partitions.
- ✅ Inspect the schema after joins to verify column names and data types.
- ✅ Avoid unnecessary joins on very large DataFrames to minimize shuffle operations.

---

# 🎯 Key Takeaways

- PySpark joins combine data from multiple DataFrames using one or more common columns.
- **Inner Join** returns only the matching records from both DataFrames.
- **Left Join** returns all records from the left DataFrame and matching records from the right DataFrame.
- **Right Join** returns all records from the right DataFrame and matching records from the left DataFrame.
- **Full Outer Join** returns all matching and non-matching records from both DataFrames.
- **Left Semi Join** returns only the matching rows from the left DataFrame without including columns from the right DataFrame.
- **Left Anti Join** returns rows from the left DataFrame that have no matching records in the right DataFrame.
- Multi-column joins provide more accurate matching when a single column is not sufficient.
- Spark follows SQL semantics, so `NULL` values do not match other `NULL` values during joins.
- Broadcast joins significantly improve performance when joining large DataFrames with small lookup tables.
- Optimizing joins using filtering, partitioning, caching, and execution plan analysis helps build efficient and scalable ETL pipelines.

---

# 🚀 Next Steps

➡️ [Readinf Spark Plan wihr explain](05_Joins_in_Spark.md)
