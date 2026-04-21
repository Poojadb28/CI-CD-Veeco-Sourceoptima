import pytest
import time
from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage


@pytest.fixture
def create_root_space(browser):
    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    project = ProjectPage(browser)

    project.click_projects()
    project.right_click_on_canvas()
    project.click_new_root_space()

    # unique name (IMPORTANT)
    space_name = f"TestSpace_{int(time.time())}"

    project.enter_space_name(space_name)
    project.open_icon_selector()
    project.select_color()
    project.click_create_space()

    return project, space_name