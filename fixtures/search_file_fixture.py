import pytest
import os

from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage


@pytest.fixture
def search_file(browser):

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

    # Wait if processing exists
    try:
        project.wait_for_processing_complete()
    except:
        pass

    # Search value
    search_value = "0184.pdf"

    project.search_file(search_value)

    # VERY IMPORTANT WAIT
    project.wait.until(lambda d: search_value in d.page_source)

    return project, search_value