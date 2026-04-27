import pytest


@pytest.mark.regression
def test_export_credit_history(export_credit_history):

    admin, download_dir = export_credit_history

    # Click export
    admin.click_export_credit_history()

    # Verify download
    assert admin.wait_for_credit_history_download(download_dir), \
        "Credit history file not downloaded"