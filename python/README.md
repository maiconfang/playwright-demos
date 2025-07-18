# 🧪 Python Playwright Login Test Project

This is a simple end-to-end (E2E) testing project using [Playwright](https://playwright.dev/python/) with Python and Pytest. The goal is to test the login functionality of a web application hosted at `http://localhost:4200/#/login`.

---

## ✅ Features included

- Organized structure with `core`, `pages`, and `tests` inside `src/`
- Page Object Model implemented in `pages/login_page.py`
- Shared logic and configuration in `core/base_page.py` and `core/config.py`
- Automated login tests in `tests/test_login.py`
- Pytest configuration via `pytest.ini` (`src` is used as PYTHONPATH)
- Compatible with Python 3.13.5
- `requirements.txt` with essential dependencies
- Custom assertions and error handling for login scenarios

---

## 📁 Project Structure

```
python/
│
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   └── config.py
│   │
│   ├── pages/
│   │   ├── __init__.py
│   │   └── login_page.py
│   │
│   └── tests/
│       ├── __init__.py
│       ├── conftest.py
│       └── test_login.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ▶️ How to run the tests

Make sure the app is running at `http://localhost:4200/#/login`, and that your virtual environment is activated.

### 🔹 Run all tests:
```bash
pytest --browser chromium
```

### 🔹 Run all tests in a file:
```bash
pytest src/tests/test_login.py --browser chromium
```

### 🔹 Run a specific test function:
```bash
pytest src/tests/test_login.py::test_login_success --browser chromium
```

### 🔹 Run tests by keyword (partial name):
```bash
pytest -k "success" --browser chromium
```

---

## 🌐 Run in specific browsers

### 🔸 Chromium:
```bash
pytest --browser chromium
```

### 🔸 Firefox:
```bash
pytest --browser firefox
```

### 🔸 WebKit:
```bash
pytest --browser webkit
```

---

## ⚙️ Run in headless or headed mode

### 🔹 Headless (default):
```bash
pytest --browser chromium
```

### 🔹 Headed (UI visible):
```bash
pytest --browser chromium --headed
```

---

## 🔄 Run in background (Windows PowerShell / Linux / macOS):

```bash
nohup pytest --browser chromium > log.txt 2>&1 &
```

> Or use `&` at the end in PowerShell:
```bash
Start-Process pytest -ArgumentList "--browser", "chromium"
```

---

## 🧪 Additional commands

### 🔸 Install dependencies:
```bash
pip install -r requirements.txt
```

### 🔸 Run all tests with full output:
```bash
pytest -s -v --browser chromium
```

### 🔸 Run with no warnings:
```bash
pytest -p no:warnings --browser chromium
```

### 🔸 Generate HTML report:
```bash
pytest --html=report.html --self-contained-html --browser chromium
```

---

## 🧠 Notes

- `pytest.ini` ensures the `src` folder is in the Python path.
- All imports use relative paths like `from core...` and `from pages...`.
- The project follows clean test automation practices using Page Object Model.

---

Happy testing! 🚀
