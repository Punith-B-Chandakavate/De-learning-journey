# ⚙️ Python Multiprocessing

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Multiprocessing](https://img.shields.io/badge/Multiprocessing-CPU%20Bound-D73A49)
![Parallel Processing](https://img.shields.io/badge/Parallel%20Processing-CPU-FFB000)
![ProcessPoolExecutor](https://img.shields.io/badge/ProcessPoolExecutor-Process%20Pool-6F42C1)

A practical guide to **Python Multiprocessing**, covering processes, CPU-bound workloads, process lifecycle, separate memory, the Python GIL, `ProcessPoolExecutor`, real-world examples, comparisons, and interview preparation.

---

# 📚 Overview

**Multiprocessing** allows a Python application to execute work using multiple independent processes.

Unlike multithreading, each process has its own:

- 🧠 Memory space
- 🐍 Python interpreter
- 🔒 GIL
- ⚙️ Execution context

Multiprocessing is particularly useful for **CPU-bound workloads**, where the application spends significant time performing calculations or other computational work.

```text
                    Operating System
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
         Process 1     Process 2     Process 3
             │             │             │
        Interpreter   Interpreter   Interpreter
             │             │             │
           CPU 1         CPU 2         CPU 3
```

---

# 🎯 Learning Objectives

By completing this module, you will understand:

- ⚙️ What multiprocessing is
- 🧩 What a process is
- 🔄 Process lifecycle
- ▶️ `start()`
- ⏳ `join()`
- 🧠 Separate process memory
- 🧮 CPU-bound workloads
- 🔒 Multiprocessing and the GIL
- 📦 Process communication concepts
- 🚀 `ProcessPoolExecutor`
- ⚡ Parallel CPU execution
- 🧵 Multiprocessing vs multithreading
- ⚡ Multiprocessing vs asyncio
- 🎤 Multiprocessing interview questions

---

# 🧠 What is Multiprocessing?

**Multiprocessing** uses multiple independent processes to execute tasks.

Each process has its own Python interpreter and memory space.

```text id="q9w1pc"
                 Application
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
      Process 1    Process 2    Process 3
          │           │           │
          ▼           ▼           ▼
        Task 1      Task 2      Task 3
```

Unlike threads, processes do not normally share the same memory space.

This makes processes more isolated but also makes communication between them more involved.

---

# 🧮 CPU-Bound Workloads

A **CPU-bound task** spends most of its time performing computation.

Examples include:

```text id="n1y4xq"
🧮 Heavy Calculations
        │
        ▼
🖼️ Image Processing
        │
        ▼
🎥 Video Processing
        │
        ▼
🤖 ML Computation
        │
        ▼
⚙️ CPU-intensive Transformations
```

### Common CPU-Bound Tasks

| Task | Example |
|---|---|
| 🧮 Calculations | Mathematical computation |
| 🖼️ Images | Image processing |
| 🎥 Video | Video processing |
| 🤖 ML | CPU-heavy computation |
| 🔢 Algorithms | Computational algorithms |
| 🔄 Transformation | CPU-intensive transformations |

---

# 🔄 Why Use Multiprocessing?

Consider a CPU-heavy calculation.

### Sequential Execution

```text id="v7y2sc"
Task 1
  │
  ▼
CPU
  │
  ▼
Finished
  │
  ▼
Task 2
  │
  ▼
CPU
  │
  ▼
Finished
```

Tasks execute one after another.

### Multiprocessing

```text id="x4u8vn"
                CPU Work
                   │
       ┌───────────┼───────────┐
       │           │           │
       ▼           ▼           ▼
    Process 1   Process 2   Process 3
       │           │           │
      CPU 1       CPU 2       CPU 3
```

Independent processes can execute CPU-heavy Python code in parallel because each process has its own Python interpreter and GIL. Pasted markdown(20261005-063950)

---

# 🧩 Process Lifecycle

A simplified process lifecycle looks like:

```text id="x5r4gs"
                Create Process
                     │
                     ▼
                  🟡 New
                     │
                  start()
                     │
                     ▼
                 🟢 Running
                     │
                     ▼
                  Execute
                     │
                     ▼
                 🔵 Finished
```

---

# ▶️ Creating a Process

Python provides the `multiprocessing` module.

```python id="y9r6tt"
from multiprocessing import Process


def calculate(n):

    total = 0

    for i in range(n):
        total += i

    print(total)


process = Process(
    target=calculate,
    args=(10_000_000,)
)
```

The process has been created but has not started yet.

---

# ▶️ Starting a Process

Use `start()` to begin execution.

```python id="8j7h3k"
process.start()
```

Example:

```python id="n7c8r4"
from multiprocessing import Process


def calculate():

    total = 0

    for i in range(10_000_000):
        total += i

    print(total)


process = Process(target=calculate)

process.start()
```

---

# ⏳ Waiting With `join()`

Use `join()` when the main process needs to wait for another process to finish.

```python id="5wq6je"
process.start()

process.join()

print("Process completed")
```

Conceptually:

```text id="y2s7rm"
Main Process
     │
     ├── start()
     │
     ▼
Worker Process
     │
     ├── Execute task
     │
     ▼
  Finished
     │
     ▼
   join()
     │
     ▼
Main Process continues
```

---

# 🚀 Basic Multiprocessing Example

```python id="8xq6b0"
from multiprocessing import Process


def calculate(n):

    total = 0

    for i in range(n):
        total += i

    print(total)


p1 = Process(
    target=calculate,
    args=(10_000_000,)
)

p2 = Process(
    target=calculate,
    args=(10_000_000,)
)


p1.start()
p2.start()


p1.join()
p2.join()
```

Execution:

```text id="j8h3v1"
                 Operating System
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
         Process 1             Process 2
             │                     │
       calculate()            calculate()
             │                     │
           CPU 1                 CPU 2
```

The two processes can perform CPU-heavy work independently. Pasted markdown(20261005-063950)

---

# 🔒 Multiprocessing and the GIL

The Python **Global Interpreter Lock (GIL)** is an important reason multiprocessing is useful for CPU-bound Python code.

In standard CPython, the GIL prevents multiple threads from executing Python bytecode simultaneously within the same process.

With multiprocessing:

```text id="0g1l5n"
Process 1
    │
Python Interpreter
    │
   GIL
    │
   CPU 1


Process 2
    │
Python Interpreter
    │
   GIL
    │
   CPU 2


Process 3
    │
Python Interpreter
    │
   GIL
    │
   CPU 3
```

Each process has its own Python interpreter and its own GIL.

Therefore, separate processes can execute CPU-heavy Python code in parallel. Pasted markdown(20261005-063950)

---

# 🧠 Multithreading vs GIL vs Multiprocessing

```text id="g3c1qy"
             CPU-Bound Python Work
                       │
             ┌─────────┴─────────┐
             │                   │
        Multithreading      Multiprocessing
             │                   │
             ▼                   ▼
        Same Process        Separate Processes
             │                   │
             ▼                   ▼
            GIL          Separate Interpreters
             │                   │
             ▼                   ▼
      Limited CPU          Parallel CPU Work
       execution
```

### Important Interview Point

Do not simply say:

> "Threads cannot run in parallel."

A better explanation is:

> "In standard CPython, multiple threads cannot execute Python bytecode simultaneously because of the GIL. Multiprocessing uses separate processes, each with its own Python interpreter and GIL, allowing CPU-bound Python code to execute in parallel."

---

# 💾 Process Memory

Processes have separate memory spaces.

```text id="z7b3c9d"
              Operating System
                     │
       ┌─────────────┼─────────────┐
       │             │             │
       ▼             ▼             ▼
   Process 1     Process 2     Process 3
       │             │             │
   Memory 1       Memory 2       Memory 3
```

This provides isolation between processes.

However, sharing data between processes requires mechanisms such as:

- Queues
- Pipes
- Shared memory
- Other inter-process communication mechanisms

---

# 🔄 Inter-Process Communication

Because processes have separate memory spaces, communication requires explicit mechanisms.

Conceptually:

```text id="b9p6w2"
Process 1
    │
    │
    ▼
 Communication
    │
    ├── Queue
    ├── Pipe
    └── Shared Memory
    │
    ▼
Process 2
```

### Queue Concept

```python id="q9n7ka"
from multiprocessing import Queue
```

A queue can be used to exchange data between processes.

---

# 🚀 ProcessPoolExecutor

For many similar CPU-bound tasks, manually creating processes can become inconvenient.

Python provides:

```python id="h3m5bx"
from concurrent.futures import ProcessPoolExecutor
```

`ProcessPoolExecutor` manages a pool of worker processes.

---

# ⚡ ProcessPoolExecutor Example

```python id="e5n9q1"
from concurrent.futures import ProcessPoolExecutor


def calculate(number):

    return number * number


numbers = [1, 2, 3, 4, 5]


with ProcessPoolExecutor(max_workers=4) as executor:

    results = executor.map(
        calculate,
        numbers
    )


print(list(results))
```

Conceptually:

```text id="w3r8kp"
                 ProcessPoolExecutor
                         │
             ┌───────────┼───────────┐
             │           │           │
             ▼           ▼           ▼
          Worker 1    Worker 2    Worker 3
             │           │           │
           Task 1      Task 2      Task 3
                         │
                      Worker 4
                         │
                       Task 4
```

---

# 📊 Process vs ProcessPoolExecutor

| Feature | `multiprocessing.Process` | `ProcessPoolExecutor` |
|---|---|---|
| Process creation | Manual | Managed |
| Process management | Manual | Automatic |
| Pool of workers | ❌ | ✅ |
| Many similar tasks | ⚠️ | ✅ |
| Code simplicity | Medium | Simple |
| Result handling | Manual | Convenient |

---

# 🖼️ Practical Example — Image Processing

Imagine processing many images.

```text id="k8r2qm"
              Images
                 │
       ┌─────────┼─────────┐
       │         │         │
       ▼         ▼         ▼
   Process 1  Process 2  Process 3
       │         │         │
   Image 1    Image 2    Image 3
       │         │         │
       ▼         ▼         ▼
   Processed  Processed  Processed
```

Image processing can be CPU-intensive, making multiprocessing a suitable approach.

---

# 🧮 Practical Example — Heavy Calculation

```python id="e2t7vm"
from concurrent.futures import ProcessPoolExecutor


def calculate(n):

    total = 0

    for i in range(n):
        total += i

    return total


numbers = [
    10_000_000,
    20_000_000,
    30_000_000,
    40_000_000
]


with ProcessPoolExecutor(max_workers=4) as executor:

    results = executor.map(
        calculate,
        numbers
    )


for result in results:
    print(result)
```

Each task can be handled by a separate worker process.

---

# ⚙️ Multiprocessing vs Multithreading

| Feature | ⚙️ Multiprocessing | 🧵 Multithreading |
|---|---|---|
| Execution Unit | Process | Thread |
| Memory | Separate | Shared |
| Best For | CPU-bound | I/O-bound |
| GIL | Separate GIL per process | Relevant |
| CPU Parallelism | ✅ | Limited for Python bytecode in standard CPython |
| Resource Usage | Higher | Lower |
| Communication | More expensive | Easier |
| API Calls | ⚠️ | ✅ |
| Database I/O | ⚠️ | ✅ |
| File I/O | ⚠️ | ✅ |
| Heavy Calculations | ✅ | ❌ |
| Image Processing | ✅ | ❌ |

The key distinction is:

> **Multithreading → I/O-bound**

> **Multiprocessing → CPU-bound**

Pasted markdown(20261005-063950)

---

# ⚡ Multiprocessing vs Asyncio

`asyncio` is primarily designed for asynchronous I/O workloads.

Multiprocessing is primarily useful for CPU-intensive workloads.

| Feature | ⚙️ Multiprocessing | ⚡ Asyncio |
|---|---|---|
| Execution | Multiple processes | Async tasks |
| Best For | CPU-bound | I/O-bound |
| CPU Parallelism | ✅ | ❌ |
| Event Loop | ❌ | ✅ |
| Separate Memory | ✅ | ❌ |
| `async` / `await` | ❌ | ✅ |
| Heavy Computation | ✅ | ❌ |
| Many API Calls | ❌ | ✅ |

---

# 🎯 When Should You Use Multiprocessing?

Use multiprocessing when the main workload is CPU-intensive.

### Good Use Cases

```text id="p3q8nv"
🧮 Heavy calculations
🖼️ Image processing
🎥 Video processing
🤖 CPU-heavy computation
🔢 Complex algorithms
⚙️ CPU-intensive transformations
```

### Decision

```text id="u5y2xr"
             Is the task CPU-intensive?
                       │
                      Yes
                       │
                       ▼
              Multiprocessing
                       │
                       ▼
             ProcessPoolExecutor
```

---

# ❌ When Not to Use Multiprocessing

Multiprocessing is generally not the first choice for simple I/O-bound operations.

Examples:

```text id="f4m8cz"
🌐 API calls
🗄️ Database queries
📁 File waiting
🌍 Network requests
```

For blocking I/O, multithreading can be simpler.

For asynchronous I/O, `asyncio` may be more appropriate when the libraries support it.

---

# 🧠 Easy Memory Trick

```text id="g7f5ks"
I/O
 │
 ├── API
 ├── Database
 ├── File
 └── Network
       │
       ▼
   🧵 Threads


CPU
 │
 ├── Calculations
 ├── Image Processing
 ├── Video Processing
 └── ML Computation
       │
       ▼
   ⚙️ Processes
```

The simple rule from the learning material is:

> **I/O → Threads**

> **CPU → Processes**

Pasted markdown(20261005-063950)

---

# 🛠️ Practice Exercises

## Exercise 1 — Create Two Processes

Create two processes that perform independent calculations.

```text
Process 1 → Calculation 1
Process 2 → Calculation 2
```

---

## Exercise 2 — CPU Calculation

Create a function that performs a large calculation.

Compare:

```text
Sequential
     vs
Multiprocessing
```

Measure the execution time.

---

## Exercise 3 — ProcessPoolExecutor

Use:

```python
ProcessPoolExecutor
```

to process:

```python
numbers = [
    10_000_000,
    20_000_000,
    30_000_000,
    40_000_000
]
```

---

## Exercise 4 — Image Processing

Create a multiprocessing program that processes multiple images.

```text
Image 1 ──► Process 1
Image 2 ──► Process 2
Image 3 ──► Process 3
Image 4 ──► Process 4
```

---

## Exercise 5 — Compare Threading and Multiprocessing

Implement the same CPU-heavy operation using:

```text
🧵 Multithreading
        vs
⚙️ Multiprocessing
```

Measure the execution time and explain the difference.

---

# 🎤 Interview Questions

## ⚙️ Basic Questions

### 1. What is multiprocessing?

Multiprocessing is a concurrency technique where multiple independent processes execute tasks.

---

### 2. What is a CPU-bound task?

A CPU-bound task spends most of its execution time performing computations rather than waiting for I/O.

---

### 3. Why is multiprocessing useful for CPU-bound work?

Each process has its own Python interpreter and GIL, allowing CPU-bound Python code to execute in parallel across processes.

Pasted markdown(20261005-063950)

---

### 4. What is the difference between a process and a thread?

A process has its own memory space and Python interpreter, while threads exist within a process and share the process's memory.

---

### 5. Does multiprocessing share memory?

Normally, separate processes have separate memory spaces.

Communication requires mechanisms such as queues, pipes, or shared memory.

---

### 6. What is `ProcessPoolExecutor`?

`ProcessPoolExecutor` provides a convenient way to execute multiple tasks using a pool of worker processes.

---

# 🎤 Interview: Multiprocessing vs Multithreading

### Question

> **When would you use multiprocessing instead of multithreading?**

### Answer

> "I would use multiprocessing for CPU-bound tasks such as heavy calculations, image processing, or other computational workloads. Multiprocessing creates separate processes, each with its own Python interpreter and GIL, allowing CPU-heavy Python code to execute in parallel. I would use multithreading mainly for I/O-bound tasks such as API calls, database operations, and file operations."

Pasted markdown(20261005-063950)

---

# 🎤 Interview: GIL

### Question

> **Why does multiprocessing help with CPU-bound Python code?**

### Answer

> "In standard CPython, the GIL prevents multiple threads from executing Python bytecode simultaneously within the same process. Multiprocessing creates separate processes, and each process has its own Python interpreter and GIL. Therefore, separate processes can execute CPU-bound Python code in parallel."

---

# 🎤 Interview: ProcessPoolExecutor

### Question

> **Why would you use ProcessPoolExecutor instead of manually creating processes?**

### Answer

> "ProcessPoolExecutor provides a higher-level interface for managing a pool of worker processes. It simplifies task submission, worker management, and result collection when I have many similar CPU-bound tasks."

---

# 📈 Learning Path

```text id="u8q3yn"
⚙️ Multiprocessing
        │
        ▼
Understand Processes
        │
        ▼
Process Lifecycle
        │
        ▼
start() / join()
        │
        ▼
CPU-Bound Workloads
        │
        ▼
Separate Memory
        │
        ▼
Python GIL
        │
        ▼
Process Communication
        │
        ▼
ProcessPoolExecutor
        │
        ▼
Real-World CPU Tasks
        │
        ▼
Interview Preparation
```

---

# 📌 Key Takeaways

```text id="j3z5yc"
⚙️ Multiprocessing
        │
        ▼
Multiple Processes
        │
        ▼
Separate Memory
        │
        ▼
Separate Python Interpreters
        │
        ▼
Separate GIL per Process
        │
        ▼
CPU Parallelism
        │
        ▼
Best for CPU-bound Work
        │
        ▼
ProcessPoolExecutor
```

### Most Important Points

1. ⚙️ Multiprocessing uses multiple independent processes.
2. 🧠 Each process has its own memory space.
3. 🐍 Each process has its own Python interpreter.
4. 🔒 Each process has its own GIL.
5. 🧮 Multiprocessing is mainly useful for CPU-bound workloads.
6. 🚀 `ProcessPoolExecutor` simplifies process-pool management.
7. 🔄 Processes require explicit communication mechanisms when data must be exchanged.
8. 🧵 Use multithreading primarily for I/O-bound workloads.
9. ⚡ Use asyncio for high-concurrency asynchronous I/O workloads.

---
