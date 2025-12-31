import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_valid_login(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.load()
    login.login("Admin", "admin123")

    assert dashboard.is_loaded(), "Dashboard page should be visible after login"
