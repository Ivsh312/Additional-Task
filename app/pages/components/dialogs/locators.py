from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class ApplyFormLocators:

    NAME_INPUT_LOC = (By.XPATH, "//*[contains(@id, 'cf-1')]")
    EMAIL_INPUT_LOC = (By.XPATH, "//*[contains(@id, 'cf-2')]")
    MOBILE_INPUT_LOC = (By.XPATH, "//*[contains(@id, 'cf-3')]")
    UPLOAD_CV_INPUT_LOC = (By.XPATH, "//*[contains(@id, 'cf-4')]")
    LINKED_PROFILE_INPUT_LOC = (By.XPATH, "//*[contains(@id, 'cf-5')]")
    YOUR_MESSAGE_INPUT_LOC = (By.XPATH, "//*[contains(@id, 'cf-6')]")
    AGREE_CHECK_BOX_LOC = (By.XPATH, "//*[contains(@id, 'adConsentChx')]")
    SUBMIT_BUTTON_LOC = (By.XPATH, "//*[contains(@type, 'submit')]")
    INVALID_EMAIL_MSG_LOC = (By.XPATH, '//span[contains(text(), "The e-mail address entered is invalid.")]')
    REQUIRED_NAME_MSG_LOC = (By.XPATH, '//span[contains(text(), "The field is required.") and  contains(@class, "wpcf7-not-valid-tip")]')
    CLOSE_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'close-form')]")


class ContactUsLocators:

    INVALID_INPUT_LOC_PATTERN = "//span[contains(text(), '{}')]"

    NAME_INPUT = (By.XPATH, "//input[contains(@id, 'cf-1')]")
    EMAIL_INPUT = (By.XPATH, "//input[contains(@id, 'cf-2')]")
    MOBILE_INPUT = (By.XPATH, "//input[contains(@id, 'cf-3')]")
    SUBJECT_INPUT = (By.XPATH, "//input[contains(@id, 'cf-4')]")
    MESSAGE_INPUT = (By.XPATH, "//textarea[contains(@id, 'cf-5')]")

    SEND_BUTTON_LOC = (By.XPATH, "//input[contains(@value, 'Send')]")

