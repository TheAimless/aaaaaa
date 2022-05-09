from __future__ import print_function
from tkinter import W
from testlink import TestlinkAPIClient, TestlinkAPIGeneric, TestLinkHelper
import testlink
import csv
from testlink.testlinkerrors import TLResponseError
import sys, os
from platform import python_version
from bs4 import BeautifulSoup

#Variables:
testprojectname = "SampleProject"
testplanname = "Sample Testplan"
robotfilename = "test.robot"
folder = f'{"sample 2"}'
ts_name = [f'{"Sample Test Suite"}', f'{"sample 2"}']
cur_build = "7"
prefix = "SP" 

def get_status(tcname):
    with open('output.xml', 'r') as f:
        data = f.read()

    bs_data = BeautifulSoup(data, 'xml')
    x = bs_data.find('test', {'name': tcname})
    y = x.find_all('status')[-1]
    z = 'p' if y.get('status') == 'PASS' else 'f'
    #print(z)
    return z

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
gen_cmd = f'robot "../testcases/{folder}"'

os.system(gen_cmd)
     
testplanid = tlink.getTestPlanByName(testprojectname, testplanname)[0]['id']
tplanid = tlink.getTestPlanByName(testprojectname, testplanname)[0]['id']
tcases = []
for i in ts_name:
    tsuite = tlink.getTestSuite(i, prefix)[0]['id']
    tc = tlink.getTestCasesForTestSuite(testsuiteid = tsuite, deep = True, details = 'simple', getkeywords = False)
    tcases = tcases + tc

para = ['testplanid', 'status','testcaseid', 'testcaseexternalid', 'buildid', 'buildname', 'platformid', 'platformname', 'notes', 'guess', 'bugid', 'customfields', 'overwrite', 'user', 'execduration', 'timestamp', 'steps']
for i in range(len(tcases)):
    ex_id = tcases[i]['external_id']
    temp = ex_id.replace("-", "")
    status = get_status(f"{temp} - {tcases[i]['name']}")
    row = [testplanid, status, None, ex_id, cur_build, None, None, None, None, None, None, None, None, None, None, None, None]
    tlink.reportTCResult(**dict(zip(para, row)))

#Update results from a *.csv file:
"""with open('results.csv', 'r') as file:
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
"""