# pytest_plugins = [
#     "fixtures.systemadmin_login_fixture",
#     "fixtures.user_creation_fixture",
#     "fixtures.admin_creation_fixture",
#     "fixtures.logout_fixture",
#     "fixtures.project_fixture",
#     "fixtures.subspace_fixture",
#     "fixtures.delete_root_space_fixture"
# ]

# import pytest
# import sys
# import os

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


# # =========================
# # FIX IMPORT PATH (IMPORTANT FOR JENKINS)
# # =========================
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, BASE_DIR)


# # =========================
# # ADD COMMAND LINE OPTION
# # =========================
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Browser to run tests"
#     )


# # =========================
# # DRIVER SETUP
# # =========================
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("--browser")

#     if browser_name == "chrome":
#         chrome_options = Options()

#         # Required for Jenkins / headless
#         chrome_options.add_argument("--headless=new")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument("--window-size=1920,1080")

#         # Fix download / security issues
#         prefs = {
#             "download.prompt_for_download": False,
#             "download.directory_upgrade": True,
#             "safebrowsing.enabled": True
#         }
#         chrome_options.add_experimental_option("prefs", prefs)

#         driver = webdriver.Chrome(
#         executable_path="drivers/chromedriver.exe",
#         options=chrome_options
#         )

#     else:
#         raise Exception(f"Browser {browser_name} not supported")

#     driver.implicitly_wait(10)

#     yield driver

#     driver.quit()


# # =========================
# # PYTEST HOOK (OPTIONAL - FOR LOGGING)
# # =========================
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()

#     if report.when == "call" and report.failed:
#         driver = item.funcargs.get("browser", None)
#         if driver:
#             screenshots_dir = os.path.join(BASE_DIR, "screenshots")
#             os.makedirs(screenshots_dir, exist_ok=True)

#             file_name = os.path.join(
#                 screenshots_dir,
#                 f"{item.name}.png"
#             )
#             driver.save_screenshot(file_name)

# pytest_plugins = [
#     "fixtures.systemadmin_login_fixture",
#     "fixtures.user_creation_fixture",
#     "fixtures.admin_creation_fixture",
#     "fixtures.logout_fixture",
#     "fixtures.project_fixture",
#     "fixtures.subspace_fixture",
#     "fixtures.delete_root_space_fixture"
# ]

# import pytest
# import sys
# import os
# from datetime import datetime

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# # Safe import for report plugin
# try:
#     import pytest_html
# except ImportError:
#     pytest_html = None


# # =========================
# # PATH SETUP
# # =========================
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, BASE_DIR)


# # =========================
# # CLI OPTIONS
# # =========================
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome")
#     parser.addoption("--headless", action="store_true", help="Run in headless mode")


# # =========================
# # SAFE DRIVER SETUP
# # =========================
# def get_driver_service():
#     try:
#         path = ChromeDriverManager().install()

#         # Fix for Windows chromedriver path issue
#         if "THIRD_PARTY_NOTICES" in path:
#             path = os.path.join(os.path.dirname(path), "chromedriver.exe")

#         return Service(path)

#     except Exception:
#         # Fallback (VERY IMPORTANT for Jenkins / offline)
#         local_path = os.path.join(BASE_DIR, "drivers", "chromedriver.exe")

#         if not os.path.exists(local_path):
#             raise Exception("Chromedriver not found locally or via webdriver-manager")

#         return Service(local_path)


# # =========================
# # BROWSER FIXTURE
# # =========================
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("--browser")
#     headless = request.config.getoption("--headless")

#     if browser_name.lower() == "chrome":
#         chrome_options = Options()

#         if headless:
#             chrome_options.add_argument("--headless=new")

#         # Stability for Jenkins
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument("--window-size=1920,1080")

#         # Download directory setup
#         download_dir = os.path.join(BASE_DIR, "downloads")
#         os.makedirs(download_dir, exist_ok=True)

#         prefs = {
#             "download.default_directory": download_dir,
#             "download.prompt_for_download": False,
#             "download.directory_upgrade": True,
#             "safebrowsing.enabled": True
#         }
#         chrome_options.add_experimental_option("prefs", prefs)

#         service = get_driver_service()
#         driver = webdriver.Chrome(service=service, options=chrome_options)

#     else:
#         raise Exception(f"Unsupported browser: {browser_name}")

#     driver.implicitly_wait(10)

#     yield driver

#     driver.quit()


# # =========================
# # SCREENSHOT + HTML REPORT
# # =========================
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()

#     if report.when == "call" and report.failed:
#         driver = item.funcargs.get("browser", None)

