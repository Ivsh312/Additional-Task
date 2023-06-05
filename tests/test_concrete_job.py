"""
The file contains test for job pages
"""
import os

import pytest
from selenium.webdriver.common.by import By

from app.pages.components.base_element import BaseElement
from app.pages.components.dialogs.apply_for_dialog import ApplyForDialog
from app.pages.concret_job_page import JobPage
from app.pages.locators import ConcreteJobPageLocator
from tests.constants import JoinUsData, ApplyForDialogData
from tests.test_join_us import TestJoinUs


class TestConcreteJob(TestJoinUs):
    """
    The class contains test for job pages
    """

    @pytest.fixture(scope='function', params=JoinUsData.location_job_combination_extract(),
                    ids=JoinUsData.LOCATION_JOB_COMBINATION.keys())
    def select_location(self, open_to_join_us, request) -> (str, 'JoinUsData'):
        """
        Select location and send correct test scenario and data for test
        :param open_to_join_us:
        :param request:
        :return:
        """
        try:
            location, job_title = request.param
            open_to_join_us.location_selector.select_by_value(location)
            yield job_title, open_to_join_us
        finally:
            open_to_join_us.browser.get(open_to_join_us.url)

    @pytest.fixture(scope='function')
    def select_job(self, select_location) -> JobPage:
        """
        Select test job
        :param select_location:
        :return:
        """
        job_title, join_us = select_location
        BaseElement(join_us.browser, (
            By.XPATH, ConcreteJobPageLocator.JOB_LINK_PATTERN.format(job_title))).scroll_to().click()
        job_page = JobPage(join_us.browser, url=join_us.browser.current_url)
        yield job_page

    @pytest.fixture(scope='function')
    def open_apply_for_dialog(self, select_job):
        """
        Open "apply for" dialog
        :param select_job:
        :return:
        """
        select_job.footer.scroll_to()
        select_job.apply_button.js_click()
        yield ApplyForDialog(select_job.browser)

    @pytest.mark.parametrize('expected_element', JoinUsData.ELEMENTS_SHOULD_PRESENT)
    def test_check_element_for_job(self, select_job: JobPage, expected_element: str):
        assert select_job.get_element_by_name(expected_element).scroll_to().is_appeared(), \
            f"Element '{expected_element}', didn't appeared on page"

    @pytest.mark.parametrize(
        'fild_config, expected_message',
        [(test_data[0], test_data[1]) for test_data in ApplyForDialogData.INVALID_COMBINATION.values()])
    def test_check_messages_in_apply_for_dialog(self, fild_config, expected_message, open_apply_for_dialog):
        open_apply_for_dialog.fill_fields(fild_config)
        open_apply_for_dialog.upload_cv_input._get_element().send_keys(os.getcwd() + ApplyForDialogData.CV_PATH)
        open_apply_for_dialog.agree_check_box.scroll_to().js_click()
        open_apply_for_dialog.submit_button.scroll_to().js_click()
        open_apply_for_dialog.close_button.wait_to_clickable()
        open_apply_for_dialog.close_button.js_click()
        assert open_apply_for_dialog.get_element_by_name(expected_message).is_appeared(), \
            f"Element '{expected_message}', didn't appeared on page"
