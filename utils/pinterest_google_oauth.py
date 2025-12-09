import os
from dotenv import load_dotenv
from pages.pinterest_login_page import PinterestLoginPage
from pages.google_oauth_page import GoogleOAuthPage

load_dotenv()

async def perform_pinterest_google_oauth(page, context, state_path, base_url):
    login = PinterestLoginPage(page, base_url)

    
    await login.open_login()

    # Clicking opens Google OAuth popup
    async with context.expect_page() as popup_info:
        await login.click_continue_with_google()

    google_page = await popup_info.value
    google_oauth = GoogleOAuthPage(google_page)

    await google_oauth.login_with_google(
        os.getenv("GOOGLE_EMAIL"),
        os.getenv("GOOGLE_PASSWORD")
    )

    # Wait for browser to redirect back to pinterest
    await page.wait_for_load_state("networkidle")

    # Save Pintrest authenticated state
    await context.storage_state(path=state_path)
