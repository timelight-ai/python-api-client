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
from timelight_ai_python_api_client.api.day_context_api import DayContextApi  # noqa: E501
from timelight_ai_python_api_client.rest import ApiException


class TestDayContextApi(unittest.TestCase):
    """DayContextApi unit test stubs"""

    def setUp(self):
        self.api = timelight_ai_python_api_client.api.day_context_api.DayContextApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_day_context_bulk_post(self):
        """Test case for v1_day_context_bulk_post

        Create many DayContext  # noqa: E501
        """
        pass

    def test_v1_day_context_get(self):
        """Test case for v1_day_context_get

        Retrieve many DayContext  # noqa: E501
        """
        pass

    def test_v1_day_context_id_delete(self):
        """Test case for v1_day_context_id_delete

        Delete one DayContext  # noqa: E501
        """
        pass

    def test_v1_day_context_id_get(self):
        """Test case for v1_day_context_id_get

        Retrieve one DayContext  # noqa: E501
        """
        pass

    def test_v1_day_context_id_patch(self):
        """Test case for v1_day_context_id_patch

        Update one DayContext  # noqa: E501
        """
        pass

    def test_v1_day_context_id_put(self):
        """Test case for v1_day_context_id_put

        Replace one DayContext  # noqa: E501
        """
        pass

    def test_v1_day_context_import_meteo_csv_source_id_post(self):
        """Test case for v1_day_context_import_meteo_csv_source_id_post

        Imports a meteo csv file for the source id  # noqa: E501
        """
        pass

    def test_v1_day_context_post(self):
        """Test case for v1_day_context_post

        Create one DayContext  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
