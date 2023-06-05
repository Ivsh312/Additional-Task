"""
The file contains test for Contact us pages
"""
import allure
import pytest
from selenium.webdriver.common.by import By

from app.pages.components.base_element import BaseElement
from app.pages.components.dialogs.contact_us_dialog import ContactUsDialog
from app.pages.components.dialogs.locators import ContactUsLocators
from tests.constants import DefaultContactUsConfig as dcuc, InvalidEmails, ContactUsData


class TestContactUsDialog:
    """
    The class contains test for Contact us pages
    """

    @pytest.fixture(scope='function')
    def open_dialog(self, base_page):
        """
        open "Contact Us" dialog
        :param base_page:
        :return:
        """
        try:
            with allure.step('Scroll to button and click'):
                base_page.contact_as_button.scroll_to().click()
                contact_us_dialog = ContactUsDialog(base_page.browser)
            with allure.step('Wait_oppening'):
                contact_us_dialog.name_input.wait_to_clickable()
            yield contact_us_dialog
        finally:
            base_page.browser.refresh()

    @pytest.mark.parametrize('email', [
        *InvalidEmails.TEMPLATE_INJECTION, InvalidEmails.XSS_INJECTION, *InvalidEmails.SQL_INJECTION,
        *InvalidEmails.INVALID_EMAILS_AS_NUMBERS, InvalidEmails.INVALID_EMAILS_MISS_DOG
    ])
    def test_invalid_email_message(self, open_dialog, email):
        with allure.step('fill dialog and click send'):
            open_dialog.fill_dialog(name=dcuc.name, mobile=dcuc.mobile, subject=dcuc.subject, your_message=dcuc.message)
            open_dialog.fill_dialog(email=email)
            open_dialog.send_button.scroll_to().click()
        assert BaseElement(
            browser=open_dialog.browser, locator=(
                By.XPATH, ContactUsLocators.INVALID_INPUT_LOC_PATTERN.format(ContactUsData.INVALID_EMAIL_MSG)))\
            .is_appeared(), f"'{ContactUsData.INVALID_EMAIL_MSG}' didn't appeared."


