from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=15)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def switch_to_new_window(self):
        self.wait.until(
            EC.new_window_is_opened,
            message="Error in switching to new window"
        )

        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])

    def wait_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by '{locator}' is not clickable."
        )

    def wait_element_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by '{locator}' is not clickable."
        ).click()

    def presence_of_element_located(self, *locator):
        self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Couldn't find the presence of element at '{locator}'"
        )

    def text_present_in_element(self, text, *locator):
        self.wait.until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Couldn't find the value '{text}' in the element"
        )

    def verify_attribute_value(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).get_attribute("value")
        assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"


