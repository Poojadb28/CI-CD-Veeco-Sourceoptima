import pytest
import time
import os

from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage


@pytest.fixture
def upload_project(browser):

    # LOGIN
    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    project = ProjectPage(browser)

    # NAVIGATION
    project.click_projects()

    # =========================
    # CREATE ROOT SPACE 
    # =========================
    project.right_click_on_canvas()   
    project.click_new_root_space()

    root_space_name = f"TestSpace_{int(time.time())}"

    project.enter_space_name(root_space_name)
    project.open_icon_selector()
    project.select_color()
    project.click_create_space()

    # IMPORTANT WAIT (UI needs time to create space)
    project.wait.until(lambda d: root_space_name in d.page_source)

    # OPEN CREATED SPACE
    project.open_root_space(root_space_name)

    # =========================
    # CREATE PROJECT
    # =========================
    project_name = f"TestFile_{int(time.time())}"

    file_path = os.path.abspath("testdata/files/0194.pdf")

    if not os.path.exists(file_path):
        raise Exception(f"File not found: {file_path}")

    project.click_new_upload()
    project.enter_project_name(project_name)
    project.upload_file(file_path)
    project.click_upload()

    # VERY IMPORTANT 
    project.wait_for_processing_complete()

    return project, project_name