"""
the file contains description interaction with page
"""
import logging
import os
import time
from traceback import print_stack

from selenium import webdriver

from app.custom_logger import custom_logger
from app.pages.components.base_element import BaseElement
from app.pages.constants import SCREENSHOT_DIRECTORY, SCREENSHOT_MSG, SCREENSHOT_ERROR_MSG


class BasePage:
    """
    the class contains description interaction with page
    """
    log = custom_logger(logging.DEBUG)

    def __init__(self, browser: webdriver, url):
        self.browser = browser
        self.url = url
        self.browser.maximize_window()

    def open(self) -> None:
        """
        This opens web page.
        """
        self.browser.get(self.url)

    def take_screenshot(self, result_message: str) -> None:
        """
        This takes a screenshot of the current open web page
        :param result_message: the string which will be used as part of file name of the screenshot.
        :return: None.
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"

        relative_file_name = SCREENSHOT_DIRECTORY + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, SCREENSHOT_DIRECTORY)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.browser.save_screenshot(destination_file)
            self.log.info(SCREENSHOT_MSG.format(SCREENSHOT_DIRECTORY))
        except MemoryError:
            self.log.error(SCREENSHOT_ERROR_MSG)
            print_stack()

    def get_element_by_name(self, name: str) -> 'BaseElement':
        """
        Get class attrebute by name
        :param name:
        :return:
        """
        return self.__getattribute__(name)
