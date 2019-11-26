import unittest
import os
import json

import conf

from simple_salesforce import Salesforce

SFDC_ACCT_ID_GOOGLE = '0010G00002CDZNZQA5'
SFDC_ACCT_NAME_GOOGLE = 'Google'
SFDC_OPP_ID_GOOGLE_AUSTIN = '0062I0000127wz4QAA'
SFDC_DEMAND_SIGNAL_ID_GOOGLE_SEATTLE = 'a3w2I0000006deYQAQ'

class TestSalesforce(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        self.sfdc = Salesforce(username=conf.SFDC_USERNAME, password=conf.SFDC_PASSWORD, security_token=conf.SFDC_SECURITY_TOKEN)
        unittest.TestCase.__init__(self, methodName=methodName)

    def dump_json(self, data, filename):
        # with open(filename, 'w') as fp:
        #     json.dump(data, fp, sort_keys=True, indent=4)
        pass

    def test_account(self):
        sfdc_acct = self.sfdc.Account.get(SFDC_ACCT_ID_GOOGLE)
        self.assertEqual(sfdc_acct['Name'], 'Google')
        self.assertIsNotNone(sfdc_acct)
        self.dump_json(sfdc_acct, 'sfdc_account_sample.json')

    def test_opportunity(self):
        sfdc_opp = self.sfdc.Opportunity.get(SFDC_OPP_ID_GOOGLE_AUSTIN)
        self.assertEqual(sfdc_opp['AccountId'], SFDC_ACCT_ID_GOOGLE)
        self.assertIsNotNone(sfdc_opp)
        self.dump_json(sfdc_opp, 'sfdc_opportunity_sample.json')

    def test_opportunity_query(self):
        sfdc_opps = self.sfdc.query("SELECT Id, AccountId FROM Opportunity WHERE AccountId = '{account_id}'".format(account_id=SFDC_ACCT_ID_GOOGLE))
        self.assertIsNotNone(sfdc_opps)
        records = sfdc_opps['records']
        self.assertIsNotNone(records)
        for sfdc_opp in records:
            self.assertEqual(sfdc_opp['AccountId'], SFDC_ACCT_ID_GOOGLE)
            self.assertIsNotNone(sfdc_opp)

    def test_demand_signal(self):
        sfdc_demand = self.sfdc.Demand_Signal__c.get(SFDC_DEMAND_SIGNAL_ID_GOOGLE_SEATTLE)
        self.assertEqual(sfdc_demand['Organization_Account__c'], SFDC_ACCT_ID_GOOGLE)
        self.assertIsNotNone(sfdc_demand)
        self.dump_json(sfdc_demand, 'sfdc_demand_signal_sample.json')


if __name__ == '__main__':
    unittest.main()