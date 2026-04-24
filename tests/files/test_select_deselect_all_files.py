import pytest


@pytest.mark.smoke
def test_select_deselect_all_files(select_deselect_all_files):

    project = select_deselect_all_files

    # Select all
    project.select_all_files()
    assert project.verify_deselect_visible(), "Deselect All button not visible"

    # Deselect all
    project.deselect_all_files()
    assert project.verify_select_visible(), "Select All button not visible again"