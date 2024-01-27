import pytest
from selene import browser
from selenium import webdriver
from settings import ConfigBrowser


@pytest.fixture(params=[(ConfigBrowser.window_width_desktop_1, ConfigBrowser.window_height_desktop_1),
                        (ConfigBrowser.window_width_desktop_2, ConfigBrowser.window_height_desktop_2),
                        (ConfigBrowser.window_width_desktop_3, ConfigBrowser.window_height_desktop_3)],
                ids=['HD', 'Full HD', '2K'])
def setup_desktop_browser(request):
    width, height = request.param
    options = webdriver.ChromeOptions()
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.driver = options
    browser.config.base_url = 'https://github.com'

    yield

    browser.close()


@pytest.fixture(params=[(ConfigBrowser.window_width_mobile_1, ConfigBrowser.window_height_mobile_1),
                        (ConfigBrowser.window_width_mobile_2, ConfigBrowser.window_height_mobile_2),
                        (ConfigBrowser.window_width_mobile_3, ConfigBrowser.window_height_mobile_3)],
                ids=['Samsung Galaxy S8', 'iPhone 8 Plus', 'iPad Mini'])
def setup_mobile_browser(request):
    width, height = request.param
    options = webdriver.ChromeOptions()
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.driver = options
    browser.config.base_url = 'https://github.com'

    yield

    browser.close()


@pytest.fixture(params=[(ConfigBrowser.window_width_desktop_1, ConfigBrowser.window_height_desktop_1),
                        (ConfigBrowser.window_width_desktop_2, ConfigBrowser.window_height_desktop_2),
                        (ConfigBrowser.window_width_desktop_3, ConfigBrowser.window_height_desktop_3),
                        (ConfigBrowser.window_width_mobile_1, ConfigBrowser.window_height_mobile_1),
                        (ConfigBrowser.window_width_mobile_2, ConfigBrowser.window_height_mobile_2),
                        (ConfigBrowser.window_width_mobile_3, ConfigBrowser.window_height_mobile_3)],
                ids=['HD', 'Full HD', '2K', 'Samsung Galaxy S8', 'iPhone 8 Plus', 'iPad Mini'])
def setup_browser(request):
    width, height = request.param
    options = webdriver.ChromeOptions()
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.driver = options
    browser.config.base_url = 'https://github.com'

    yield

    browser.close()
