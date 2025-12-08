from .base_page import BasePage
from playwright.async_api import Page

class GoogleOAuthPage(BasePage):
    # Google's selectors; may change over time — update if needed.
    EMAIL_INPUT = 'input[type="email"]'
    EMAIL_NEXT = 'div[id="identifierNext"]'
    PASSWORD_INPUT = 'input[type="password"]'
    PASS_NEXT = 'div[id="passwordNext"]'
    CONSENT_BUTTON = 'button:has-text("Allow")'

    def __init__(self, page: Page):
        super().__init__(page)

    async def login_with_google(self, email: str, password: str):
        # Assumes the page is Google's sign-in
        await self.page.wait_for_selector(self.EMAIL_INPUT, timeout=15000)
        await self.page.fill(self.EMAIL_INPUT, email)
        await self.page.click(self.EMAIL_NEXT)
        await self.page.wait_for_selector(self.PASSWORD_INPUT, timeout=15000)
        await self.page.fill(self.PASSWORD_INPUT, password)
        await self.page.click(self.PASS_NEXT)
        # Consent if needed
        try:
            await self.page.wait_for_selector(self.CONSENT_BUTTON, timeout=5000)
            await self.page.click(self.CONSENT_BUTTON)
        except Exception:
            pass
