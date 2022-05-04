*** Settings ***
Resource    ..${/}resources${/}imports.robot
Resource    ..${/}object${/}LoginPage.robot
Test Setup    open browser ${url} with ${browser} browser
Test Teardown    Run Keywords
          ...    close all browsers

*** Test Cases ***
Login successfully
    [Tags]    Login     web
    [Documentation]
    ...     1. Login with valid username and password
    ...     2. Verify that login successfully
    ...       - Page displays message "Welcome to Address Book"
    ...       - Profile email should be same as email
    Login with    ${username}      ${password}
    Page should contain     Welcome to Address Book
    Element Text Should Be      //*[@data-test='current-user']      ${username}

Login fail
    [Tags]    Login     web
    [Documentation]
    ...     1. Login with valid username and password
    ...     2. Verify that login successfully
    ...       - Page displays message "Bad email or password."
    ...       - Page will not show successful message
    Login with    ${username}      ${invalid_password}
    Page should not contain     Welcome to Address Book
    Page should contain     Bad email or password.

API - Verify login successfully
    [Tags]    Login     API
    [Documentation]
    ...     1. Login with valid username and password
    ...     2. Verify that response code is 200
    Create Session    host    http://a.testaddressbook.com
    ${headers}    Create Dictionary     contentType=multipart/form-data
    ${login_body}     Create Dictionary       session[email]=a@a.com      session[password]=a     commit=Sign in
    ${response}=    RequestsLibrary.post request    host        /session        data=${login_body}      headers=${headers}
    should be equal as integers    ${response.status_code}      200