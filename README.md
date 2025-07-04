# 🎭 Playwright Demos

This repo contains Playwright end-to-end test demos in multiple languages — **C#**, **Java**, **JavaScript**, **Python**, and **TypeScript** — showcasing cross-language test automation practices with a shared login page example.

---

## 🚀 Languages & Projects

- **C#**  
  In `csharp/csharp.Tests/`, demonstrates Playwright with NUnit, using:
  - Page Object Model (`LoginPage.cs`)
  - Configuration (`TestConfig.cs`)
  - Realistic login scenarios with success, invalid inputs, max-length limits, and server error simulation

- **Java**  
  (`java/`) – *Playwright setup with login automation in a Java-based framework.*

- **JavaScript**  
  (`javascript/`) – *Playwright test runner using login page object and validations.*

- **Python**  
  (`python/`) – *Playwright with Pytest and reusable login POM.*

- **TypeScript**  
  (`typescript/`) – *Typed Playwright project using POM and detailed login scenarios.*

Each project replicates a login page test suite following best practices:
- Navigate to login page
- Enter credentials
- Validate behaviors: success, errors, validations
- Uses POM and shared configuration

---

## ✅ Common Features

- Page Object Model for reusable UI interactions  
- Login scenarios: valid credentials, empty/too short/too long inputs, server-error mock  
- Shared settings: base URL, viewport size, headless toggle  
- Capturing traces, videos, reports supported across implementations

---

## 🔧 How to Run

Robot your language:

### C#
```bash
cd csharp/csharp.Tests
playwright install
dotnet test
```

### Java
```bash
cd java/
mvn test    # or gradle
```

### JavaScript
```bash
cd javascript/
npm install
npx playwright install
npm test
```

### Python
```bash
cd python/
pip install -r requirements.txt
playwright install
pytest
```

### TypeScript
```bash
cd typescript/
npm install
npx playwright install
npm test
```

---

## 🧾 Project Structure

```
playwright-demos/
├── csharp/
│   └── csharp.Tests/       ← C# with NUnit
├── java/                   ← Java demo (Playwright + JUnit/TestNG)
├── javascript/             ← JS demo (POM + playwright.config.js)
├── python/                 ← Python demo (pytest + POM)
├── typescript/             ← TS demo (POM + Playwright Test runner)
├── .gitignore              ← common ignore rules
└── README.md               ← This file
```


## 📄 License

MIT © **Maicon Fang**, 2025  
Feel free to use, adapt, and share across your Playwright projects!
