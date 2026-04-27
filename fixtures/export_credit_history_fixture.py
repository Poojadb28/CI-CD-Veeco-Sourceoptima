import os
import pytest

from pages.systemadmin_login_page import LoginPage
from pages.systemadmin_page import SystemAdminPage


@pytest.fixture
def export_credit_history(browser):

    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    admin = SystemAdminPage(browser)

    # Navigate to User Admin
    admin.open_user_admin()

    # Download folder (Jenkins safe)
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    # Clean old files
    for f in os.listdir(download_dir):
        if "credit_history" in f.lower():
            os.remove(os.path.join(download_dir, f))

    return admin, download_dir