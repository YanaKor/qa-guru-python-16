from selene import browser


class LoginPage:

    login_link = 'https://github.com/login'

    def assert_open_page(self):
        current_url = browser.driver.current_url
        return current_url == self.login_link, f'Expected {self.login_link}, but got {current_url}'
