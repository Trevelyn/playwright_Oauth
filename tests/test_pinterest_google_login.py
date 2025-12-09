import os
import pytest
from playwright.async_api import async_playwright
from utils.pinterest_google_oauth import perform_pinterest_google_oauth
from pages.pinterest_home_page import PinterestHomePage

@pytest.mark.asyncio
async def test_pinterest_google_login(verify_env, auth_state_path):
    pinterest_url = os.getenv("PINTEREST_BASE_URL")
    
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            print(f"Starting OAuth flow for {pinterest_url}")
            
            await perform_pinterest_google_oauth(
                page,
                context,
                auth_state_path,
                pinterest_url
            )

            print("OAuth completed, verifying login...")

            # Verify saved state works
            ctx2 = await browser.new_context(storage_state=auth_state_path)
            page2 = await ctx2.new_page()
            home = PinterestHomePage(page2, pinterest_url)
            await page2.goto(pinterest_url)

            is_logged_in = await home.is_logged_in()
            print(f"Login verification: {is_logged_in}")
            assert is_logged_in is True

            await page2.close()
            await ctx2.close()
            
        finally:
            await page.close()
            await context.close()
            await browser.close()