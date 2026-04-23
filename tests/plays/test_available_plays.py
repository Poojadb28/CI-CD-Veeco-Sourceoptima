import pytest
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.regression
def test_available_plays_enable_disable(available_plays):

    admin, plays = available_plays

    for play in plays:

        admin.toggle_play(play)
        assert admin.get_disable_message() == "Play disabled successfully"

        admin.toggle_play(play)
        assert admin.get_enable_message() == "Play enabled successfully"