*** Settings ***
Resource        ..${/}resources${/}imports.robot

*** Variables ***
${input_username}         session_email
${input_password}         session_password
${btn_login}                //*[@name='commit']


*** Keywords ***
Login with
    [Arguments]     ${username}         ${password}
    Input ${username} into Email textbox
    Input ${password} into Password textbox
    click login button

Input ${username} into Email textbox
    input Text          ${input_username}         ${username}
Input ${password} into Password textbox
    Input password      ${input_password}         ${password}
Click Login button
    Click element       ${btn_login}
