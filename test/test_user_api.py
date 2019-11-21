# coding: utf-8

"""
    timelight

    This is the timelight api.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import timelight-ai-python-api-client
from timelight-ai-python-api-client.api.user_api import UserApi  # noqa: E501
from timelight-ai-python-api-client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = timelight-ai-python-api-client.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_user_login_post(self):
        """Test case for v1_user_login_post

        Log the user in  # noqa: E501
        """
        pass

    def test_v1_user_me_get(self):
        """Test case for v1_user_me_get

        Retrieve current user information  # noqa: E501
        """
        pass

    def test_v1_user_register_demo_post(self):
        """Test case for v1_user_register_demo_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
