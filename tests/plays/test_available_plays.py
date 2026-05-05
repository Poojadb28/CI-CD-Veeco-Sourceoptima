# import pytest
# from selenium.webdriver.support.ui import WebDriverWait

# @pytest.mark.regression
# def test_available_plays_enable_disable(available_plays):

#     admin, plays = available_plays

#     for play in plays:

#         # Disable
#         admin.toggle_play(play)

#         message = admin.wait_for_disable_message()
#         assert "disabled" in message.lower()

#         # Enable
#         admin.toggle_play(play)

#         message = admin.wait_for_enable_message()
#         assert "enabled" in message.lower()

import pytest


@pytest.mark.regression
def test_available_plays_enable_disable(available_plays):

    admin, plays = available_plays

    for play in plays:

        # Disable
        admin.toggle_play(play)

        # Wait for actual state instead of toast
        assert admin.is_play_enabled(play) == "disabled"

        # Enable
        admin.toggle_play(play)

        # Again validate real UI state
        assert admin.is_play_enabled(play) == "enabled"