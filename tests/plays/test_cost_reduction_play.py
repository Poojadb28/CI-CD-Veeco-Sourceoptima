import time

import pytest


@pytest.mark.regression
def test_cost_reduction_play(cost_reduction_play):

    cost = cost_reduction_play

    cost.click_view_results()
    cost.click_view_details()
    cost.open_report_tab()
    time.sleep(2)  # Wait for report to load

    cost.take_screenshot()
    cost.close_popup()