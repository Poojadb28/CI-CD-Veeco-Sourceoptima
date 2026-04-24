import pytest
import os


@pytest.mark.regression
def test_design_review_play(design_review_play):

    design = design_review_play

    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    design.click_view_results()
    design.click_view_details()
    design.open_report_tab()

    design.download_report(download_dir)

    design.close_popup()