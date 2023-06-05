"""
the file contains description of interaction with menu on all pages
"""

from app.pages.components.base_element import BaseElement
from app.pages.components.component_constants import COMPANY_POINT_NAME, CAREERS_POINT_NAME
from app.pages.components.locators import MenuLocators


class Menu:
    """
    the class contains description of interaction with menu on all pages
    """

    def __init__(self, browser):
        self.browser = browser
        self.company_point = BaseElement(browser, MenuLocators.COMPANY_POINT)
        self.careers_point = BaseElement(browser, MenuLocators.CAREERS_POINT)

    def select_by_name(self, name: str) -> None:
        {
            COMPANY_POINT_NAME: self.company_point,
            CAREERS_POINT_NAME: self.careers_point
        }.get(name).click()
