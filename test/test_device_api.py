"""
    ThyStreet

    Thy Street APIs are completely RESTful and all our responses are returned in JSON.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@thystreet.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import thystreet
from thystreet.api.device_api import DeviceApi  # noqa: E501


class TestDeviceApi(unittest.TestCase):
    """DeviceApi unit test stubs"""

    def setUp(self):
        self.api = DeviceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_token(self):
        """Test case for generate_token

        """
        pass

    def test_set_device_token(self):
        """Test case for set_device_token

        """
        pass

    def test_set_status(self):
        """Test case for set_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
