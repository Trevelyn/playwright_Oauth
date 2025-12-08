import os
import pytest
from playwright.async_api import async_playwright
from utils.github_google_oauth import perform_github_google_oauth
from pages.github_home_page import GitHubHomePage

@pytest.mark.asyncio
async def test_github_google_login():

    auth_state_path = "auth/github_state.json"
    github_url = os.getenv("GITHUB_BASE_URL")

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)

        # First context: perform OAuth login
        context = await browser.new_context()
        page = await context.new_page()

        await perform_github_google_oauth(
            page,
            context,
            auth_state_path,
            github_url
        )

        # Second context: verify saved state works
        ctx2 = await browser.new_context(storage_state=auth_state_path)
        page2 = await ctx2.new_page()

        home = GitHubHomePage(page2, github_url)
        await page2.goto(github_url)

        assert await home.is_logged_in() is True

        await ctx2.close()
        await context.close()
        await browser.close()
