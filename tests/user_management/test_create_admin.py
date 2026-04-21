import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_create_admin(create_admin_user):
    success_msg = create_admin_user.get_success_message()

    assert "User created successfully" in success_msg