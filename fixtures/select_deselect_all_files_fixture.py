import os
import time
import pytest

from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage


@pytest.fixture
def select_deselect_all_files(browser):

    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    project = ProjectPage(browser)

    # ================= PROJECT =================
    project.click_projects()

    # ================= CREATE ROOT SPACE =================
    root_space = f"TestSpace_{int(time.time())}"

    project.right_click_on_canvas()
    project.click_new_root_space()
    project.enter_space_name(root_space)
    project.choose_icon()
    project.select_color()
    project.click_create_space()

    # WAIT for root space (VERY IMPORTANT)
    project.wait.until(lambda d: root_space in d.page_source)

    project.open_root_space(root_space)

    # =========================
    # CREATE PROJECT
    # =========================
    project_name = f"TestFile_{int(time.time())}"

    file_path = os.path.abspath("testdata/files/0184.pdf")
    assert os.path.exists(file_path), "File not found"

    project.click_new_upload()
    project.enter_project_name(project_name)
    project.upload_file(file_path)
    project.click_upload()

    project.wait_for_processing_complete()

    # =========================
    # OPEN PROJECT
    # =========================
    project.open_project(project_name)

    return project