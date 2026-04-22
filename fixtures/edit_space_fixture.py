import pytest
import time
from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage


@pytest.fixture
def edit_space(browser):

    # LOGIN (independent)
    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    project = ProjectPage(browser)  

    # NAVIGATION
    project.click_projects()

    # existing space
    old_name = "TestSpace_1"
    new_name = f"TestSpace_{int(time.time())}"

    # Right click
    project.right_click_root_space(old_name)

    # Edit flow
    project.click_edit_details()
    project.edit_space_name(new_name)
    project.change_icon()
    project.select_purple_color()
    project.save_changes()

    return project, new_name