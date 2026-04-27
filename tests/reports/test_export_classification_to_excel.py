import pytest


@pytest.mark.regression
def test_export_classification_to_excel(export_classification_to_excel):

    project, download_dir = export_classification_to_excel

    # Click export
    project.click_export_classification()

    # Verify download
    assert project.wait_for_classification_download(download_dir), \
        "Classification Excel file was not downloaded"