*** Settings ***
Resource    ..${/}resources${/}imports.robot
*** Keywords ***
Open browser ${url} with ${browser} browser
    [Documentation]    supported browsers: phantomjs, chrome, headlesschrome
    ${browser}    convert to lowercase    ${browser}
    ${os}=         Evaluate            platform.system()
    ${execute_file}=        set variable if         '${browser}'=='chrome'          chromedriver
                                        ...         '${browser}'=='firefox'      geckodriver
#                                        ...         '${browser}'=='ie'      iedriver
#                                        ...         '${browser}'=='edge'      we
    ${extension}=           set variable if            '${os}'=='Windows'           .exe            ${empty}
    set test variable     ${executable_path}            ${CURDIR}${/}..${/}resources${/}drivers${/}${execute_file}${extension}
    open browser        url=${url}     browser=${browser}        executable_path=${CURDIR}${/}..${/}resources${/}drivers${/}${execute_file}${extension}    alias=window1
    Maximize browser window

Start new browser session
    Delete all cookies
    Reload page

Set Up And Open Android Application
    ${port}=        set variable        4723
    ${URL}=         set variable             http://localhost:${port}/wd/hub
    Open Application    ${URL}
    ...     platformName=Android
    ...     deviceName=Test
    ...     appPackage=com.google.android.calculator
    ...     appActivity=com.android.calculator2.Calculator
    ...     automationName=UIAutomator2