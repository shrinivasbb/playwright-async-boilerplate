from playwright.async_api import async_playwright




class StartUpPage:
    
    def __init__(self,page):
        self.page=page        

    async def navigateToLogin(self,url):
        await self.page.goto(url)

