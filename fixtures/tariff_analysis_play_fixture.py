import os
import time
import pytest

from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage
from pages.tariff_analysis_play_page import TariffPage


@pytest.fixture
def tariff_analysis_play(browser):

    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    project = ProjectPage(browser)
    tariff = TariffPage(browser)

    # ================= PROJECT =================
    project.click_projects()

    project.right_click_on_canvas()
    project.click_new_root_space()

    root_space = f"TestSpace_{int(time.time())}"

    project.enter_space_name(root_space)
    project.open_icon_selector()
    project.select_color()
    project.click_create_space()

    project.wait.until(lambda d: root_space in d.page_source)
    project.open_root_space(root_space)

    project_name = f"TestFile_{int(time.time())}"
    file_path = os.path.abspath("testdata/files/0194.pdf")

    if not os.path.exists(file_path):
        raise Exception(f"File not found: {file_path}")

    project.click_new_upload()
    project.enter_project_name(project_name)
    project.upload_file(file_path)
    project.click_upload()

    project.wait_for_processing_complete()

    project.open_project(project_name)
    project.select_all_files()

    # ================= PLAY =================
    tariff.select_tariff_analysis()
    tariff.treat_as_assembly()
    tariff.set_top_level()
    tariff.run_tariff_analysis()

    return tariff