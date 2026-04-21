import pytest
from pages.systemadmin_login_page import LoginPage


@pytest.fixture
def logout_user(browser):
    login = LoginPage(browser)

    # Login first
    login.login("prekshita@sourceoptima.com", "aspl1234")

    # Perform logout
    login.click_logout()

    return browser