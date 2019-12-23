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
from timelight_ai_python_api_client.api.day_trend_api import DayTrendApi  # noqa: E501
from timelight_ai_python_api_client.rest import ApiException


class TestDayTrendApi(unittest.TestCase):
    """DayTrendApi unit test stubs"""

    def setUp(self):
        self.api = timelight_ai_python_api_client.api.day_trend_api.DayTrendApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_day_trend_bulk_post(self):
        """Test case for v1_day_trend_bulk_post

        Create many DayTrend  # noqa: E501
        """
        pass

    def test_v1_day_trend_get(self):
        """Test case for v1_day_trend_get

        Retrieve many DayTrend  # noqa: E501
        """
        pass

    def test_v1_day_trend_id_delete(self):
        """Test case for v1_day_trend_id_delete

        Delete one DayTrend  # noqa: E501
        """
        pass

    def test_v1_day_trend_id_get(self):
        """Test case for v1_day_trend_id_get

        Retrieve one DayTrend  # noqa: E501
        """
        pass

    def test_v1_day_trend_id_patch(self):
        """Test case for v1_day_trend_id_patch

        Update one DayTrend  # noqa: E501
        """
        pass

    def test_v1_day_trend_id_put(self):
        """Test case for v1_day_trend_id_put

        Replace one DayTrend  # noqa: E501
        """
        pass

    def test_v1_day_trend_post(self):
        """Test case for v1_day_trend_post

        Create one DayTrend  # noqa: E501
        """
        pass

    def test_v1_day_trend_replace_all_in_source_source_id_post(self):
        """Test case for v1_day_trend_replace_all_in_source_source_id_post

        Imports many trends and replace existing. Recomputes alerts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
