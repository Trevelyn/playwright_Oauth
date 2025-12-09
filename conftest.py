import os
import pytest
from playwright.async_api import async_playwright
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture(scope="session")
def verify_env():
    """Verify all required environment variables are set"""
    required_vars = ["PINTEREST_BASE_URL", "GOOGLE_EMAIL", "GOOGLE_PASSWORD"]
    missing = [var for var in required_vars if not os.getenv(var)]
    
    if missing:
        pytest.fail(f"Missing required environment variables: {', '.join(missing)}")

@pytest.fixture(scope="session")
def auth_state_path():
    return "auth/pinterest_state.json"