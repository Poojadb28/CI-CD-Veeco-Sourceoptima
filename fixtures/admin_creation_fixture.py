import time

import pytest
from pages.systemadmin_login_page import LoginPage
from pages.user_admin_page import UserAdminPage


@pytest.fixture
def create_admin_user(browser):
    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    user_page = UserAdminPage(browser)

    user_page.click_user_admin_view()

    # Check cancel functionality
    user_page.click_create_user()
    user_page.click_cancel()

    # Admin user creation
    user_page.click_create_user()

    email = f"test{time.time()}@aspl.ai"

    timestamp = str(int(time.time()))

    user_page.enter_full_name(f"test_admin_{timestamp}")
    user_page.enter_email(email)
    user_page.enter_password("aspl@1234")
    user_page.enter_confirm_password("aspl@1234")
    user_page.select_user_role("Admin")
    user_page.submit_user()

    return user_page

