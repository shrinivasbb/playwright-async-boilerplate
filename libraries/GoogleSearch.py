


from libraries.StartUpPage import StartUpPage


class GoogleSearch(StartUpPage):

    def __init__(self, page):
        self.gsearch="[name='q']"
        self.gbutton="[aria-label='Search']"
        super().__init__(page)

    async def performSearch(self, searchCriterion):
        await self.page.fill(self.gsearch, searchCriterion)
        await self.page.click(self.gbutton)
