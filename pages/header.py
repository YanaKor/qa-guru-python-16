from selene import browser
from base.locators import MainPageLocators


class Header:

    def click_on_sign_in_button(self):
        browser.element(MainPageLocators.SING_IN_BUTTON).click()

    def open_burger_menu(self):
        browser.element(MainPageLocators.BURGER_MENU).click()
