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

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def checkbox_check(self, *locator):
        if not self.find_element(*locator).is_selected():
            self.click(*locator)

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

    def visibility_of_element_located(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
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

    def verify_checkbox_attribute_value(self, *locator):
        actual_text = self.driver.find_element(*locator).is_selected()
        assert actual_text, f"Expected True but got {actual_text}"

    def verify_by_webelement(self, element, expected_text):
        actual_text = element.text
        assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"

    def wait_for_url_to_change(self, initial_url):
        self.wait.until(
            EC.url_changes(initial_url),
            message=f'Url {initial_url} did not change'
        )

    def scroll(self):
        self.driver.execute_script('window.scrollBy(0, 1000)')

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'Expected {expected_partial_url} not in url'
        )

    def verify_url(self, url):
        self.wait.until(
            EC.url_to_be(url),
            message=f'Expected {url} is not present.'
        )