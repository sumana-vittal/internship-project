from pages.base_page import Page
from pages.register_agency_page import RegisterAgency


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.register_agency = RegisterAgency(driver)
