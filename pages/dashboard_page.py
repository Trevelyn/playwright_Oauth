from .base_page import BasePage
from playwright.async_api import Page

class DashboardPage(BasePage):
    PROFILE_LINK = 'a[href*="/settings/profile"]'

    def __init__(self, page: Page, base_url: str = None):
        super().__init__(page, base_url)

    async def is_logged_in(self):
        try:
            await self.page.wait_for_selector(self.PROFILE_LINK, timeout=5000)
            return True
        except Exception:
            return False
