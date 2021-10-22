import unittest
from finbourne_access import api as sa
from finbourne_access.utilities import ApiClientFactory


class FinbourneAccessTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        api_client = ApiClientFactory()
        cls.policies_api = api_client.build(sa.PoliciesApi)

    def test_roles(self):
        policies = self.policies_api.page_policies()
        self.assertGreater(len(policies.values), 0)


if __name__ == '__main__':
    unittest.main()
