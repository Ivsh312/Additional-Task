"""
the file contains description interaction with all job pages
"""
from app.pages.components.base_element import BaseElement
from app.pages.locators import ConcreteJobPageLocator as cjpl
from app.pages.start_page import StartPage


class JobPage(StartPage):
    """
    The class contains description interaction with all job pages
    """

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.general_description = BaseElement(browser, cjpl.GENERAL_DESCRIPTION)
        self.requirements = BaseElement(browser, cjpl.REQUIREMENTS)
        self.responsibilities = BaseElement(browser, cjpl.RESPONSIBILITIES)
        self.what_we_offer = BaseElement(browser, cjpl.WHAT_WE_OFFER)
        self.apply_button = BaseElement(browser, cjpl.APPLY_BUTTON_LOCATOR)
        self.footer = BaseElement(browser, cjpl.FOOTER_LOCATOR)
        self.accept_cookie_button = BaseElement(browser, cjpl.ACCEPT_COOKIE_BUTTON_LOCATOR)


