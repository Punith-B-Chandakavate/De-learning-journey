# 🧵 Python Multithreading

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Multithreading](https://img.shields.io/badge/Multithreading-I%2FO%20Bound-2EA44F)
![Threading](https://img.shields.io/badge/Threading-Concurrency-FFB000)
![ThreadPoolExecutor](https://img.shields.io/badge/ThreadPoolExecutor-Thread%20Pool-6F42C1)

A practical guide to **Python Multithreading**, covering threads, I/O-bound workloads, thread lifecycle, synchronization, the Python GIL, `ThreadPoolExecutor`, real-world API examples, and interview preparation.

---

# 📚 Overview

**Multithreading** allows multiple threads to execute within the same Python process.

Threads are particularly useful for **I/O-bound tasks**, where the program spends significant time waiting for external operations such as:

- 🌐 API requests
- 🗄️ Database queries
- 📁 File operations
- 🌍 Network requests
- 📥 Downloading files
- 🔌 Blocking external services

```text
                    Python Process
                          │
            ┌─────────────┼─────────────┐
            │             │             │
            ▼             ▼             ▼
        Thread 1      Thread 2      Thread 3
            │             │             │
          API Call     DB Query      File I/O
            │             │             │
         Waiting       Waiting       Waiting
            │             │             │
            └─────────────┼─────────────┘
                          │
                       Results
```

The main idea is that while one thread is **waiting for I/O**, another thread can make progress.

---

# 🎯 Learning Objectives

By completing this module, you will understand:

- 🧵 What a thread is
- 🔄 How multithreading works
- 🚦 Thread lifecycle
- ▶️ `start()`
- ⏳ `join()`
- 💾 Shared memory
- ⚠️ Race conditions
- 🔐 Locks and synchronization
- 🌐 I/O-bound workloads
- 🔒 Python GIL
- 🚀 `ThreadPoolExecutor`
- 📊 Multithreading vs multiprocessing
- ⚡ Multithreading vs `asyncio`
- 🎤 Multithreading interview questions

---

# 🧠 What is Multithreading?

A **thread** is a lightweight unit of execution inside a process.

Multiple threads can exist inside the same process and share the process's memory.

```text
                    Process
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Thread 1     Thread 2     Thread 3
          │            │            │
          ▼            ▼            ▼
       Task 1       Task 2       Task 3
```

### Simple Example

```python
import threading
import time


def download(file):
    print(f"Downloading {file}")

    time.sleep(2)

    print(f"Finished {file}")


threads = []

files = ["file1", "file2", "file3"]

for file in files:

    thread = threading.Thread(
        target=download,
        args=(file,)
    )

    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()
```

Here, three threads are created and started.

```text
Thread 1 ──► file1 ── waiting ──► finished
Thread 2 ──► file2 ── waiting ──► finished
Thread 3 ──► file3 ── waiting ──► finished
```

---

# 🔄 Why Use Multithreading?

Consider three API requests.

### Sequential Execution

```text
API 1
 │
 ▼
Wait
 │
 ▼
API 2
 │
 ▼
Wait
 │
 ▼
API 3
 │
 ▼
Wait
```

Each operation waits before the next one starts.

### Multithreading

```text
API 1 ──► Waiting ─────────► Result
API 2 ──► Waiting ─────────► Result
API 3 ──► Waiting ─────────► Result
```

While one thread is waiting for an API response, another thread can perform work.

This makes multithreading useful for I/O-bound workloads. Pasted markdown(20261005-063950)

---

# 🌐 I/O-Bound Workloads

An **I/O-bound task** spends a significant amount of time waiting for external operations.

Examples:

```text
🌐 API Request
       │
       ▼
   Waiting for
    response


🗄️ Database Query
       │
       ▼
   Waiting for
    database


📁 File Operation
       │
       ▼
   Waiting for
      disk


🌍 Network Request
       │
       ▼
   Waiting for
     network
```

### Common I/O-bound Tasks

| Task | Example |
|---|---|
| 🌐 API | REST API request |
| 🗄️ Database | SQL query |
| 📁 File | Read/write files |
| 🌍 Network | Download data |
| 📥 Download | Download multiple files |
| 🔌 External service | Blocking service call |

---

# 🧩 Thread Lifecycle

A thread generally moves through different states during execution.

```text
                 Create Thread
                      │
                      ▼
                  🟡 New
                      │
                   start()
                      │
                      ▼
                  🟢 Running
                      │
            ┌─────────┴─────────┐
            │                   │
            ▼                   ▼
         Waiting             Running
            │                   │
            └─────────┬─────────┘
                      │
                      ▼
                  🔵 Finished
```

### Creating a Thread

```python
thread = threading.Thread(
    target=download,
    args=("file1",)
)
```

### Starting a Thread

```python
thread.start()
```

### Waiting for a Thread

```python
thread.join()
```

`join()` allows the main thread to wait until the worker thread finishes.

---

# ▶️ `start()` vs `join()`

### `start()`

Starts the execution of the thread.

```python
thread.start()
```

### `join()`

Waits for the thread to complete.

```python
thread.join()
```

Example:

```python
thread.start()

print("Main thread continues...")

thread.join()

print("Thread finished")
```

Conceptually:

```text
Main Thread
    │
    ├── start()
    │
    ▼
Worker Thread
    │
    ├── executes task
    │
    ▼
  finished
    │
    ▼
 join()
    │
    ▼
Main Thread continues
```

---

# 💾 Shared Memory

Threads within the same process can access shared data.

```text
                 Process Memory
                       │
          ┌────────────┼────────────┐
          │            │            │
       Thread 1     Thread 2     Thread 3
          │            │            │
          └────────────┼────────────┘
                       │
                  Shared Data
```

This makes communication between threads relatively convenient.

However, shared data can introduce problems.

---

# ⚠️ Race Conditions

A **race condition** can occur when multiple threads access and modify shared data at the same time.

Example:

```python
counter = 0


def increment():
    global counter

    for _ in range(100000):
        counter += 1
```

If multiple threads modify `counter`, the final result may not behave as expected because multiple threads are accessing shared state.

```text
Thread 1 ──┐
           │
           ├──► Shared Variable
           │
Thread 2 ──┤
           │
           └──► Shared Variable
```

This is why synchronization mechanisms may be required.

---

# 🔐 Locks

A **lock** can be used to protect shared resources.

```python
import threading


counter = 0

lock = threading.Lock()


def increment():

    global counter

    for _ in range(100000):

        with lock:
            counter += 1
```

Conceptually:

```text
Thread 1 ──► 🔒 Lock ──► Shared Resource ──► Unlock
Thread 2 ──► Waiting
Thread 3 ──► Waiting
```

Only the thread holding the lock can enter the protected section.

---

# 🧰 ThreadPoolExecutor

For practical applications, manually creating and managing many threads can become inconvenient.

Python provides:

```python
from concurrent.futures import ThreadPoolExecutor
```

`ThreadPoolExecutor` manages a pool of worker threads.

---

# 🚀 ThreadPoolExecutor Example

```python
from concurrent.futures import ThreadPoolExecutor
import time


def fetch_data(task):

    print(f"Processing {task}")

    time.sleep(2)

    return f"{task} completed"


tasks = [
    "API-1",
    "API-2",
    "API-3",
    "API-4"
]


with ThreadPoolExecutor(max_workers=4) as executor:

    results = executor.map(
        fetch_data,
        tasks
    )


for result in results:
    print(result)
```

Execution:

```text
                 ThreadPoolExecutor
                         │
             ┌───────────┼───────────┐
             │           │           │
             ▼           ▼           ▼
          Worker 1    Worker 2    Worker 3
             │           │           │
           API-1       API-2       API-3
                         │
                       Worker 4
                         │
                       API-4
```

---

# 📊 `Thread` vs `ThreadPoolExecutor`

| Feature | `threading.Thread` | `ThreadPoolExecutor` |
|---|---|---|
| Thread creation | Manual | Automatic |
| Thread management | Manual | Managed |
| Reuse threads | ❌ | ✅ |
| Suitable for many tasks | ⚠️ | ✅ |
| Code simplicity | Medium | Simple |
| Common production usage | Sometimes | Frequently |

For multiple similar I/O operations, `ThreadPoolExecutor` is often a convenient choice.

---

# 🌐 Practical API Example

Suppose you need to call multiple APIs.

```python
from concurrent.futures import ThreadPoolExecutor
import requests


def fetch_data(url):

    response = requests.get(url)

    return response.json()


urls = [
    "https://api.example.com/1",
    "https://api.example.com/2",
    "https://api.example.com/3",
]


with ThreadPoolExecutor(max_workers=3) as executor:

    results = executor.map(
        fetch_data,
        urls
    )
```

Architecture:

```text
                 API Requests
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
       Thread 1    Thread 2    Thread 3
          │           │           │
        API 1       API 2       API 3
          │           │           │
          └───────────┼───────────┘
                      │
                      ▼
                   Results
```

This is a typical example of using multithreading for blocking I/O operations. Pasted markdown(20261005-063950)

---

# 🔒 Understanding the Python GIL

The **GIL (Global Interpreter Lock)** is an important concept when discussing Python multithreading.

In standard CPython, the GIL allows only one thread at a time to execute Python bytecode within a process.

```text
                 Python Process
                       │
                     GIL 🔒
                       │
             ┌─────────┴─────────┐
             │                   │
          Thread 1            Thread 2
             │                   │
       Python bytecode    Python bytecode
             │                   │
             └────── one at a time ──────┘
```

### Why Threads Still Help With I/O

For I/O-bound operations:

```text
Thread 1
   │
API Request
   │
Waiting ───────────────┐
                      │
Thread 2               │
   │                   │
API Request            │
   │                   │
Processing             │
   │                   │
   └───────────────────┘
```

The thread can spend time waiting for I/O while another thread makes progress.

Therefore:

> **I/O-bound → Multithreading can be useful**

> **CPU-bound Python code → Multiprocessing is generally preferred**

The important distinction is that it is too broad to say "multithreading cannot run in parallel." A better explanation is that standard CPython's GIL prevents multiple threads from executing Python bytecode simultaneously, while threads can still provide useful I/O concurrency. Pasted markdown(20261005-063950)

---

# 🧵 Multithreading vs Multiprocessing

| Feature | 🧵 Multithreading | ⚙️ Multiprocessing |
|---|---|---|
| Unit | Thread | Process |
| Memory | Shared | Separate |
| Best for | I/O-bound | CPU-bound |
| GIL | Relevant | Each process has its own interpreter/GIL |
| Communication | Easier | More expensive |
| Resource usage | Lower | Higher |
| API calls | ✅ | ⚠️ |
| File I/O | ✅ | ⚠️ |
| Database I/O | ✅ | ⚠️ |
| Heavy calculations | ❌ | ✅ |
| Image processing | ❌ | ✅ |

The core distinction is:

> **Multithreading uses multiple threads inside the same process, while multiprocessing uses multiple independent processes.** Pasted markdown(20261005-063950)

---

# ⚡ Multithreading vs Asyncio

Both multithreading and `asyncio` are useful for I/O-bound workloads, but their concurrency models are different.

| Feature | 🧵 Multithreading | ⚡ Asyncio |
|---|---|---|
| Concurrency model | Multiple threads | Async tasks |
| Scheduler | OS / runtime | Event loop |
| Syntax | Normal functions | `async` / `await` |
| Best for | Blocking I/O | Many async I/O operations |
| Threads | Multiple | Usually one thread |
| Memory overhead | Higher | Lower |
| Blocking code | Can handle it | Can block the event loop |
| Example | `requests`, files, DB drivers | Async HTTP, WebSockets |

### Easy Memory Trick

```text
🧵 Multithreading
       │
       ▼
Multiple Threads
       │
       ▼
Blocking I/O
       │
       ▼
ThreadPoolExecutor


⚡ Asyncio
       │
       ▼
Event Loop
       │
       ▼
async / await
       │
       ▼
Non-blocking I/O
```

Pasted markdown(20261005-063950)

---

# 🌐 Multithreading vs Asyncio — 1,000 APIs

Suppose an application needs to call **1,000 APIs**.

### Multithreading

```text
1,000 API Requests
        │
        ▼
ThreadPoolExecutor
        │
        ▼
20 / 50 Threads
        │
        ▼
API Responses
```

### Asyncio

```text
1,000 API Requests
        │
        ▼
Asyncio Event Loop
        │
        ▼
Async Tasks
        │
        ▼
API Responses
```

For a very high number of I/O operations, `asyncio` can be more efficient because it does not require maintaining a large number of threads. Pasted markdown(20261005-063950)

---

# 🎯 When Should You Use Multithreading?

Use multithreading when you have existing **blocking or synchronous code**.

### Good Use Cases

```text
🌐 requests
📁 File operations
🗄️ Database drivers
📦 Legacy libraries
🔌 Blocking APIs
🌍 Network requests
📥 File downloads
```

Example:

```python
from concurrent.futures import ThreadPoolExecutor


def fetch_data(url):
    # Blocking API call
    ...


with ThreadPoolExecutor(max_workers=5) as executor:

    results = executor.map(
        fetch_data,
        urls
    )
```

Pasted markdown(20261005-063950)

---

# ❌ When Not to Use Multithreading

Multithreading is generally not the first choice for heavy CPU-bound Python workloads.

Examples:

```text
🧮 Heavy calculations
🖼️ Image processing
🎥 Video processing
🤖 CPU-intensive ML computation
```

For these workloads, multiprocessing is generally more appropriate because separate processes can execute CPU-heavy Python code independently. Pasted markdown(20261005-063950)

---

# 🎤 Interview Questions

## 🧵 Basic Questions

### 1. What is multithreading?

**Answer:**

Multithreading is a concurrency technique where multiple threads execute within the same process. It is especially useful for I/O-bound tasks such as API calls, database operations, file operations, and network requests.

---

### 2. What is an I/O-bound task?

An I/O-bound task spends significant time waiting for external operations.

Examples:

- API requests
- Database queries
- File operations
- Network requests

---

### 3. What is the GIL?

The **Global Interpreter Lock** in standard CPython allows only one thread at a time to execute Python bytecode within a process.

However, threads can still be useful for I/O-bound operations because they can overlap waiting periods.

---

### 4. Why is multithreading useful for I/O-bound tasks?

When one thread is waiting for an external operation such as an API or database response, another thread can perform useful work.

---

### 5. What is `ThreadPoolExecutor`?

`ThreadPoolExecutor` provides a convenient way to manage a pool of worker threads and execute multiple tasks concurrently.

---

# 🎤 Interview: Multithreading vs Multiprocessing

### Question

> **When would you use multithreading vs multiprocessing in Python?**

### Answer

> "I would use multithreading mainly for I/O-bound tasks such as API calls, database operations, file processing, and network requests. I would use multiprocessing for CPU-bound tasks such as heavy calculations or image processing, because multiprocessing creates separate processes with separate Python interpreters and avoids the GIL limitation."

Pasted markdown(20261005-063950)

---

# 🎤 Interview: Multithreading vs Asyncio

### Question

> **What is the difference between multithreading and asyncio?**

### Answer

> "Both are useful for I/O-bound tasks. Multithreading uses multiple threads, while asyncio uses an event loop to manage asynchronous tasks, usually within a single thread. In asyncio, `await` allows the event loop to switch to other tasks while one task is waiting for I/O. I would use multithreading when working with blocking or synchronous libraries, and asyncio when the application and libraries support asynchronous I/O."

Pasted markdown(20261005-063950)

---

# 🧠 Quick Decision Guide

```text
                 What type of task?
                         │
             ┌───────────┴───────────┐
             │                       │
          I/O Bound              CPU Bound
             │                       │
       ┌─────┴─────┐                 │
       │           │                 │
      🧵          ⚡                ⚙️
  Multithreading Asyncio       Multiprocessing
       │           │                 │
 Blocking I/O   Async I/O       Heavy CPU work
```

### Remember

> 🧵 **Blocking I/O → Multithreading**

> ⚡ **Many async I/O operations → Asyncio**

> ⚙️ **CPU-intensive work → Multiprocessing**

---

# 🛠️ Practice Exercises

### Exercise 1 — Basic Threads

Create three threads that print:

```text
Thread 1 started
Thread 2 started
Thread 3 started
```

---

### Exercise 2 — File Downloads

Create multiple threads to simulate downloading multiple files.

```python
files = [
    "file1.csv",
    "file2.csv",
    "file3.csv",
    "file4.csv"
]
```

---

### Exercise 3 — API Requests

Use `ThreadPoolExecutor` to call multiple APIs concurrently.

```text
API 1
API 2
API 3
API 4
API 5
```

---

### Exercise 4 — Database Queries

Simulate multiple database operations using a thread pool.

```text
Query 1
Query 2
Query 3
Query 4
```

---

### Exercise 5 — Race Condition

Create multiple threads that modify the same shared variable.

Then fix the problem using:

```python
threading.Lock()
```

---

### Exercise 6 — Compare Execution

Compare:

```text
Sequential
    vs
Multithreading
```

Measure execution time for multiple I/O operations.

---

# 📈 Learning Path

```text
🧵 Multithreading
       │
       ▼
Understand Threads
       │
       ▼
start() / join()
       │
       ▼
I/O-Bound Workloads
       │
       ▼
Shared Memory
       │
       ▼
Race Conditions
       │
       ▼
Locks
       │
       ▼
Python GIL
       │
       ▼
ThreadPoolExecutor
       │
       ▼
Real-World API Example
       │
       ▼
Interview Preparation
```

---

# 📌 Key Takeaways

```text
🧵 Multithreading
        │
        ▼
Multiple Threads
        │
        ▼
Same Process
        │
        ▼
Shared Memory
        │
        ▼
Best for I/O-bound Work
        │
        ▼
ThreadPoolExecutor
```