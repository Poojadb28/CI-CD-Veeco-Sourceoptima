import os
import platform
import shutil
import sys
import tempfile
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
    from selenium.webdriver.chrome.service import Service
except ImportError:
    Service = None


pytest_plugins = [
    "fixtures.systemadmin_login_fixture",
    "fixtures.user_creation_fixture",
    "fixtures.admin_creation_fixture",
    "fixtures.logout_fixture",
    "fixtures.project_fixture",
    "fixtures.subspace_fixture",
    "fixtures.delete_root_space_fixture",
    "fixtures.project_creation_fixture",
    "fixtures.project_upload_fixture",
    "fixtures.file_upload_fixture",
    "fixtures.edit_space_fixture",
    "fixtures.delete_project_fixture",
    "fixtures.search_file_fixture",
    "fixtures.available_plays_fixture",
    "fixtures.cost_reduction_play_fixture",
    "fixtures.design_review_fixture",
    "fixtures.drawing_checker_both_play_fixture",
    "fixtures.drawing_checker_general_play_fixture",
    "fixtures.drawing_checker_v2_play_fixture",
    "fixtures.drawing_checker_veeco_play_fixture",
    "fixtures.tariff_analysis_play_fixture",
    "fixtures.download_logs_fixture",
    "fixtures.delete_file_fixture",
    "fixtures.select_deselect_all_files_fixture",
    "fixtures.filter_labels_fixture",
    "fixtures.create_new_project_fixture",
    "fixtures.export_credit_history_fixture",
    "fixtures.export_classification_to_excel_fixture",
    "fixtures.duplicate_admin_creation_fixture",
    "fixtures.duplicate_user_creation_fixture",
]


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser tests without opening a visible Chrome window.",
    )


def _env_flag(name):
    return os.getenv(name, "").strip().lower() in ("1", "true", "yes", "on")


def _chromedriver_path():
    env_path = os.getenv("CHROMEDRIVER_PATH")
    if env_path and os.path.exists(env_path):
        return env_path

    local_driver = os.path.join(BASE_DIR, "drivers", "chromedriver.exe")
    if platform.system().lower() == "windows" and os.path.exists(local_driver):
        return local_driver

    return None


def _create_chrome_driver(options):
    driver_path = _chromedriver_path()

    if Service is not None and driver_path:
        try:
            return webdriver.Chrome(service=Service(driver_path), options=options)
        except TypeError:
            pass

    if driver_path:
        return webdriver.Chrome(executable_path=driver_path, options=options)

    return webdriver.Chrome(options=options)


def _enable_headless_downloads(driver, download_dir):
    try:
        driver.execute_cdp_cmd(
            "Page.setDownloadBehavior",
            {"behavior": "allow", "downloadPath": download_dir},
        )
    except Exception:
        pass


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser").lower()
    if browser_name != "chrome":
        raise ValueError("Unsupported browser: {}".format(browser_name))

    download_dir = os.path.join(BASE_DIR, "downloads")
    os.makedirs(download_dir, exist_ok=True)
    chrome_profile_dir = tempfile.mkdtemp(prefix="sourceoptima_chrome_")

    chrome_options = Options()
    if (
        request.config.getoption("--headless")
        or _env_flag("HEADLESS")
        or os.getenv("JENKINS_URL")
        or os.getenv("CI")
    ):
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-crash-reporter")
    chrome_options.add_argument("--disable-breakpad")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--remote-debugging-port=0")
    chrome_options.add_argument("--user-data-dir={}".format(chrome_profile_dir))
    chrome_options.add_argument("--window-size=1920,1080")

    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "profile.default_content_setting_values.automatic_downloads": 1,
        },
    )

    driver = None
    try:
        driver = _create_chrome_driver(chrome_options)
        _enable_headless_downloads(driver, download_dir)
        driver.implicitly_wait(10)

        yield driver
    finally:
        if driver:
            driver.quit()
        shutil.rmtree(chrome_profile_dir, ignore_errors=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("browser")
    if not driver:
        return

    screenshots_dir = os.path.join(BASE_DIR, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = "{}_{}.png".format(item.name, timestamp)
    driver.save_screenshot(os.path.join(screenshots_dir, file_name))
