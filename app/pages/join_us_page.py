"""
The file contains description interaction with join us pages
"""
from typing import Union

from selenium.webdriver.support.select import Select

from app.pages.components.base_element import BaseElement, ListOfElements
from app.pages.components.menu import Menu
from app.pages.locators import JoinUsPegeLocators as jupl
from app.pages.constants import INCORRECT_LOCATION_TYPE_MSG
from app.pages.start_page import StartPage


class JoinUsPage(StartPage):
    """
    The class contains description interaction with join us pages
    """
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.location_select_element = BaseElement(browser, jupl.LOCATION_SELECTOR_LOCATOR)
        self.location_selector = Select(self.location_select_element._get_element())
        self.job_link_element = ListOfElements(browser, jupl.JOB_LINK_ELEMENT_LOCATOR)
        self.job_link_title_element = ListOfElements(browser, jupl.JOB_LINK_TITLE_ELEMENT_LOCATOR)
        self.menu = Menu(browser)

    def select_location(self, location: Union[str, int]) -> None:
        """
        Allow select location by name or number
        :param location:
        :return:
        """
        if type(location) is str:
            Select(self.location_selector).select_by_value(location)
        elif type(location) is int:
            Select(self.location_selector).select_by_index(location)
        else:
            raise TypeError(INCORRECT_LOCATION_TYPE_MSG)
