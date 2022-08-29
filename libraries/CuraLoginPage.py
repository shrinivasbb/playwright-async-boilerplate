from libraries.StartUpPage import StartUpPage


class CuraLoginPage(StartUpPage):

    def __init__(self, page):
        super().__init__(page)

    async def performLogin(self,username,password):
        await self.page.fill("#txt-username",username)
        await self.page.fill("#txt-password", password)
        await self.page.click("#btn-login")
        await self.page.is_visible("#combo_facility")