
*************************************Flask-Installation-Steps*************************************************************************

1) create a directory 

            mkdir dir_name 

2) Create an environment

            sudo apt-get update

            sudo apt install python3-pip
            
            sudo python3 -m pip install --upgrade pip setuptools wheel

            sudo apt install python3-venv 
             
            sudo python3 -m venv env

3) Change the permission of virtuel environment 

            sudo chown -R pi:pi env

4) check the permission of virtuel environment
       
            stat env

5) Activate the environment

             . env/bin/activate

6) Install Flask
             
             pip install Flask

7) Create a minimal Flask application
           
             nano Myapplication.py
           
8) Execute the application

            export FLASK_APP=Myapplication.py

To enable all development features (including debug mode) you can export 

the FLASK_ENV environment variable and set it to development before running the server

            export FLASK_ENV=development

If we want change the default port number (5000)
 
            export FLASK_RUN_PORT=8000

If we have the debugger disabled or trust the users on our network, we can make 

the server publicly available simply by adding --host=0.0.0.0 to the command line

           flask run --host=0.0.0.0 

9)deactivate the environment
   
           deactivate

Sources :

https://flask.palletsprojects.com/en/1.1.x/installation/

https://flask.palletsprojects.com/en/1.1.x/quickstart/


*************************************************Server creation Steps******************************************************************************


1) create  directories

            mkdir Multiplexing-API
        
            mkdir client

            cd  Multiplexing-API

            mkdir environment  models  resources  server
             
    
2) Create an environment

            sudo apt install python3-pip

            sudo apt install python3-venv 
             
            sudo python3 -m venv env

3) Change the permission of virtuel environment 

            sudo chown -R pi:pi env

4) Activate the environment

             . env/bin/activate

5) Install all dependencies
             
             pip install Flask

             pip install flask-restplus

6) Create the code structure

            nano Icc_Server.py
           
            nano  environment/ instance.py
 
            nano  server/ instance.py
            
            nano models/card.py 

            nano models/terminal.py 

            nano models/channel.py

            nano resources/card.py

            nano resources/terminal.py 

            nano resources/channel.py
           
7) Execute the application

            export FLASK_APP=Icc_Server.py

            export FLASK_ENV=development

            flask run --host=0.0.0.0 

8)Execute the client
     
            cd client 

            python Icc_Client.py
Commandes:

GET:

curl -X GET "http://192.168.8.102:5000/Cards/" -H "accept: application/json" -H "X-API-KEY: mytoken"
curl -X GET "http://192.168.8.102:5000/Terminals/" -H "accept: application/json" -H "X-API-KEY: mytoken"
curl -X GET "http://192.168.8.102:5000/Channels/" -H "accept: application/json" -H "X-API-KEY: mytoken"

POST:

curl -X POST "http://192.168.8.102:5000/Cards/" -H "accept: application/json" -H "X-API-KEY: mytoken" -H "Content-Type: application/json" -d "{ \"Name\": \"mastercard\"}"
curl -X POST "http://192.168.8.102:5000/Terminals/" -H "accept: application/json" -H "X-API-KEY: mytoken" -H "Content-Type: application/json" -d "{ \"Device_id\": \"123\"}"
curl -X POST "http://192.168.8.102:5000/Channels/" -H "accept: application/json" -H "X-API-KEY: mytoken" -H "Content-Type: application/json" -d "{ \"Slot_id\": \"1\", \"Probe_id\": \"2\"}"

GET by id:

curl -X GET "http://192.168.8.102:5000/Cards/1" -H "accept: application/json" -H "X-API-KEY: mytoken"
curl -X GET "http://192.168.8.102:5000/Terminals/1" -H "accept: application/json" -H "X-API-KEY: mytoken"
curl -X GET "http://192.168.8.102:5000/Channels/1" -H "accept: application/json" -H "X-API-KEY: mytoken"

PUT:

curl -X PUT "http://192.168.8.102:5000/Cards/1" -H "accept: application/json" -H "X-API-KEY: mytoken" -H "Content-Type: application/json" -d "{ \"Name\": \"visa\"}"
curl -X PUT "http://192.168.8.102:5000/Terminals/1" -H "accept: application/json" -H "X-API-KEY: mytoken" -H "Content-Type: application/json" -d "{ \"Device_id\": \"142\"}"
curl -X PUT "http://192.168.8.102:5000/Channels/1" -H "accept: application/json" -H "X-API-KEY: mytoken" -H "Content-Type: application/json" -d "{ \"Slot_id\": \"2\", \"Probe_id\": \"1\"}"

DELET:

curl -X DELETE "http://192.168.8.102:5000/Cards/1" -H "accept: application/json" -H "X-API-KEY: mytoken"
curl -X DELETE "http://192.168.8.102:5000/Terminals/1" -H "accept: application/json" -H "X-API-KEY: mytoken"
curl -X DELETE "http://192.168.8.102:5000/Channels/1" -H "accept: application/json" -H "X-API-KEY: mytoken"



***********************************************How to access UART using Python *******************************************************


1) Free the serial port

Before going further, you must check that the console is not listening on the serial port. To do this, run

          sudo raspi-config

	  Select -> Interfacing Options

          select Serial option to enable UART

          Then it will ask for login shell to be accessible over Serial, select No shown as follows.

          At the end, it will ask for enabling Hardware Serial port, select Yes.

          Finally, our UART is enabled for Serial Communication on RX and TX pin of Raspberry Pi 3.


2) reboot the Raspberry Pi.


3)Install pyserial 

Pyserial provides backend for serial communication using python. The module named ‘serial’ selects appropriate backend automatically. 
To install pySerial, by using following command.


          sudo pip3 install pyserial

          sudo apt-get install python-serial python3-serial


And in case you don't have working internet connection on Raspberry Pi

1) download the PySerial package  

           https://pypi.org/project/pyserial/

2) cd pyserial-3.4 

           sudo python setup.py install








