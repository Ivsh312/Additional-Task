import allure

from app.pages.components.base_element import BaseElement
from app.pages.components.dialogs.base_dialog import BaseDialog
from app.pages.components.dialogs.locators import ContactUsLocators as cul


class ContactUsDialog(BaseDialog):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.name_input = BaseElement(browser, cul.NAME_INPUT)
        self.email_input = BaseElement(browser, cul.EMAIL_INPUT)
        self.mobile_input = BaseElement(browser, cul.MOBILE_INPUT)
        self.subject_input = BaseElement(browser, cul.SUBJECT_INPUT)
        self.message_input = BaseElement(browser, cul.MESSAGE_INPUT)
        self.send_button = BaseElement(browser, cul.SEND_BUTTON_LOC)

    def fill_dialog(self, name=None, email=None, mobile=None, subject=None, your_message=None):
        if name is not None:
            self.name_input.text = name
        if email is not None:
            self.email_input.text = email
        if mobile is not None:
            self.mobile_input.text = mobile
        if subject is not None:
            self.subject_input.text = subject
        if your_message is not None:
            self.message_input.text = your_message



