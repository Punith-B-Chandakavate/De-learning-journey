# ⚡ Python Asyncio

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Asyncio](https://img.shields.io/badge/Asyncio-Asynchronous-6F42C1)
![Async Programming](https://img.shields.io/badge/Programming-Asynchronous-FFB000)
![I/O Bound](https://img.shields.io/badge/Workload-I%2FO%20Bound-2EA44F)
![FastAPI](https://img.shields.io/badge/FastAPI-Async%20Support-009688?logo=fastapi&logoColor=white)

A practical guide to **Python Asyncio**, covering asynchronous programming, event loops, coroutines, `async`, `await`, tasks, `asyncio.gather()`, `asyncio.create_task()`, concurrent API calls, real-world use cases, comparisons, and interview preparation.

---

# 📚 Overview

**Asyncio** is Python's framework for writing asynchronous programs.

It is especially useful for **I/O-bound workloads** where applications spend significant time waiting for operations such as:

- 🌐 HTTP API requests
- 🔌 WebSockets
- 🌍 Network operations
- 🗄️ Async database operations
- 🚀 High-concurrency applications

The main idea is that while one task is waiting for I/O, the **event loop can execute another task**.

```text
                    Event Loop
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
       Task 1        Task 2        Task 3
          │             │             │
       API Call      API Call      API Call
          │             │             │
       Waiting       Waiting       Waiting
          │             │             │
          └─────────────┼─────────────┘
                        │
                        ▼
                 Event Loop switches
                 to another task
```

This allows many I/O-bound operations to make progress concurrently without creating one OS thread for every task. 

---

# 🎯 Learning Objectives

By completing this module, you will understand:

- ⚡ What asynchronous programming is
- 🔄 What an event loop does
- 🧩 What a coroutine is
- `async`
- `await`
- 📦 Async tasks
- 🔀 Concurrent execution
- `asyncio.gather()`
- `asyncio.create_task()`
- 🌐 Concurrent API requests
- 🧵 Asyncio vs multithreading
- ⚙️ Asyncio vs multiprocessing
- 🎤 Asyncio interview questions

---

# 🧠 What is Asyncio?

`asyncio` provides an **event-driven asynchronous programming model**.

Instead of creating multiple threads, asynchronous tasks are managed by an **event loop**.

```text
              Asyncio Application
                       │
                       ▼
                  Event Loop
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Coroutine    Coroutine    Coroutine
          │            │            │
        Task 1       Task 2       Task 3
          │            │            │
       API Call     API Call     API Call
```

The event loop coordinates the execution of these tasks.

---

# 🔄 Event Loop

The **event loop** is the central component of asyncio.

It manages asynchronous tasks and determines which task can continue running.

```text
                    Event Loop
                        │
                        ▼
                  Check Task 1
                        │
                  Waiting for I/O
                        │
                        ▼
                  Check Task 2
                        │
                  Waiting for I/O
                        │
                        ▼
                  Check Task 3
                        │
                  Continue Task
                        │
                        ▼
                  API response
                        │
                        ▼
                  Resume Task 1
```

The important idea is:

> When one asynchronous task is waiting, the event loop can run another task.



---

# 🧩 Coroutine

A **coroutine** is an asynchronous function defined using `async def`.

```python id="g5r2qs"
async def fetch_data():

    print("Fetching data")
```

Calling the coroutine creates an awaitable object.

```python id="v5w3rt"
task = fetch_data()
```

The coroutine can then be executed by the event loop.

---

# 🔑 `async`

The `async` keyword defines an asynchronous function.

```python id="9w4s2k"
async def fetch_data():

    print("Fetching data")
```

An `async` function is commonly called a **coroutine function**.

---

# ⏳ `await`

`await` is one of the most important concepts in asyncio.

When Python reaches:

```python id="j3s5pa"
await some_operation()
```

the current task effectively says:

> "I'm waiting for this operation. You can run another task while I'm waiting."



---

# 🔄 What Happens When We Use `await`?

Consider:

```python id="q8v6mc"
async def task1():

    print("Task 1 started")

    await asyncio.sleep(2)

    print("Task 1 finished")
```

While `task1()` is waiting, the event loop can run another task.

```text id="w9x4be"
Task 1 starts
      │
      ▼
Task 1 waits
      │
      ▼
Event Loop switches
      │
      ▼
Task 2 starts
      │
      ▼
Task 2 waits
      │
      ▼
Task 1 resumes
      │
      ▼
Task 2 resumes
```

This is the basic mechanism behind asynchronous concurrency. 

---

# 🚀 Basic Asyncio Example

```python id="r5x9kp"
import asyncio


async def download(url):

    print(f"Downloading {url}")

    await asyncio.sleep(2)

    print(f"Finished {url}")


async def main():

    tasks = [
        download("url1"),
        download("url2"),
        download("url3")
    ]

    await asyncio.gather(*tasks)


asyncio.run(main())
```

Conceptually:

```text id="f8m2wd"
                 Event Loop
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
     Task 1       Task 2       Task 3
        │            │            │
     Waiting      Waiting      Waiting
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
                  Results
```

---

# 🧵 Asyncio vs Sequential Execution

Suppose three API calls each take approximately 2 seconds.

### Sequential

```text id="h7v3qa"
API 1 → wait 2 sec
          │
          ▼
API 2 → wait 2 sec
          │
          ▼
API 3 → wait 2 sec

Total ≈ 6 seconds
```

### Asyncio

```text id="m5k8dp"
API 1 ──────────────┐
API 2 ──────────────┼──► concurrent I/O
API 3 ──────────────┘

Total ≈ 2 seconds
```

The exact runtime depends on network, server, connection, and other system limits, but the key advantage is that independent I/O operations can overlap.

---

# 📦 `asyncio.gather()`

`asyncio.gather()` is useful when you have multiple independent asynchronous operations and want to wait for their results.

```python id="n2p7wx"
import asyncio


async def fetch_data(task):

    await asyncio.sleep(2)

    return f"{task} completed"


async def main():

    results = await asyncio.gather(
        fetch_data("API-1"),
        fetch_data("API-2"),
        fetch_data("API-3")
    )

    print(results)


asyncio.run(main())
```

Conceptually:

```text id="k8q4ms"
             asyncio.gather()
                    │
                    ▼
          Multiple awaitables
                    │
          ┌─────────┼─────────┐
          │         │         │
          ▼         ▼         ▼
        API 1     API 2     API 3
          │         │         │
          └─────────┼─────────┘
                    │
                    ▼
               All results
```

---

# 🎯 When to Use `gather()`

Use `asyncio.gather()` when:

- You have multiple independent async operations.
- You want to execute them concurrently.
- You need all of their results.
- The operations are naturally grouped together.

### Interview Shortcut

If an interviewer asks:

> **"I have 10 API calls and need all 10 results. How would you execute them efficiently?"**

A good answer is:

> "Since the API calls are I/O-bound and independent, I would use `asyncio.gather()` to execute them concurrently and collect all the results."



---

# 🛠️ Practical API Example

A realistic async HTTP client can be used with `aiohttp`.

```python id="x3r7vk"
import asyncio
import aiohttp


async def fetch_api(session, url):

    async with session.get(url) as response:

        return await response.json()


async def main():

    urls = [
        "https://api.example.com/1",
        "https://api.example.com/2",
        "https://api.example.com/3",
    ]

    async with aiohttp.ClientSession() as session:

        tasks = [
            fetch_api(session, url)
            for url in urls
        ]

        results = await asyncio.gather(*tasks)

    return results


results = asyncio.run(main())

print(results)
```

Architecture:

```text id="r8p4zn"
                    Asyncio
                       │
                       ▼
                  Event Loop
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
        API 1        API 2        API 3
          │            │            │
          ▼            ▼            ▼
       Response     Response     Response
          │            │            │
          └────────────┼────────────┘
                       ▼
                    Results
```

This pattern is useful when many independent API calls need to be executed concurrently. 

---

# 📋 `asyncio.create_task()`

`asyncio.create_task()` schedules a coroutine as an asyncio **Task**.

It is useful when you want more control over individual tasks.

```python id="w4s6nt"
import asyncio


async def fetch_data(task):

    await asyncio.sleep(2)

    return f"{task} completed"


async def main():

    task1 = asyncio.create_task(
        fetch_data("API-1")
    )

    task2 = asyncio.create_task(
        fetch_data("API-2")
    )

    result1 = await task1
    result2 = await task2

    print(result1)
    print(result2)


asyncio.run(main())
```

Conceptually:

```text id="p6q2xz"
Coroutine
    │
    ▼
create_task()
    │
    ▼
Asyncio Task
    │
    ▼
Event Loop
    │
    ▼
Task executes concurrently
```

---

# 🆚 `asyncio.gather()` vs `asyncio.create_task()`

Both are used for asynchronous concurrency, but they have different purposes.

| Feature | `asyncio.gather()` | `asyncio.create_task()` |
|---|---|---|
| Main purpose | Run multiple awaitables together | Schedule a coroutine as a Task |
| Returns | Combined results | Task object |
| Result handling | Convenient | More control |
| Task lifecycle | Less explicit | More explicit |
| Best use | Multiple independent results | Individual task management |

### Easy Memory Trick

```text id="x9w4kq"
asyncio.gather()
       │
       ▼
Run multiple awaitables
       │
       ▼
Wait for them
       │
       ▼
Collect results


asyncio.create_task()
       │
       ▼
Create Task object
       │
       ▼
Schedule coroutine
       │
       ▼
Manage task separately
```



---

# 🔥 Combining `create_task()` and `gather()`

You can also create tasks explicitly and then gather their results.

```python id="v7p3mx"
import asyncio


async def fetch_data(task):

    await asyncio.sleep(2)

    return f"{task} completed"


async def main():

    tasks = [
        asyncio.create_task(fetch_data("API-1")),
        asyncio.create_task(fetch_data("API-2")),
        asyncio.create_task(fetch_data("API-3"))
    ]

    results = await asyncio.gather(*tasks)

    print(results)


asyncio.run(main())
```

Architecture:

```text id="k3z8hm"
                Coroutines
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
     Task 1      Task 2      Task 3
        │           │           │
        └───────────┼───────────┘
                    │
                    ▼
             asyncio.gather()
                    │
                    ▼
                 Results
```

---

# 🌐 Example: 1,000 API Requests

Suppose you need to call **1,000 APIs**.

### Sequential

```text id="f4q7pn"
API 1 → wait
API 2 → wait
API 3 → wait
...
API 1000 → wait
```

### Multithreading

```text id="m9x2kd"
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

```text id="q7w5cx"
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

For very high numbers of I/O operations, asyncio can be more efficient because it avoids maintaining a large number of OS threads. 

---

# 🧵 Asyncio vs Multithreading

Both approaches are commonly used for I/O-bound workloads.

| Feature | 🧵 Multithreading | ⚡ Asyncio |
|---|---|---|
| Concurrency model | Multiple threads | Async tasks |
| Scheduler | OS / Python runtime | Event loop |
| Syntax | Normal functions | `async` / `await` |
| Best for | Blocking I/O | Async I/O |
| Threads | Multiple | Usually single thread |
| Memory overhead | Higher | Lower |
| Blocking libraries | Good fit | Can block event loop |
| API calls | ✅ | ✅ |
| Network operations | ✅ | ✅ |
| High concurrency | ⚠️ | ✅ |

### Simple Difference

> **Multithreading uses multiple threads, while asyncio uses asynchronous tasks managed by an event loop.**



---

# ⚙️ Asyncio vs Multiprocessing

| Feature | ⚡ Asyncio | ⚙️ Multiprocessing |
|---|---|---|
| Main purpose | I/O concurrency | CPU parallelism |
| Execution | Async tasks | Processes |
| Best for | I/O-bound | CPU-bound |
| Event loop | ✅ | ❌ |
| `async` / `await` | ✅ | ❌ |
| Separate memory | ❌ | ✅ |
| CPU parallelism | ❌ | ✅ |
| API calls | ✅ | ⚠️ |
| Heavy calculations | ❌ | ✅ |

### Easy Rule

```text id="p3k9vf"
I/O-bound
   │
   ├── 🧵 Multithreading
   └── ⚡ Asyncio


CPU-bound
   │
   └── ⚙️ Multiprocessing
```

---

# 🚦 When Should You Use Asyncio?

Use asyncio when you have many **asynchronous I/O operations**.

### Good Use Cases

```text id="q5v8ws"
🌐 HTTP APIs
🔌 WebSockets
🌍 Network services
🗄️ Async database clients
🚀 High-concurrency applications
⚡ FastAPI applications
```

For example:

```python id="c7y3vp"
@app.get("/users")
async def get_users():

    data = await fetch_users()

    return data
```

Asynchronous programming is commonly used in FastAPI applications and other high-concurrency network services. 

---

# ❌ When Not to Use Asyncio

Do not choose asyncio simply because you have multiple tasks.

If the workload is **CPU-intensive**, asyncio does not provide CPU parallelism.

Examples:

```text id="g6m2qn"
🧮 Heavy calculations
🖼️ Image processing
🎥 Video processing
🤖 CPU-intensive computation
```

For CPU-bound workloads, multiprocessing is generally the better approach. 

Also, blocking synchronous operations can block the event loop, so async applications should use appropriate asynchronous libraries or carefully isolate blocking work.

---

# 🧠 Easy Memory Trick

```text id="a6r2hx"
                    Workload
                       │
             ┌─────────┴─────────┐
             │                   │
          I/O Bound           CPU Bound
             │                   │
       ┌─────┴─────┐             │
       │           │             │
      🧵          ⚡            ⚙️
   Threads      Asyncio    Multiprocessing
       │           │             │
   Blocking     Async I/O    CPU-intensive
      I/O
```

### Remember

> 🧵 **Blocking I/O → Multithreading**

> ⚡ **Many async I/O operations → Asyncio**

> ⚙️ **CPU-intensive work → Multiprocessing**



---

# 🛠️ Practice Exercises

## Exercise 1 — Basic Coroutine

Create an async function:

```python
async def hello():
    print("Hello Asyncio")
```

Run it using:

```python
asyncio.run(hello())
```

---

## Exercise 2 — Multiple Tasks

Create three asynchronous functions:

```text
Task 1
Task 2
Task 3
```

Use:

```python
asyncio.gather()
```

to execute them concurrently.

---

## Exercise 3 — Understand `await`

Create two tasks that each wait for two seconds.

Observe how the event loop switches between them.

Expected concept:

```text
Task 1 starts
      ↓
Task 1 waits
      ↓
Task 2 starts
      ↓
Task 2 waits
      ↓
Task 1 resumes
      ↓
Task 2 resumes
```

---

## Exercise 4 — API Requests

Use `aiohttp` to call multiple APIs concurrently.

```text
API 1
API 2
API 3
API 4
API 5
```

Collect all responses using:

```python
asyncio.gather()
```

---

## Exercise 5 — `gather()` vs `create_task()`

Implement the same API example using:

```text
asyncio.gather()
```

and:

```text
asyncio.create_task()
```

Compare how task creation and result collection differ.

---

## Exercise 6 — 1,000 API Calls

Build a program that simulates a large number of API calls.

Compare:

```text
Sequential
     ↓
Multithreading
     ↓
Asyncio
```

Measure execution time and understand the scalability differences.

---

# 🎤 Interview Questions

## ⚡ Basic Questions

### 1. What is asyncio?

`asyncio` is Python's framework for asynchronous programming, allowing I/O-bound tasks to make progress concurrently through an event loop.

---

### 2. What is an event loop?

The event loop manages asynchronous tasks and switches between tasks when one task is waiting for I/O.

---

### 3. What is a coroutine?

A coroutine is an asynchronous function defined using `async def`.

---

### 4. What does `async` mean?

`async` defines a coroutine function that can perform asynchronous operations using `await`.

---

### 5. What does `await` do?

`await` pauses the current coroutine while it waits for an asynchronous operation, allowing the event loop to run other tasks.

---

### 6. What is `asyncio.gather()`?

`asyncio.gather()` allows multiple awaitables to run concurrently and collects their results.

---

### 7. What is `asyncio.create_task()`?

`asyncio.create_task()` schedules a coroutine as an asyncio Task and gives you a Task object that can be managed independently.

---

# 🎤 Interview: `gather()` vs `create_task()`

### Question

> **What is the difference between `asyncio.gather()` and `asyncio.create_task()`?**

### Answer

> "`asyncio.gather()` is useful when I have multiple independent asynchronous operations and want to run them concurrently and collect their results. `asyncio.create_task()` schedules a coroutine as an asyncio Task and gives me more explicit control over that task."


---

# 🎤 Interview: 10 API Calls

### Question

> **I have 10 API calls and need all 10 results. How would you execute them efficiently?**

### Answer

> "Since the API calls are I/O-bound and independent of each other, I would use `asyncio.gather()` to execute them concurrently and collect all the results."


---

# 🎤 Interview: Why Not Multithreading?

### Question

> **Why would you choose asyncio instead of multithreading for API calls?**

### Answer

> "Both threading and asyncio can provide concurrency for network I/O. If I'm already using an async HTTP client and have many independent API calls, asyncio is usually preferable because it avoids creating many OS threads and scales well for I/O-bound workloads."



---

# 🎤 Interview: CPU-Bound Work

### Question

> **What if the API tasks are CPU-intensive?**

### Answer

> "I would not choose asyncio simply because there are multiple tasks. If the workload is CPU-bound, I would consider multiprocessing or `ProcessPoolExecutor` because asyncio is designed primarily for I/O-bound concurrency."



---

# 📈 Learning Path

```text id="n6q4yb"
⚡ Asyncio
     │
     ▼
Asynchronous Programming
     │
     ▼
Event Loop
     │
     ▼
Coroutines
     │
     ▼
async
     │
     ▼
await
     │
     ▼
Async Tasks
     │
     ├──────────────┐
     ▼              ▼
gather()       create_task()
     │              │
     └──────┬───────┘
            ▼
     Concurrent APIs
            │
            ▼
     High Concurrency
            │
            ▼
    Real-World Projects
            │
            ▼
     Interview Practice
```

---

# 📌 Key Takeaways

```text id="d5k8qx"
⚡ Asyncio
     │
     ▼
Event Loop
     │
     ▼
Coroutines
     │
     ▼
async / await
     │
     ▼
Async Tasks
     │
     ▼
Non-blocking I/O
     │
     ▼
High Concurrency
     │
     ▼
asyncio.gather()
     │
     ▼
asyncio.create_task()
```

### Most Important Points

1. ⚡ `asyncio` is designed primarily for asynchronous I/O.
2. 🔄 The event loop manages asynchronous tasks.
3. 🧩 `async def` creates coroutine functions.
4. ⏳ `await` allows a coroutine to pause while waiting for I/O.
5. 📦 `asyncio.gather()` is useful for running multiple independent awaitables and collecting results.
6. 🛠️ `asyncio.create_task()` schedules a coroutine as a Task.
7. 🌐 Asyncio is useful for many API and network operations.
8. 🚀 Asyncio can handle high-concurrency I/O without requiring a large number of OS threads.
9. ⚙️ CPU-bound workloads are generally better suited to multiprocessing.
10. 🧵 Blocking synchronous code may be better suited to multithreading unless it is appropriately isolated from the event loop.

---