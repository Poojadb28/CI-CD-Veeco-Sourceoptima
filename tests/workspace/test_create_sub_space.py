import pytest

@pytest.mark.smoke
def test_add_sub_space(create_sub_space):
    project, sub_space_name = create_sub_space

    assert project.verify_sub_space_created(sub_space_name)