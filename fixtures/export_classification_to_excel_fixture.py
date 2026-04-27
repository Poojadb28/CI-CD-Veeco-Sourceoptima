import os
import time
import pytest

from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage


@pytest.fixture
def export_classification_to_excel(browser):

    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    project = ProjectPage(browser)

    # ================= PROJECT =================
    project.click_projects()

    # -------- CREATE ROOT SPACE --------
    project.right_click_on_canvas()
    project.click_new_root_space()

    root_space = f"TestSpace_{int(time.time())}"

    project.enter_space_name(root_space)
    project.open_icon_selector()
    project.select_color()
    project.click_create_space()

    project.wait.until(lambda d: root_space in d.page_source)
    project.open_root_space(root_space)

    # -------- CREATE PROJECT --------
    project_name = f"TestFile_{int(time.time())}"
    file_path = os.path.abspath("testdata/files/0194.pdf")

    project.create_project(project_name, file_path)

    project.wait_for_processing_complete()

    project.open_project(project_name)

    # Select files (IMPORTANT)
    project.select_all_files()

    # Download folder (Jenkins safe)
    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    # Clean old files
    for f in os.listdir(download_dir):
        if "classification" in f.lower():
            os.remove(os.path.join(download_dir, f))

    return project, download_dir