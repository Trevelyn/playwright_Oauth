from .base_page import BasePage
from playwright.async_api import Page

class GitHubLoginPage(BasePage):
    CONTINUE_WITH_GOOGLE = 'button[value="google"]'

    def __init__(self, page: Page, base_url=None):
        super().__init__(page, base_url)

    async def open_login(self):
        await self.goto("/login")

    async def click_continue_with_google(self):
        await self.page.click(self.CONTINUE_WITH_GOOGLE)
