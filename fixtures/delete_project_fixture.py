import pytest
from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage


# @pytest.fixture
# def delete_project(browser):

#     # LOGIN
#     login = LoginPage(browser)
#     login.login("prekshita@sourceoptima.com", "aspl1234")

#     project = ProjectPage(browser)

#     # NAVIGATION
#     project.open_projects()

#     root_space = "TestSpace_1"
#     project_name = "TestFile_1"

#     project.open_root_space(root_space)

#     project.open_project(project_name)

#     # DELETE FLOW
#     project.click_delete_project()
#     project.confirm_delete()

#     return project, project_name
@pytest.fixture
def delete_project(create_project):

    project, project_name = create_project

    # WAIT for processing popup to disappear
    project.wait_for_processing_complete()

    # NOW open project (safe)
    project.open_project(project_name)

    # DELETE FLOW
    project.click_delete_project()
    project.confirm_delete()
    project.wait_for_delete_complete()

    return project, project_name