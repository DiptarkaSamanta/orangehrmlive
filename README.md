# OrangeHRM Live - Selenium Automation Framework (Page Object Model)

This repository contains an end-to-end automated testing framework for OrangeHRM Live built using Python, Selenium WebDriver, pytest, and the Page Object Model (POM) design pattern.

## 🚀 Project Structure

```
page object model 2/
├── base_pages/         # Page Object classes (locators & web interactions)
├── configurations/     # Configuration files (config.ini)
├── test_cases/         # Test scripts and conftest fixture setup
├── test_data/          # Test data files
├── utilities/          # Utility modules (custom logger, property reader)
├── Logs/               # Execution log output
├── screenshots/        # Test failure screenshots
├── reports/            # Test execution reports
├── README.md           # Project documentation
└── .gitignore          # Git ignore file
```

## 🛠️ Requirements & Setup

1. **Python 3.x** installed
2. Install dependencies:
   ```bash
   pip install pytest selenium pytest-html
   ```

## 🧪 Running Tests

To run all tests with HTML report generation:
```bash
pytest -v -s --html=reports/report.html test_cases/
```

To run a specific test case (e.g. Admin Login):
```bash
pytest -v -s test_cases/test_admin_login.py
```
