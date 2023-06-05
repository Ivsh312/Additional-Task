import configparser
import os
from dataclasses import dataclass

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.firefox.options import Options as FirefoxOptions

from app.pages.start_page import StartPage
from tests.constants import config_path, DEFAULT_SECTION, BROWSER_TYPE, BASE_URL_WORD, TOKEN_FOR_FIREFOX_WORD


def config_browser(browser_config: 'BrowserParams'):
    """
    Create browser instance according config file
    :param browser_config:
    :return:
    """
    if browser_config.browser_type == "Chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_config.browser_language})
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                   options=options)
    elif browser_config.browser_type == "Firefox":
        options = FirefoxOptions()
        import os
        os.environ['GH_TOKEN'] = browser_config.fire_fox_token
        options.set_preference('intl.accept_languages', browser_config.browser_language)
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                    options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    return browser


@dataclass
class BrowserParams:
    """
    Just save browser config as class
    """
    base_url: str
    browser_type: str = 'Chrome'
    browser_language: str = 'en'
    fire_fox_token: str = 'None'


@pytest.fixture(scope="session")
def browser_config() -> 'BrowserParams':
    """
    create browser config
    :return:
    """
    config = configparser.ConfigParser()
    config_path_abs = os.getcwd() + config_path
    config.read(config_path_abs)

    browser_type = config[DEFAULT_SECTION][BROWSER_TYPE]
    base_url = config[DEFAULT_SECTION][BASE_URL_WORD]
    fire_fox_token = config[DEFAULT_SECTION][TOKEN_FOR_FIREFOX_WORD]
    browser_params = BrowserParams(browser_type=browser_type, base_url=base_url, fire_fox_token=fire_fox_token)
    yield browser_params


@pytest.fixture(scope="session")
def browser(browser_config: BrowserParams):
    browser = config_browser(browser_config)
    yield browser, browser_config
    browser.quit()


@pytest.fixture(autouse=True)
def base_page(browser):
    """
    Open base for every test and reopen browser if problem with detected
    :param browser:
    :return:
    """
    browser_instance, browser_config = browser
    try:
        if len(browser_instance.window_handles) > 1:
            browser_instance.quit()
            browser_instance = config_browser(browser_config)
        else:
            browser_instance.get(browser_config.base_url)
    except Exception():
        with allure.step('Run after browser crash'):
            browser_instance = config_browser(browser_config)
    browser_instance.add_cookie({'name': 'firstname', 'value': 'James'})

    start_page = StartPage(browser_instance, browser_instance.current_url)
    if start_page.accept_cookie_button.is_present():
        start_page.accept_cookie_button.js_click()
    return start_page
