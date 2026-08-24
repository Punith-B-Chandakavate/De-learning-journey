# 🌬️ Apache Airflow — Windows Docker Setup

![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Workflow%20Orchestration-017CEE?logo=apacheairflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Desktop-2496ED?logo=docker&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-Docker%20Desktop-0078D4?logo=windows&logoColor=white)
![WSL2](https://img.shields.io/badge/WSL2-Enabled-0078D4?logo=linux&logoColor=white)

> 🛠️ A complete step-by-step guide to install and run **Apache Airflow locally on Windows using Docker Desktop and Docker Compose**.

---

# 📌 Table of Contents

* 🎯 Objective
* 🏗️ Setup Architecture
* 💻 Prerequisites
* 🐳 Step 1 — Install Docker Desktop
* 🐧 Step 2 — Enable WSL 2
* 📁 Step 3 — Create Project Directory
* 📥 Step 4 — Download Airflow Docker Compose File
* 📂 Step 5 — Create Required Directories
* ⚙️ Step 6 — Configure Airflow User
* 🗄️ Step 7 — Initialize Airflow Database
* 🚀 Step 8 — Start Airflow
* 🌐 Step 9 — Access Airflow UI
* 📊 Step 10 — Add DAGs
* 📋 Useful Docker Commands
* 🐛 Troubleshooting
* 🧩 Common DAG Issues
* 🔄 Complete Workflow
* 🎯 Next Steps
* 🏆 Summary

---

# 🎯 Objective

The goal of this setup is to run **Apache Airflow locally on Windows using Docker**.

After completing this guide, you will have:

```text
🪟 Windows
    │
    ▼
🐳 Docker Desktop
    │
    ▼
📦 Airflow Docker Compose
    │
    ▼
🌬️ Apache Airflow
    │
    ▼
🌐 Airflow UI
    │
    ▼
📊 DAGs
```

This setup allows you to start creating DAGs and experimenting with data workflows locally.

---

# 🏗️ Setup Architecture

```text
                    🪟 Windows
                        │
                        ▼
                  🐳 Docker Desktop
                        │
                        ▼
                       WSL2
                        │
                        ▼
              📄 docker-compose.yaml
                        │
            ┌───────────┴───────────┐
            │                       │
            ▼                       ▼
       airflow-init            Airflow Services
            │                       │
            ▼                       ▼
      🗄️ Initialize DB         🌬️ Airflow
                                    │
                                    ▼
                              🌐 localhost:8080
                                    │
                                    ▼
                               📊 DAGs
```

### 🔄 Data Engineering Workflow

```text
Create DAG
    ↓
Place Python file in dags/
    ↓
Airflow detects DAG
    ↓
DAG appears in Airflow UI
    ↓
Trigger / Schedule DAG
    ↓
Execute Tasks
    ↓
Monitor Workflow
```

---

# 💻 Prerequisites

Before installing Airflow, make sure you have:

- 🪟 Windows
- 🐳 Docker Desktop
- 🐧 WSL 2
- 💻 Command Prompt or PowerShell
- 🌐 Web browser

---

# 🐳 Step 1 — Install Docker Desktop

Download **Docker Desktop for Windows** from:

[Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Installation

1. Download Docker Desktop.
2. Run the installer.
3. Follow the setup wizard.
4. Restart your computer if prompted.
5. Launch Docker Desktop.
6. Confirm that Docker is running.

You should see the Docker icon in the Windows system tray.

### ✅ Verify Docker

Open PowerShell or Command Prompt:

```powershell
docker --version
```

Also verify Docker Compose:

```powershell
docker compose version
```

Expected output will show installed Docker and Compose versions.

---

# 🐧 Step 2 — Enable WSL 2

Docker Desktop on Windows uses **WSL 2 (Windows Subsystem for Linux)**.

If WSL 2 is not already enabled:

1. Open Docker Desktop.
2. Follow the prompt to enable WSL 2.
3. Complete the WSL 2 setup.
4. Restart if requested.

### 🧠 Setup Flow

```text
🪟 Windows
    │
    ▼
🐧 WSL 2
    │
    ▼
🐳 Docker Desktop
    │
    ▼
🌬️ Airflow
```

> 📌 Docker Desktop may prompt you to enable WSL 2 when required.

---

# 📁 Step 3 — Create Project Directory

Open **Command Prompt** or **PowerShell**.

Create the Airflow project directory:

```powershell
mkdir airflow-docker
cd airflow-docker
```

Your project directory is now:

```text
airflow-docker/
```

---

# 📥 Step 4 — Download Airflow Docker Compose File

Download the official Airflow Docker Compose file:

```powershell
curl -LfO "https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml"
```

After downloading, verify:

```powershell
dir
```

You should see:

```text
docker-compose.yaml
```

### 📌 Project Flow

```text
airflow-docker/
    │
    └── docker-compose.yaml
```

---

# 📂 Step 5 — Create Required Directories

Create the directories required by the Airflow Docker setup:

```powershell
mkdir dags
mkdir logs
mkdir plugins
mkdir config
```

Your project now looks like:

```text
airflow-docker/
│
├── docker-compose.yaml
│
├── dags/
│
├── logs/
│
├── plugins/
│
└── config/
```

### 📌 Directory Purpose

| Directory | Purpose |
|---|---|
| `dags/` | 📊 Airflow DAG files |
| `logs/` | 📜 Airflow logs |
| `plugins/` | 🧩 Airflow plugins |
| `config/` | ⚙️ Airflow configuration |
| `docker-compose.yaml` | 🐳 Docker Compose configuration |

---

# ⚙️ Step 6 — Configure Airflow User

Create a `.env` file inside the `airflow-docker` directory.

```text
airflow-docker/
│
├── .env
├── docker-compose.yaml
├── dags/
├── logs/
├── plugins/
└── config/
```

Add:

```env
AIRFLOW_UID=50000
```

### 📌 Why This Is Required

The Docker setup uses the Airflow user ID to help manage file permissions between the host machine and Airflow containers.

> 🔐 Keep the `.env` file local to your environment unless you intentionally want to share it.

---

# 🗄️ Step 7 — Initialize Airflow Database

Run:

```powershell
docker compose up airflow-init
```

Docker will initialize the Airflow database and prepare the environment.

Wait until you see:

```text
airflow-init exited with code 0
```

### ✅ Expected Flow

```text
docker compose up airflow-init
              │
              ▼
       🐳 Start init container
              │
              ▼
       🗄️ Initialize database
              │
              ▼
       ⚙️ Prepare Airflow
              │
              ▼
       ✅ exited with code 0
```

> ⚠️ Do not continue until the initialization process completes successfully.

---

# 🚀 Step 8 — Start Airflow

Start all Airflow services:

```powershell
docker compose up
```

Docker Compose will start the Airflow environment.

You will see container logs in the terminal.

### 🔄 Startup Flow

```text
docker compose up
        │
        ▼
🐳 Start Airflow containers
        │
        ▼
⚙️ Airflow services initialize
        │
        ▼
🌐 Web service becomes available
        │
        ▼
📊 Airflow UI
```

Wait a few minutes for the services to become ready.

---

# 🌐 Step 9 — Access Airflow UI

Open your browser:

```text
http://localhost:8080
```

### 🔐 Default Login

According to this setup guide:

```text
Username: airflow
Password: airflow
```

### 🌐 Access Flow

```text
🌐 Browser
     │
     ▼
localhost:8080
     │
     ▼
🌬️ Apache Airflow
     │
     ▼
📊 DAG Dashboard
```

---

# 📊 Step 10 — Add DAGs

Place your Python DAG files inside:

```text
airflow-docker/dags/
```

Example:

```text
airflow-docker/
│
├── dags/
│   └── hello_airflow.py
│
├── logs/
├── plugins/
├── config/
├── .env
└── docker-compose.yaml
```

Airflow will automatically detect DAG files placed in the `dags` directory.

The source setup notes that DAG detection may take approximately **1–2 minutes**.

---

# 🧪 Example DAG

Create:

```text
dags/hello_airflow.py
```

Example:

```python
from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


def say_hello():
    print("Hello from Apache Airflow!")


with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )
```

After saving the file:

```text
dags/
   │
   └── hello_airflow.py
          │
          ▼
     Airflow detects DAG
          │
          ▼
      Airflow UI
          │
          ▼
     hello_airflow
```

---

# ▶️ Run Your DAG

Open:

```text
http://localhost:8080
```

Find:

```text
hello_airflow
```

Then trigger the DAG from the Airflow UI.

### 🔄 DAG Execution

```text
📄 DAG File
    ↓
📊 Airflow UI
    ↓
▶️ Trigger
    ↓
⚙️ Task Execution
    ↓
📜 Logs
    ↓
✅ Success
```

---

# 📋 Useful Docker Commands

## 🛑 Stop Airflow

Stop the running Airflow services:

```powershell
docker compose down
```

---

## 🚀 Start Airflow in Background

Run Airflow in detached mode:

```powershell
docker compose up -d
```

This allows the terminal to remain available while Airflow runs in the background.

---

## 📜 View Logs

View Docker Compose logs:

```powershell
docker compose logs
```

Follow logs continuously:

```powershell
docker compose logs -f
```

---

## 📦 Check Running Containers

```powershell
docker compose ps
```

This is useful for checking whether the Airflow services are running.

---

## 🛑 Stop and Remove Volumes

For a clean reset:

```powershell
docker compose down --volumes --remove-orphans
```

> ⚠️ **Warning:** This removes Docker volumes associated with the Compose project. Use this only when you intentionally want to reset the environment.

---

# 🐛 Troubleshooting

## ❌ Port 8080 Already in Use

If:

```text
http://localhost:8080
```

cannot be opened because another service is using port `8080`, edit:

```text
docker-compose.yaml
```

and change the port mapping.

Then restart:

```powershell
docker compose down
docker compose up
```

---

# 🐳 Docker Not Starting

If Docker is not starting:

### Check Docker Desktop

Make sure Docker Desktop is running.

### Check virtualization

Verify that hardware virtualization is enabled in your computer's BIOS.

### Verify from PowerShell

```powershell
docker --version
```

Then:

```powershell
docker compose version
```

---

# 🐌 Slow Performance

If Airflow is running slowly:

Open:

```text
Docker Desktop
    ↓
Settings
    ↓
Resources
```

Allocate more resources to Docker Desktop.

### 🧠 Performance Flow

```text
🐳 Docker Desktop
       │
       ▼
⚙️ Resources
       │
       ├── CPU
       ├── Memory
       └── Disk
```

---

# 📊 DAG Not Appearing

If your DAG does not appear in the Airflow UI:

### 1️⃣ Check DAG Location

Make sure the Python file is inside:

```text
airflow-docker/dags/
```

### 2️⃣ Check Python Syntax

Verify that your DAG contains no syntax errors.

### 3️⃣ Check Airflow UI

Verify whether the DAG is paused.

Toggle the DAG switch in the UI if necessary.

### 4️⃣ Wait for Detection

Allow approximately:

```text
1–2 minutes
```

for Airflow to detect the DAG.

### 🔍 Troubleshooting Flow

```text
DAG not visible
      │
      ▼
Check dags/ directory
      │
      ▼
Check Python syntax
      │
      ▼
Check DAG paused status
      │
      ▼
Wait 1–2 minutes
      │
      ▼
Refresh Airflow UI
```

---

# 🧩 Common DAG Issues

## 📦 Deprecated Imports

For the Airflow version used by this setup, use:

```python
from airflow.providers.standard.operators.python import PythonOperator
```

instead of the older import:

```python
from airflow.operators.python import PythonOperator
```

### ❌ Older Import

```python
from airflow.operators.python import PythonOperator
```

### ✅ Recommended Import

```python
from airflow.providers.standard.operators.python import PythonOperator
```

---

# ⏰ Scheduling Changes

Use:

```python
schedule="@daily"
```

instead of:

```python
schedule_interval="@daily"
```

### Example

```python
with DAG(
    dag_id="daily_etl",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    ...
```

---

### 📌 Git Recommendation

For a GitHub Data Engineering repository, keep your project structure clean and avoid committing generated Airflow logs or sensitive environment values.

Example:

```text
07_Apache_Airflow_Setup/
│
├── README.md
├── docker-compose.yaml
├── dags/
├── plugins/
└── config/
```

---

# 🔄 Complete Setup Workflow

```text
┌───────────────────────────────┐
│ 🪟 Windows                    │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 🐳 Install Docker Desktop     │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 🐧 Enable WSL 2               │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 📁 Create airflow-docker/     │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 📥 Download docker-compose    │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 📂 Create dags/logs/plugins   │
│    and config directories     │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ ⚙️ Create .env                │
│    AIRFLOW_UID=50000          │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 🗄️ docker compose up          │
│    airflow-init               │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 🚀 docker compose up          │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 🌐 localhost:8080             │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ 📊 Add DAGs to dags/          │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│ ▶️ Trigger & Monitor DAG      │
└───────────────────────────────┘
```

---

# 🔐 Security Notes

- 🔒 Do not commit passwords or credentials.
- 🔒 Review `.env` before committing it to Git.
- 🔒 Do not put cloud credentials directly inside DAG Python files.
- 🧩 Keep development configuration separate from production configuration.
- 🐳 Use Docker Desktop only for local development/testing in this setup.

---

# 💡 Best Practices

### 📁 Project Organization

- ✅ Keep DAGs inside `dags/`.
- ✅ Keep reusable Python logic separate from DAG definitions.
- ✅ Use meaningful DAG and task names.
- ✅ Keep Docker Compose configuration under version control when appropriate.

### 🧪 DAG Development

- ✅ Validate Python syntax.
- ✅ Check the Airflow UI after adding a DAG.
- ✅ Check logs when a task fails.
- ✅ Use task dependencies to build clear workflows.

### 🐳 Docker

- ✅ Make sure Docker Desktop is running before starting Airflow.
- ✅ Use `docker compose ps` to check service status.
- ✅ Use `docker compose logs` when troubleshooting.
- ✅ Use `docker compose down --volumes --remove-orphans` only when you intentionally want a clean reset.

---

# 🎤 Interview Questions

### 1. Why use Docker to run Airflow on Windows?

Docker provides a consistent containerized environment and avoids relying on a native Windows Airflow installation.

### 2. What is WSL 2?

WSL 2 provides a Linux environment on Windows and is used by Docker Desktop for its Linux-based container environment.

### 3. What is `docker-compose.yaml`?

It defines the services, configuration, networking, volumes, and other settings required to run the Airflow environment with Docker Compose.

### 4. Why run `airflow-init` first?

The initialization step prepares the Airflow database and environment before the main services are started.

### 5. What does this command do?

```powershell
docker compose up airflow-init
```

It starts the Airflow initialization service.

### 6. How do you start Airflow?

```powershell
docker compose up
```

Or in the background:

```powershell
docker compose up -d
```

### 7. How do you stop Airflow?

```powershell
docker compose down
```

### 8. How do you see Docker logs?

```powershell
docker compose logs
```

### 9. Where do you place DAG files?

```text
dags/
```

### 10. What should you check if a DAG does not appear?

Check:

```text
dags/ directory
      ↓
Python syntax
      ↓
DAG paused status
      ↓
Wait for Airflow detection
```

---

# 📋 Quick Reference

| Action | Command |
|---|---|
| 🐳 Docker version | `docker --version` |
| 📦 Compose version | `docker compose version` |
| 📁 Create project | `mkdir airflow-docker` |
| 📥 Download Compose | `curl -LfO "https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml"` |
| 🗄️ Initialize | `docker compose up airflow-init` |
| 🚀 Start | `docker compose up` |
| 🚀 Start background | `docker compose up -d` |
| 📊 Check containers | `docker compose ps` |
| 📜 View logs | `docker compose logs` |
| 📜 Follow logs | `docker compose logs -f` |
| 🛑 Stop | `docker compose down` |
| 🧹 Clean reset | `docker compose down --volumes --remove-orphans` |
| 🌐 Airflow UI | `http://localhost:8080` |

---

# 🎯 Next Steps

Once Airflow is running:

1. 📊 Create your first DAG.
2. 🌐 Explore the Airflow UI.
3. 🧱 Learn task dependencies.
4. 🔄 Learn scheduling.
5. 🔁 Learn retries and failure handling.
6. 📜 Learn task logging.
7. 🔌 Experiment with different operators.
8. 🏗️ Build a small ETL pipeline.
9. ☁️ Connect Airflow with AWS/Azure services.
10. 🚀 Build a production-style Data Engineering workflow.

---

# 🏆 Summary

You now have a local Apache Airflow environment running on Windows using Docker.

```text
🪟 Windows
    │
    ▼
🐳 Docker Desktop
    │
    ▼
🐧 WSL2
    │
    ▼
📦 Docker Compose
    │
    ▼
🌬️ Apache Airflow
    │
    ▼
🌐 localhost:8080
    │
    ▼
📊 DAGs
    │
    ▼
⚙️ Tasks
    │
    ▼
📜 Logs
    │
    ▼
✅ Data Workflow
```

> 🚀 **Key Takeaway:** The basic setup is **Docker Desktop → WSL2 → Airflow Docker Compose → `airflow-init` → `docker compose up` → `localhost:8080` → DAGs**.

---

# 📚 References

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Apache Airflow Docker Documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
- [Apache Airflow Docker Compose File](https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
