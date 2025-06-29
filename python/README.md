# 🧪 Python Playwright Login Test Project

This is a simple end-to-end (E2E) testing project using [Playwright](https://playwright.dev/python/) with Python and Pytest. The goal is to test the login functionality of a web application hosted at `http://localhost:4200/#/login`.

---

## ✅ Features included so far

- Project structured with `core`, `pages`, and `tests` folders
- Page Object Model implemented in `pages/login_page.py`
- Base layer setup in `core/base_page.py` and configuration in `core/config.py`
- Automated login test located in `tests/test_login.py`
- Pytest configuration through `pytest.ini`
- Virtual environment with Python 3.13.5
- `requirements.txt` with essential dependencies

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
│       ├── conftest.py
│       └── test_login.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ▶️ How to run the tests

Make sure the web application server is running at `http://localhost:4200/#/login`. Then, in the project terminal (with the virtual environment activated), run:

```bash
pytest -p no:warnings -s -v src/tests/test_login.py
```

> This will run the login test with full output and no warnings.

---

## 💡 Additional tips

- To install the project dependencies, run:

```bash
pip install -r requirements.txt
```

- To run all tests inside the folder:

```bash
pytest -p no:warnings -s -v src/tests/
```

- To generate an optional HTML report:

```bash
pytest --html=report.html --self-contained-html -p no:warnings -s -v src/tests/
```