#         if driver:
#             screenshots_dir = os.path.join(BASE_DIR, "screenshots")
#             os.makedirs(screenshots_dir, exist_ok=True)

#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             file_name = f"{item.name}_{timestamp}.png"
#             file_path = os.path.join(screenshots_dir, file_name)

#             driver.save_screenshot(file_path)

#             # Attach screenshot to HTML report
#             if pytest_html:
#                 extra = getattr(report, "extra", [])
#                 extra.append(pytest_html.extras.image(file_path))
#                 report.extra = extra

pytest_plugins = [
    "fixtures.systemadmin_login_fixture",
    "fixtures.user_creation_fixture",
    "fixtures.admin_creation_fixture",
    "fixtures.logout_fixture",
    "fixtures.project_fixture",
    "fixtures.subspace_fixture",
    "fixtures.delete_root_space_fixture"
]

import pytest
import sys
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Safe import for pytest-html
try:
    import pytest_html
except ImportError:
    pytest_html = None


# =========================
# PATH SETUP
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)


# =========================
# CLI OPTIONS
# =========================
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true", help="Run in headless mode")


# =========================
# DRIVER SETUP
# =========================
def get_driver_service():
    try:
        path = ChromeDriverManager().install()

        if "THIRD_PARTY_NOTICES" in path:
            path = os.path.join(os.path.dirname(path), "chromedriver.exe")

        return Service(path)

    except Exception:
        local_path = os.path.join(BASE_DIR, "drivers", "chromedriver.exe")

        if not os.path.exists(local_path):
            raise Exception("Chromedriver not found locally or via webdriver-manager")

        return Service(local_path)


# =========================
# BROWSER FIXTURE
# =========================
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_name.lower() == "chrome":
        chrome_options = Options()

        if headless:
            chrome_options.add_argument("--headless=new")

        # Jenkins stability
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        # Download folder
        download_dir = os.path.join(BASE_DIR, "downloads")
        os.makedirs(download_dir, exist_ok=True)

        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)

        service = get_driver_service()
        driver = webdriver.Chrome(service=service, options=chrome_options)

    else:
        raise Exception(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# =========================
# SCREENSHOT ON FAILURE
# =========================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser", None)

        if driver:
            screenshots_dir = os.path.join(BASE_DIR, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)

            if pytest_html:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(file_path))
                report.extra = extra


# =========================
# REPORT TITLE + METADATA
# =========================
def pytest_html_report_title(report):
    report.title = "🚀 SourceOptima Automation Report"


def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Project"] = "SourceOptima"
        config._metadata["Tester"] = "Pooja D B"
        config._metadata["Environment"] = "QA"
        config._metadata["Browser"] = "Chrome"
        config._metadata["Framework"] = "Pytest + Selenium"


# =========================
# TEST RESULT STORAGE
# =========================
test_results = {
    "passed": 0,
    "failed": 0,
    "skipped": 0
}


# =========================
# CAPTURE TEST RESULTS
# =========================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_logreport(report):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        if rep.passed:
            test_results["passed"] += 1
        elif rep.failed:
            test_results["failed"] += 1
        elif rep.skipped:
            test_results["skipped"] += 1


# =========================
# DASHBOARD + CHART
# =========================
def pytest_html_results_summary(prefix, summary, postfix):
    if not pytest_html:
        return

    passed = test_results["passed"]
    failed = test_results["failed"]
    skipped = test_results["skipped"]

    prefix.extend([
        pytest_html.extras.html(f"""
        <h2>📊 Test Execution Dashboard</h2>

        <p><b>Passed:</b> {passed}</p>
        <p><b>Failed:</b> {failed}</p>
        <p><b>Skipped:</b> {skipped}</p>

        <canvas id="testChart" width="400" height="200"></canvas>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script>
        var ctx = document.getElementById('testChart').getContext('2d');

        new Chart(ctx, {{
            type: 'pie',
            data: {{
                labels: ['Passed', 'Failed', 'Skipped'],
                datasets: [{{
                    data: [{passed}, {failed}, {skipped}],
                    backgroundColor: ['#28a745', '#dc3545', '#ffc107']
                }}]
            }}
        }});
        </script>
        """)
    ])


# =========================
# TERMINAL SUMMARY
# =========================
def pytest_terminal_summary(terminalreporter):
    print("\n========= FINAL TEST SUMMARY =========")
    print(f"PASSED: {test_results['passed']}")
    print(f"FAILED: {test_results['failed']}")
    print(f"SKIPPED: {test_results['skipped']}")
    print("=====================================")