# import pytest
# import time
# from pages.systemadmin_login_page import LoginPage
# from pages.project_page import ProjectPage


# @pytest.fixture
# def edit_space(browser):

#     # LOGIN (independent)
#     login = LoginPage(browser)
#     login.login("prekshita@sourceoptima.com", "aspl1234")

#     project = ProjectPage(browser)  

#     # NAVIGATION
#     project.click_projects()

#     # existing space
#     old_name = "TestSpace_1"
#     new_name = f"TestSpace_{int(time.time())}"

#     # Right click
#     project.right_click_root_space(old_name)

#     # Edit flow
#     project.click_edit_details()
#     project.edit_space_name(new_name)
#     project.change_icon()
#     project.select_purple_color()
#     project.save_changes()

#     return project, new_name

import pytest
import time

from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage


@pytest.fixture
def edit_space(browser):

    # =========================
    # LOGIN
    # =========================
    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    project = ProjectPage(browser)

    # =========================
    # NAVIGATION
    # =========================
    project.click_projects()

    # =========================
    # CREATE ROOT SPACE
    # =========================
    project.right_click_on_canvas()
    project.click_new_root_space()

    old_name = f"TestSpace_{int(time.time())}"

    project.enter_space_name(old_name)
    project.open_icon_selector()
    project.select_color()
    project.click_create_space()

    # Wait for creation
    project.wait.until(lambda d: old_name in d.page_source)

    # =========================
    # EDIT SPACE
    # =========================
    new_name = f"{old_name}_Edited"

    project.right_click_root_space(old_name)

    project.click_edit_details()
    project.edit_space_name(new_name)
    project.change_icon()
    project.select_purple_color()
    project.save_changes()

    # Wait for update reflected
    project.wait.until(lambda d: new_name in d.page_source)

    return project, new_name