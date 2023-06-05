"""
the file contains description interaction with Careers Page
"""
from app.pages.components.base_element import BaseElement
from app.pages.components.menu import Menu
from app.pages.locators import CompanyPageLocators, CareersPegeLocators
from app.pages.start_page import StartPage


class CareersPage(StartPage):
    """
    the class contains description interaction with Careers Page
    """

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.position_button_locator = BaseElement(browser, CareersPegeLocators.POSITION_BUTTON_LOCATOR)
        self.menu = Menu(browser)
