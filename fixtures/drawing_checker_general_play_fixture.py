import os
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.systemadmin_login_page import LoginPage
from pages.project_page import ProjectPage
from pages.drawing_checker_general_play_page import DrawingCheckerGeneralPage


@pytest.fixture
def drawing_checker_general_play(browser):

    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    project = ProjectPage(browser)
    general = DrawingCheckerGeneralPage(browser)

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
    general.select_drawing_checker_general()
    general.click_run()
    general.wait_for_processing()
    general.click_view_results()

    # ================= TAB SWITCH =================
    main_window = browser.current_window_handle

    WebDriverWait(browser, 20).until(lambda d: len(d.window_handles) > 1)

    for window in browser.window_handles:
        if window != main_window:
            browser.switch_to.window(window)
            break

    return general, main_window