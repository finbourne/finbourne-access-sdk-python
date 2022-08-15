import os
import unittest
from finbourne_access import api as sa
from finbourne_access.utilities import ApiClientFactory


class FinbourneAccessTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = os.getenv("FBN_ACCESS_TOKEN", None)
        api_client = ApiClientFactory(token=token)
        cls.policies_api = api_client.build(sa.PoliciesApi)

    def test_roles(self):
        policies = self.policies_api.page_policies()
        self.assertGreater(len(policies.values), 0)


if __name__ == '__main__':
    unittest.main()
