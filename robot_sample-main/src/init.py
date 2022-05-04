from __future__ import print_function
from testlink import TestlinkAPIClient, TestlinkAPIGeneric, TestLinkHelper
import testlink
import csv
from testlink.testlinkerrors import TLResponseError
import sys, os.path
from platform import python_version

temp = ""
with open('website_details.txt', 'r') as file_web:
    for i in file_web:
        temp += i
try:
    BASE_URL, DEVKEY = temp.split('\n', 1)  
except:
    print("Please provide the base URL: ", end = "")
    BASE_URL = input()
    print('Please provide the DevKey: ', end = "")
    DEVKEY = input()

API_NAME = '/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
SERVER_URL = BASE_URL + API_NAME
try:
    tl_helper = TestLinkHelper(SERVER_URL, DEVKEY)
except:
    print("Please provide the base URL: ", end = "")
    BASE_URL = input()
    print('Please provide the DevKey: ', end = "")
    DEVKEY = input()
    SERVER_URL = BASE_URL + API_NAME

tlink = tl_helper.connect(TestlinkAPIClient)
for i in tlink.getProjects():
    print(i)
    print("")

#print(tlink.getProjectTestPlans(1969))
#print(tlink.getTestSuitesForTestPlan(1990))
#print("")
#for i in tlink.getTestCasesForTestSuite(1991, True, 'full'):
#    print(i) 
"""
py_ver = python_version()
py_ver_short = py_ver.replace('.', '')[:2]
myApiVersion='%s v%s' % (tlink.__class__.__name__ , tlink.__version__)
this_file_dirname=os.path.dirname(__file__)

print(tlink.connectionInfo())
x, y = 'user', 'hieunm0701@gmail.com'

def checkUser(name1, mail):
    # checks if user NAME1_NAME2 exists
        when not , user will be created
              returns username + userid
    
    
    login = "{}".format(name1)
    mail = "{}".format(mail)
    try:
        response = tlink.getUserByLogin(login)
        userID = response[0]['dbID']
    except TLResponseError as tl_err:
        if tl_err.code == 10000:
            # Cannot Find User Login - create new user
#            userID = tlink.
            print('No user')
        else:
            # seems to be another response failure -  we forward it
            raise   

    return login, userID

test_name, test_id = checkUser(x, y)
print("checkuser", test_name, test_id)
#response = tlink.getUserByLogin(x)
#print("getUserByLogin", response)
#myTestUserID=response[0]['dbID']
#response = tlink.getUserByID(myTestUserID)
#print("getUserByID   ", response)
print("")
print(tlink.whatArgs('assignTestCaseExecutionTask'))
tlink.listProjects()
"""
#Update results from a *.csv file:
para = ['testplanid', 'status','testcaseid', 'testcaseexternalid', 'buildid', 'buildname', 'platformid', 'platformname', 'notes', 'guess', 'bugid', 'customfields', 'overwrite', 'user', 'execduration', 'timestamp', 'steps']
with open('results.csv', 'r') as file:
    reader = csv.reader(file)
    count = 1
    for row in reader:
        if count == 1:
            count = 0
            continue
        for i in range(len(row)):
            if row[i] == 'None':
                row[i] = None
            try:
                row[i] = int(row[i])
            except:
                continue
        tlink.reportTCResult(**dict(zip(para, row)))
    