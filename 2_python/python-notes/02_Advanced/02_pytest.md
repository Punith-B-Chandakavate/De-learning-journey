# 📘 Pytest

---

# 🧪 Pytest

`pytest` is a powerful Python testing framework used to write and run test cases easily.

It helps developers:

* ✅ Find bugs
* ✅ Validate code
* ✅ Automate testing
* ✅ Improve code quality

---

# 🔥 Why Use Pytest?

| Feature             | Description                    |
| ------------------- | ------------------------------ |
| ✅ Easy Syntax      | Simple test writing            |
| ⚡ Fast Testing     | Runs tests quickly             |
| 📘 Detailed Output  | Clear test reports             |
| 🔄 Fixtures Support | Reusable setup code            |
| 🧠 Auto Discovery   | Finds test files automatically |
| 🚀 Widely Used      | Popular in Python projects     |

---

# 📦 Install Pytest

```bash
pip install pytest
```

---

# ▶️ Verify Installation

```bash
pytest --version
```

---

# ✅ Output

```text
pytest 8.x.x
```

---

# 📘 Basic Test Structure

## 📄 calculator.py

```python
def add(a, b):
    return a + b
```

---

## 📄 test_calculator.py

```python
from calculator import add

def test_add():
    assert add(2, 3) == 5
```

---

# ▶️ Run Tests

```bash
pytest
```

---

# ✅ Output

```text
1 passed
```

---

# 🔥 Important Rules

| Rule                                    | Example          |
| --------------------------------------- | ---------------- |
| Test file must start with `test_`     | `test_app.py`  |
| Test function must start with `test_` | `test_login()` |

---

# 📘 Assert Statement

Used to verify expected output.

```python
def test_sum():
    assert 2 + 2 == 4
```

---

# ❌ Failed Test Example

```python
def test_fail():
    assert 2 + 2 == 5
```

---

# ✅ Output

```text
AssertionError
```

---

# 📘 Multiple Test Cases

```python
def test_add():
    assert 2 + 3 == 5

def test_subtract():
    assert 5 - 2 == 3
```

---

# 📘 Fixtures in Pytest

Fixtures are reusable setup functions.

---

## Example

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_length(sample_data):
    assert len(sample_data) == 3
```

---

# 🔥 Advantages of Fixtures

| Benefit            | Description           |
| ------------------ | --------------------- |
| Reusable           | Use in multiple tests |
| Clean Code         | Avoid duplicate setup |
| Better Maintenance | Easy updates          |

---

# 📘 Setup and Teardown

```python
import pytest

@pytest.fixture
def setup_data():
    print("Setup")
  
    yield
  
    print("Teardown")

def test_example(setup_data):
    print("Running Test")
```

---

# ✅ Output

```text
Setup
Running Test
Teardown
```

---

# 📘 Parametrize Tests

Used to run same test with multiple inputs.

```python
import pytest

@pytest.mark.parametrize(
    "a,b,result",
    [
        (2, 3, 5),
        (5, 5, 10),
        (1, 1, 2)
    ]
)

def test_add(a, b, result):
    assert a + b == result
```

---

# ✅ Output

```text
3 passed
```

---

# 📘 Exception Testing

```python
import pytest

def divide(a, b):
    return a / b

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

---

# ✅ Output

```text
1 passed
```

---

# 📘 Skip Test

```python
import pytest

@pytest.mark.skip
def test_skip():
    assert True
```

---

# 📘 Skip with Condition

```python
import pytest
import sys

@pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason="Requires Python 3.10"
)

def test_version():
    assert True
```

---

# 📘 Group Tests Using Class

```python
class TestMath:

    def test_add(self):
        assert 2 + 2 == 4

    def test_subtract(self):
        assert 5 - 2 == 3
```

---

# 📘 Pytest Markers

| Marker                       | Purpose          |
| ---------------------------- | ---------------- |
| `@pytest.mark.skip`        | Skip test        |
| `@pytest.mark.xfail`       | Expected failure |
| `@pytest.mark.parametrize` | Multiple inputs  |

---

# 📘 Expected Failure Example

```python
import pytest

@pytest.mark.xfail
def test_fail():
    assert False
```

---

# 📘 Run Specific Test File

```bash
pytest test_calculator.py
```

---

# 📘 Run Specific Test Function

```bash
pytest test_calculator.py::test_add
```

---

# 📘 Verbose Mode

```bash
pytest -v
```

---

# 📘 Show Print Statements

```bash
pytest -s
```

---

# 📘 Generate HTML Report

Install plugin:

```bash
pip install pytest-html
```

---

## Run Command

```bash
pytest --html=report.html
```

---

# 📘 Pytest Directory Structure

```text
project/
│
├── app/
│   └── calculator.py
│
├── tests/
│   └── test_calculator.py
│
├── requirements.txt
```

---

# 📘 conftest.py

Used to store shared fixtures.

## Example

```python
import pytest

@pytest.fixture
def common_data():
    return "Shared Fixture"
```

---

# 📘 Mocking in Pytest

Used to simulate external services/APIs.

```python
from unittest.mock import patch

def test_mock():
    with patch("module.function") as mock_func:
        mock_func.return_value = "Mocked"
      
        assert mock_func() == "Mocked"
```

---

# 📘 Pytest with FastAPI

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
  
    assert response.status_code == 200
```

---

# 📘 Pytest with Django

Install:

```bash
pip install pytest-django
```

---

## Run Tests

```bash
pytest
```

---

# 🔥 Best Practices

| Practice             | Reason             |
| -------------------- | ------------------ |
| Write small tests    | Easy debugging     |
| Use fixtures         | Reusable setup     |
| Use meaningful names | Better readability |
| Test edge cases      | Avoid bugs         |
| Automate tests       | Faster development |

---

# 📘 Real-Time Use Cases

| Use Case           | Example      |
| ------------------ | ------------ |
| API Testing        | FastAPI APIs |
| Unit Testing       | Functions    |
| Database Testing   | Queries      |
| Automation Testing | CI/CD        |
| Backend Validation | Django Apps  |

---

# 🔥 Interview Questions

## ❓ What is Pytest?

A Python testing framework used for automated testing.

---

## ❓ Why use Pytest instead of unittest?

✅ Simpler syntax
✅ Better fixtures
✅ Powerful plugins

---

## ❓ What are Fixtures?

Reusable setup functions used before tests.

---

## ❓ What is Parametrize?

Runs one test with multiple inputs.

---

## ❓ What is conftest.py?

Shared fixture configuration file.

---

# 🏁 Summary

| Topic        | Description              |
| ------------ | ------------------------ |
| Pytest       | Python testing framework |
| Fixtures     | Reusable setup           |
| Assert       | Validate output          |
| Parametrize  | Multiple test inputs     |
| Mocking      | Simulate external calls  |
| HTML Reports | Generate reports         |
