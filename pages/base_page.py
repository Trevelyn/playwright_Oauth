from playwright.async_api import Page

class BasePage:
    def __init__(self, page: Page, base_url: str = None):
        self.page = page
        self.base_url = base_url or ""

    async def goto(self, path: str):
        await self.page.goto(self.base_url + path)

    async def click(self, selector: str):
        await self.page.click(selector)

    async def fill(self, selector: str, text: str):
        await self.page.fill(selector, text)

    async def wait_for_url(self, pattern: str, timeout: int = 30000):
        await self.page.wait_for_url(pattern, timeout=timeout)
