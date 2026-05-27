
# 🐍 Python Installation Guide

This guide explains how to install Python on:

- 🪟 Windows
- 🐧 Linux
- 🍎 macOS

It also includes:
- 📦 pip installation
- 📓 Jupyter Notebook setup
- 🚀 Launch commands

---

# 🪟 Windows Installation

## 1️⃣ Download Python

Visit the official Python website:

[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

Download the latest version of Python.

---

## 2️⃣ Run the Installer

Open the downloaded installer.

✅ IMPORTANT:
Check the option:

```bash
Add Python to PATH
````

Then click:

```bash
Install Now
```

---

## 3️⃣ Verify Installation

Open **Command Prompt** and run:

```bash
python --version
```

Expected output:

```bash
Python 3.x.x
```

---

## 4️⃣ Verify pip

```bash
pip --version
```

---

# 🐧 Linux Installation

## Ubuntu / Debian

### 1️⃣ Update Packages

```bash
sudo apt update
```

### 2️⃣ Install Python

```bash
sudo apt install python3
```

### 3️⃣ Install pip

```bash
sudo apt install python3-pip
```

### 4️⃣ Verify Installation

```bash
python3 --version
```

Verify pip:

```bash
pip3 --version
```

---

## Fedora

Install Python and pip:

```bash
sudo dnf install python3 python3-pip
```

Verify:

```bash
python3 --version
```

---

## Arch Linux

Install Python:

```bash
sudo pacman -S python python-pip
```

Verify:

```bash
python --version
```

---

# 🍎 macOS Installation

## Method 1: Official Installer

### 1️⃣ Download Python

[https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)

Download the latest macOS installer.

---

### 2️⃣ Install Python

Open the `.pkg` file and follow the installation steps.

---

### 3️⃣ Verify Installation

Open Terminal and run:

```bash
python3 --version
```

---

### 4️⃣ Verify pip

```bash
pip3 --version
```

---

# 🍺 macOS Installation Using Homebrew

## 1️⃣ Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Official website:

[https://brew.sh](https://brew.sh)

---

## 2️⃣ Install Python

```bash
brew install python
```

---

## 3️⃣ Verify Installation

```bash
python3 --version
```

---

# 📓 Install Jupyter Notebook

## 🪟 Windows

Install Jupyter:

```bash
pip install jupyter
```

Launch Notebook:

```bash
python -m notebook
```

---

## 🐧 Linux / 🍎 macOS

Install Jupyter:

```bash
pip3 install jupyter
```

Launch Notebook:

```bash
python3 -m notebook
```

Or:

```bash
jupyter notebook
```

---

# 🧪 Virtual Environment (Optional)

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

### Linux / macOS

```bash
python3 -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

# 📚 Useful Commands

| ✅ Task               | 🪟 Windows                 | 🐧 Linux / 🍎 macOS         |
| -------------------- | -------------------------- | --------------------------- |
| Check Python Version | `python --version`         | `python3 --version`         |
| Check pip Version    | `pip --version`            | `pip3 --version`            |
| Install Package      | `pip install package_name` | `pip3 install package_name` |
| Launch Jupyter       | `python -m notebook`       | `python3 -m notebook`       |

---

