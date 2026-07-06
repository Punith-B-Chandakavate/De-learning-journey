# 🚀 Reading Spark Plans using `explain()`

⬅️ [Back to Joins In Spark](../01_DataFrame_Basic/05_Joins_in_Spark.md)

---

# 📚 Table of Contents

- Overview
- Spark Query Execution Flow
- Catalyst Query Optimizer
- Photon Query Engine
- Why Use `explain()`?
- Sample DataFrame
- Reading Spark Plans using `explain("extended")`
- Parsed Logical Plan
- Analyzed Logical Plan
- Optimized Logical Plan
- Physical Plan
- Photon Explanation
- Reading Spark Plans using `explain("formatted")`
- Interview Questions
- Best Practices
- Key Takeaways

---

# 📖 Overview

Apache Spark is popular because of its highly optimized query planning and execution engine. Before executing a query, Spark converts user-written code into multiple execution plans and selects the most efficient one.

Spark uses the **Catalyst Query Optimizer** to generate and optimize query plans. Once the best execution plan is selected, the **Photon Query Engine** executes the query efficiently.

The `explain()` function helps visualize how Spark interprets, optimizes, and executes your DataFrame operations.

---

# 🏗 Spark Query Execution Flow

![Spark Query Execution Flow](./images/01_Reading_Spark_Plans/spark_explain.png)

---

# 🧠 Catalyst Query Optimizer

The **Catalyst Query Optimizer** is Spark's optimization framework.

It is responsible for:

- Creating logical query plans
- Resolving tables and columns using the catalog
- Applying optimization rules
- Generating multiple physical execution plans
- Selecting the best execution strategy

Catalyst performs query optimization before any data is processed.

---

# ⚡ Photon Query Engine

The **Photon Query Engine** is Databricks' high-performance execution engine written in **C++**.

Its responsibilities include:

- Executing the optimized physical plan
- Vectorized query execution
- Faster scans
- Efficient joins
- Improved aggregation performance

Catalyst creates the execution plan, while Photon executes it.

---

# 🔍 Why Use `explain()`?

The `explain()` method displays Spark's execution plan for a DataFrame.

It helps developers:

- Understand query execution
- Debug performance issues
- Identify unnecessary scans
- Analyze optimization
- Verify predicate pushdown
- Check column pruning

---

# 📂 Sample DataFrame

```python
df = spark.table("workspace.default.movies")
```

---

# Example Query

```python
from pyspark.sql import functions as F

df_narrow = (
    df.select(
        "title",
        "studio",
        "imdb_rating"
    )
    .filter(F.col("release_year") > 2010)
)
```

---

# 📖 Reading Spark Plans

Display the complete execution plan.

```python
df_narrow.explain("extended")
```

---

# 🔹 Parsed Logical Plan

The **Parsed Logical Plan** is the first stage of query processing.

At this stage:

- Spark parses the user query.
- Tables and columns are not yet validated.
- Relations remain unresolved.

Example

```text
Filter
Project
UnresolvedRelation
```

This represents the raw query before Spark understands the metadata.

---

# 🔹 Analyzed Logical Plan

The **Analyzed Logical Plan** resolves the query using the Spark Catalog.

Spark performs:

- Table resolution
- Column resolution
- Data type validation
- Metadata lookup

Example

```text
Relation workspace.default.movies parquet
```

At this stage Spark knows:

- Table location
- Column names
- Data types
- File format

---

# 🔹 Optimized Logical Plan

The **Optimized Logical Plan** is produced after Catalyst applies optimization rules.

Common optimizations include:

- Predicate Pushdown
- Column Pruning
- Constant Folding
- Null Filtering

Example

```text
Project
Filter
Relation parquet
```

Notice Spark automatically added

```text
isnotnull(release_year)
```

to avoid unnecessary processing.

---

# 🔹 Physical Plan

The **Physical Plan** describes how Spark will actually execute the query.

Example

```text
PhotonResultStage
    │
PhotonColumnarToRow
    │
PhotonProject
    │
PhotonScan
```

The physical plan shows:

- Scan operations
- Projection
- Filtering
- Execution engine

This is the actual plan executed on the cluster.

---

# ⚡ Photon Explanation

Spark also displays whether the query is fully supported by the Photon Engine.

Example

```text
The query is fully supported by Photon.
```

This indicates that the entire query will benefit from Photon optimizations.

---

# 📖 Formatted Explain Plan

You can display a cleaner physical execution plan using:

```python
df_narrow.explain("formatted")
```

Example Output

```text
PhotonScan
      │
PhotonProject
      │
PhotonColumnarToRow
      │
PhotonResultStage
```

The formatted plan is easier to read and focuses on the physical execution steps.

---

# 💼 Interview Questions

### 1. What is the purpose of `explain()` in Spark?

It displays the execution plan of a DataFrame query, helping developers understand how Spark processes and optimizes the query.

---

### 2. What are the stages shown in `explain("extended")`?

- Parsed Logical Plan
- Analyzed Logical Plan
- Optimized Logical Plan
- Physical Plan

---

### 3. What is the Catalyst Query Optimizer?

Catalyst is Spark's optimization engine responsible for generating, analyzing, optimizing, and selecting the best query execution plan.

---

### 4. What is the Photon Query Engine?

Photon is Databricks' vectorized query execution engine written in C++ that executes optimized physical plans for improved performance.

---

### 5. Which component generates query plans?

Catalyst Query Optimizer.

---

### 6. Which component executes the query?

Photon Query Engine (in Databricks).

---

### 7. Why does Spark generate multiple physical plans?

Spark evaluates different execution strategies and selects the most efficient one using its cost model and Adaptive Query Execution (AQE).

---

# 🏆 Best Practices

- Use `explain()` to understand how Spark executes your queries.
- Prefer `explain("extended")` when learning Spark internals.
- Use `explain("formatted")` for a cleaner view of the physical execution plan.
- Check whether **Predicate Pushdown** and **Column Pruning** are applied.
- Select only the required columns before filtering.
- Filter data as early as possible to reduce the amount of data processed.
- Use Parquet or Delta formats to enable Spark optimizations.
- Review the execution plan before optimizing large ETL jobs.

---

# 🎯 Key Takeaways

- Spark converts DataFrame operations into execution plans before running them.
- Catalyst Query Optimizer analyzes and optimizes logical plans.
- Optimized logical plans are converted into one or more physical plans.
- Spark selects the best physical plan using its optimization strategies.
- Photon executes the optimized physical plan efficiently.
- `explain("extended")` displays every stage of query planning.
- `explain("formatted")` provides a cleaner view of the physical execution plan.
- Understanding Spark execution plans is essential for debugging and performance tuning.

---

# 📚 Next Topic

➡️ [Spark Architecture](02_Spark_Architecture.md)