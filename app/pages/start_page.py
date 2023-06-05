"""
The file contains description interaction with first pages
"""

from app.pages.components.base_element import BaseElement
from app.pages.base_page import BasePage
from app.pages.components.menu import Menu
from app.pages.locators import StartPageLocators as spl, CompanyPageLocators


class StartPage(BasePage):
    """
    The class contains description interaction with first pages
    """

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.contact_as_button = BaseElement(browser, spl.CONTACT_AS_BUTTON_LOCATOR)
        self.accept_cookie_button = BaseElement(browser, CompanyPageLocators.ACCEPT_COOKIE_BUTTON_LOCATOR)
        self.menu = Menu(browser)

