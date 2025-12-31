from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    MENU_MY_INFO = (By.XPATH, "//span[text()='My Info']")

    def is_loaded(self):
        return self.is_visible(self.DASHBOARD_HEADER)

    def go_to_my_info(self):
        self.click(self.MENU_MY_INFO)
