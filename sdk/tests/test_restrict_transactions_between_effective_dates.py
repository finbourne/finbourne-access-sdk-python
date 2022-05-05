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

    def test_restrict_transactions_between_effective_dates(self):

        """
        This policy allows you to restrict the creation, deletion or updating of
         transactions between two effective dates (in this case 1 May 2022 to 1 June 2022).

        We specify the effective date restriction in the 'for' attribute of the PolicyCreationRequest
        model.
        """

        scope = "ibor"

        policy_code = f"restrict-transactions-on-scope-{scope}-for-may-2022"

        deactivate = datetime(9999, 12, 31, tzinfo=pytz.utc)

        for_spec = access_models.ForSpec(
            effective_range=access_models.EffectiveRange(
                _from=datetime(2022, 5, 1, tzinfo=pytz.utc).isoformat(),
                to=datetime(2022, 6, 1, tzinfo=pytz.utc).isoformat(),
            )
        )

        when_spec = access_models.WhenSpec(
            activate=datetime.now(tz=pytz.utc) - timedelta(days=1), deactivate=deactivate,
        )

        restrict_selector = access_models.SelectorDefinition(
            id_selector_definition=access_models.IdSelectorDefinition(
                identifier={"scope": scope, "code": "1250"},
                actions=[
                    access_models.ActionId(scope="default", activity="Update", entity="Portfolio"),
                    access_models.ActionId(scope="default", activity="Delete", entity="Portfolio"),
                    access_models.ActionId(scope="default", activity="Add", entity="Portfolio"),
                ]
            )
        )

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

            if detail["code"] not in [612, 613, 615]:
                raise e

        get_policy = self.policies_api.get_policy(code=policy_code)

        self.assertEqual(get_policy.id.code, policy_code)

if __name__ == '__main__':
    unittest.main()
