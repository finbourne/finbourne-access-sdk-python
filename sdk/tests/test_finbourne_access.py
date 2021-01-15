import unittest
from finbourne_access import api as sa
from finbourne_access.utilities import ApiClientFactory

api_client = ApiClientFactory()
policies_api = api_client.build(sa.PoliciesApi)

class FinbourneAccessTests(unittest.TestCase):

    def test_roles(self):
        policies = policies_api.list_policies()
        self.assertGreater(len(policies), 0)


if __name__ == '__main__':
    unittest.main()
