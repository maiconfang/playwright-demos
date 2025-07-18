
# 🧪 Python Playwright Login Test Project

This is a complete end-to-end (E2E) testing project using [Playwright](https://playwright.dev/python/) with Python and Pytest. The goal is to test the login functionality and other core features of a web application using modern QA best practices.

---

## ✅ Features included

- Modular structure with `core`, `pages`, and `tests` inside `src/`
- Page Object Model implemented in `pages/login_page.py`
- Shared base logic in `core/base_page.py`
- Dynamic environment-based configuration via `core/config.py` and JSON files in `/configs`
- Environment options: `local`, `staging`, `prod`
- Automatic config loading using the `ENV` variable
- Automated login, task, and user CRUD tests in organized subfolders
- Fixtures separated in `tests/fixtures/` for reuse
- Pytest configuration via `pytest.ini` (`src` as PYTHONPATH)
- Compatible with Python 3.13.5
- `requirements.txt` with essential dependencies
- Allure reporting integration
- 🖼️ Automatic screenshot attachment on test failure using Allure

---

## 📁 Project Structure

```
python/
│
├── configs/
│   ├── config_local.json
│   ├── config_staging.json
│   └── config_prod.json
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
│       ├── conftest.py
│       ├── fixtures/
│       │   ├── auth_fixtures.py
│       │   └── db_fixtures.py
│       ├── login/
│       │   ├── test_login.py
│       │   └── test_login_parametrizado.py
│       ├── tasks/
│       │   └── test_task_filters.py
│       └── users/
│           └── test_user_crud.py
│
├── pytest.ini
├── requirements.txt
├── README.md
└── report.html
```

---

## ▶️ How to run the tests

Make sure the app is running (e.g., `http://localhost:4200/#/login`), and that your virtual environment is activated.

### 🔹 Run all tests:
```bash
pytest --browser chromium
```

### 🔹 Run all tests in a specific file:
```bash
pytest src/tests/login/test_login.py --browser chromium
```

### 🔹 Run a specific test function:
```bash
pytest src/tests/login/test_login.py::test_login_success --browser chromium
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

## 🌍 Run with environment configs

### 🔸 Windows (PowerShell):
```powershell
$env:ENV = "staging"
pytest --browser chromium
```

### 🔸 Linux/macOS:
```bash
export ENV=staging
pytest --browser chromium
```

> Defaults to `local` if `ENV` is not set.

---

## 📊 Allure Report (recommended)

### 🔸 Install Allure CLI (only once):
- On Windows: `choco install allure` (via Chocolatey)
- Or manually download from: https://github.com/allure-framework/allure2/releases

Make sure `allure` is available in your system PATH.

### 🔸 Add to requirements.txt:
```
allure-pytest==2.14.3
```

### 🔸 Generate test results:
```bash
pytest --alluredir=allure-results --browser chromium
```

### 🔸 Serve the report locally:
```bash
allure serve allure-results
```

### 🖼️ Automatically attach screenshot on test failure

Implemented in `conftest.py` using `pytest_runtest_makereport`. When a test fails, a screenshot is captured and embedded into the Allure report.

---


## ⚙️ Configuration (config_local.json)

The project reads configuration values such as `base_url`, `username`, `password`, and `timeout` from the file:

```
configs/config_local.json
```

Example:
```json
{
  "base_url": "http://localhost:4200",
  "username": "luna.moon@maif.com",
  "password": "123",
  "timeout": 5000
}
```

These values are automatically loaded and used in test cases such as login. You can change the behavior per environment using the `ENV` variable (e.g., `local`, `staging`, `prod`).


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

### 🔸 Generate HTML report (basic):
```bash
pytest --html=report.html --self-contained-html --browser chromium
```

---

## 🧠 Notes

- `pytest.ini` ensures the `src` folder is in the Python path.
- Configuration files in `/configs` allow dynamic behavior per environment.
- The project uses clean test architecture with Page Object Model, fixtures, and Allure integration.
- Ideal for scalable QA automation in modern projects.

---

Happy testing! 🚀
