# 🎭 Playwright C# End-to-End Test Project

This project is a complete example of how to write and execute end-to-end (E2E) tests for a web application using **Playwright**, **NUnit**, and **.NET 8**. It is focused on testing the login page of a real-world Angular application.

---

## 📁 Project Structure

```
csharp/
└── csharp.Tests/
    ├── bin/                            # Build output (generated automatically)
    ├── obj/                            # Temporary build files
    ├── src/
    │   ├── core/
    │   │   └── TestConfig.cs          # Base URL and shared configs
    │   ├── pages/
    │   │   └── LoginPage.cs           # Page Object Model for login interactions
    │   └── tests/
    │       └── LoginTests.cs          # Test class with multiple login scenarios
    ├── csharp.Tests.csproj            # Project file with dependencies
    ├── playwright.runsettings         # Playwright-specific settings (e.g. trace, video)
    ├── Program.cs                     # Entry point (optional for local debug)
    ├── csharp.sln                     # Solution file
    ├── csharp.sln.DotSettings.user    # IDE user settings
    └── README.md                      # This file
```

---

## ✅ Features

- 🚀 Playwright + NUnit test automation
- 👤 Login form validation (success, invalid, input limits, server errors)
- 🧪 Custom Page Object for reusable login actions
- 🔁 Non-parallel execution to avoid flaky results
- 🧾 Clean structure and comments for learning and scaling

---

## 🧪 How to Run the Tests

> Make sure you have [Node.js](https://nodejs.org/), [.NET SDK](https://dotnet.microsoft.com/en-us/download), and Playwright installed.

### 1. Install Playwright browsers

```bash
playwright install
```

> You can run this inside the `csharp` folder.

---

### 2. Run tests in console (with browser visible)

```bash
dotnet test --settings "playwright.runsettings"
```

This command will:
- Open the browser (non-headless mode)
- Run tests with trace and video capture (if configured)
- Use the `playwright.runsettings` file

---

### 3. Run tests and generate readable output

```bash
dotnet test --settings "playwright.runsettings" --logger "console;verbosity=detailed"
```

---

## 🛑 Notes

- Tests are marked as `[NonParallelizable]` to avoid browser/context issues in parallel mode.
- The browser is configured to run with:

```csharp
Headless = false,
SlowMo   = 100
```

You can change this inside the `PageTest` class or override `BrowserTypeLaunchOptions`.

---

## 📜 Requirements

- .NET 8 SDK
- Playwright CLI
- Visual Studio or VS Code (recommended for development)
- Rider (jetbrains rider community)

---

## 🙌 Author

Created by **Maicon Fang**  
📍 Based in Canada | 💻 Passionate about QA & Test Automation  
GitHub: [maiconfang](https://github.com/maiconfang)