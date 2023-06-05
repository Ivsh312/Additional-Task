"""
the file contains all constants for work with elements of pages
"""
# ----------------------------------------base constants------------------------------------------

DEFAULT_ELEMENT_WAIT_TIME = 10
BASE_ELEMENT_NAME = 'not set'
SCREENSHOT_PATH_FOR_ELEMENT = '..\\..\\screens\\'
SCREENSHOT_TYPE = '.png'

scroll_to_script = "arguments[0].scrollIntoView(true); return arguments[0].getBoundingClientRect()"
click_script = "arguments[0].click();"
# ----------------------------------------msg patterns -------------------------------------------
GET_TEXT_LOG = "Get text value: '{}'"
GET_TEXT_FAILED_LOG = "Failed to get text for locator: '{}'"
GET_TEXT_SCREEN_NAME_LOG = "Text property calling problem"

TEXT_SET_TEXT_ERROR = "Failed to send value to element with locator: '{}'"
TEXT_LOCATOR_DID_NOT_APPEAR_ERROR = "Locator: {} did not appear in {} seconds!"

TEXT_LOCATOR_DID_NOT_DISAPPEAR_ERROR = "Locator: {} did not appear in {} seconds!"
TEXT_EXCEPTION_CAUGHT = "Exception Caught: {}"
FAILED_TO_PUT_SCREEN_NAME = "failed_to_put_value"
WAIT_LOCATING_MAX_MSG = "Waiting for maximum '{}' seconds for element to be clickable"
ELEMENT_IS_NOT_APPEARED_MSG = "Element appeared on the web page"

ELEMENT_IS_NOT_APPEARED_AFTER_TIME_MSG = "Element not appeared on the web page for {} seconds"
ELEMENT_IS_NOT_APPEARED_SCREEN_NAME = 'not_appeared'
ELEMENT_IS_NOT_APPEARED_ERROR_MSG = "Still not located"
ELEMENT_IS_NOT_CLICKABLE_ERROR_MSG = "Still not clickable"
WAIT_CLICKABLE_MAX_MSG = "Waiting for maximum '{}' seconds for element to be clickable"
ELEMENT_IS_NOT_DISAPPEARED_SCREEN_NAME = "not_disappeared"
ELEMENT_IS_NOT_CLICKABLE_SCREEN_NAME = "not clickable"
ELEMENT_IS_CLICKABLE_SCREEN_NAME = "still clickable"

TEXT_SCREEN_SAVE_TO = "Screenshot in '{}' "
TEXT_SAVE_SCREEN_EXCEPTION = "Error connected with memory used for screens"

GET_ATTRIBUTE_FOR_ELEMENT = "Getting an attribute from element '{}'"
GET_ATTRIBUTE_ERROR_MSG = "Problem with getting attribute for '{}'"
FAILED_TO_GET_ATTRIBUTE_SCREEN_NAME = "Problem with getting attribute for '{}'"

ELEMENT_SHOULD_ABSENCE_SCREEN_NAME = 'found_but_should_not'
ELEMENT_SHOULD_PRESENT_SCREEN_NAME = 'not_found'

CLEAR_ELEMENT_MSG = 'Clear an element "{}"'
CLEAR_ELEMENT_ERROR_MSG = 'Can not clear "{}"'

ENTER_FOR_ELEMENT_LOG = 'Pressed ENTER to an element "{}"'
ENTER_FOR_ELEMENT_ERROR_LOG = 'Pressed ENTER to an element "{}"'
ENTER_FOR_ELEMENT_ERROR_SCREEN_NAME = 'enter_element_failing'

ELEMENTS_SHOULD_PRESENT_SCREEN_NAME = 'not_found'

# ----------------------------------------menu constants -------------------------------------------

COMPANY_POINT_NAME = 'Company'
CAREERS_POINT_NAME = 'Careers'
