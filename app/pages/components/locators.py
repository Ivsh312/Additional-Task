"""
The file contains locators constants for work with components of pages
"""
from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class MenuLocators:
    COMPANY_POINT = (By.XPATH, "(//a[contains(text(), 'Company')])[4]")
    CAREERS_POINT = (By.XPATH, "(//a[contains(text(), 'Careers')])[4]")
