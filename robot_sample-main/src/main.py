from __future__ import print_function
from operator import truediv
from testlink import TestlinkAPIClient, TestlinkAPIGeneric, TestLinkHelper
from testlink.testlinkerrors import TLResponseError
import sys, os
from pathlib import Path
from platform import python_version
from bs4 import BeautifulSoup

class ExternalIDError(Exception):
    pass

#Helper class for connecting api
class loginTlink(TestLinkHelper):
    def __init__(self):
        self.credentials = ""
        with open('website_details.txt', 'r') as file_web:
            for i in file_web:
                self.credentials += i

        try:
            BASE_URL, self.DEVKEY = self.credentials.split('\n', 1)  
        except:
            print("Please provide the base URL: ", end = "")
            BASE_URL = input()
            print('Please provide the DevKey: ', end = "")
            self.DEVKEY = input()

        API_NAME = '/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
        self.SERVER_URL = BASE_URL + API_NAME
        super().__init__(server_url = self.SERVER_URL, devkey = self.DEVKEY) 

class APITlink():
    #Class attributes

    def __init__(self):
        self.helper = loginTlink()
        self.tlink = self.helper.connect(TestlinkAPIClient)
        self.updateParam = ['testplanid', 'status','testcaseid', 'testcaseexternalid', 'buildid',
        'buildname', 'platformid', 'platformname', 'notes', 'guess', 'bugid', 'customfields',
        'overwrite', 'user', 'execduration', 'timestamp', 'steps']
        self.creationParam = ['testcasename', 'testsuiteid', 'testprojectid', 'authorlogin', 'summary',
        'steps']

    def setAttr(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        """
        Arguments in kwargs: testProjectName, prefix, testPlanName, testProjectFolder, curBuild,
        """
        self.projectID = self.tlink.getTestProjectByName(self.testProjectName)['id']
        self.testPlanID = self.tlink.getTestPlanByName(self.testProjectName, self.testPlanName)[0]['id']

    def dfs(self, dir = None):
        if dir == None:
            dir = Path(fr'..\testcases\{self.testProjectName}')
        for i in dir.glob('*'):
            if i.is_file():
                self.dealWithSuiteCase(i)
            self.dfs(i)

    def dealWithSuiteCase(self, dir):
        self.suiteName = dir.stem
        self.suiteID = self.tlink.getTestSuite(self.suiteName, self.prefix)[0]['id']
        self.cur_dir = fr'{str(dir)}'
        self.gen_cmd = f'robot --console none "{self.cur_dir}"'
        os.system(self.gen_cmd)
        self.getStatus()
        for exID, value in self.statusResult.items():
            testName, testStatus, fullName = value
            try:
                self.tlink.getTestCaseIDByName(testcasename = testName,
                testsuitename = self.suiteName, testprojectname = self.testProjectName)
            except TLResponseError:
                self.createSteps(fullName)
                self.creationData = [testName, self.suiteID, self.projectID,
                'user', '', self.testData]
                self.created = self.tlink.createTestCase(**dict(zip(self.creationParam, self.creationData))) 
                self.correctID = f"{self.prefix}-{self.created[0]['additionalInfo']['external_id']}"
                if self.correctID != exID:
                    raise ExternalIDError(f"Robot file external ID ({exID}) does not match Testlink ID ({self.correctID} in {dir})")

                self.tlink.addTestCaseToTestPlan(self.projectID, self.testPlanID, self.correctID, 
                self.version)

            flag = False
            for i in self.tlink.getTestCaseIDByName(testcasename = testName, testsuitename = self.suiteName, testprojectname = self.testProjectName):
                if f"{self.prefix}-{i['tc_external_id']}" == exID:
                    flag = True 
                    break
            if not flag:
                raise ExternalIDError(f"Robot file external ID ({exID}) does not exist in Testlink in {dir}") 
            self.updateData = [self.testPlanID, testStatus, None, exID, self.curBuild, None, None, None, None, None, None, None, None, None, None, None, None]
            self.tlink.reportTCResult(**dict(zip(self.updateParam, self.updateData)))
            
    def getStatus(self):
        self.statusResult = {}
        with open('output.xml', 'r') as fo:
            data = fo.read()

        self.bs_data = BeautifulSoup(data, 'xml')
        tests = self.bs_data.find_all('test')
        for test in tests:
            temp, fullname = test.get('name'), test.get('name')
            testCaseID, testCaseName, status = "", "", 'p' if test.find_all('status')[-1].get('status') == 'PASS' else 'f'
            for j in range(len(temp)):
                if temp[j] == ' ':
                    testCaseID = temp[:j]
                    testCaseName = temp[j+3:]
                    break
            idx = 0
            for j in range(len(testCaseID)):
                if testCaseID[j].isdigit():
                    idx = j
                    break
            testCaseID = testCaseID[:idx] + '-' + testCaseID[idx:]
            self.statusResult[testCaseID] = [testCaseName, status, fullname]

    def createSteps(self, fullname):
        self.testData = []
        tests = self.bs_data.find_all('test')
        for test in tests:
            fname = test.get('name')
            if fname != fullname:
                continue
            step_number = 1
            for j in test.find_all('kw'):
                self.testData.append({'step_number': step_number, 'actions': j.get('name'), 'expected_results': j.find('arg').get_text(), 'execution_type': 1})
                step_number += 1

    def updateTestCases(self):
        pass

if __name__ == '__main__':
    API = APITlink()
    param = {'testProjectName': "SampleProject", 'prefix': "SP", 'testPlanName': "Sample Testplan",
    'testProjectFolder': "sample 2", 'curBuild': 7, 'version': 1}
    API.setAttr(**param)
    API.dfs()
    pass