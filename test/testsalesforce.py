import unittest
import os

import conf

from simple_salesforce import Salesforce

class TestSalesforce(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        self.sfdc = Salesforce(username=conf.SFDC_USERNAME, password=conf.SFDC_PASSWORD, security_token=conf.SFDC_SECURITY_TOKEN)
        unittest.TestCase.__init__(self, methodName=methodName)

    def test_account(self):
        sfdc_acct_id = '0010G00002CDacLQAT'
        sfdc_acct = self.sfdc.Account.get(sfdc_acct_id)
        # print ("Salesforce account {sfdc_acct_id} name is {name}.".format(sfdc_acct_id=sfdc_acct_id, name=sfdc_acct['Name']))
        self.assertIsNotNone(sfdc_acct)

if __name__ == '__main__':
    unittest.main()