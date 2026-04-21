import pytest

@pytest.mark.smoke
def test_create_root_space(create_root_space):
    project, space_name = create_root_space

    success_msg = project.get_success_message()

    assert "Space created successfully" in success_msg