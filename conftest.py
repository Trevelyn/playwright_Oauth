import os
import pytest
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
async def playwright_instance():
    async with async_playwright() as p:
        yield p

@pytest.fixture(scope="session")
async def browser(playwright_instance):
    browser = await playwright_instance.chromium.launch(headless=False)
    yield browser
    await browser.close()

@pytest.fixture(scope="session")
async def auth_state_path():
    return "auth/github_state.json"

@pytest.fixture
async def context(browser, auth_state_path):
    if os.path.exists(auth_state_path):
        return await browser.new_context(storage_state=auth_state_path)
    return await browser.new_context()
