from app.pages.components.base_element import BaseElement
from app.pages.components.dialogs.base_dialog import BaseDialog
from app.pages.components.dialogs.locators import ApplyFormLocators


class ApplyForDialog(BaseDialog):
    def __init__(self, browser):
        super().__init__(browser)
        self.name_input = BaseElement(browser, ApplyFormLocators.NAME_INPUT_LOC)
        self.mobile_input = BaseElement(browser, ApplyFormLocators.MOBILE_INPUT_LOC)
        self.email_input = BaseElement(browser, ApplyFormLocators.EMAIL_INPUT_LOC)
        self.upload_cv_input = BaseElement(browser, ApplyFormLocators.UPLOAD_CV_INPUT_LOC)
        self.linked_profile_input = BaseElement(browser, ApplyFormLocators.LINKED_PROFILE_INPUT_LOC)
        self.your_message_input = BaseElement(browser, ApplyFormLocators.YOUR_MESSAGE_INPUT_LOC)
        self.agree_check_box = BaseElement(browser, ApplyFormLocators.AGREE_CHECK_BOX_LOC)
        self.submit_button = BaseElement(browser, ApplyFormLocators.SUBMIT_BUTTON_LOC)
        self.invalid_email_msg = BaseElement(browser, ApplyFormLocators.INVALID_EMAIL_MSG_LOC)
        self.required_name_msg = BaseElement(browser, ApplyFormLocators.REQUIRED_NAME_MSG_LOC)
        self.close_button = BaseElement(browser, ApplyFormLocators.CLOSE_BUTTON_LOCATOR, )


