import pytest
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.smoke
def test_user_login(user_login):
    browser = user_login

    WebDriverWait(browser, 15).until(
        lambda d: "dashboard" in d.current_url.lower() or "orgchart" in d.current_url.lower()
    )

    assert "dashboard" in browser.current_url.lower() or "orgchart" in browser.current_url.lower()