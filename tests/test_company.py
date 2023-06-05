"""
The file contains test for company pages
"""
import pytest

from app.pages.company_page import CompanyPage
from app.pages.components.component_constants import COMPANY_POINT_NAME
from tests.constants import COMPANY_PATH, FACEBOOK_LINK


class TestCompany:

    @pytest.fixture(scope='function')
    def open_company(self, base_page) -> 'CompanyPage':
        """
        open company page
        :param base_page:
        :return:
        """
        base_page.menu.select_by_name(COMPANY_POINT_NAME)
        company = CompanyPage(base_page.browser, base_page.url + COMPANY_PATH)
        yield company

    @pytest.fixture(scope='function')
    def external_link(self, open_company: 'CompanyPage') -> 'CompanyPage':
        """
        click external link
        :param open_company:
        :return:
        """
        open_company.facebook_link.scroll_to().click()
        current_tab = open_company.browser.current_window_handle
        try:
            new_tab = open_company.browser.window_handles[1]
            open_company.browser.switch_to.window(new_tab)
            yield open_company
        finally:
            open_company.browser.close()
            open_company.browser.switch_to.window(current_tab)

    def test_facebook_link(self, external_link):
        assert FACEBOOK_LINK == external_link.browser.current_url
