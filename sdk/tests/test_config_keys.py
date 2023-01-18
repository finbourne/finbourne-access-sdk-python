from unittest import TestCase
from finbourne_access.utilities.config_keys import ConfigKeys


class TestConfigKeys(TestCase):
    def test_identity_url_in_config_keys(self):
        # Arrange
        expected_config_keys_subset = {
            "access_url": {"env": "FBN_LUSID_ACCESS_URL", "config": "accessUrl"},
        }

        # Act
        actual_config_keys = ConfigKeys().get()

        # Assert
        self.assertEqual(
            actual_config_keys, expected_config_keys_subset | actual_config_keys
        )
