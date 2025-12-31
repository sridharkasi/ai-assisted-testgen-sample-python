from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MyInfoPage(BasePage):

    MENU_MY_INFO = (By.XPATH, "//span[text()='My Info']")
    HEADER_MY_INFO = (By.XPATH, "//h6[text()='PIM']")

    def open_my_info(self):
        self.click(self.MENU_MY_INFO)

    def is_loaded(self):
        return self.is_visible(self.HEADER_MY_INFO)
