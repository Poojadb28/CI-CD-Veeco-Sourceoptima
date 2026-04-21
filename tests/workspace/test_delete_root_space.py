import pytest


@pytest.mark.smoke
def test_delete_root_space(delete_root_space):
    project, root_space_name = delete_root_space

    assert project.verify_space_deleted(root_space_name)