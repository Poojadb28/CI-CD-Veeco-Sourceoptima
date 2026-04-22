import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_create_project(create_project):
    project, name = create_project

    assert project.verify_project_created(name)