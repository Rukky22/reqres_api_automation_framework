# Reqres API Automation Framework 🚀

![CI](https://github.com/Rukky22/reqres_api_automation_framework/actions/workflows/python-tests.yml/badge.svg)

A scalable and maintainable **Python API Test Automation Framework** built using:

- **Pytest** – test execution & reporting
- **Requests** – HTTP client for API interaction

This project is designed to demonstrate real-world SDET practices… including reusable utilities, environment separation, payload management, and CI readiness.

---

## ✅ Features

✔ API testing using Python (Pytest + Requests)  
✔ Centralized API Client for reusability  
✔ Test data stored in structured JSON files  
✔ Project structure aligned with industry standards  
✔ Easy integration with CI/CD (GitHub Actions ready)  
✔ Supports positive & negative test scenarios  
✔ Beginner-friendly but production-inspired design

---

## 🏗️ Project Structure

reqres_api_automation_framework/
│
├── clients/
│ └── reqres_client.py # Reusable API client methods
│
├── data/
│ └── user_payload.json # JSON test data
│
├── tests/
│ └── test_users.py # User tests
│
├── utils/
│ └── config.py # Configuration management
│
├── requirements.txt
└── README.md

---

## ✅ How to Run Tests

### 1️⃣ Create & activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # (Mac/Linux)
.venv\Scripts\activate     # (Windows)

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Execute all tests
pytest -v

4️⃣ Generate HTML Report (optional)
pytest -v --html=report.html

🌍 API Reference

This framework tests the public API from:
https://reqres.in

Examples tested:

Register user

Create user

List users

Update user

Delete user

👤 Author

Randolph Oghwe
Automation Test Engineer | SDET  💪

📌 Portfolio Project — Contributions Welcome

⭐ If you like this framework, feel free to give the repo a star!
```
