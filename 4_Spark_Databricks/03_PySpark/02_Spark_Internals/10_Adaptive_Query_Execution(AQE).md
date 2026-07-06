# ⚡ Adaptive Query Execution (AQE) in Apache Spark

⬅️ [Data Skew and mitigation techniques](09_Data_Skew.md)

---

# 📚 Table of Contents

- Overview
- Learning Objectives
- What is Adaptive Query Execution (AQE)?
- Why AQE is Needed
- AQE Architecture
- AQE Execution Flow
- Runtime Statistics
- AQE Optimizations
  - Dynamic Join Selection
  - Dynamic Partition Coalescing
  - Skew Join Optimization
- Enabling AQE
- Reading the Execution Plan
- AQE vs Traditional Query Execution
- Performance Comparison
- Real-World Use Cases
- Best Practices
- Interview Questions
- Summary
- Key Takeaways

---

# 📖 Overview

**Adaptive Query Execution (AQE)** is one of the most powerful optimization features introduced in Apache Spark.

Unlike the traditional query optimizer, which generates the execution plan **before** a job starts, AQE continuously monitors the job during execution and **re-optimizes the query plan using actual runtime statistics**.

This allows Spark to automatically choose better execution strategies, reduce shuffle operations, optimize joins, handle skewed partitions, and improve overall job performance.

AQE helps Spark applications become **faster, smarter, and more resource-efficient** without requiring manual code changes.

---

# 🎯 Learning Objectives

After completing this guide, you will understand:

- What Adaptive Query Execution (AQE) is
- Why AQE is important
- How AQE works internally
- Dynamic Join Selection
- Dynamic Partition Coalescing
- Skew Join Optimization
- How to enable AQE
- Performance benefits of AQE

---

# ⚡ What is Adaptive Query Execution (AQE)?

**Adaptive Query Execution (AQE)** is Spark's **runtime query optimization framework** that dynamically improves query execution plans based on **actual runtime statistics** collected while the job is running.

Instead of relying only on estimated table statistics, AQE observes the real size of shuffle partitions and automatically adjusts the execution plan to improve performance.

AQE performs several optimizations during execution, including:

- 🔄 Dynamic Join Selection
- 📦 Dynamic Partition Coalescing
- ⚖️ Skew Join Optimization

These optimizations help reduce execution time, minimize shuffle operations, and improve resource utilization.

---

# ❓ Why AQE is Needed

Traditional Spark query optimization occurs **before execution**.

At planning time, Spark estimates:

- Table sizes
- Partition sizes
- Join strategies

However, these estimates may not accurately reflect the actual data processed at runtime.

As a result:

- Wrong join strategies may be selected.
- Too many shuffle partitions may be created.
- Data skew may cause straggler tasks.
- Resources may be underutilized.

AQE solves these problems by making optimization decisions **during execution** based on real statistics.

---

# 🏗 AQE Architecture

![Spark AQE Architecture](images/10_Adaptive_Query_Execution(AQE)/Spark_AQE_Architecture.png)

---

# 🔄 AQE Execution Flow

AQE continuously monitors the execution of Spark jobs.

![Spark AQE Execution Flow](images/10_Adaptive_Query_Execution(AQE)/Spark_AQE_Workflow.png)

---

# 📊 Runtime Statistics

AQE collects actual execution statistics after every shuffle stage.

Examples include:

- Shuffle partition size
- Number of records
- Data distribution
- Join input size
- Partition skew

These runtime statistics enable Spark to make better optimization decisions than static estimates.

---

# 🔀 Dynamic Join Selection

One of AQE's most valuable features is **Dynamic Join Selection**.

Instead of deciding the join strategy before execution, Spark waits until shuffle statistics are available.

Based on the observed data size, AQE may change the join strategy.

Example

![Spark Dynamic Join Selection](images/10_Adaptive_Query_Execution(AQE)/Spark_AQE_Dynamic_Join.png)

This automatic conversion significantly reduces shuffle operations and improves performance.

---

## Benefits

- Automatically selects the most efficient join strategy.
- Eliminates unnecessary shuffle operations.
- Improves query performance.
- Requires no manual optimization.

---

# 📦 Dynamic Partition Coalescing

During execution, Spark may discover that shuffle partitions are much smaller than expected.

Instead of processing many tiny partitions, AQE automatically merges them into fewer larger partitions.

This reduces scheduling overhead and avoids generating too many small output files.

---

## With and Without AQE

![Spark AQE Coalesce](images/10_Adaptive_Query_Execution(AQE)/Spark_AQE_Coalesce.png)

---

## Benefits

- Reduces scheduling overhead
- Fewer output files
- Better executor utilization
- Faster execution

---

# ⚖️ Skew Join Optimization

AQE automatically detects skewed shuffle partitions.

