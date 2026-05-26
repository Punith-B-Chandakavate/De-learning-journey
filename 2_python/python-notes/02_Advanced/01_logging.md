# 📘 Python Logging - README.md

---

# 🔥 Python Logging

Logging is used to track events, errors, warnings, and application flow during program execution.

Instead of using `print()`, developers use **logging** for:

* Debugging
* Error tracking
* Monitoring applications
* Production support

---

# ✅ Advantages of Logging

| Feature                | Description               |
| ---------------------- | ------------------------- |
| 🐞 Debugging           | Find issues easily        |
| 📄 Monitoring          | Track application flow    |
| ⚠️ Error Tracking    | Store errors permanently  |
| 🧠 Better than print() | Professional approach     |
| 📂 Log Files           | Save logs into files      |
| 🚀 Production Ready    | Used in real applications |

---

# 📦 Import Logging Module

```python
import logging
```

---

# 🔥 Basic Logging Example

```python
import logging

logging.warning("This is warning message")
```

---

# ✅ Output

```text
WARNING:root:This is warning message
```

---

# 📘 Logging Levels

| Level    | Purpose                        |
| -------- | ------------------------------ |
| DEBUG    | Detailed debugging information |
| INFO     | General application events     |
| WARNING  | Warning messages               |
| ERROR    | Error occurred                 |
| CRITICAL | Serious error                  |

---

# 📊 Logging Level Priority

```text
DEBUG < INFO < WARNING < ERROR < CRITICAL
```

---

# 🔥 Logging Example with Levels

```python
import logging

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
```

---

# ✅ Output

(Default level = WARNING)

```text
WARNING:root:Warning message
ERROR:root:Error message
CRITICAL:root:Critical message
```

---

# 📘 Configure Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debugging started")
```

---

# ✅ Output

```text
DEBUG:root:Debugging started
```

---

# 📘 Logging Format

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)

logging.info("Application Started")
```

---

# ✅ Output

```text
INFO:Application Started
```

---

# 🔥 Common Format Options

| Format            | Description |
| ----------------- | ----------- |
| `%(asctime)s`   | Time        |
| `%(levelname)s` | Log level   |
| `%(message)s`   | Log message |
| `%(filename)s`  | File name   |
| `%(lineno)d`    | Line number |

---

# 📘 Advanced Format Example

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Server Started")
```

---

# ✅ Output

```text
2025-05-26 10:30:20 - INFO - Server Started
```

---

# 📂 Logging to File

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application Started")
```

---

# ✅ Output

Logs saved in:

```text
app.log
```

---

# 📘 Append Mode vs Write Mode

| Mode  | Description    |
| ----- | -------------- |
| `a` | Append logs    |
| `w` | Overwrite logs |

---

# 🔥 Example

```python
logging.basicConfig(
    filename="app.log",
    filemode="a"
)
```

---

# 📘 Exception Logging

```python
import logging

try:
    x = 10 / 0
except Exception as e:
    logging.error(e)
```

---

# ✅ Output

```text
ERROR:root:division by zero
```

---

# 🔥 Logging Exception Traceback

```python
import logging

try:
    x = 10 / 0
except Exception:
    logging.exception("Exception occurred")
```

---

# ✅ Output

```text
ERROR:root:Exception occurred
Traceback (most recent call last):
ZeroDivisionError: division by zero
```

---

# 📘 Create Custom Logger

```python
import logging

logger = logging.getLogger("my_logger")

logger.warning("Custom logger warning")
```

---

# 📘 Logger Handlers

Handlers define where logs should go.

| Handler       | Purpose      |
| ------------- | ------------ |
| StreamHandler | Console logs |
| FileHandler   | File logs    |
| SMTPHandler   | Email logs   |

---

# 🔥 FileHandler Example

```python
import logging

logger = logging.getLogger()

file_handler = logging.FileHandler("app.log")

logger.addHandler(file_handler)

logger.warning("File logging")
```

---

# 📘 Rotating Log Files

Used to avoid huge log files.

```python
from logging.handlers import RotatingFileHandler
import logging

handler = RotatingFileHandler(
    "app.log",
    maxBytes=2000,
    backupCount=3
)

logger = logging.getLogger()
logger.addHandler(handler)

logger.warning("Rotating logs")
```

---

# 🔥 Logging in FastAPI

```python
import logging
from fastapi import FastAPI

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    logging.info("Home API called")
  
    return {"message": "Success"}
```

---

# 📘 Logging in Django

```python
LOGGING = {
    "version": 1,
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "debug.log",
        },
    },
    "root": {
        "handlers": ["file"],
        "level": "INFO",
    },
}
```

---

# 🔥 Best Practices

| Practice                     | Reason                 |
| ---------------------------- | ---------------------- |
| Use logging instead of print | Professional debugging |
| Use proper log levels        | Better monitoring      |
| Store logs in files          | Track issues later     |
| Avoid sensitive data in logs | Security               |
| Use rotating logs            | Prevent huge files     |

---

# 📘 Real-Time Use Cases

| Use Case           | Example           |
| ------------------ | ----------------- |
| Error Tracking     | API failures      |
| Monitoring         | User activity     |
| Security Logs      | Login attempts    |
| Debugging          | Finding bugs      |
| Production Support | Server monitoring |

---

# 🔥 Interview Questions

## ❓ Why use logging instead of print()?

✅ Better debugging
✅ Log levels
✅ File storage
✅ Production ready

---

## ❓ What is `basicConfig()`?

Used to configure:

* Log level
* Format
* File name

---

## ❓ What is RotatingFileHandler?

Creates multiple log files when size increases.

---

## ❓ Difference Between WARNING and ERROR

| WARNING               | ERROR          |
| --------------------- | -------------- |
| Possible issue        | Actual issue   |
| Application continues | Error occurred |

---

# 🏁 Summary

| Topic             | Description              |
| ----------------- | ------------------------ |
| Logging           | Track application events |
| Levels            | DEBUG, INFO, ERROR       |
| Handlers          | Control log destination  |
| File Logging      | Save logs permanently    |
| Exception Logging | Store traceback          |
| Rotating Logs     | Manage large logs        |
