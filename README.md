
# TestComplete Hybrid Automation Framework

A hybrid test automation framework developed using **TestComplete** for automating desktop applications. The framework adopts a combination of **Data-Driven** and **Page Object Model (POM)** methodologies to provide modular, scalable, and reusable test automation. This tool is designed for **Windows-based desktop applications** and utilizes **JSON** for test data management.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Test Data Management](#test-data-management)
- [Page Object Model (POM) Approach](#page-object-model-pom-approach)
- [Test Suites](#test-suites)
- [Contribution](#contribution)
- [Support](#support)

---

## Features

- Hybrid framework combining **Data-Driven + Page Object Model**
- Reusable function libraries
- Structured test suites: Sanity, Smoke, Regression
- **JSON**-based test data
- Supports execution via TestComplete IDE and command line
- Logging and reporting included
- Screenshot capture on test failure

---

## Tech Stack

- **Tool**: [TestComplete](https://smartbear.com/product/testcomplete/)
- **Language**: Python or JavaScript (depending on your project setting)
- **Framework Type**: Hybrid (Data-Driven + POM)
- **Target Application**: Windows Desktop Applications
- **Test Data Format**: JSON

---

## Prerequisites

- Windows OS
- TestComplete 15 or higher (Licensed or Trial)
- JSON library (native or external, depending on scripting language)
- Access to the desktop application under test (AUT)

---

## Installation

1. **Install TestComplete**
   - Download from [SmartBear TestComplete](https://smartbear.com/product/testcomplete/)
   - Install on a Windows machine.

2. **Clone this Repository**
   ```bash
   git clone https://github.com/Nosy-Abbasi/TestCompleteUIAutomation
   cd TestCompleteUIAutomation
   ```

3. **Open in TestComplete**
   - Launch TestComplete
   - Open the `.pjs` project file from the cloned repo

---

## Project Structure

```
testcomplete-desktop-hybrid-framework/
│
├── Reports/
│   ├── Allure Report
│   ├── ScreenShot on Failure
│
├── Scripts/
│   ├── CommonFucntions/          # Common reusable functions
│   ├── DataFile/                 # JSON test data files
│   ├── FucntionFile/             # Business logic for test cases
│   ├── GlobalVariables/          # Global and environment variables
│   ├── Locators/                 # Object repository files
│
├── SuiteFile/
│   ├── RegressionSuite/          # Regression test suite
│   ├── Smoke/                    # Smoke test suite
│
└── README.md
```

---

## How to Use

### Run from TestComplete IDE:
1. Open TestComplete
2. Load the project
3. Choose the suite from `SuiteFile/`
4. Click **Run Project**

### Run from Command Line:
```bash
TestComplete.exe project.pjs /r /p:"ProjectName" /u:"User" /ps:"Password"
```

> You can integrate with Jenkins or any CI tool using command-line execution.

---

## Test Data Management

Test data is maintained in JSON format under `Scripts/DataFile/`. Here's an example:

```json
{
  "valid_user": {
    "username": "admin",
    "password": "admin123"
  },
  "invalid_user": {
    "username": "user",
    "password": "wrongpass"
  }
}
```

Test scripts parse these files and load data dynamically during execution.

---

## Page Object Model (POM) Approach

- **Locators** are defined in `Scripts/Locators/`
- **Business Logic** functions are written in `Scripts/FucntionFile/`
- **Common Utilities** reside in `Scripts/CommonFucntions/`
- **Global Variables** and configurations go in `Scripts/GlobalVariables/`

This structure promotes reusability and separation of concerns.

---

## Test Suites

- **Smoke Tests** → `SuiteFile/Smoke`
- **Regression Tests** → `SuiteFile/RegressionSuite`

Each suite includes:
- `.tcScript` or `.py` test scripts
- Test items configuration
- Data-driven logic using JSON inputs

---

## Contribution

We welcome contributions! Please follow these guidelines:

- Maintain consistency with the current framework structure
- Adhere to POM and Data-Driven principles
- Add documentation for any new feature

---

## Support

For issues, bugs, or feature requests, feel free to open an issue in the repository or contact the maintainer.
