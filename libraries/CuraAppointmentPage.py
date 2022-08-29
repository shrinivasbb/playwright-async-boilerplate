from libraries.StartUpPage import StartUpPage


class CuraAppointmentPage(StartUpPage):
    
    def __init__(self, page):
        self.facility_cmb_box="#combo_facility"
        self.readmission_chk_box="#chk_hospotal_readmission"
        self.healthcare_prg_radio_btn="input[value='RADIO_VALUE']"
        self.visit_date="#txt_visit_date"
        self.comment_data="#txt_comment"
        self.book_appointment_btn="#btn-book-appointment"
        self.datepicker=".datepicker"
        super().__init__(page)

    async def select_facility(self, facilityName:str):
        await self.page.select_option(self.facility_cmb_box,value=facilityName)

    async def click_re_admission(self, readmission: bool):
        if readmission:
            if await self.page.is_checked(self.readmission_chk_box):
                assert await self.page.is_checked(self.readmission_chk_box) is True
            else:
                assert await self.page.is_checked(self.readmission_chk_box) is False        
                await self.page.click(self.readmission_chk_box)
                assert await self.page.is_checked(self.readmission_chk_box) is True                                                                                                     
        else:
            if await self.page.is_checked(self.readmission_chk_box):
                await self.page.click(self.readmission_chk_box)
                assert await self.page.is_checked(self.readmission_chk_box) is False
        

    async def select_healthcare_program(self,healthcareProgram:str):
        # await self.page.click(self.healthcare_prg_radio_btn.replace("RADIO_VALUE",healthcareProgram))
        await self.page.check('text='+healthcareProgram)

    async def enter_date(self,visitDate:str):
        # locator = self.page.locator(self.visit_date)
        # await locator.press(visitDate)
        # await self.page.click(self.visit_date)
        a_handle = await self.page.evaluate_handle("document.querySelector('#txt_visit_date')")
        await self.page.evaluate_handle("([body,val])=>body.value=val", [a_handle,"17/01/2022"])
        # await self.page.
        # hhandle = await self.page.query_selector(self.visit_date)
        # hhandle.fill(visitDate)
        # await self.page.fill(self.visit_date,visitDate,force=True)
        a_handle = await self.page.evaluate_handle("document.querySelector('#txt_visit_date').value")
        print(a_handle)
        await self.page.is_visible(self.datepicker)
        # await self.page.click("text=12")
        await self.page.keyboard.press("Escape", delay=500)

    async def enter_comments(self,comment:str):
        await self.page.fill(self.comment_data,comment)

    async def click_book_appointment(self):
        await self.page.click(self.book_appointment_btn)
        assert await self.page.is_visible("text=Please be informed that your appointment has been booked as following") is True