import pytest


@pytest.mark.smoke
def test_add_new_project(upload_project):

    projects, project_name = upload_project

    assert projects.verify_project_created(project_name), "Project not created"