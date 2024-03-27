from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


class RegistrationPage(Page):

    # create account locators
    FULLNAME = (By.ID, "Full-Name")
    PHONE = (By.ID, "phone2")
    EMAIL_FIELD = (By.ID, "Email-3")
    PASSWORD_FIELD = (By.ID, "field")
    COMPANY = (By.ID, "Company-website")
    ROLE = (By.ID, "Role")
    POSITION = (By.ID, "Position")
    COUNTRY = (By.ID, "country-select")
    COMPANY_SIZE = (By.ID, "Agents-amount-2")
    PRIVACY_POLICY_CHECKBOX = (By.ID, "checkbox")

    def input_create_account_information(self):
        self.input_text("test careerist", *self.FULLNAME)
        self.input_text("0000000000", *self.PHONE)
        self.input_text("test@test.com", *self.EMAIL_FIELD)
        self.input_text("passW0rd!", *self.PASSWORD_FIELD)
        self.input_text("test", *self.COMPANY)
        self.input_text("Broker", *self.ROLE)
        self.input_text("Seller / Manager", *self.POSITION)
        self.input_text("Sweden", *self.COUNTRY)
        self.input_text("10-25", *self.COMPANY_SIZE)
        self.checkbox_check(*self.PRIVACY_POLICY_CHECKBOX)

    def verify_input_data(self):
        self.verify_attribute_value("test careerist", *self.FULLNAME)
        self.verify_attribute_value("0000000000", *self.PHONE)
        self.verify_attribute_value("test@test.com", *self.EMAIL_FIELD)
        self.verify_attribute_value("passW0rd!", *self.PASSWORD_FIELD)
        self.verify_attribute_value("test", *self.COMPANY)
        self.verify_attribute_value("Broker", *self.ROLE)
        self.verify_attribute_value("Seller", *self.POSITION)
        self.verify_attribute_value("Sweden", *self.COUNTRY)
        self.verify_attribute_value("10-25", *self.COMPANY_SIZE)
        self.verify_checkbox_attribute_value(*self.PRIVACY_POLICY_CHECKBOX)

