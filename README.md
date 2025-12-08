# Playwright Async Google OAuth Project (POM)

This project demonstrates:
- Google OAuth sign-in (automated)
- Async Playwright (Python)
- Page Object Model (POM)
- Saving and reusing authentication state
- Allure + HTML reporting

Setup:
1. python -m venv .venv
2. source .venv/bin/activate  (or .venv\Scripts\activate on Windows)
3. pip install -r requirements.txt
4. playwright install
5. cp .env.example .env and fill values

Run first-time OAuth test to save state:
pytest tests/test_pinterest_google_login.py -k test_pinterest_google_login

Run all tests:
pytest
