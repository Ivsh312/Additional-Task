"""
the file contains an abstraction over page elements, defines a number of basic actions with it and their set
"""
import logging
import os
import time
import traceback
from typing import List

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException, \
    ElementNotVisibleException, ElementNotSelectableException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement

from .component_constants import DEFAULT_ELEMENT_WAIT_TIME, BASE_ELEMENT_NAME, GET_TEXT_LOG, GET_TEXT_FAILED_LOG, \
    GET_TEXT_SCREEN_NAME_LOG, TEXT_SET_TEXT_ERROR, TEXT_EXCEPTION_CAUGHT, FAILED_TO_PUT_SCREEN_NAME, \
    WAIT_LOCATING_MAX_MSG, ELEMENT_IS_NOT_APPEARED_MSG, ELEMENT_IS_NOT_APPEARED_AFTER_TIME_MSG, \
    ELEMENT_IS_NOT_APPEARED_SCREEN_NAME, ELEMENT_IS_NOT_APPEARED_ERROR_MSG, \
    WAIT_CLICKABLE_MAX_MSG, ELEMENT_IS_NOT_CLICKABLE_ERROR_MSG, \
    ELEMENT_IS_NOT_DISAPPEARED_SCREEN_NAME, ELEMENT_IS_NOT_CLICKABLE_SCREEN_NAME, ELEMENT_IS_CLICKABLE_SCREEN_NAME, \
    SCREENSHOT_PATH_FOR_ELEMENT, SCREENSHOT_TYPE, TEXT_SCREEN_SAVE_TO, TEXT_SAVE_SCREEN_EXCEPTION, \
    GET_ATTRIBUTE_FOR_ELEMENT, GET_ATTRIBUTE_ERROR_MSG, FAILED_TO_GET_ATTRIBUTE_SCREEN_NAME, scroll_to_script, \
    ELEMENT_SHOULD_ABSENCE_SCREEN_NAME, ELEMENT_SHOULD_PRESENT_SCREEN_NAME, CLEAR_ELEMENT_MSG, CLEAR_ELEMENT_ERROR_MSG, \
    ENTER_FOR_ELEMENT_LOG, ENTER_FOR_ELEMENT_ERROR_LOG, ENTER_FOR_ELEMENT_ERROR_SCREEN_NAME, \
    ELEMENTS_SHOULD_PRESENT_SCREEN_NAME
from app.custom_logger import custom_logger
from traceback import print_stack


class BaseElementException(Exception):
    pass


