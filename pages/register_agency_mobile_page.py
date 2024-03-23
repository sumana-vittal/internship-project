from selenium.webdriver.common.by import By
from pages.base_page import Page


class RegisterAgencyMobile(Page):

    # Locators
    USER_PROFILE_IMAGE = (By. CSS_SELECTOR, "a.menu-photo_avatar")
    USER_PROFILE_CONNECT_COMPANY_BTN = (By.XPATH, "//div[@class='settings-block-menu']"
                                                  "//a[@class='button-link-menu w-inline-block']")

    def click_user_profile(self):
        self.wait_element_clickable_click(*self.USER_PROFILE_IMAGE)

    def click_user_profile_connect_company(self):
        self.wait_element_clickable_click(*self.USER_PROFILE_CONNECT_COMPANY_BTN)
