SauceDemo Automation Framework

URL: https://www.saucedemo.com

Features

- Page Object Model (POM) structure
- Covers login, sorting, cart, checkout, and logout flows
- HTML test reports
- Parallel test execution
- Easy to maintain and extend

---

🚀 Setup Instructions

Clone the repository

git clone https://github.com/SurajKukkipady/FreJun_Assig.git

Navigate to the respective folder in Terminal

pip install -r requirements.txt
playwright install

🧪 Run Tests
Run all tests
pytest

Run specific test
pytest tests/test_checkout.py::test_successful_checkout

Run with HTML report
pytest --html=report.html

Run Tests in Parallel
pytest -n 4
Use -n auto to auto-detect CPU cores.

Run tests in multiple browsers
pytest --browser chromium --browser firefox --browser webkit

👤 Author
Suraj Kukkipady
