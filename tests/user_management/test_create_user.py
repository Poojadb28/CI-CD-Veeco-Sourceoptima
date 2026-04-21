import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_create_user(create_customer_user):
    success_msg = create_customer_user.get_success_message()

    assert "User created successfully" in success_msg