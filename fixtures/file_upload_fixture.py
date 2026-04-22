import pytest
import time
import os

from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage

@pytest.fixture
def upload_new_file(browser):

    # LOGIN (independent)
    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    project = ProjectPage(browser)

    # NAVIGATION
    project.click_projects()

    root_space = "TestSpace_1"
    project_name = "TestFile"   

    project.open_root_space(root_space)
    project.open_project(project_name)

    file_path = os.path.abspath("testdata/files/0187.pdf")

    assert os.path.exists(file_path), "File not found"

    # Upload flow
    project.click_new_upload()
    project.upload_file(file_path) 
    project.click_upload()
    project.wait_for_processing_complete()

   
    return project, os.path.basename(file_path)