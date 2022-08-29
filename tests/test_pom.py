import pytest
from libraries.StartUpPage import StartUpPage
from libraries.GoogleSearch import GoogleSearch
from libraries.CuraLandingPage import CuraLandingPage
from libraries.CuraLoginPage import CuraLoginPage
from libraries.CuraAppointmentPage import CuraAppointmentPage
from utils.BrowserUtils import BrowserUtils
from utils.JsonReader import JsonReader


@pytest.fixture()
async def test_setup_teardown(request):
    br = BrowserUtils()
    pg= await br.start_browser(request.config.option.browser)
    yield pg
    await br.quit_browser()


async def test_browser_actions(test_setup_teardown):
    pg=test_setup_teardown
    dataRead = JsonReader()
    st= StartUpPage(pg)
    await st.navigateToLogin("http://ww.google.com")
    gs=GoogleSearch(pg)
    await gs.performSearch((dataRead.readJsonFile("search.json"))["search"]["criteria"])


async def test_cura_Login(test_setup_teardown):
    pg=test_setup_teardown
    st=StartUpPage(pg)
    await st.navigateToLogin("https://katalon-demo-cura.herokuapp.com")
    cu = CuraLandingPage(pg)
    await cu.navigateToLoginPage()
    lg = CuraLoginPage(pg)
    await lg.performLogin("John Doe", "ThisIsNotAPassword")
    ap = CuraAppointmentPage(pg)
    await ap.select_facility("Seoul CURA Healthcare Center")
    await ap.click_re_admission(True)
    await ap.select_healthcare_program("Medicaid")
    await ap.enter_date("17/01/2022")
    await ap.enter_comments("AUTOMATION IS IN PROGRESS")
    await ap.click_book_appointment()    

async def test_cura_Login1(test_setup_teardown):
    pg=test_setup_teardown
    st=StartUpPage(pg)
    await st.navigateToLogin("https://katalon-demo-cura.herokuapp.com")
    cu = CuraLandingPage(pg)
    await cu.navigateToLoginPage()
    lg = CuraLoginPage(pg)
    await lg.performLogin("John Doe", "ThisIsNotAPassword")
    ap = CuraAppointmentPage(pg)
    await ap.select_facility("Seoul CURA Healthcare Center")
    await ap.click_re_admission(True)
    await ap.select_healthcare_program("Medicaid")
    await ap.enter_date("17/01/2022")
    await ap.enter_comments("AUTOMATION IS IN PROGRESS")
    await ap.click_book_appointment() 