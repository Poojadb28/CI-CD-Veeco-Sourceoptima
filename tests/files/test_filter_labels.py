import pytest
import os


@pytest.mark.regression
def test_filter_labels(filter_labels_setup):

    project = filter_labels_setup

    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    # -------- All Labels --------
    project.apply_filter("All Labels")

    project.driver.save_screenshot(
        os.path.join(screenshots_dir, "All_Labels_Filter.png")
    )

    # -------- CAD Drawing --------
    project.apply_filter("CAD Drawing")

    project.driver.save_screenshot(
        os.path.join(screenshots_dir, "CAD_Drawing_Filter.png")
    )

    project.clear_filter()

    # -------- Technical Specification --------
    project.apply_filter("Technical Specification")

    project.driver.save_screenshot(
        os.path.join(screenshots_dir, "Technical_Specification_Filter.png")
    )

    project.clear_filter()