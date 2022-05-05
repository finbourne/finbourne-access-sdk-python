import unittest
import pytz
import finbourne_access
import json

from datetime import datetime, timedelta
from finbourne_access import api as sa
from finbourne_access import models as access_models
from finbourne_access.utilities import ApiClientFactory


class FinbourneAccessTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        api_client = ApiClientFactory()
        cls.policies_api = api_client.build(sa.PoliciesApi)

    def test_prevent_transactions_before_an_effective_date(self):

        """
        This policy allows you to prevent the creation, deletion or updating of
         transactions for any effective date before 1 April 2022 for all portfolios in a given scope.

        We specify the effective date restriction in the 'for' attribute of the PolicyCreationRequest
        model.
        """

        scope = "ibor"
        portfolio_code = "*"

        policy_code = f"restrict-transactions-on-scope-{scope}-for-effective-date-before-20220401"

        # Configure the effective datetime for the portfolio or transaction updates
        # This is the effective datetime of the data entity the policy is evaluating

        for_spec = access_models.ForSpec(
            effective_range=access_models.EffectiveRange(
                _from=datetime.min.replace(tzinfo=pytz.UTC),
                to=datetime(2022, 4, 1, tzinfo=pytz.utc),
            )
        )

        # Configure the effective datetime for the policy itself
        # This is the datetime during which the policy is active

        when_spec = access_models.WhenSpec(
            activate=datetime.min.replace(tzinfo=pytz.UTC),
            deactivate=datetime.max.replace(tzinfo=pytz.UTC)
        )

        # Here we define some selectors which control update, delete, and add access to the portfolios
        # See the following article for more details on creating data policies:
        # https://support.lusid.com/knowledgebase/article/KA-01660/en-us

        restrict_selector = access_models.SelectorDefinition(
            id_selector_definition=access_models.IdSelectorDefinition(
                identifier={"scope": scope, "code": portfolio_code},
                actions=[
                    access_models.ActionId(scope="default", activity="Update", entity="Portfolio"),
                    access_models.ActionId(scope="default", activity="Delete", entity="Portfolio"),
                    access_models.ActionId(scope="default", activity="Add", entity="Portfolio"),
                ]
            )
        )

        # Here we build the policy creation request using the configuration options defined above

        restrict_transactions_policy_request = access_models.PolicyCreationRequest(
            code=policy_code,
            applications=["LUSID"],
            grant="Deny",
            selectors=[restrict_selector],
            _for=[for_spec],
            when=when_spec,
        )

        try:
            policy_response = self.policies_api.create_policy(restrict_transactions_policy_request)

        except finbourne_access.ApiException as e:

            detail = json.loads(e.body)

            print(detail)

            # Do not fail if policy already exists

            if detail["code"] not in [613]:
                raise e

        get_policy = self.policies_api.get_policy(code=policy_code)

        self.assertEqual(get_policy.id.code, policy_code)

if __name__ == '__main__':
    unittest.main()
