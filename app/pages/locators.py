"""
All locators on all pages
"""
from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class StartPageLocators:
    CONTACT_AS_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'contact-label btn btn-1b')]")


@dataclass
class CompanyPageLocators:
    INNOVATION_BUTTON_LOCATOR = (By.XPATH, '//button[contains(@class, "contact-label-evolve btn btn-1b")]')
    FACEBOOK_LINK_LOCATOR = (By.XPATH, '//span[contains(@class, "musala musala-icon-facebook")]')
    ACCEPT_COOKIE_BUTTON_LOCATOR = (By.XPATH, '//a[contains(text(), "ACCEPT")]')

    FACEBOOK_IDENTIFICATION_LOCATOR = (By.XPATH, '//input[contains(@id, ":ro:")]')


@dataclass
class CareersPegeLocators:
    POSITION_BUTTON_LOCATOR = (By.XPATH, '//button[contains(@class, "contact-label")]')


@dataclass
class JoinUsPegeLocators:
    LOCATION_SELECTOR_LOCATOR = (By.ID, 'get_location')
    JOB_LINK_ELEMENT_LOCATOR = (By.XPATH, "//a[contains(@class, 'card-jobsHot__link')]")
    JOB_LINK_TITLE_ELEMENT_LOCATOR = (By.XPATH, "//a[contains(@class, 'card-jobsHot__link')]//h2")


@dataclass
class ConcreteJobPageLocator:
    GENERAL_DESCRIPTION = (By.XPATH, '(//div[contains(@class, "requirements pull-right")])[1]')
    REQUIREMENTS = (By.XPATH, '(//div[contains(@class, "requirements pull-left")])[1]')
    RESPONSIBILITIES = (By.XPATH, '(//div[contains(@class, "requirements pull-right")])[2]')
    WHAT_WE_OFFER = (By.XPATH, '(//div[contains(@class, "requirements pull-left")])[2]')
    APPLY_BUTTON_LOCATOR = (By.XPATH, "//input[contains(@value, 'Apply')]")
    FOOTER_LOCATOR = (By.XPATH, "//footer")
    ACCEPT_COOKIE_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'cli-bar-btn_container')]/a")

    JOB_LINK_PATTERN = "//img[contains(@alt, '{}')]"
