# 🏗️ SQL in Spark (Spark SQL)

![Spark](https://img.shields.io/badge/Apache-Spark-E25A1C?logo=apachespark&logoColor=white)
![Databricks](https://img.shields.io/badge/Platform-Databricks%20Free%20Edition-red)
![SQL](https://img.shields.io/badge/SQL-Query_Language-blue)
![Python](https://img.shields.io/badge/PySpark-Python-yellow)

⬅️ [Back to Handle Missing Values](03_Handle_Missing_Values.md)

# 📚 Table of Contents

- Overview
- Why Spark SQL?
- Spark SQL Architecture
- Ways to Execute SQL in Spark
  - spark.sql()
  - SQL Notebook Cell (%sql)
- Sample Output
- Creating a DataFrame
- Sample Dataset
- Temporary Views
- Global Temporary Views
- Session View vs Global Temporary View
- Query Example-. Expected Output
- Aggregation Example
- Expected Aggregation Output
- Common SQL Operations in Spark
  - SELECT
  - FILTER
  - ORDER BY
  - GROUP BY
  - Aggregate Functions
  - NULL Handling
  - Multiple Conditions
- When to Use Spark SQL?
- Spark SQL vs Traditional SQL
- Spark SQL Interview Questions
-  Best Practices
- Key Takeaways

---

# 📖 Overview

**SQL (Structured Query Language)** is the standard language used to query, manipulate, and manage data stored in relational databases.

**Spark SQL** is Apache Spark's built-in SQL engine that allows developers and data engineers to execute SQL queries on:

- 📊 Spark DataFrames
- 📂 Delta Tables
- 📁 Managed Tables
- ☁️ External Tables
- 🗄️ Temporary Views

Spark SQL combines the simplicity of SQL with the distributed processing power of Apache Spark.

---

# 🚀 Why Spark SQL?

Spark SQL allows SQL developers to analyze massive datasets without learning the DataFrame API.

### Benefits

- ⚡ Distributed SQL execution
- 📈 Handles Big Data efficiently
- 🔄 Integrates with DataFrames
- ☁️ Works seamlessly with Delta Lake
- 💾 Supports Parquet, JSON, CSV, ORC and more
- 🧠 Catalyst Query Optimizer automatically optimizes SQL queries

---

# 🏗️ Spark SQL Architecture

```text
CSV / Parquet / Delta
          │
          ▼
     Spark DataFrame
          │
createOrReplaceTempView()
          │
          ▼
      Spark SQL Engine
          │
          ▼
   Optimized Execution
          │
          ▼
     Query Results
```

---

# 📂 Ways to Execute SQL in Spark

Spark supports SQL execution using two methods.

## 1️⃣ spark.sql()

Execute SQL from Python.

```python
query = """
SELECT *
FROM workspace.default.movies
WHERE studio='Marvel Studios'
"""

df = spark.sql(query)
df.show(truncate=False)
```

---

## 2️⃣ SQL Notebook Cell

Databricks notebooks support SQL directly using

```sql
%sql

SELECT *
FROM workspace.default.movies
WHERE studio='Marvel Studios';
```

---

# 📊 Sample Output

| Title                                       | Studio         | IMDB |
| ------------------------------------------- | -------------- | ---- |
| Doctor Strange in the Multiverse of Madness | Marvel Studios | 7.0  |
| Thor: Ragnarok                              | Marvel Studios | 7.9  |
| Avengers: Endgame                           | Marvel Studios | 8.4  |
| Avengers: Infinity War                      | Marvel Studios | 8.4  |
| Captain America: The Winter Soldier         | Marvel Studios | 7.8  |

---

# 📁 Creating a DataFrame

```python
from pyspark.sql import functions as F

data = [
    ("2017-01-01",32.0,6.0,"Rain"),
    ("2017-01-04",None,9.0,"Sunny"),
    ("2017-01-05",28.0,None,"Snow"),
    ("2017-01-06",None,7.0,None),
    ("2017-01-07",32.0,None,"Rain"),
    ("2017-01-08",None,None,"Sunny"),
    ("2017-01-09",None,None,None),
    ("2017-01-10",34.1,8.1,"Cloudy"),
    ("2017-01-11",40.0,12.0,"Sunny")
]

schema="""
day string,
temperature double,
windspeed double,
event string
"""

df=spark.createDataFrame(data,schema)

df=df.withColumn(
    "day",
    F.to_date("day","yyyy-MM-dd")
)

display(df)
```

---

# 📊 Dataset

| Day        | Temperature | Wind Speed | Event  |
| ---------- | ----------: | ---------: | ------ |
| 2017-01-01 |          32 |          6 | Rain   |
| 2017-01-04 |        null |          9 | Sunny  |
| 2017-01-05 |          28 |       null | Snow   |
| 2017-01-06 |        null |          7 | null   |
| 2017-01-07 |          32 |       null | Rain   |
| 2017-01-08 |        null |       null | Sunny  |
| 2017-01-09 |        null |       null | null   |
| 2017-01-10 |        34.1 |        8.1 | Cloudy |
| 2017-01-11 |          40 |         12 | Sunny  |

---

# 🏗️ Temporary Views

A temporary view allows SQL queries on a Spark DataFrame.

```python
df.createOrReplaceTempView("weather")
```

Now SQL can access it.

```sql
SELECT *
FROM weather;
```

---

# 🌍 Global Temporary View

Global temporary views are visible across notebooks running on the same Spark cluster.

```python
df.createOrReplaceGlobalTempView("global_weather")
```

Query

```sql
SELECT *
FROM global_temp.global_weather;
```

---

# 📌 Session View vs Global Temp View

| Feature                          | Temp View | Global Temp View    |
| -------------------------------- | --------- | ------------------- |
| Visible only in current notebook | ✅        | ❌                  |
| Visible across notebooks         | ❌        | ✅                  |
| Exists until Spark session ends  | ✅        | ✅                  |
| Reference name                   | weather   | global_temp.weather |

---

# 🔍 Query Example

Retrieve rows where temperature exists.

```python
spark.sql("""
SELECT *
FROM weather
WHERE temperature IS NOT NULL
ORDER BY day
""").show()
```

---

# 📊 Expected Output

| Day        | Temperature | Wind Speed | Event  |
| ---------- | ----------: | ---------: | ------ |
| 2017-01-01 |          32 |          6 | Rain   |
| 2017-01-05 |          28 |       null | Snow   |
| 2017-01-07 |          32 |       null | Rain   |
| 2017-01-10 |        34.1 |        8.1 | Cloudy |
| 2017-01-11 |          40 |         12 | Sunny  |

---

# 📊 Aggregation Example

Average temperature by weather event.

```sql
%sql

SELECT
event,
ROUND(AVG(temperature),1) AS avg_temp
FROM weather
GROUP BY event
ORDER BY avg_temp DESC;
```

---

# 📊 Expected Output

| Event  | Average Temperature |
| ------ | ------------------: |
| Sunny  |                40.0 |
| Cloudy |                34.1 |
| Rain   |                32.0 |
| Snow   |                28.0 |
| NULL   |                NULL |

---

# 📌 Common SQL Operations in Spark

## Select

```sql
SELECT *
FROM weather;
```

---

## Filter

```sql
SELECT *
FROM weather
WHERE event='Rain';
```

---

## Sorting

```sql
SELECT *
FROM weather
ORDER BY temperature DESC;
```

---

## Group By

```sql
SELECT
event,
COUNT(*)
FROM weather
GROUP BY event;
```

---

## Aggregate Functions

```sql
SELECT

AVG(temperature),
MAX(temperature),
MIN(temperature),
COUNT(*)

FROM weather;
```

---

## Null Check

```sql
SELECT *
FROM weather
WHERE temperature IS NULL;
```

---

## Multiple Conditions

```sql
SELECT *
FROM weather
WHERE temperature > 30
AND event='Rain';
```

---

# 🎯 When to Use Spark SQL?

Use Spark SQL when:

- ✔ SQL developers work with Spark
- ✔ Interactive analytics
- ✔ Reporting
- ✔ Data exploration
- ✔ Data validation
- ✔ ETL pipelines
- ✔ Delta Lake queries

---

# 🔥 Spark SQL vs Traditional SQL

| SQL                       | Spark SQL                        |
| ------------------------- | -------------------------------- |
| Runs on a database server | Runs on Apache Spark             |
| Limited by one machine    | Distributed across many machines |
| Suitable for GB data      | Suitable for TB/PB data          |
| No distributed execution  | Distributed execution            |
| Good for OLTP             | Good for Analytics & Big Data    |

---

# 💼 Spark SQL Interview Questions

## 1. What is Spark SQL?

**Answer**

Spark SQL is Apache Spark's module for processing structured and semi-structured data using SQL queries.

---

## 2. What is the difference between SQL and Spark SQL?

| SQL                  | Spark SQL          |
| -------------------- | ------------------ |
| Database engine      | Distributed engine |
| Single machine       | Cluster computing  |
| Relational databases | Big Data           |

---

## 3. What is `spark.sql()`?

Executes SQL queries from Python or Scala on Spark DataFrames and tables.

---

## 4. What is a Temporary View?

A temporary table created from a DataFrame that exists only during the current Spark session.

```python
df.createOrReplaceTempView("weather")
```

---

## 5. What is a Global Temporary View?

A view accessible across notebooks within the same Spark application.

```python
df.createOrReplaceGlobalTempView("weather")
```

Query

```sql
SELECT *
FROM global_temp.weather;
```

---

## 6. Difference between Temp View and Global Temp View?

| Temp View            | Global Temp View            |
| -------------------- | --------------------------- |
| Current session only | Accessible across notebooks |
| No prefix required   | Uses global_temp prefix     |

---

## 7. Can Spark SQL query DataFrames?

✅ Yes.

After creating a temporary view.

---

## 8. Which optimizer does Spark SQL use?

Catalyst Optimizer.

---

## 9. Which execution engine does Spark SQL use?

Tungsten Execution Engine.

---

## 10. Which file formats work with Spark SQL?

- CSV
- JSON
- Parquet
- ORC
- Delta Lake
- Avro

---

## 11. Which is faster: DataFrame API or Spark SQL?

Both generate similar execution plans because both are optimized by the Catalyst Optimizer.

---

## 12. How do you check the execution plan?

```python
df.explain(True)
```

---

# 💡 Best Practices

- Use Parquet or Delta instead of CSV
- Avoid `SELECT *`
- Filter data early
- Cache frequently used DataFrames `df.cache()`
- Use `LIMIT` while exploring data
- Handle NULL values properly
- Prefer built-in Spark SQL functions
- Use broadcast joins for small tables
- Partition large datasets
- Analyze queries using `EXPLAIN`
- Optimize Delta tables
- Monitor jobs using Spark UI

---

# 🎯 Key Takeaways

- ✅ Spark SQL enables distributed SQL querying over Big Data.
- ✅ Temporary views bridge DataFrames and SQL.
- ✅ Global temporary views support multi-notebook collaboration.
- ✅ Catalyst Optimizer improves query performance automatically.
- ✅ Spark SQL integrates seamlessly with Delta Lake and Databricks.

---

# 🚀 Next Steps

➡️ [Joins In Spark](05_Joins_in_Spark.md)