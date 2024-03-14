from selenium.webdriver.common.by import By
from pages.base_page import Page


class RegisterAgency(Page):

    # locators
    SIGN_IN = (By.CSS_SELECTOR, "[class='sing-in-text']")
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[class*='login-button']")
    CONNECT_THE_COMPANY_BTN = (By.CSS_SELECTOR, "[class*='get-free-period']")
    COUNTRY_NAME = (By.ID, "Your-country")
    COMPANY_NAME = (By.ID, "Company-name-2")
    POSITION = (By.ID, "Position")
    YOUR_NAME = (By.ID, "Director-name")
    YOUR_PHONE = (By.CSS_SELECTOR, "[placeholder='Your phone']")
    COMPANY_AGENT_COUNT = (By.ID, "Amount-of-agents-in-company")
    YOUR_EMAIL = (By.ID, "Email-2")
    SEND_REQUEST_BTN = (By.CSS_SELECTOR, "[value='Send request']")
    BUY_SUBSCRIPTION_BTN = (By.CSS_SELECTOR, "[class*='step-button']")

    def __init__(self, driver):
        super().__init__(driver)

    # open the main page with given URL
    def open_home_page(self):
        self.open("https://soft.reelly.io/sign-up")

    # Click on the sign in link
    def click_sign_in(self):
        self.wait_element_clickable_click(*self.SIGN_IN)

    # Enter the log in credentials and click on the continue button
    def login_details_and_click(self):
        self.input_text("vn.sumana@gmail.com", *self.EMAIL_FIELD)
        self.input_text("sReelly", *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BUTTON)

    # Click on the button Connect the company
    def click_connect_company(self):
        self.wait_element_clickable_click(*self.CONNECT_THE_COMPANY_BTN)

    # switch to the new window.
    def switch_new_tab(self):
        self.switch_to_new_window()

    # Enter all the details for new agency to register
    def enter_information(self):
        self.input_text("USA", *self.COUNTRY_NAME)
        self.input_text("test", *self.COMPANY_NAME)
        self.input_text("Developer", *self.POSITION)
        self.input_text("abc", *self.YOUR_NAME)
        self.input_text("0000000000", *self.YOUR_PHONE)
        self.input_text("10", *self.COMPANY_AGENT_COUNT)
        self.input_text("test@test.com", *self.YOUR_EMAIL)

    # validate all the information entered
    def verify_information(self):
        # print("country -- " + self.find_element(*self.COUNTRY_NAME).get_attribute("value"))
        self.verify_attribute_value("USA", *self.COUNTRY_NAME)
        self.verify_attribute_value("test", *self.COMPANY_NAME)
        self.verify_attribute_value("Developer", *self.POSITION)
        self.verify_attribute_value("abc", *self.YOUR_NAME)
        self.verify_attribute_value("0000000000", *self.YOUR_PHONE)
        self.verify_attribute_value("10", *self.COMPANY_AGENT_COUNT)
        self.verify_attribute_value("test@test.com", *self.YOUR_EMAIL)

    # validate the send request button is clickable
    def verify_request_button(self):
        self.presence_of_element_located(*self.SEND_REQUEST_BTN)
        self.wait_element_clickable(*self.SEND_REQUEST_BTN)

    # validate the Buy Subscription button is clickable
    def verify_buy_subscription(self):
        self.presence_of_element_located(*self.BUY_SUBSCRIPTION_BTN)
        self.wait_element_clickable(*self.BUY_SUBSCRIPTION_BTN)