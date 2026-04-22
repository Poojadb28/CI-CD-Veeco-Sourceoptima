import pytest


@pytest.mark.regression
def test_edit_details(edit_space):

    project, new_name = edit_space

    assert project.verify_space_updated(new_name), "Space update failed"