# Robot framework for cloudcath project

## Installing for Mac

1. Install brew: to install brew, follow this [link](https://brew.sh/)

2. Install Python3 and virtual environment


    `brew install python@3`  
    `pip3 install virtualenv`

3. Install package, go to root folder (robot_cloudcath), run


    `sh install.sh`

4. Install webdriver manager and download target browser driver to
   resources/drivers

/Users/hieunguyen/Freelance/robot_cloudcath/testcases/Login.robot
    `pip install webdrivermanager`  
    `webdrivermanager firefox chrome --linkpath resources/drivers`

## Installing for Window
1. Install Python

To install python, go to python official site − https://www.python.org/downloads/ and download the latest version or the prior version of python as per your operating system (Windows).

2. Setting path for Windows

* Open the Start menu and start the Run app.
* Type sysdm.cpl and click OK. This opens the System Properties window.
* Navigate to the Advanced tab and select Environment Variables.
* Under System Variables, find and select the Path variable.
* Click Edit.
* Select the Variable value field. Add the path to the python.exe file
  preceded with a semicolon (;).

3. Install package, go to root folder (robot_cloudcath),
* Install virtualenv
  * Open the Start menu and start the Command Line app.
  * Type the following pip command in the console:


    `pip install virtualenv`
  * Active virtual environment:

    `run file venv/Scripts/activation.bat`
  * Install packages:

    `pip3 install -r ./resources/requirement.txt`

4. Install webdriver manager and download target browser driver to
   resources/drivers


    `pip install webdrivermanager`  
    `webdrivermanager firefox chrome --linkpath resources\drivers`

## Test execution on Mac/Windows
To run tests:

1. Activate virtual environment for Mac:

   `source ./venv/bin/activate`

2.  Activate virtual environment for Windows:

    `run file venv/Scripts/activation.bat`

3.  Run Tests:

    * To run all tests:

        `robot "<testfolder>"`

        `E.g:  robot testcases`

    * Run test file:

        `robot <path to test file>`

        `E.g: robot testcases/ViewPatient.robot`

    * Run single test:

        `robot -t "<Test case name>" <path to test file>`

        `E.g: robot -t "FR-157 The Admin user shall have a list based interface to patient data" testcases/ViewPatient.robot`
    * Run with browser test, we can add browser variable in command line
      (-v browser:chrome...) or change it in resources/constant.yaml,
      the value should be chrome/firefox/ie/edge:

        `robot -v browser:chrome -t "<Test case name>" <path to test
        file>`

        `E.g: robot -t "FR-157 The Admin user shall have a list based interface to patient data" testcases/ViewPatient.robot`

    * Run in parallel(pabot --processes *number of processes*):

        `pabot --processes 5 -v browser:chrome -t "<Test case name>"
        <path to test file>`
## What it is
This Python package adds support for [Robot Framework](http://robotframework.org/) and Robot Framework's [SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary). Though this package is a [Robot library](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#extending-robot-framework), it's usable outside the Robot context and facilitates use of the page object pattern independently of any Python testing framework. This means you can use it to create page objects and run tests in other testing frameworks like  [`unittest`](http://docs.python.org/2/library/unittest.html), [lettuce](http://lettuce.it/tutorial/simple.html), etc.


