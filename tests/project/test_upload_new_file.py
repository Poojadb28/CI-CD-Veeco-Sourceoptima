import pytest


@pytest.mark.regression
def test_upload_new_file(upload_new_file):
    project, file_name = upload_new_file

    assert project.verify_file_uploaded(file_name)