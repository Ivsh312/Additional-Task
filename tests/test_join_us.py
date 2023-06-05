"""
The file contains test for Join us pages
"""
import pytest

from app.pages.careers_page import CareersPage
from app.pages.components.component_constants import CAREERS_POINT_NAME
from app.pages.join_us_page import JoinUsPage
from tests.constants import CAREERS_PATH, JOIN_US_PATH, JoinUsData


class TestJoinUs:

    @pytest.fixture(scope='function')
    def open_to_join_us(self, base_page) -> 'JoinUsPage':
        """
        open to "join us" page for each test
        :param base_page:
        :return:
        """
        join_us_url = base_page.url + JOIN_US_PATH
        base_page.browser.get(join_us_url)
        join_us_page = JoinUsPage(base_page.browser, base_page.url + JOIN_US_PATH)
        yield join_us_page

    @pytest.fixture(scope='function')
    def navigate_to_join_us(self, base_page) -> 'JoinUsPage':
        """
        Navigate to join us by using ui
        :param base_page:
        :return:
        """
        base_page.menu.select_by_name(CAREERS_POINT_NAME)
        career_page = CareersPage(base_page.browser, base_page.url + CAREERS_PATH)
        career_page.position_button_locator.click()
        join_us_page = JoinUsPage(base_page.browser, base_page.url + JOIN_US_PATH)
        yield join_us_page

    def test_facebook_link(self, navigate_to_join_us):
        assert navigate_to_join_us.url == navigate_to_join_us.browser.current_url

    @pytest.mark.parametrize('location', JoinUsData.NUMBER_FOUR_LOCATION)
    def test_print(self, open_to_join_us, location):
        open_to_join_us.location_selector.select_by_value(location)
        for i, j in zip(open_to_join_us.job_link_element._get_elements(),
                        open_to_join_us.job_link_title_element._get_elements()):
            print(f"location: '{location}'")
            print(f"link: '{i.get_attribute('href')}'")
            print(f'job_title: "{j.text}"')
        assert True
