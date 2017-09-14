"""
from simple_salesforce import Salesforce
sf = Salesforce(instance_url='https://login.salesforce.com', session_id='')

sf1 = Salesforce(username='bodasjeevan@gmail.com', password='GSSpuc@2007', security_token='P2NEXuIjWp99ptCZ5tglRnVT')

sf3 = sf1.Contact.create({'LastName':'Smith','Email':'example@example.com'})
sf2 = sf1.Position__c.create({'Name':'testrecordfrommynaka','Min_Pay__c':15000,'Max_Pay__c':20000})
print('standared = ', sf3, 'custom = ', sf2)
"""
