*** Settings ***
Library    SerialLibrary
Library  RequestsLibrary 
Library  Collections


*** Variables ***
${Browser}  Chrome
${base_url}  http://192.168.8.102:5000

*** Test Cases ***
TC1: Returns all the cards(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Cards/   headers=${header}
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200
	
TC2: Read Login
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable    
	Write Data    0x00026000
    ${read} =    Read Until
	Should Be Equal As Strings    ${read}    0x00026000
	[Teardown]    Delete All Ports
	
TC3: Insert Card 1
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable    
	Write Data    0x00026100
	[Teardown]    Delete All Ports
	
TC4: Insert Card 2
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable    
	Write Data    0x00026101
	[Teardown]    Delete All Ports
	
TC5: Returns all the cards(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Cards/   headers=${header}
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200
	
TC6: Returns the details of a single card by ID(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Cards/0   headers=${header}  
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200	
	
	
	${res_body}=	convert to string  ${response.content}
	should contain  ${res_body}		card_00
	
TC7: Insert Terminal
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable    
	Write Data    0x00026300
	[Teardown]    Delete All Ports
	
TC8: Returns all the terminals(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Terminals/   headers=${header}
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200
	
TC9: Returns the details of a single terminal by ID(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Terminals/0   headers=${header}  
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200	
	
	
	${res_body}=	convert to string  ${response.content}
	should contain  ${res_body}		type_00
	
TC11: Add a new channel (POST)
	Create Session  mysession  ${base_url}
	${body}=	Create dictionary	 channel_id=0  card_name=card_00  terminal_type=type_00  channel_status=New
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=	post request  mysession  Channels/	 data=${body}	headers=${header}  
	
	log to console  ${response.status_code}
	log to console  ${response.content}
	
	
	#Validation
	${status_code}=	 convert to string  ${response.status_code}
	should be equal  ${status_code}		201
	
	${res_body}=	convert to string  ${response.content}
	
TC12: Check Status
	[Setup]    Add Port    COM3    baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable     
	Write Data    0x00026400	
    ${read} =    Read Until
	Should Be Equal As Strings    ${read}    0x0003650000
	[Teardown]    Delete All Ports
	
	
TC13: Returns all the channels(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Channels/   headers=${header}
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200

TC14: Free Channel
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable     
	Write Data    0x00026800	
	[Teardown]    Delete All Ports
	
TC15: Returns the details of a single channel by ID(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Channels/0   headers=${header}  
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200	
	
	
	${res_body}=	convert to string  ${response.content}
	should contain  ${res_body}		00


	
TC16: Deletes a card by ID
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable    
	Write Data    0x00026900
    ${read} =    Read Until
	Should Be Equal As Strings    ${read}    0x00026900
	[Teardown]    Delete All Ports
		
TC17: Deletes a terminal by ID
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable    
	Write Data    0x00027000
    ${read} =    Read Until
	Should Be Equal As Strings    ${read}    0x00027000
	[Teardown]    Delete All Ports
	

TC18: Deletes a channel by ID (DELETE)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=   delete request  mysession	Channels/0   headers=${header}
	
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		204
	
	${res_body}=	convert to string  ${response.content}

TC19: Returns all the cards(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Cards/   headers=${header}
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200

TC20: Returns all the terminals(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Terminals/   headers=${header}
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200

TC21: Returns all the channels(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Channels/   headers=${header}
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200

	
TC22: Add a new channel (POST)
	Create Session  mysession  ${base_url}
	${body}=	Create dictionary	 channel_id=0  card_name=card_01  terminal_type=type_00  channel_status=New
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=	post request  mysession  Channels/	 data=${body}	headers=${header}  
	
	log to console  ${response.status_code}
	log to console  ${response.content}
	
	
	#Validation
	${status_code}=	 convert to string  ${response.status_code}
	should be equal  ${status_code}		201
	
	${res_body}=	convert to string  ${response.content}

TC23: Insert Terminal
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable    
	Write Data    0x00026300
	[Teardown]    Delete All Ports

TC24: Add a new channel (POST)
	Create Session  mysession  ${base_url}
	${body}=	Create dictionary	 channel_id=01  card_name=card_01  terminal_type=type_01  channel_status=New
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=	post request  mysession  Channels/	 data=${body}	headers=${header}  
	
	log to console  ${response.status_code}
	log to console  ${response.content}
	
	
	#Validation
	${status_code}=	 convert to string  ${response.status_code}
	should be equal  ${status_code}		201
	
	${res_body}=	convert to string  ${response.content}
	
TC25: Add a new channel (POST)
	Create Session  mysession  ${base_url}
	${body}=	Create dictionary	 channel_id=01  card_name=card_01  terminal_type=type_00  channel_status=New
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=	post request  mysession  Channels/	 data=${body}	headers=${header}  
	
	log to console  ${response.status_code}
	log to console  ${response.content}
	
	
	#Validation
	${status_code}=	 convert to string  ${response.status_code}
	should be equal  ${status_code}		201
	
	${res_body}=	convert to string  ${response.content}
	
TC26: Lock Channel
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable     
	Write Data    0x00026700	
	[Teardown]    Delete All Ports

TC27: Returns all the channels(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Channels/   headers=${header}
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200

TC28: Update an existing channel by specifying a new body (PUT)
	Create Session  mysession  ${base_url}
	${body}=	Create dictionary	  card_name=card_01  terminal_type=type_00	channel_status=New
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=	put request  mysession  Channels/1	 data=${body}	headers=${header}  
	
	log to console  ${response.status_code}
	log to console  ${response.content}
	
	
	#Validation
	${status_code}=	 convert to string  ${response.status_code}
	should be equal  ${status_code}		200
	
	${res_body}=	convert to string  ${response.content}
	should contain  ${res_body}		01   00


TC29: Deletes a channel by ID (DELETE)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=   delete request  mysession	Channels/1   headers=${header}
	
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		204
	
	${res_body}=	convert to string  ${response.content}
	
TC30: Free Channel
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable     
	Write Data    0x00026800	
	[Teardown]    Delete All Ports

TC31: Returns all the channels(GET)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=    get request  mysession	Channels/   headers=${header}
	log to console  ${response.status_code}
	log to console  ${response.content}
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		200
	
TC32: Insert Terminal
	[Setup]    Add Port    COM3    timeout=0.1  baudrate=115200
	${encoding} =    Set Encoding    utf-8
	${bytes} =    Set Variable    
	Write Data    0x00026301
	[Teardown]    Delete All Ports

TC33: Update an existing channel by specifying a new body (PUT)
	Create Session  mysession  ${base_url}
	${body}=	Create dictionary	  card_name=card_01  terminal_type=type_01	channel_status=New
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=	put request  mysession  Channels/1	 data=${body}	headers=${header}  
	
	log to console  ${response.status_code}
	log to console  ${response.content}
	
	
	#Validation
	${status_code}=	 convert to string  ${response.status_code}
	should be equal  ${status_code}		200
	
	${res_body}=	convert to string  ${response.content}
	should contain  ${res_body}		01   01
	
TC34: Deletes a channel by ID (DELETE)
	Create Session  mysession  ${base_url}
	${header}=	Create dictionary  Content-Type=application/json   X-API-KEY=mytoken
	${response}=   delete request  mysession	Channels/1   headers=${header}
	
	#Validation
	${status_code}=		convert to string  ${response.status_code}
	should be equal  ${status_code}		204
	
	${res_body}=	convert to string  ${response.content}