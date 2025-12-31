import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_navigate_to_my_info(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    my_info = MyInfoPage(driver)

    # Step 1 — Login
    login.load()
    login.login("Admin", "admin123")
    assert dashboard.is_loaded(), "Dashboard should be visible after login"

    # Step 2 — Navigate to My Info
    my_info.open_my_info()

    # Step 3 — Validate page loaded
    assert my_info.is_loaded(), "My Info page should be visible"
