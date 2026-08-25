
# 🌬️ Apache Airflow — DAGs, Operators & Tasks

![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Workflow%20Orchestration-017CEE?logo=apacheairflow&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![DAG](https://img.shields.io/badge/Airflow-DAG-blue)
![ETL](https://img.shields.io/badge/Data%20Engineering-ETL-green)

---
# 📚 Table of Contents

* 📖 Overview
* 🎯 Learning Objectives
* 📊 What is a DAG?
* ➡️ Directed
* 🔄 Acyclic
* 🧩 What is a Task?
* ⚙️ What is an Operator?
* 🧠 Operator vs Task
* 🏗️ DAG → Operator → Task
* 🐍 PythonOperator
* 🏗️ Creating a Simple DAG
* 🔗 Task Dependencies
* ➡️ Bitshift Operators
* 📊 Example ETL DAG
* 🏗️ More Realistic DAG
* ⏰ DAG Scheduling
* 🔄 DAG Run
* 📊 Task Lifecycle
* 🔁 Task Retries
* 🧩 Common Operators
* 🔄 ETL Example
* 🏢 Real-World Example
* 📊 DAG vs Task vs Operator
* 🧠 Simple Example to Remember
* 🔄 Complete Airflow Execution Model
* 🎤 Interview Questions
* 📋 Quick Reference
* 🎯 Key Takeaways
* 🏆 Final Mental Model

---


# 📖 Overview

Apache Airflow represents data workflows using **Directed Acyclic Graphs (DAGs)**.

A DAG defines:

- 📊 The workflow
- 🧩 Tasks
- 🔗 Dependencies between tasks
- ⏰ Scheduling
- 🔄 Execution order

The main building blocks of an Airflow workflow are:

```text
DAG
 │
 ├── Tasks
 │
 ├── Operators
 │
 └── Dependencies
````

A simple ETL workflow can be represented as:

```text
Extract
   │
   ▼
Transform
   │
   ▼
Load
```

---

# 🎯 Learning Objectives

After completing this module, you will understand:

* 📊 What is a DAG?
* 🧩 What is a Task?
* ⚙️ What is an Operator?
* 🔗 How tasks are connected
* ➡️ How task dependencies work
* 🐍 How Python functions become Airflow tasks
* ⏰ How DAG scheduling works
* 🔄 How Airflow executes workflows
* 📊 Difference between DAG, Task and Operator

---

# 📊 What is a DAG?

**DAG** stands for:

> **Directed Acyclic Graph**

A DAG is a graph with **directed edges and no cycles**.

In Apache Airflow, a DAG represents a workflow containing multiple tasks and their dependencies.

Example:

```text
Extract
   │
   ▼
Transform
   │
   ▼
Load
```

The direction is:

```text
Extract → Transform → Load
```

---

# ➡️ Directed

A DAG is **directed** because tasks have a specific execution direction.

For example:

```text
Task A
  │
  ▼
Task B
  │
  ▼
Task C
```

The direction is:

```text
A → B → C
```

Airflow understands that:

```text
A must execute before B

B must execute before C
```

---

# 🔄 Acyclic

A DAG is **acyclic** because the workflow cannot contain a cycle.

### ✅ Valid DAG

```text
A
│
▼
B
│
▼
C
```

There is no path back to `A`.

### ❌ Invalid Cycle

```text
A
│
▼
B
│
▼
C
│
└──────► A
```

This creates:

```text
A → B → C → A
```

which is a cycle.

Airflow workflows must be acyclic.

---

# 🧩 What is a Task?

A **Task** is a single unit of work inside an Airflow DAG.

Examples:

```text
Extract Data
Transform Data
Load Data
Send Email
Run SQL Query
Execute Python Function
```

Example ETL workflow:

```text
DAG
 │
 ├── Extract Task
 │
 ├── Transform Task
 │
 └── Load Task
```

Each task performs a specific operation.

---

# ⚙️ What is an Operator?

An **Operator** defines what type of work a task performs.

In simple terms:

```text
Operator
    ↓
Defines the type of work
    ↓
Task
    ↓
Executes that work
```

Examples of operators include:

| Operator                    | Purpose                         |
| --------------------------- | ------------------------------- |
| `PythonOperator`            | Execute Python functions        |
| `BashOperator`              | Execute shell commands          |
| `SQLExecuteQueryOperator`   | Execute SQL queries             |
| `EmailOperator`             | Send emails                     |
| Provider-specific operators | Interact with external services |

---

# 🧠 Operator vs Task

These two concepts are closely related but different.

### Operator

Defines **how the work should be performed**.

### Task

Represents the **actual execution instance of that operator inside a DAG**.

Example:

```python
PythonOperator(
    task_id="extract",
    python_callable=extract,
)
```

Here:

```text
PythonOperator
       │
       ▼
Defines execution behavior
       │
       ▼
Task: extract
```

---

# 🏗️ DAG → Operator → Task

The relationship can be understood as:

```text
                 DAG
                  │
                  ▼
              Operator
                  │
                  ▼
                Task
                  │
                  ▼
              Execution
```

Example:

```text
etl_pipeline
      │
      ├── PythonOperator
      │       │
      │       ▼
      │    extract
      │
      ├── PythonOperator
      │       │
      │       ▼
      │   transform
      │
      └── PythonOperator
              │
              ▼
            load
```

---

# 🐍 PythonOperator

`PythonOperator` allows a Python function to execute as an Airflow task.

Example:

```python
from airflow.providers.standard.operators.python import PythonOperator


def extract():
    print("Extracting data")


extract_task = PythonOperator(
    task_id="extract",
    python_callable=extract,
)
```

Here:

```text
Python Function
      ↓
extract()
      ↓
PythonOperator
      ↓
Airflow Task
```

---

# 🏗️ Creating a Simple DAG

A basic DAG can be created using:

```python
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def extract():
    print("Extracting data")


def transform():
    print("Transforming data")


def load():
    print("Loading data")


with DAG(
    "etl_pipeline",
    start_date=datetime(2025, 10, 20),
    schedule=None,
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )
```

At this point we have:

```text
DAG
 │
 ├── Extract Task
 ├── Transform Task
 └── Load Task
```

But Airflow does not yet know the execution order.

---

# 🔗 Task Dependencies

Task dependencies define the order in which tasks execute.

Use:

```python
extract_task >> transform_task >> load_task
```

This creates:

```text
Extract
   │
   ▼
Transform
   │
   ▼
Load
```

Airflow understands:

```text
Extract
   ↓
Transform
   ↓
Load
```

---

# ➡️ Bitshift Operators

Airflow provides convenient syntax for defining dependencies.

## Forward Dependency

```python
task1 >> task2
```

Means:

```text
task1
  ↓
task2
```

`task1` executes before `task2`.

---

## Multiple Dependencies

```python
task1 >> task2 >> task3
```

Creates:

```text
task1
  ↓
task2
  ↓
task3
```

---

## Parallel Tasks

Tasks can also execute independently.

```python
task1 >> [task2, task3]
```

Creates:

```text
          ┌──► task2
task1 ────┤
          └──► task3
```

After `task1` completes, `task2` and `task3` can proceed independently according to their scheduling and available resources.

---

## Converging Dependencies

```python
[task2, task3] >> task4
```

Creates:

```text
task2 ────┐
          ├──► task4
task3 ────┘
```

This means `task4` depends on both upstream tasks.

---

# 📊 Example ETL DAG

A typical ETL workflow:

```text
                 ETL DAG
                    │
                    ▼
                Extract
                    │
                    ▼
               Transform
                    │
                    ▼
                  Load
```

Example:

```python
extract_task >> transform_task >> load_task
```

---

# 🏗️ More Realistic DAG

A workflow can contain multiple branches.

```text
                  Start
                    │
                    ▼
                 Extract
                    │
             ┌──────┴──────┐
             ▼             ▼
       Transform A    Transform B
             │             │
             └──────┬──────┘
                    ▼
                  Load
                    │
                    ▼
                  Finish
```

This is still a DAG because there is no circular dependency.

---

# ⏰ DAG Scheduling

A DAG can be scheduled to run automatically.

Example:

```python
with DAG(
    "daily_etl",
    start_date=datetime(2025, 10, 20),
    schedule="0 2 * * *",
) as dag:
    ...
```

The cron expression:

```text
0 2 * * *
```

represents:

```text
Every day at 2:00 AM
```

---

# 🔄 DAG Run

A DAG definition describes the workflow.

A **DAG Run** represents one execution of that workflow.

Example:

```text
DAG Definition
      │
      ▼
etl_pipeline
      │
      ├── Run 1
      ├── Run 2
      ├── Run 3
      └── Run 4
```

Each run contains task executions.

```text
DAG Run
   │
   ├── Extract
   ├── Transform
   └── Load
```

---

# 📊 Task Lifecycle

A task can move through different states during execution.

Simplified workflow:

```text
Scheduled
    │
    ▼
Queued
    │
    ▼
Running
    │
    ├──────────► Success
    │
    └──────────► Failed
```

If retries are configured:

```text
Running
   │
   ▼
Failed
   │
   ▼
Retry
   │
   ▼
Running
```

---

# 🔁 Task Retries

Tasks can be configured with retries.

Example:

```python
from datetime import timedelta

extract_task = PythonOperator(
    task_id="extract",
    python_callable=extract,
    retries=3,
    retry_delay=timedelta(minutes=5),
)
```

The task can retry after failure according to the configured retry policy.

Example:

```text
Extract
   │
   ❌
   │
   ▼
Wait 5 minutes
   │
   ▼
Retry
```

---

# 🧩 Common Operators

## 🐍 PythonOperator

Used to execute Python functions.

```python
PythonOperator(
    task_id="process_data",
    python_callable=process_data,
)
```

---

## 💻 BashOperator

Used to execute shell commands.

```python
BashOperator(
    task_id="run_command",
    bash_command="echo 'Hello Airflow'",
)
```

---

## 🗄️ SQL Operators

SQL operators execute SQL statements against supported databases.

Example concept:

```text
Airflow
   │
   ▼
SQL Task
   │
   ▼
Database
```

---

## ☁️ Provider Operators

Airflow providers contain integrations for external systems.

Examples include:

```text
AWS
Azure
Google Cloud
Snowflake
Databricks
PostgreSQL
MySQL
Slack
```

These allow Airflow to orchestrate tasks across different Data Engineering platforms.

---

# 🔄 ETL Example

A simple ETL DAG can be designed as:

```text
                📊 ETL DAG
                    │
                    ▼
             📥 Extract Task
                    │
                    ▼
           🔄 Transform Task
                    │
                    ▼
              📤 Load Task
```

Example:

```python
extract_task >> transform_task >> load_task
```

---

# 🏢 Real-World Example

Consider an e-commerce pipeline.

```text
                    E-Commerce Pipeline
                            │
                            ▼
                       Extract Orders
                            │
                            ▼
                    Validate / Clean Data
                            │
                            ▼
                    Transform Orders
                            │
                            ▼
                   Load into Warehouse
                            │
                            ▼
                       Power BI
```

Airflow can orchestrate the entire workflow.

---

# 📊 DAG vs Task vs Operator

| Concept       | Meaning                              |
| ------------- | ------------------------------------ |
| 📊 DAG        | Defines the complete workflow        |
| 🧩 Task       | A single unit of work inside a DAG   |
| ⚙️ Operator   | Defines how a task performs its work |
| 🔗 Dependency | Defines task execution order         |
| ▶️ DAG Run    | One execution of a DAG               |

### Simple Mental Model

```text
DAG
 │
 │ contains
 ▼
Tasks
 │
 │ use
 ▼
Operators
 │
 │ execute
 ▼
Work
```

---

# 🧠 Simple Example to Remember

Think of a DAG as a **recipe**.

```text
🍳 Recipe = DAG
```

Each step is a task:

```text
🥕 Cut vegetables = Task
🍳 Cook vegetables = Task
🍽️ Serve food = Task
```

The operator defines the type of work:

```text
PythonOperator
    ↓
Execute Python function
```

Therefore:

```text
DAG
 │
 ├── Task
 │     └── Operator
 │
 ├── Task
 │     └── Operator
 │
 └── Task
       └── Operator
```

---

# 🔄 Complete Airflow Execution Model

```text
                 DAG Definition
                       │
                       ▼
                     Tasks
                       │
                       ▼
                   Operators
                       │
                       ▼
                 Dependencies
                       │
                       ▼
                   DAG Run
                       │
                       ▼
                Task Execution
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
          Success              Failure
                                   │
                                   ▼
                                Retry
                                   │
                                   ▼
                                Success
```

---

# 🎤 Interview Questions

### 1. What is a DAG?

A DAG is a Directed Acyclic Graph that represents a workflow with directed dependencies and no cycles.

---

### 2. Why is it called Directed?

Because dependencies have a specific direction.

```text
A → B
```

means `A` must occur before `B`.

---

### 3. Why is it called Acyclic?

Because a workflow cannot contain circular dependencies.

```text
A → B → C
```

is valid.

```text
A → B → C → A
```

contains a cycle.

---

### 4. What is a Task?

A Task is a single unit of work within an Airflow DAG.

---

### 5. What is an Operator?

An Operator defines the type of work a task performs.

---

### 6. What is PythonOperator?

`PythonOperator` is used to execute Python functions as Airflow tasks.

---

### 7. What is the difference between a DAG and a Task?

```text
DAG  → Complete workflow
Task → Individual unit of work
```

---

### 8. What is the difference between a Task and an Operator?

```text
Operator → Defines how work is performed
Task     → Represents that work inside the DAG
```

---

### 9. What does this mean?

```python
task1 >> task2
```

It means:

```text
task1
  ↓
task2
```

`task1` is upstream of `task2`.

---

### 10. Can tasks run in parallel?

Yes.

For example:

```python
task1 >> [task2, task3]
```

creates independent downstream tasks.

---

### 11. What is a DAG Run?

A DAG Run is one execution of a DAG.

---

### 12. What happens when a task fails?

Depending on the configuration, the task may:

* Retry
* Fail
* Trigger downstream behavior according to dependencies and trigger rules

---

# 📋 Quick Reference

| Concept         | Example                |
| --------------- | ---------------------- |
| DAG             | `etl_pipeline`         |
| Task            | `extract_task`         |
| Operator        | `PythonOperator`       |
| Python function | `extract()`            |
| Dependency      | `task1 >> task2`       |
| Schedule        | `schedule="0 2 * * *"` |
| Retry           | `retries=3`            |
| Retry delay     | `timedelta(minutes=5)` |

---

# 🎯 Key Takeaways

```text
📊 DAG
 │
 │ contains
 ▼
🧩 Tasks
 │
 │ use
 ▼
⚙️ Operators
 │
 │ execute
 ▼
💻 Work
```

* 📊 **DAG** = Complete workflow.
* 🧩 **Task** = Individual unit of work.
* ⚙️ **Operator** = Defines how the task performs its work.
* 🔗 **Dependencies** = Define execution order.
* ➡️ DAGs are directed.
* 🚫 DAGs cannot contain cycles.
* 🐍 `PythonOperator` executes Python functions.
* ⏰ DAGs can be scheduled.
* 🔄 Tasks can be configured with retries.
* ▶️ A DAG can be executed manually or according to its schedule.

---

# 🏆 Final Mental Model

```text
                  🌬️ APACHE AIRFLOW
                         │
                         ▼
                       📊 DAG
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
           Task        Task        Task
             │           │           │
             ▼           ▼           ▼
         Operator    Operator    Operator
             │           │           │
             ▼           ▼           ▼
           Work        Work        Work
             │           │           │
             └───────────┼───────────┘
                         ▼
                    📊 Workflow
```

> 🚀 **Key Idea:** A DAG defines the workflow, Tasks represent individual units of work, and Operators define how those tasks perform their work.
