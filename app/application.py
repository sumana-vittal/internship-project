from pages.base_page import Page
from pages.off_plan_page import OffPlanPage
from pages.register_agency_mobile_page import RegisterAgencyMobile
from pages.register_agency_page import RegisterAgency
from pages.registration_page import RegistrationPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.register_agency = RegisterAgency(driver)
        self.register_agency_mobile = RegisterAgencyMobile(driver)
        self.registration_page = RegistrationPage(driver)
        self.off_plan_page = OffPlanPage(driver)
