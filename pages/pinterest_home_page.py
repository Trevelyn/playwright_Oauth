from .base_page import BasePage
from playwright.async_api import Page

class PinterestHomePage(BasePage):
    PROFILE_ICON = 'summary[aria-label="View profile and more"]'

    def __init__(self, page: Page, base_url=None):
        super().__init__(page, base_url)

    async def is_logged_in(self):
        try:
            await self.page.wait_for_selector(self.PROFILE_ICON, timeout=5000)
            return True
        except:
            return False
