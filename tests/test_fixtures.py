from selene import browser

from pages.header import Header
from pages.login_page import LoginPage

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


def test_github_desktop(setup_desktop_browser):
    header = Header()
    login_page = LoginPage()

    browser.open('/')
    header.click_on_sign_in_button()
    login_page.assert_open_page()


def test_github_mobile(setup_mobile_browser):
    header = Header()
    login_page = LoginPage()

    browser.open('/')
    header.open_burger_menu()
    header.click_on_sign_in_button()
    login_page.assert_open_page()
