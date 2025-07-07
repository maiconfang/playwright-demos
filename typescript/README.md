# 🎭 Playwright TypeScript E2E Tests - Login Page

This project demonstrates end-to-end (E2E) test automation using **Playwright** with **TypeScript**, focused on validating the login page of a web application running at `http://localhost:4200/#/login`.

---

## 🤖 What is Playwright?

Playwright is a framework for automated **end-to-end testing** of web applications.  
It simulates real user actions—like clicking buttons, typing into forms, and navigating pages—across multiple browsers (Chrome, Firefox, Safari).

It's a powerful tool to ensure your app works as expected from the user's perspective.

---

## 🚀 Features

- Login validation with multiple scenarios
- Form validation for empty, short, and max-length credentials
- Error handling for server-side failures (mocked)
- Tests written using Playwright’s `@playwright/test` and Page Object Model (POM)

---

## 📁 Project Structure

```
project-root/
├── pages/
│   └── LoginPage.ts         # Page Object class for login
├── tests/
│   └── login.spec.ts        # All login test scenarios
├── playwright.config.ts     # Playwright configuration file
├── package.json             # Project dependencies and scripts
```

---

## 🛠️ Setup Instructions

Make sure you have Node.js installed (version 16 or above).

### 1. Install dependencies

```bash
npm install
```

### 2. Install Playwright browsers

```bash
npx playwright install
```

---

## ▶️ Running the Tests

### Run all tests (headless by default)

```bash
npx playwright test
```

### Run with browser visible (headed mode)

```bash
npx playwright test --headed
```

### Run a specific test file

```bash
npx playwright test tests/login.spec.ts
```

### Run a specific test by its title

```bash
npx playwright test -g "should login successfully and redirect to app page"
```

You can copy the test name exactly from `login.spec.ts` to run just that one.

---

## 📊 View HTML Test Report

After running the tests, generate the report with:

```bash
npx playwright show-report
```

---

## 🔧 Base URL

The base URL for this project is configured as:

```
http://localhost:4200
```

Make sure the application is running locally before executing the tests.

---

## 📌 Author

This project was created and maintained by **Maicon Fang** to demonstrate testing best practices using Playwright and TypeScript.
