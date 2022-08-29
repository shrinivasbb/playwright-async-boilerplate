from playwright.async_api import async_playwright
from libraries.StartUpPage import StartUpPage


class CuraLandingPage(StartUpPage):

    def __init__(self, page):

        super().__init__(page)

    async def navigateToLoginPage(self):
        await self.page.click("#menu-toggle")
        await self.page.click('text="Login"')
        await self.page.is_visible("#txt-username")
        await self.page.is_visible("#txt-password")