import pytest
from pages.user_admin_page import UserAdminPage


@pytest.mark.smoke
def test_duplicate_creation_of_admin_user(system_admin_login):
    browser = system_admin_login
    user_page = UserAdminPage(browser)

    user_page.click_user_admin_view()

    # First open + cancel
    user_page.click_create_user()
    user_page.click_cancel()

    # Create duplicate user
    user_page.click_create_user()
    user_page.enter_full_name("user1")
    user_page.enter_email("user1@gmail.com")
    user_page.enter_password("aspl@1234")
    user_page.enter_confirm_password("aspl@1234")
    user_page.select_user_role("Admin")
    user_page.submit_user()

    error_msg = user_page.get_duplicate_error()

    assert "Failed to create user" in error_msg