If one partition is significantly larger than the others, Spark splits it into multiple smaller partitions.

Instead of one executor processing all the skewed data, multiple executors share the workload.

---

## With and Without AQE

![Spark AQE Skew Optimization](images/10_Adaptive_Query_Execution(AQE)/Spark_AQE_Skew_Optimizations.png)

---

## Benefits

- Eliminates straggler tasks
- Balances workload
- Improves cluster utilization
- Faster joins

---

# ⚙️ Enabling AQE

Enable AQE

```python
spark.conf.set(
    "spark.sql.adaptive.enabled",
    "true"
)
```

Enable Skew Join Optimization

```python
spark.conf.set(
    "spark.sql.adaptive.skewJoin.enabled",
    "true"
)
```

Enable Dynamic Partition Coalescing

```python
spark.conf.set(
    "spark.sql.adaptive.coalescePartitions.enabled",
    "true"
)
```

---

# 💻 Practical Example

Suppose Spark initially selects a **Sort Merge Join**.

During execution, AQE discovers that one table is only **8 MB**.

Instead of continuing with the expensive Sort Merge Join, AQE automatically switches to a **Broadcast Hash Join**.

This eliminates unnecessary shuffle operations and significantly improves query performance.

---

# 🔍 Reading the Execution Plan

One of the easiest ways to verify whether **Adaptive Query Execution (AQE)** is working is by examining the Spark execution plan.

Spark provides the `explain()` method to display the logical and physical execution plans.

```python
df.explain("formatted")
```

When AQE is enabled, the execution plan includes an **AdaptiveSparkPlan** node.

Example

```text
AdaptiveSparkPlan (isFinalPlan=false)
        │
        ▼
Shuffle Exchange
        │
        ▼
Broadcast Hash Join
        │
        ▼
Result
```

Look for the following operators in the execution plan:

| Operator                | Description                         |
| ----------------------- | ----------------------------------- |
| `AdaptiveSparkPlan`   | Indicates AQE is enabled            |
| `BroadcastHashJoin`   | AQE switched to a Broadcast Join    |
| `SortMergeJoin`       | AQE retained a Sort Merge Join      |
| `CustomShuffleReader` | AQE merged small shuffle partitions |
| `ShuffleQueryStage`   | Runtime shuffle stage               |

---

# 🔄 AQE vs Traditional Query Execution

| Traditional Spark                 | Adaptive Query Execution (AQE)           |
| --------------------------------- | ---------------------------------------- |
| Query plan fixed before execution | Query plan optimized during execution    |
| Uses estimated statistics         | Uses actual runtime statistics           |
| Fixed join strategy               | Dynamically changes join strategy        |
| Fixed shuffle partitions          | Dynamatically coalesces partitions       |
| Cannot automatically handle skew  | Automatically detects and mitigates skew |
| Manual optimization required      | Automatic optimization                   |

![Spark AQE vs Traditional Query Execution](images/10_Adaptive_Query_Execution(AQE)/Spark_AQE_vs_Traditional.png)


---

# 📊 AQE Performance Comparison

| Feature                   | Without AQE | With AQE                |
| ------------------------- | ----------- | ----------------------- |
| Join Selection            | Static      | Dynamic                 |
| Shuffle Partitions        | Fixed       | Automatically Coalesced |
| Data Skew Handling        | Manual      | Automatic               |
| Broadcast Join Conversion | No          | Yes                     |
| Resource Utilization      | Moderate    | High                    |
| Execution Time            | Slower      | Faster                  |
| Small File Generation     | More        | Less                    |
| Cluster Efficiency        | Lower       | Higher                  |

---

# 🚀 AQE Optimizations at Runtime

![Spark Reading the Execution Plan](images/10_Adaptive_Query_Execution(AQE)/Spark_AQE_Runtime_Optimizations.png)

---

# 🌍 Real-World Use Cases

## 📊 Data Warehousing

Large fact tables often have unpredictable partition sizes.

AQE automatically adjusts partition sizes and join strategies to improve query performance.

---

## 🛒 E-Commerce Analytics

Daily order volumes vary significantly.

AQE dynamically switches from **Sort Merge Join** to **Broadcast Hash Join** when lookup tables become small enough.

---

## 💳 Banking & Finance

Large transaction datasets frequently contain skewed account IDs.

AQE automatically detects skewed partitions and splits them into smaller tasks.

---

## 📈 ETL Pipelines

ETL jobs often generate many small shuffle partitions after filtering and aggregation.

AQE coalesces these partitions, reducing scheduling overhead and improving execution efficiency.

---

## ☁️ Cloud Data Platforms

Platforms such as **Databricks**, **Amazon EMR**, and **Azure Synapse** enable AQE to optimize distributed workloads automatically without requiring manual tuning.

---

# 💡 Best Practices

