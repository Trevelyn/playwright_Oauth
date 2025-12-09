import os
import pytest
from pages.pinterest_home_page import PinterestHomePage

@pytest.mark.asyncio
async def test_authenticated_pinterest(browser, auth_state_path):
    ctx = await browser.new_context(storage_state=auth_state_path)
    page = await ctx.new_page()
    home = PinterestHomePage(page, os.getenv("PINTEREST_BASE_URL"))

    await page.goto(os.getenv("PINTEREST_BASE_URL"))
    assert await home.is_logged_in()

    await page.close()
    await ctx.close()
