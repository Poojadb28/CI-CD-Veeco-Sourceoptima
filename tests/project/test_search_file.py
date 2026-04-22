import pytest

@pytest.mark.regression
def test_search_file(search_file):

    project, file_name = search_file

    assert project.verify_file_present(file_name), "File not found after search"