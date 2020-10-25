

**************************************Robot-Framework-Installation-Steps******************************



1)Install python

          sudo apt-get install python3-pip
or

          python -m pip install -U pip

2) Install robotframework

          sudo pip3 install robotframework
or

          python3 -m pip install robotframework 


3) To upgrade robotframework

          pip install --upgrade robotframework
or

          pip install --pre --upgrade robotframework


To know the robotframework version and information

          robot --version

          pip show robotframework 

4)Install libraries

          pip install -U robotframework-requests

          pip install robotframework-seleniumlibrary


To uninstall the robotframework

          pip uninstall robotframework

5)create a directory

          mkdir dir_name 

6) Create a test 
           
          nano test.robot

7) Execute the test

          robot test.robot
Sources:

https://www.swtestacademy.com/getting-started-robotframework/
