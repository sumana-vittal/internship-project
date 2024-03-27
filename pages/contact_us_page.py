from selenium.webdriver.common.by import By

from pages.base_page import Page


class ContactUsPage(Page):

    SETTINGS_MENU = (By.XPATH, "//div[text()='Settings']")
    CONTACT_US_SETTINGS = (By.XPATH, "//div[@class='settings-block-menu'] //div[text()='Contact us']")
    SOCIAL_ICONS = (By.CSS_SELECTOR, "[href*='reelly'] [class='text-social']")

    social_icons_names = ['Instagram', 'Telegram', 'Youtube', 'Facebook', 'Twitter', 'TikTok', 'Pinterest', 'Snapchat',
                          'LinkedIn']

    def click_settings(self):
        self.wait_element_clickable_click(*self.SETTINGS_MENU)

    def click_contact_us(self):
        self.wait_element_clickable_click(*self.CONTACT_US_SETTINGS)

    def verify_contact_us(self):
        self.verify_partial_url('contact-us')

    def verify_social_icons(self):
        social_icons = self.find_elements(*self.SOCIAL_ICONS)
        for icon in social_icons:
            print(icon.text)
            self.verify_by_webelement(icon, icon.text)

