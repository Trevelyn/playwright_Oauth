import os
import pytest
from pages.github_home_page import GitHubHomePage

@pytest.mark.asyncio
async def test_authenticated_github(browser, auth_state_path):
    ctx = await browser.new_context(storage_state=auth_state_path)
    page = await ctx.new_page()
    home = GitHubHomePage(page, os.getenv("GITHUB_BASE_URL"))

    await page.goto(os.getenv("GITHUB_BASE_URL"))
    assert await home.is_logged_in()

    await page.close()
    await ctx.close()
