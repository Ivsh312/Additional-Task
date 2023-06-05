from dataclasses import dataclass

DIR_WITH_REPORT = 'Report'

COMPANY_PATH = 'company/'
CAREERS_PATH = 'careers/'
JOIN_US_PATH = 'careers/join-us/'

FACEBOOK_LINK = 'https://www.facebook.com/MusalaSoft?fref=ts'

config_path = '\\..\\config\\config.txt'
DEFAULT_SECTION = 'BASE_CONFIG'
BROWSER_TYPE = 'BROWSER'
BASE_URL_WORD = 'BASE_URL'
TOKEN_FOR_FIREFOX_WORD = 'TOKEN_FOR_FIREFOX'

@dataclass
class DefaultContactUsConfig:
    name = 'default'
    email = 'default'
    mobile = 'default'
    subject = 'default'
    message = 'default'

@dataclass
class InvalidEmails:
    TEMPLATE_INJECTION = ['{{7*7}}','${7*7}','<%= 7*7 %>','${{7*7}}','#{7*7}','*{7*7}']
    XSS_INJECTION = ['<IMG SRC=/ onerror="alert(String.fromCharCode(88,83,83))"></img>',
                     """<IMG SRC="jav ascript:alert('XSS');">""",
                     """<IMG SRC=" &#14; javascript:alert('XSS');">""",
                     r"""\";alert('XSS');//""",
                     """</TITLE><SCRIPT>alert("XSS");</SCRIPT>"""]
    SQL_INJECTION = ["'", "''", "`", "``", ",", '"']
    INVALID_EMAILS_AS_NUMBERS = ['1', '2', '3', '4', '5']
    INVALID_EMAILS_MISS_DOG = ["TESTGMAIL.COM", "BASEMAIL.RU", "GITTUT.BY", "ALTGMAIL.COM", "TEAMGMAIL.COM"]

@dataclass
class ContactUsData:
    INVALID_EMAIL_MSG = 'The e-mail address entered is invalid.'


@dataclass
class JoinUsData:
    INVALID_EMAIL_MSG = 'The e-mail address entered is invalid.'
    ELEMENTS_SHOULD_PRESENT = ['general_description', 'requirements', 'responsibilities', 'what_we_offer']
    TEST_LOCATION_LIST = ['Anywhere',]
    LOCATION_JOB_COMBINATION = {'Anywhere': ['Full-Stack Developer']}

    @staticmethod
    def location_job_combination_extract():
        for location in JoinUsData.LOCATION_JOB_COMBINATION.keys():
            for job_title in JoinUsData.LOCATION_JOB_COMBINATION[location]:
                yield location, job_title

    NUMBER_FOUR_LOCATION = ['Sofia', 'Bulgaria']

@dataclass
class ApplyForDialogData:
    name_input_class_variable_name = 'name_input'
    mobile_input_class_variable_name = 'mobile_input'
    email_input_class_variable_name = 'email_input'
    linked_profile_input_class_variable_name = 'linked_profile_input'
    your_message_input_class_variable_name = 'your_message_input'
    invalid_email_msg_class_variable_name = 'invalid_email_msg'
    required_name_msg_class_variable_name = 'required_name_msg'
    CV_PATH = "\\data\\cv.txt"
    INVALID_COMBINATION = {
        'INCORRECT_EMAIL': ({
            name_input_class_variable_name: 'History Value',
            mobile_input_class_variable_name: '+8234735485748',
            email_input_class_variable_name: 'serkkl@gmeilcom',
            linked_profile_input_class_variable_name: "https://ru.linkedin.com/",
            your_message_input_class_variable_name: '1234'
        }, invalid_email_msg_class_variable_name),
        'EMPTY_NAME': ({
            mobile_input_class_variable_name: '+8234735485748',
            email_input_class_variable_name: 'serkkl@gmeilcom',
            linked_profile_input_class_variable_name: "https://ru.linkedin.com/",
            your_message_input_class_variable_name: '1234'
        }, required_name_msg_class_variable_name)
    }

    @staticmethod
    def location_job_combination_extract():
        for test_data in ApplyForDialogData.INVALID_COMBINATION.values():
            yield test_data[0], test_data[1]

