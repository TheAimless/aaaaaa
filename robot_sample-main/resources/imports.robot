*** Settings ***
Library           Selenium2Library       run_on_failure=Capture Page Screenshot     timeout=10.0     implicit_wait=0.0
Library           AppiumLibrary
Library           String
Library           Collections
Library           DateTime
Library           OperatingSystem
Library           BuiltIn
Library           RequestsLibrary
#Library           SSHLibrary
#Library           CSVLibrary
Library           JSONLibrary
Library           REST          ssl_verify=${False}         url=http://a.testaddressbook.com
Library           ImapLibrary2

Variables    ../resources/config.yaml

Resource        ../keywords/common_keywords.robot