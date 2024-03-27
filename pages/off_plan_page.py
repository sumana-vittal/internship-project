from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


class OffPlanPage(Page):

    OFF_PLAN = (By.CSS_SELECTOR, "[class='menu-twobutton']")
    HIGH_DEMAND_PROPERTIES = (By.XPATH, "//div[@class='commision_box']//div[text()='High Demand']")
    OFF_PLAN_PAGE_TITLE = (By.CSS_SELECTOR, "[class*='off_plan']")
    HIGH_DEMAND_TAG = (By.XPATH, "//*[text()='High Demand']")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#wf-form-Search-form a[class*='filter-button']")
    HIGH_DEMAND_FILTER_BUTTON = (By.CSS_SELECTOR, "div[class='filters-tags'] [wized='priorityStatusHighDemand']")
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, ".button-filter")
    FROM_UNIT_PRICE = (By.CSS_SELECTOR, "[wized='unitPriceFromFilter']")
    TO_UNIT_PRICE = (By.CSS_SELECTOR, "[wized='unitPriceToFilter']")
    PROJECT_PRICE = (By.XPATH, "//div[@class='price-value']")
    PRICE_BOX = (By.CSS_SELECTOR, ".price-box")

    def click_off_plan(self):
        self.wait_element_clickable_click(*self.OFF_PLAN)

    def verify_off_plan_opens(self):
        # verify website
        self.verify_partial_url("off-plan")
        # verify page title
        self.verify_text('Total projects', *self.OFF_PLAN_PAGE_TITLE)

    def filter_projects(self):
        self.wait_element_clickable_click(*self.FILTER_BUTTON)
        self.wait_element_clickable_click(*self.HIGH_DEMAND_FILTER_BUTTON)
        # self.visibility_of_element_located(*self.APPLY_FILTER_BUTTON)
        # self.wait_element_clickable_click(*self.APPLY_FILTER_BUTTON)

    def verify_high_demand_project_tag(self):
        high_demand_properties = self.find_elements(*self.HIGH_DEMAND_PROPERTIES)
        # print(f"{len(high_demand_properties)} projects are in high demand.")
        for project in high_demand_properties:
            assert project.text == 'High Demand', f"Expected 'High Demand' tag but got {project.text}"
            self.verify_by_webelement(project, 'High Demand')

    def filter_project_price(self):
        self.wait_element_clickable_click(*self.FILTER_BUTTON)
        self.input_text('1200000', *self.FROM_UNIT_PRICE)
        self.input_text('2000000', *self.TO_UNIT_PRICE)
        self.wait_element_clickable_click(*self.APPLY_FILTER_BUTTON)

    def verify_project_price(self):
        sleep(2)  # required sleep here as external wait is not enough to load the page.
        # self.presence_of_element_located(*self.PRICE_BOX)
        project_prices = self.find_elements(*self.PROJECT_PRICE)
        # print(len(project_prices))
        for price in project_prices:
            project_price = price.text.split(" ")[1].replace(',', '')
            # print(project_price)
            assert 1200000 < int(project_price) < 2000000, f"Expected Project price between 1200000 to 2000000."



