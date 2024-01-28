import pytest
from selene import browser

from settings import ConfigBrowser
from pages.header import header
from pages.login_page import login

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

desktop_only = pytest.mark.parametrize(
    'setup_browser', [(ConfigBrowser.window_width_desktop_1, ConfigBrowser.window_height_desktop_1),
                      (ConfigBrowser.window_width_desktop_2, ConfigBrowser.window_height_desktop_2),
                      (ConfigBrowser.window_width_desktop_3, ConfigBrowser.window_height_desktop_3)],
    ids=['HD', 'Full HD', '2K'], indirect=True)

mobile_only = pytest.mark.parametrize(
    'setup_browser', [(ConfigBrowser.window_width_mobile_1, ConfigBrowser.window_height_mobile_1),
                      (ConfigBrowser.window_width_mobile_2, ConfigBrowser.window_height_mobile_2),
                      (ConfigBrowser.window_width_mobile_3, ConfigBrowser.window_height_mobile_3)],
    ids=['Samsung Galaxy S8', 'iPhone 8 Plus', 'iPad Mini'], indirect=True)


@desktop_only
def test_github_desktop(setup_browser):

    browser.open('/')
    header.click_on_sign_in_button()
    login.assert_open_page()


@mobile_only
def test_github_mobile(setup_browser):

    browser.open('/')
    header.open_burger_menu()
    header.click_on_sign_in_button()
    login.assert_open_page()
