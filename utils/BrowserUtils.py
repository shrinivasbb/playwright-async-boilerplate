
from playwright.async_api import async_playwright
from screeninfo import get_monitors



class BrowserUtils:

    async def start_browser(self,browserName):
        if browserName is None:
            self.playwright=await async_playwright().start()
            self.browser = await self.playwright.firefox.launch(headless=False, args=["--start-maximized"])
            self.context = await self.browser.new_context(viewport={'width': get_monitors()[0].width,'height':get_monitors()[0].height})
            self.page =  self.context.new_page()
            return await self.page
        elif browserName.lower()=='chromium':
            self.playwright=await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=False,args=["--start-maximized"])
            self.context = await self.browser.new_context(viewport={'width': get_monitors()[0].width,'height':get_monitors()[0].height})
            self.page =  self.context.new_page()
            return await self.page
        elif browserName.lower()=='firefox':
            self.playwright=await async_playwright().start()
            self.browser = await self.playwright.firefox.launch(headless=False, args=["--start-maximized"])
            self.context = await self.browser.new_context(viewport={'width': get_monitors()[0].width,'height':get_monitors()[0].height})
            self.page =  self.context.new_page()
            return await self.page
        elif browserName.lower()=='safari':
            self.playwright=await async_playwright().start()
            self.browser = await self.playwright.webkit.launch(headless=False, args=["--start-maximized"])
            self.context = await self.browser.new_context(viewport={'width': get_monitors()[0].width,'height':get_monitors()[0].height})
            self.page =  self.context.new_page()
            return await self.page
        else:
            return None

    async def quit_browser(self):
        await self.browser.close()