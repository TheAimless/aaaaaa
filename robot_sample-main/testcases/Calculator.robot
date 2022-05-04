*** Settings ***
Resource    ..${/}resources${/}imports.robot
Resource    ..${/}object${/}calculator.robot
Test Setup    Set Up And Open Android Application
Test Teardown    Quit application

*** Test Cases ***
Calculate
    [Tags]    Mobile
    Input number    9
    Click plus
    Input number    5
    click equal
    verify result    14