import pytest
import time
import os

from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage

@pytest.fixture
def upload_project(browser):

    # LOGIN (independent)
    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    project = ProjectPage(browser)

    # NAVIGATION
    project.click_projects()

    # Use stable root space
    root_space_name = "TestSpace_1"
    project.open_root_space(root_space_name)

    # Dynamic project name
    project_name = f"TestFile_{int(time.time())}"

    # FILE PATH (Jenkins safe)
    file_path = os.path.abspath("testdata/files/0194.pdf")

    if not os.path.exists(file_path):
        raise Exception(f"File not found: {file_path}")

    # UPLOAD FLOW
    project.click_new_upload()
    project.enter_project_name(project_name)
    project.upload_file(file_path)
    project.click_upload()

    return project, project_name