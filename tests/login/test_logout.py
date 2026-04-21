import pytest


@pytest.mark.smoke
def test_logout(logout_user):
    browser = logout_user

    # Assertion: back to login page
    assert "login" in browser.current_url.lower()