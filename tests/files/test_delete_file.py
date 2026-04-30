import pytest


@pytest.mark.smoke
def test_delete_file(delete_file):

    project, file_name = delete_file

    assert project.is_file_deleted(file_name), "File deletion failed"