class BaseElement:
    """
    the class contains an abstraction over page elements, defines a number of basic actions with it
    """
    log = custom_logger(logging.DEBUG)

    def __init__(
            self, browser: webdriver, locator: tuple, timeout=DEFAULT_ELEMENT_WAIT_TIME,
            name=BASE_ELEMENT_NAME, wait_located=False):
        self.browser = browser
        self.by, self.locator = locator
        self.timeout = timeout
        self.name = name
        self.wait_located = wait_located

    @property
    def text(self)->str:
        try:
            text = self._get_element().text
            self.log.info(GET_TEXT_LOG.format(text))
        except BaseElementException:
            self.log.error(GET_TEXT_FAILED_LOG.format(self.locator))
            self.take_screenshot(GET_TEXT_SCREEN_NAME_LOG)
            print_stack()
            text = None
        return text

    @property
    def title(self)->str:
        return self.get_attribute('title')

    @property
    def type(self)->str:
        return self.get_attribute('type')

    @property
    def value(self)->str:
        return self.get_attribute('value')

    @text.setter
    def text(self, text)->None:
        """
        Set text in element
        :param text: text for element
        :return:
        """
        try:
            element = self._get_element()
            self.clear_field()
            element.send_keys(text)
        except BaseElementException:
            self.log.error(TEXT_SET_TEXT_ERROR.format(self.locator))
            self.log.error(TEXT_EXCEPTION_CAUGHT.format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))
            self.take_screenshot(FAILED_TO_PUT_SCREEN_NAME)

    def _get_element(self) -> WebElement:
        self.wait_to_clickable() if not self.wait_located else self.wait_to_located()
        return self.browser.find_element(self.by, self.locator)

    def enter(self)->'BaseElement':
        self._get_element().send_keys(Keys.ENTER)
        return self

    def wait_to_located(self) -> None:
        """
        Wait until element will appear
        :return: None
        """
        try:
            self.log.info(WAIT_LOCATING_MAX_MSG.format(str(self.timeout)))
            wait = WebDriverWait(self.browser, timeout=self.timeout,
                                 poll_frequency=0.5,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementClickInterceptedException])
            wait.until(ec.visibility_of_element_located((self.by, self.locator)))
            self.log.info(ELEMENT_IS_NOT_APPEARED_MSG)
        except TimeoutException:
            self.log.info(ELEMENT_IS_NOT_APPEARED_AFTER_TIME_MSG.format(self.timeout))
            self.take_screenshot(ELEMENT_IS_NOT_APPEARED_SCREEN_NAME)
            print_stack()
            raise TimeoutException(ELEMENT_IS_NOT_APPEARED_ERROR_MSG)

    def wait_to_clickable(self) -> "BaseElement":
        """
        Wait until element will appear
        :return: None
        """
        try:
            self.log.info(WAIT_CLICKABLE_MAX_MSG.format(str(self.timeout)))
            wait = WebDriverWait(self.browser, timeout=self.timeout,
                                 poll_frequency=0.5,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementClickInterceptedException])
            wait.until(ec.element_to_be_clickable((self.by, self.locator)))
            self.log.info(ELEMENT_IS_NOT_APPEARED_SCREEN_NAME)
        except TimeoutException:
            self.log.info(ELEMENT_IS_NOT_APPEARED_AFTER_TIME_MSG.format(self.timeout))
            self.take_screenshot(ELEMENT_IS_NOT_APPEARED_SCREEN_NAME)
            print_stack()
            raise TimeoutException(ELEMENT_IS_NOT_CLICKABLE_ERROR_MSG)
        return self

    def wait_to_disappeared(self) -> "BaseElement":
        """
        Wait until element will appear
        :return: None
        """
        try:
            self.log.info(ELEMENT_IS_NOT_DISAPPEARED_SCREEN_NAME.format(str(self.timeout)))
            wait = WebDriverWait(self.browser, timeout=self.timeout,
                                 poll_frequency=0.5,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementClickInterceptedException])
            wait.until_not(ec.element_to_be_clickable((self.by, self.locator)))
            self.log.info(ELEMENT_IS_NOT_DISAPPEARED_SCREEN_NAME)
        except TimeoutException:
            self.log.info(ELEMENT_IS_NOT_APPEARED_AFTER_TIME_MSG.format(self.timeout))
            self.take_screenshot(ELEMENT_IS_NOT_DISAPPEARED_SCREEN_NAME)
            print_stack()
            raise TimeoutException(ELEMENT_IS_NOT_DISAPPEARED_SCREEN_NAME)
        return self

    def is_disappeared(self) -> bool:
        """
        This checks that an element is disappeared from the web page
        :return: True if the element is disappeared and False if it is not.
        """
        try:
            WebDriverWait(self.browser, self.timeout, 1, TimeoutException). \
                until_not(ec.presence_of_element_located((self.by, self.locator)))
        except TimeoutException:
            self.take_screenshot(ELEMENT_IS_NOT_DISAPPEARED_SCREEN_NAME)
            return False
        return True

    def is_appeared(self) -> bool:
        """
        This checks that an element is disappeared from the web page
        :return: True if the element is disappeared and False if it is not.
        """
        try:
            WebDriverWait(self.browser, self.timeout, 1, TimeoutException). \
                until(ec.presence_of_element_located((self.by, self.locator)))
        except TimeoutException:
            self.take_screenshot(ELEMENT_IS_NOT_APPEARED_SCREEN_NAME)
            return False
        return True

    def is_not_clickable_some_time(self) -> bool:
        """
        This checks that an element is not clickable from the web page
        :return: True if the element is not clickable and False if it is not.
        """
        try:
            WebDriverWait(self.browser, self.timeout, 1, TimeoutException). \
                until_not(ec.element_to_be_clickable((self.by, self.locator)))
        except TimeoutException:
            self.take_screenshot(ELEMENT_IS_NOT_CLICKABLE_SCREEN_NAME)
            return False
        return True

    def is_clickable_some_time(self) -> bool:
        """
        This checks that an element is clickable from the web page
        :return: True if the element is clickable and False if it is not.
        """
        try:
            WebDriverWait(self.browser, self.timeout, 1, TimeoutException). \
                until(ec.element_to_be_clickable((self.by, self.locator)))
        except TimeoutException:
            self.take_screenshot(ELEMENT_IS_CLICKABLE_SCREEN_NAME)
            return False
        return True

    def click(self) -> "BaseElement":
        element = self._get_element()
        element.click()
        return self

    def js_click(self):
        element = self._get_element()
        self.browser.execute_script("arguments[0].click();", element)

    def take_screenshot(self, result_message: str) -> "BaseElement":
        """
        This takes a screenshot of the current open web page
        :param result_message: the string which will be used as part of file name of the screenshot.
        :return: None.
        """
        file_name = result_message + "_" + str(round(time.time() * 1000)) + SCREENSHOT_TYPE
        relative_file_name = SCREENSHOT_PATH_FOR_ELEMENT + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(
            current_directory, SCREENSHOT_PATH_FOR_ELEMENT)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.browser.save_screenshot(destination_file)
            self.log.info(TEXT_SCREEN_SAVE_TO.format(destination_file))
        except MemoryError:
            self.log.error(TEXT_SAVE_SCREEN_EXCEPTION)
            print_stack()
        return self

    def get_attribute(self, attribute: str) -> str:
        """
        Get attribute value
        :param attribute:
        :return:
        """
        try:
            element = self._get_element()
            value = element.get_attribute(attribute)
            self.log.info(GET_ATTRIBUTE_FOR_ELEMENT.format(value))
        except BaseElementException:
            self.log.error(GET_ATTRIBUTE_ERROR_MSG.format(self.locator))
            print_stack()
            self.take_screenshot(FAILED_TO_GET_ATTRIBUTE_SCREEN_NAME)
            value = None
        return value

    def scroll_to(self) -> "BaseElement":
        """
        This scrolls the page to the desired element
        :return: None
        """
        element = WebDriverWait(self.browser, self.timeout, 1, TimeoutException).\
            until(ec.presence_of_element_located((self.by, self.locator)))
        self.browser.execute_script(scroll_to_script, element)
        self.browser.execute_script(scroll_to_script, element)
        self.wait_to_clickable()
        return self

    def is_not_present(self, timeout=3) -> bool:
        """
        Checks for the absence of an element
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located((self.by, self.locator)))
        except TimeoutException:
            return True
        self.take_screenshot(ELEMENT_SHOULD_ABSENCE_SCREEN_NAME)
        return False

    def is_present(self) -> bool:
        """
        Checks for the present of an element
        :param timeout:
        :return:
        """
        return self.browser.find_element(self.by, self.locator).is_displayed()

    def hover_to(self)->'BaseElement':
        """
        This is for hovering over an element
        :return: None
        """
        hover_element = self._get_element()
        ActionChains(self.browser).move_to_element(hover_element).perform()
        return self

    def clear_field(self) -> None:
        """
        Clear fild
        :return: None
        """
        try:
            element = self.browser.find_element(self.by, self.locator)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.DELETE)
            self.log.info(CLEAR_ELEMENT_MSG.format(self.locator))
        except NoSuchElementException:
            self.log.info(CLEAR_ELEMENT_ERROR_MSG.format(self.locator))
            print_stack()
            self.take_screenshot('clearing_fail')

    def press_enter_no_wait(self) -> None:
        """
        Press Enter for element
        :return: None
        """
        try:
            element = self.browser.find_element(self.by, self.locator)
            element.send_keys(Keys.ENTER)
            self.log.info(ENTER_FOR_ELEMENT_LOG.format(self.locator))
        except NoSuchElementException:
            self.log.info(ENTER_FOR_ELEMENT_ERROR_LOG.format(self.locator))
            print_stack()
            self.take_screenshot(ENTER_FOR_ELEMENT_ERROR_SCREEN_NAME)
            raise NoSuchElementException()


class ListOfElements:
    """
    For interaction with list of elements
    """
    def __init__(
            self, browser: webdriver, locator: tuple, timeout=DEFAULT_ELEMENT_WAIT_TIME,
            name=BASE_ELEMENT_NAME):
        self.browser = browser
        self.by, self.locator = locator
        self.timeout = timeout
        self.name = name
        self.base_element = BaseElement(browser=browser, locator=locator,timeout=timeout,name=name)
        self.list_elements = []

    def __len__(self)->int:
        return len(self._get_elements())

    def __getitem__(self, index)->'BaseElement':
        return self._get_elements()[index]

    def _get_elements(self) -> List[BaseElement]:
        """
         This finds all elements on the web page
         :param how: locator type, for example By.CSS_SELECTOR, By. ID, By.NAME, By.CLASS_NAME, By.XPATH, By.LINK_TEXT
         :param what:  element locator
         :return: list of elements.
         """
        try:
            self.base_element.wait_to_clickable() if not self.base_element.wait_located else self.base_element.wait_to_located()
            element_list = self.browser.find_elements(self.by, self.locator)
            if len(element_list) > 0:
                return element_list
            return element_list
        except NoSuchElementException:
            self.base_element.take_screenshot(ELEMENTS_SHOULD_PRESENT_SCREEN_NAME)
            return []

    @property
    def text(self)->List[str]:
        """
        Extract text attribute for all elements
        :return:
        """
        list_elements = self._get_elements()
        list_text = [name.text for name in list_elements]
        return list_text