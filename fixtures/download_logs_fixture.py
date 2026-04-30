import pytest
import os
import time
from datetime import datetime

from pages.systemadmin_login_page import LoginPage
from pages.system_stats_page import SystemStatsPage

@pytest.fixture
def download_logs(browser):

    login = LoginPage(browser)
    login.login("prekshita@sourceoptima.com", "aspl1234")

    system_stats = SystemStatsPage(browser)

    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    today_date = datetime.today().strftime("%Y-%m-%d")
    file_prefix = f"sourceoptima_logs_{today_date}"

    # clean old files
    for f in os.listdir(download_dir):
        if f.startswith(file_prefix):
            os.remove(os.path.join(download_dir, f))

    time_ranges = [
        system_stats.time_range_today,
        system_stats.time_range_2_days,
        system_stats.time_range_3_days,
        system_stats.time_range_5_days,
        system_stats.time_range_7_days
    ]

    # FIXED FLOW
    for time_range in time_ranges:
        system_stats.select_time_range(time_range)
        system_stats.download_logs_for_range(download_dir)

    return download_dir, file_prefix