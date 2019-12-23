# coding: utf-8

"""
    timelight

    This is the timelight api.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import timelight_ai_python_api_client
from timelight_ai_python_api_client.api.day_api import DayApi  # noqa: E501
from timelight_ai_python_api_client.rest import ApiException


class TestDayApi(unittest.TestCase):
    """DayApi unit test stubs"""

    def setUp(self):
        self.api = timelight_ai_python_api_client.api.day_api.DayApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_day_bulk_patch(self):
        """Test case for v1_day_bulk_patch

        Update day entities  # noqa: E501
        """
        pass

    def test_v1_day_list_source_id_year_get(self):
        """Test case for v1_day_list_source_id_year_get

        List day data of the reference year  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
