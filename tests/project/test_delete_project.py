import pytest


@pytest.mark.smoke
def test_delete_project(delete_project):

    project, project_name = delete_project

    assert project.verify_project_deleted(project_name), "Project deletion failed"