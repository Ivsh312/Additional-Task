"""
the file contains description interaction with Company Page
"""
from app.pages.base_page import BasePage
from app.pages.components.base_element import BaseElement
from app.pages.components.menu import Menu
from app.pages.locators import CompanyPageLocators


class CompanyPage(BasePage):
    """
    the class contains description interaction with Company Page
    """

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.innovation_button = BaseElement(browser, CompanyPageLocators.INNOVATION_BUTTON_LOCATOR)
        self.facebook_link = BaseElement(browser, CompanyPageLocators.FACEBOOK_LINK_LOCATOR)
        self.accept_cookie_button = BaseElement(browser, CompanyPageLocators.ACCEPT_COOKIE_BUTTON_LOCATOR)
        self.facebook_identification = BaseElement(browser, CompanyPageLocators.FACEBOOK_IDENTIFICATION_LOCATOR)
        self.menu = Menu(browser)
