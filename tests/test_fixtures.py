from selene import browser

from pages.header import header
from pages.login_page import login

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


def test_github_desktop(setup_desktop_browser):

    browser.open('/')
    header.click_on_sign_in_button()
    login.assert_open_page()


def test_github_mobile(setup_mobile_browser):

    browser.open('/')
    header.open_burger_menu()
    header.click_on_sign_in_button()
    login.assert_open_page()
