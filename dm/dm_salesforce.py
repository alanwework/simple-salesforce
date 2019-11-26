import unittest
import os
import json

import conf

from simple_salesforce import Salesforce

SFDC_ACCT_ID_GOOGLE = '0010G00002CDZNZQA5'
SFDC_ACCT_NAME_GOOGLE = 'Google'
SFDC_OPP_ID_GOOGLE_AUSTIN = '0062I0000127wz4QAA'
SFDC_DEMAND_SIGNAL_ID_GOOGLE_SEATTLE = 'a3w2I0000006deYQAQ'

sfdc = Salesforce(username=conf.SFDC_USERNAME, password=conf.SFDC_PASSWORD, security_token=conf.SFDC_SECURITY_TOKEN)

def main():
    all_demands = sfdc.query_all("SELECT Id, Geolocation__Latitude__s, Geolocation__Longitude__s, IsDeleted FROM Demand_Signal__c")
    with open("data/sfdc_demand_signals_all.json", 'w') as fp:
        json.dump(all_demands, fp, sort_keys=True, indent=4)

    # all_demands = sfdc.query_all("SELECT Id, Geolocation__Latitude__s, Geolocation__Longitude__s FROM Demand_Signal__c WHERE IsDeleted = false")
    # with open("data/sfdc_demand_signals.json", 'w') as fp:
    #     json.dump(all_demands, fp, sort_keys=True, indent=4)

    # all_opps = sfdc.query_all("SELECT Id, AccountId FROM Opportunity WHERE IsDeleted = false")
    # with open("data/sfdc_opportunities.json", 'w') as fp:
    #     json.dump(all_opps, fp, sort_keys=True, indent=4)

    # all_accts = sfdc.query_all("SELECT Id, Name FROM Account WHERE IsDeleted = false")
    # with open("data/sfdc_accounts.json", 'w') as fp:
    #     json.dump(all_accts, fp, sort_keys=True, indent=4)

if __name__ == '__main__':
    main()