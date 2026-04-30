import pytest
import os


@pytest.mark.smoke
def test_download_logs(download_logs):

    download_dir, file_prefix = download_logs

    files = [
        f for f in os.listdir(download_dir)
        if f.startswith(file_prefix) and not f.endswith(".crdownload")
    ]

    print("Downloaded files:", files)

    # Assertions
    assert len(files) == 5, "Not all log files downloaded"

    for file in files:
        file_path = os.path.join(download_dir, file)
        assert os.path.getsize(file_path) > 0, f"{file} is empty"