- ✅ Enable **Adaptive Query Execution (AQE)** for production Spark workloads to automatically optimize query execution at runtime.
- ✅ Store data in **Parquet**, **ORC**, or **Delta Lake** formats to maximize AQE optimizations and reduce I/O.
- ✅ Allow Spark to automatically choose the most efficient join strategy instead of forcing join hints unless you have a specific optimization requirement.
- ✅ Keep table statistics up to date to help Spark generate better initial execution plans.
- ✅ Use `explain("formatted")` to inspect execution plans and verify that AQE optimizations are being applied.
- ✅ Monitor the **Spark UI** to analyze shuffle size, partition distribution, skewed tasks, and AQE optimization decisions.
- ✅ Enable **Skew Join Optimization** to automatically split skewed partitions and improve workload balancing.
- ✅ Avoid unnecessary repartitioning before AQE has an opportunity to optimize shuffle partitions.
- ✅ Combine AQE with proper partitioning, efficient file formats, and optimized Spark configurations for maximum performance.
- ✅ Validate AQE performance using representative production workloads before deploying large-scale Spark applications.

---

# 🎤 Interview Questions

### 1. What is Adaptive Query Execution (AQE)?

AQE is Spark's runtime optimization framework that dynamically modifies execution plans using actual runtime statistics.

---

### 2. Why was AQE introduced?

AQE improves query performance by making optimization decisions during execution instead of relying only on estimated statistics.

---

### 3. What are the major AQE optimizations?

- Dynamic Join Selection
- Dynamic Partition Coalescing
- Skew Join Optimization

---

### 4. How does AQE improve join performance?

It automatically changes the join strategy based on the actual size of the datasets observed during execution.

---

### 5. Can AQE convert a Sort Merge Join into a Broadcast Join?

✅ Yes.

If runtime statistics show that one table is small enough, AQE automatically switches to a **Broadcast Hash Join**.

---

### 6. How does AQE reduce small files?

By automatically merging small shuffle partitions through **Dynamic Partition Coalescing**.

---

### 7. How does AQE handle skewed data?

AQE detects oversized partitions and splits them into smaller partitions for balanced execution.

---

### 8. How can you verify AQE is enabled?

Use

```python
df.explain("formatted")
```

and look for

```text
AdaptiveSparkPlan
```

---

### 9. Does AQE require code changes?

No.

AQE works automatically once it is enabled.

---

### 10. Which Spark versions support AQE?

AQE is available from **Apache Spark 3.x** and later.

---

### 11. What operator indicates AQE in the execution plan?

`AdaptiveSparkPlan`

---

### 12. What is Dynamic Partition Coalescing?

It automatically merges small shuffle partitions into fewer larger partitions to reduce scheduling overhead.

---

### 13. What is Skew Join Optimization?

It automatically detects skewed partitions and splits them into smaller tasks for balanced execution.

---

### 14. Does AQE improve cluster utilization?

Yes.

AQE balances workloads, reduces idle executors, and improves resource utilization.

---

### 15. Should AQE always be enabled?

For most production workloads, **yes**. AQE generally improves performance with little or no code modification.

---

# 📊 Summary

| Concept                        | Description                                         |
| ------------------------------ | --------------------------------------------------- |
| Adaptive Query Execution (AQE) | Runtime query optimization framework                |
| Dynamic Join Selection         | Chooses the best join strategy during execution     |
| Dynamic Partition Coalescing   | Merges small shuffle partitions                     |
| Skew Join Optimization         | Splits skewed partitions into smaller tasks         |
| Runtime Statistics             | Actual execution metrics collected during execution |
| AdaptiveSparkPlan              | Indicates AQE is enabled                            |

---

# 🎯 Key Takeaways

- **Adaptive Query Execution (AQE)** is Spark's runtime query optimization framework that improves execution plans using actual runtime statistics.
- AQE dynamically selects the most efficient **join strategy**, including switching between **Broadcast Hash Join** and **Sort Merge Join** when appropriate.
- **Dynamic Partition Coalescing** automatically merges small shuffle partitions, reducing scheduling overhead and minimizing the number of small output files.
- **Skew Join Optimization** detects oversized partitions and splits them into smaller tasks, improving workload balance and reducing straggler tasks.
- AQE automatically adapts to changing data characteristics during execution, improving query performance without requiring code modifications.
- Using `explain("formatted")` and the **Spark UI** helps verify AQE optimizations and understand Spark's runtime execution behavior.
- Enabling AQE improves query performance, reduces shuffle costs, enhances cluster utilization, and minimizes manual performance tuning.
- Combining AQE with efficient storage formats, proper partitioning, and good Spark development practices results in scalable and production-ready Spark applications.

---

# 📚 Next Topic

➡️ [RDD vs Dataframe vs Dataset](11_RDD_vs_DataFrame_vs_Dataset.md)