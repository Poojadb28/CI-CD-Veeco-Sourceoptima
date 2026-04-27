import pytest


@pytest.mark.smoke
def test_create_new_project(create_new_project):

    project, project_name = create_new_project

    assert project.verify_project_created(project_name), "Project not created"