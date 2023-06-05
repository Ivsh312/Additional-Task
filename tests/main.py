import os
import time

import pytest


# tests for concrete page
from tests.constants import DIR_WITH_REPORT

test_start_page = 'test_start_page.py::TestContactUsDialog'
test_company_page = 'test_company.py::TestCompany'
test_concrete_job_page = 'test_concrete_job.py::TestConcreteJob'
test_join_us_page = 'test_join_us.py::TestJoinUs'
# full regression tests
regression = [
    test_start_page,
    test_company_page,
    test_concrete_job_page,
    test_join_us_page,
]

"""
Code to create a new report folder each time and save the old one with 
a different name (This allows you to quickly delete the old report)
"""
current_directory = os.path.dirname(__file__)
destination_directory = os.path.join(current_directory, DIR_WITH_REPORT)
if os.path.exists(destination_directory):
    new_name = DIR_WITH_REPORT + str(round(time.time() * 1000))
    os.rename(DIR_WITH_REPORT, new_name)
    os.makedirs(destination_directory)
    print('backup report finished successfully')


# set folder for allure report
regression.append('--alluredir=../reports/')
regression.append('-n 3')
# set folder for allure report
pytest.main(regression)
