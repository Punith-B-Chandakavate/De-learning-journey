# 🌬️ Apache Airflow Complete Learning Repository

> A comprehensive learning repository covering **Apache Airflow**, **DAGs**, **Tasks**, **Operators**, **Hooks**, **Providers**, **Task Groups**, **Scheduling**, and practical **ETL workflow orchestration** with hands-on examples.

![Apache Airflow](https://img.shields.io/badge/Apache-Airflow-017CEE?logo=apacheairflow\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker\&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud%20Integration-FF9900?logo=amazonaws\&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-29B5E8?logo=snowflake\&logoColor=white)
![ETL](https://img.shields.io/badge/ETL-Workflow%20Orchestration-4CAF50)

---

# 📚 Table of Contents

* Apache Airflow Complete Learning Repository
* Table of Contents
* About This Repository
* Features
* Repository Structure
* Learning Modules
  * Airflow Fundamentals
  * Airflow Setup & First DAG
  * DAGs, Operators & Tasks
  * Hooks, Providers & Task Groups
* Airflow Learning Roadmap
* Airflow Architecture
* DAG Execution Architecture
* DAG Components
* ETL Workflow Architecture
* Airflow Cloud Integration
* Hooks
* Providers
* Task Groups
* Technologies Covered
* Learning Outcomes
* Prerequisites
* Best Practices
* Repository Progress
* Practical Data Engineering Workflow
* Repository Goal
* Recommended Learning Order

---

# 📖 About This Repository

This repository is a structured learning resource for understanding **Apache Airflow** and its role in modern Data Engineering workflows.

The learning journey starts with **Airflow fundamentals**, continues with **local setup and the first DAG**, then progresses into **DAGs, Tasks, Operators, Hooks, Providers, and Task Groups**.

The repository focuses on practical workflow orchestration concepts that are commonly used to build and automate ETL/ELT pipelines.

This repository is designed for:

* 🎓 Students learning Data Engineering
* 👨‍💻 Python Developers
* 📊 Data Engineers
* 🔄 ETL/ELT Developers
* ☁️ Cloud Data Engineers
* 🏗️ Workflow Orchestration Learners
* 🎯 Interview Preparation

---

# 🚀 Features

* ✅ Apache Airflow Fundamentals
* ✅ Airflow Architecture
* ✅ DAGs
* ✅ Tasks
* ✅ Operators
* ✅ PythonOperator
* ✅ Task Dependencies
* ✅ Scheduling
* ✅ Retries
* ✅ Retry Delay
* ✅ Airflow Setup
* ✅ Docker-based Setup
* ✅ Airflow Web UI
* ✅ Hooks
* ✅ Providers
* ✅ Task Groups
* ✅ AWS Integration
* ✅ S3 Integration
* ✅ Snowflake Integration
* ✅ ETL Workflow Orchestration
* ✅ XCom
* ✅ Airflow Connections
* ✅ Airflow Variables
* ✅ Practical DAG Examples
* ✅ Interview Questions
* ✅ Data Engineering Workflows

---

# 📂 Repository Structure

```text id="airflow-tree"
6_Airflow/
│
├── datasets/
│   └── ...
│
├── images/
│   └── ...
│
├── 01_Airflow_fundamentals.md
│
├── 02_Airflow_Setup_and_First_DAG.md
│
├── 03_DAG_Operators_and_Tasks.md
│
├── 04_Hooks_Providers_Task_Groups.md
│
└── README.md
```

---

# 🗂️ Learning Modules

## 🔹 Module 1 — Airflow Fundamentals

Learn the fundamental concepts behind Apache Airflow and workflow orchestration.

| Topic                | Description                                                 | File                                                         |
| -------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| Airflow Fundamentals | Introduction to Airflow, DAGs, scheduling and orchestration | [`01_Airflow_fundamentals.md`](./01_Airflow_fundamentals.md) |

### Topics Covered

* Apache Airflow
* Workflow orchestration
* ETL / ELT
* DAG
* Tasks
* Task dependencies
* Scheduler
* Executor
* Web Server
* Metadata Database
* Workers
* Airflow UI

---

## 🔹 Module 2 — Airflow Setup & First DAG

Learn how to install and configure Airflow and create your first DAG.

| Topic         | Description                            | File                                                                       |
| ------------- | -------------------------------------- | -------------------------------------------------------------------------- |
| Airflow Setup | Configure Airflow locally using Docker | [`02_Airflow_Setup_and_First_DAG.md`](./02_Airflow_Setup_and_First_DAG.md) |

### Topics Covered

* Docker Desktop
* WSL2
* Airflow Docker Compose
* Airflow initialization
* Airflow Web UI
* DAG folder
* Logs folder
* Plugins folder
* First DAG
* Running a DAG
* DAG validation
* Troubleshooting

---

## 🔹 Module 3 — DAGs, Operators & Tasks

Understand how Airflow workflows are designed using DAGs, tasks, operators, and dependencies.

| Topic                   | Description                     | File                                                               |
| ----------------------- | ------------------------------- | ------------------------------------------------------------------ |
| DAGs, Operators & Tasks | Build and connect Airflow tasks | [`03_DAG_Operators_and_Tasks.md`](./03_DAG_Operators_and_Tasks.md) |

### Topics Covered

* DAG
* Task
* Operator
* PythonOperator
* Task dependencies
* Task execution
* Scheduling
* Retries
* Retry delay
* Task states
* DAG Graph View

Example workflow:

```text
                 DAG
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

---

## 🔹 Module 4 — Hooks, Providers & Task Groups

Learn how Airflow communicates with external systems and organizes complex workflows.

| Topic                          | Description                                    | File                                                                       |
| ------------------------------ | ---------------------------------------------- | -------------------------------------------------------------------------- |
| Hooks, Providers & Task Groups | External connections and workflow organization | [`04_Hooks_Providers_Task_Groups.md`](./04_Hooks_Providers_Task_Groups.md) |

### Topics Covered

* Hooks
* Providers
* Airflow Connections
* AWS Hooks
* S3 integration
* PostgreSQL connections
* Snowflake connections
* Provider packages
* Task Groups
* Workflow organization

Example:

```text
                Airflow DAG
                     │
             ┌───────┴───────┐
             ▼               ▼
        Task Group A    Task Group B
             │               │
       ┌─────┴─────┐    ┌────┴─────┐
       ▼           ▼    ▼          ▼
    Extract     Validate Load     Monitor
```

---

# 📈 Airflow Learning Roadmap

```text id="airflow-roadmap"
                    Apache Airflow
                          │
                          ▼
                Workflow Orchestration
                          │
                          ▼
                   Airflow Architecture
                          │
                          ▼
                   Airflow Installation
                          │
                          ▼
                    Airflow Web UI
                          │
                          ▼
                         DAGs
                          │
                          ▼
                        Tasks
                          │
                          ▼
                      Operators
                          │
                          ▼
                  Task Dependencies
                          │
                          ▼
                     Scheduling
                          │
                          ▼
                 Hooks & Connections
                          │
                          ▼
                      Providers
                          │
                          ▼
                    Task Groups
                          │
                          ▼
                 External Systems
                          │
            ┌─────────────┼─────────────┐
            ▼             ▼             ▼
           AWS         Snowflake     Databases
            │             │             │
            └─────────────┼─────────────┘
                          ▼
                    ETL Pipelines
```

---

# 🏗️ Airflow Architecture

Apache Airflow consists of multiple components that work together to schedule, execute, and monitor workflows.

```text id="airflow-architecture"
                         Apache Airflow
                              │
              ┌───────────────┼────────────────┐
              │               │                │
              ▼               ▼                ▼
          Scheduler       Web Server       Metadata DB
              │               │                │
              │               ▼                │
              │          Airflow UI             │
              │                                │
              └───────────────┬────────────────┘
                              ▼
                          Executor
                              │
                              ▼
                           Workers
                              │
                              ▼
                            Tasks
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
             AWS           Snowflake        Database
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                       External Systems
```

---

# 🔄 DAG Execution Architecture

A DAG defines the workflow and the dependencies between individual tasks.

```text id="dag-execution"
                    DAG
                     │
                     ▼
                  Extract
                     │
                     ▼
                 Validate
                     │
                     ▼
                Transform
                     │
                     ▼
                   Load
                     │
                     ▼
                 Monitor
```

Each task represents a unit of work, while the dependencies determine the execution order.

---

# ⚙️ DAG Components

A typical Airflow DAG contains:

```text id="dag-components"
DAG
 │
 ├── start_date
 │
 ├── schedule
 │
 ├── Tasks
 │    │
 │    ├── Operator
 │    ├── Python Function
 │    └── Configuration
 │
 ├── Dependencies
 │
 ├── Retry Configuration
 │
 └── Execution Rules
```

Example:

```python
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta


def extract():
    print("Extracting data")


def transform():
    print("Transforming data")


def load():
    print("Loading data")


with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(2025, 10, 20),
    schedule="0 2 * * *",
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
        retries=3,
        retry_delay=timedelta(minutes=5),
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    extract_task >> transform_task >> load_task
```

---

# 🔄 ETL Workflow Architecture

Airflow is commonly used to orchestrate ETL/ELT pipelines.

```text id="etl-architecture"
                      Source
                        │
                        ▼
                     Extract
                        │
                        ▼
                    Validate
                        │
                        ▼
                   Transform
                        │
                        ▼
                      Load
                        │
                        ▼
                   Data Store
                        │
                        ▼
                    Analytics
```

---

# ☁️ Airflow Cloud Integration

Airflow can orchestrate workflows involving multiple cloud and data platforms.

```text id="cloud-integrations"
                         Airflow
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
        AWS              Snowflake        Database
          │                 │                 │
          ▼                 ▼                 ▼
         S3             Warehouse       PostgreSQL
          │                 │
          └─────────────────┼─────────────────┘
                            ▼
                       Data Pipeline
```

---

# 🔗 Hooks

A **Hook** provides a high-level interface for communicating with an external system.

```text
Airflow Task
     │
     ▼
   Hook
     │
     ▼
External System
```

Examples include:

* AWS Hook
* S3 Hook
* PostgreSQL Hook
* Snowflake Hook
* HTTP Hook

Benefits:

* 🔐 Centralized connection management
* ♻️ Reusable connections
* 🔑 Secure credential handling
* 🧩 Simplified external-system interaction

---

# 📦 Providers

Providers extend Airflow functionality for external platforms and services.

Examples:

```text
Apache Airflow
      │
      ├── Amazon Provider
      │       └── AWS / S3
      │
      ├── Snowflake Provider
      │       └── Snowflake
      │
      ├── Google Provider
      │       └── GCP
      │
      └── Database Providers
```

Example installation:

```bash
pip install apache-airflow-providers-amazon
```

---

# 🧩 Task Groups

Task Groups help organize related tasks into logical sections within a DAG.

```text
                    ETL DAG
                       │
            ┌──────────┴──────────┐
            ▼                     ▼
       Extract Group         Load Group
            │                     │
       ┌────┴────┐           ┌────┴────┐
       ▼         ▼           ▼         ▼
     API      Validate       S3     Snowflake
```

Task Groups improve:

* 📁 DAG organization
* 👀 UI readability
* 🧩 Logical grouping
* 🔍 Workflow monitoring

---

# 🛠️ Technologies Covered

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| 🌬️ Apache Airflow | Workflow orchestration    |
| 🐍 Python          | DAG development           |
| 🐳 Docker          | Local Airflow environment |
| ☁️ AWS             | Cloud integration         |
| 🪣 Amazon S3       | Object storage            |
| ❄️ Snowflake       | Data warehouse            |
| 🗄️ PostgreSQL     | Database integration      |
| 🔄 ETL / ELT       | Data pipelines            |
| 📊 Power BI        | Analytics                 |

---

# 🎯 Learning Outcomes

After completing this repository, you should be able to:

* Understand Apache Airflow architecture
* Explain DAGs and task dependencies
* Create Airflow DAGs
* Create Python-based tasks
* Use Airflow Operators
* Configure schedules
* Configure retries
* Understand task states
* Run and monitor DAGs
* Configure Airflow Connections
* Work with Hooks
* Install and use Providers
* Organize workflows using Task Groups
* Integrate Airflow with AWS
* Integrate Airflow with S3
* Integrate Airflow with Snowflake
* Build ETL workflows
* Orchestrate data pipelines
* Debug failed tasks
* Monitor workflow execution

---

# ▶️ Prerequisites

To get the most from this repository, you should have basic knowledge of:

* Python
* SQL
* Data Engineering fundamentals
* ETL / ELT concepts
* Git and GitHub
* Docker fundamentals
* Basic cloud concepts

---

# 💡 Best Practices

## 🌬️ Apache Airflow

* Keep DAGs modular and readable.
* Use meaningful DAG and task IDs.
* Keep business logic outside the DAG definition when appropriate.
* Avoid unnecessary tasks.
* Configure retries for transient failures.
* Use appropriate retry delays.
* Monitor task logs.
* Keep dependencies simple and explicit.

---

## 🐍 Python

* Use reusable functions.
* Follow consistent naming conventions.
* Avoid putting large amounts of business logic directly inside DAG files.
* Handle exceptions appropriately.
* Keep external credentials outside source code.

---

## 🔐 Connections & Security

* Use Airflow Connections for credentials.
* Never hardcode passwords or access keys.
* Use IAM roles where appropriate.
* Follow the Principle of Least Privilege.
* Separate development and production connections.

---

## ⚙️ DAG Design

* Design DAGs around business workflows.
* Keep tasks focused on a single responsibility.
* Avoid circular dependencies.
* Use Task Groups for complex workflows.
* Configure appropriate schedules.
* Make workflows restartable where possible.

---

## 📊 Monitoring

* Monitor DAG runs.
* Review task logs.
* Investigate failed tasks.
* Configure retries.
* Track execution duration.
* Monitor external-system failures.

---

# 📋 Repository Progress

```text
01  Airflow Fundamentals
 │
 ▼
02  Airflow Setup & First DAG
 │
 ▼
03  DAGs, Operators & Tasks
 │
 ▼
04  Hooks, Providers & Task Groups
 │
 ▼
05  Connections & External Systems
 │
 ▼
06  AWS / S3 Integration
 │
 ▼
07  Snowflake Integration
 │
 ▼
08  ETL / ELT Pipelines
 │
 ▼
09  Production Workflow Orchestration
```

---

# 🏗️ Practical Data Engineering Workflow

The concepts in this repository can be applied to an end-to-end EOD data pipeline:

```text
                         Massive API
                              │
                              ▼
                       Apache Airflow
                              │
                              ▼
                       Extract EOD Data
                              │
                              ▼
                         Local CSV
                              │
                              ▼
                         Amazon S3
                              │
                              ▼
                    Snowflake External Stage
                              │
                              ▼
                       Snowflake RAW
                              │
                              ▼
                       Snowflake CORE
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
                 DIMENSION             FACT
                    │                   │
                    └─────────┬─────────┘
                              ▼
                         Subject Area
                              │
                              ▼
                           Power BI
```

---

# 🎯 Repository Goal

The goal of this repository is to build a strong understanding of **Apache Airflow from fundamentals to practical Data Engineering workflow orchestration**.

The learning journey progresses from:

```text
Airflow Fundamentals
        │
        ▼
Airflow Setup
        │
        ▼
DAGs
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
Scheduling
        │
        ▼
Hooks
        │
        ▼
Providers
        │
        ▼
Task Groups
        │
        ▼
AWS / S3
        │
        ▼
Snowflake
        │
        ▼
ETL Pipelines
        │
        ▼
Production Workflows
```

This repository is intended to bridge the gap between **learning Airflow concepts** and building **practical Data Engineering orchestration pipelines**.

---

# 📚 Recommended Learning Order

Follow the modules in this order:

```text
1. Airflow Fundamentals
          │
          ▼
2. Airflow Setup & First DAG
          │
          ▼
3. DAGs, Operators & Tasks
          │
          ▼
4. Hooks, Providers & Task Groups
          │
          ▼
5. Airflow Connections
          │
          ▼
6. AWS / S3 Integration
          │
          ▼
7. Snowflake Integration
          │
          ▼
8. ETL / ELT Pipelines
          │
          ▼
9. Production Workflow Orchestration
```

---