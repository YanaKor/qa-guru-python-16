import pytest
from selene import browser

from settings import ConfigBrowser
from pages.header import header
from pages.login_page import login

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""


def test_github_desktop(setup_browser):
    if (browser.config.window_width == ConfigBrowser.window_width_mobile_1 and
        browser.config.window_height == ConfigBrowser.window_height_mobile_1) or (
            browser.config.window_width == ConfigBrowser.window_width_mobile_2 and
            browser.config.window_height == ConfigBrowser.window_height_mobile_2) or (
            browser.config.window_width == ConfigBrowser.window_width_mobile_3 and
            browser.config.window_height == ConfigBrowser.window_height_mobile_3):
        pytest.skip(reason='Тест только для desktop')

    browser.open('/')
    header.click_on_sign_in_button()
    login.assert_open_page()


def test_github_mobile(setup_browser):
    if (browser.config.window_width == ConfigBrowser.window_width_desktop_1 and
        browser.config.window_height == ConfigBrowser.window_height_desktop_1) or (
            browser.config.window_width == ConfigBrowser.window_width_desktop_2 and
            browser.config.window_height == ConfigBrowser.window_height_desktop_2) or (
            browser.config.window_width == ConfigBrowser.window_width_desktop_3 and
            browser.config.window_height == ConfigBrowser.window_height_desktop_3):
        pytest.skip(reason='Тест только для mobile')

    browser.open('/')
    header.open_burger_menu()
    header.click_on_sign_in_button()
    login.assert_open_page()
