# ⚡ Spark Transformations, Actions & Lazy Evaluation

⬅️ [Back to Spark Architecture](02_Spark_Architecture.md)

---

# 📚 Table of Contents

- Overview
- Learning Objectives
- What are Transformations?
- What are Actions?
- Transformation vs Action
- What is Lazy Evaluation?
- Spark Execution Flow
- How Lazy Evaluation Works
- Examples of Transformations
- Examples of Actions
- Spark DAG (Directed Acyclic Graph)
- Benefits of Lazy Evaluation
- Interview Questions
- Best Practices
- Key Takeaways
- Next Topic

---

# 📖 Overview

Apache Spark processes data using two fundamental operations:

- **Transformations**
- **Actions**

A **Transformation** creates a new dataset from an existing one without executing immediately.

An **Action** triggers the execution of all pending transformations and either returns a result to the Driver Program or writes the output to storage.

Spark follows the principle of **Lazy Evaluation**, meaning transformations are not executed until an action is invoked. This allows Spark to optimize the execution plan before processing the data.

---

# 🎯 Learning Objectives

After completing this guide, you will understand:

- What Transformations are
- What Actions are
- Difference between Transformations and Actions
- Lazy Evaluation
- Directed Acyclic Graph (DAG)
- Spark Execution Flow
- Benefits of Lazy Evaluation

---

# 🔄 What are Transformations?

A **Transformation** is an operation that creates a new DataFrame or RDD from an existing one.

Transformations are **lazy**, meaning they do not execute immediately.

Instead, Spark records the transformation and waits until an action is called.

### Common Transformations

- `select()`
- `filter()`
- `where()`
- `map()`
- `withColumn()`
- `drop()`
- `join()`
- `groupBy()`
- `orderBy()`

---

# ⚡ What are Actions?

An **Action** triggers the execution of all previously defined transformations.

Actions either:

- Return results to the Driver Program
- Write data to storage
- Display output

### Common Actions

- `show()`
- `count()`
- `collect()`
- `first()`
- `take()`
- `foreach()`
- `write()`
- `save()`

---

# 📊 Transformation vs Action

| Transformation                | Action                          |
| ----------------------------- | ------------------------------- |
| Creates a new DataFrame/RDD   | Executes the computation        |
| Lazy Operation                | Eager Operation                 |
| Returns another DataFrame/RDD | Returns a result or writes data |
| Does not execute immediately  | Triggers Spark Job              |
| Builds the DAG                | Executes the DAG                |

---

# ⏳ What is Lazy Evaluation?

**Lazy Evaluation** means Spark postpones execution until an Action is called.

Instead of executing every transformation one by one, Spark builds an optimized execution plan.

Only when an Action is invoked does Spark execute the entire pipeline.

---

# 🏗 Spark Execution Flow

```text
Read Data
     │
     ▼
Transformation
(select)
     │
     ▼
Transformation
(filter)
     │
     ▼
Transformation
(withColumn)
     │
     ▼
Lazy Evaluation
(Build DAG)
     │
     ▼
Action
(show / count / write)
     │
     ▼
Spark Executes Job
```

---

# 🔍 How Lazy Evaluation Works

Consider the following example:

```python
df = spark.read.csv("employees.csv", header=True)

df_filtered = df.filter(df.salary > 50000)

df_selected = df_filtered.select("name", "salary")

df_selected.show()
```

### Step 1

Read the dataset.

(No execution)

⬇️

### Step 2

Apply `filter()`.

(No execution)

⬇️

### Step 3

Apply `select()`.

(No execution)

⬇️

### Step 4

Call `show()`.

Spark now executes the complete DAG.

---

# 🔧 Examples of Transformations

### Select Columns

```python
df.select("name", "salary")
```

---

### Filter Rows

```python
df.filter(df.salary > 50000)
```

---

### Add New Column

```python
df.withColumn(
    "bonus",
    df.salary * 0.10
)
```

---

### Join DataFrames

```python
employees.join(
    departments,
    "dept_id"
)
```

---

### Group Data

```python
df.groupBy("department").count()
```

---

# 🚀 Examples of Actions

### Show Data

```python
df.show()
```

---

### Count Rows

```python
df.count()
```

---

### Collect Data

```python
df.collect()
```

---

### Get First Row

```python
df.first()
```

---

### Save Data

```python
df.write.mode("overwrite").parquet("output/")
```

---

# 🌐 Spark DAG (Directed Acyclic Graph)

Spark combines all transformations into a **Directed Acyclic Graph (DAG)** before execution.

```text
Read CSV
     │
     ▼
Filter
     │
     ▼
Select
     │
     ▼
GroupBy
     │
     ▼
Show()
```

The DAG allows Spark to optimize execution before running the job.

---

# ✨ Benefits of Lazy Evaluation

### ⚡ Query Optimization

Spark optimizes the entire execution plan before processing data.

---

### 🚀 Avoids Unnecessary Computation

Only the required operations are executed.

---

### 💾 Memory Efficiency

Spark minimizes intermediate data storage and optimizes memory usage.

---

### 🔄 Fault Tolerance

Spark can recompute lost partitions using lineage information.

---

### 📈 Better Performance

Combining multiple transformations into a single optimized execution plan reduces execution time.

---

# 🎤 Interview Questions

### 1. What is a Transformation in Spark?

A Transformation creates a new DataFrame or RDD from an existing one without executing immediately.

---

### 2. What is an Action in Spark?

An Action triggers the execution of all pending transformations and returns a result or writes data.

---

### 3. What is Lazy Evaluation?

Lazy Evaluation means Spark delays execution until an Action is called.

---

### 4. Name some Transformations.

- select()
- filter()
- map()
- join()
- groupBy()
- withColumn()

---

### 5. Name some Actions.

- show()
- count()
- collect()
- first()
- take()
- write()

---

### 6. Why does Spark use Lazy Evaluation?

To optimize the execution plan, reduce unnecessary computation, improve memory usage, and enhance performance.

---

### 7. What is a DAG in Spark?

A Directed Acyclic Graph (DAG) is the execution plan created by Spark that represents all transformations before execution.

---

### 8. When are Transformations executed?

Only when an Action is called.

---

### 9. Which operation triggers a Spark Job?

Actions trigger Spark Jobs.

---

### 10. What are the benefits of Lazy Evaluation?

- Query Optimization
- Better Performance
- Memory Efficiency
- Fault Tolerance
- Reduced Computation

---

# 💡 Best Practices

- ✅ Chain multiple transformations before calling an Action.
- ✅ Minimize the use of `collect()` on large datasets.
- ✅ Use `show()` instead of `collect()` when inspecting data.
- ✅ Cache or persist DataFrames reused multiple times.
- ✅ Apply filters early to reduce the amount of data processed.
- ✅ Select only the required columns.
- ✅ Understand that transformations are lazy and actions trigger execution.
- ✅ Use `explain()` to inspect the execution plan.

---

# 🎯 Key Takeaways

- Transformations define computations but do not execute immediately.
- Actions trigger the execution of all pending transformations.
- Spark follows Lazy Evaluation to optimize execution.
- Transformations build a Directed Acyclic Graph (DAG).
- Spark executes the optimized DAG only when an Action is invoked.
- Lazy Evaluation improves query optimization, memory efficiency, fault tolerance, and overall performance.

---

# 📚 Next Topic

➡️ [Narrow vs Wide Transformations](04_Narrow_vs_Wide_Transformations.md)