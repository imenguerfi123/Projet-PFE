from flask_serial import Serial
import json
import io
from resources.terminal import *
from resources.channel import *
from resources.card import *

app, api = server.app, server.api

ser =Serial(app)
CMD = { "LOGIN": "60",
        "CREATE_CARD" : "61",
        "INSERT_TERMINAL": "62",
        "CREATE_TERMINAL": "63",
        "CHECK_CHANNEL": "64",
        "CREATE_CHANNEL": "65",
        "CHANGE_STATUS": "66",
        "LOCK_CHANNEL": "67",
        "FREE_CHANNEL": "68",
        "DELETE_CARD": "69",
        "DELETE_TERMINAL":"70",
        "COMMAND_ERROR":"71",
        "DELETE_CHANNEL": "72"}

def get_length(msg):
    """this function returns the command length
    """
    return msg[2:6]

def get_cmd(msg):
    """this function returns the request command
    """
    return msg[6:8]

def get_payload(msg):
    """this function returns payload 
    """
    return msg[8:]
    
    
@ser.on_message()
def handle_message(msg):

    print("receive a message:", str(msg))

    cmd = get_cmd(msg)

    if cmd == CMD['LOGIN'].encode():
        print('login correct')
        ser.on_send(msg)

    elif cmd == CMD['CREATE_CARD'].encode():
        ''' requests to create cards:
            0x00026100
            0x00026101
            0x00026110
            0x00026111
        '''
        slot_id = get_payload(msg.decode())
        DAO.create_card({'slot_id':int(slot_id),'name':'card_{}'.format(slot_id)})
        ser.on_send(msg)
        print('card has been created')
    
    elif cmd == CMD['INSERT_TERMINAL'].encode():
        ser.on_send(msg)
        
    elif cmd == CMD['CREATE_TERMINAL'].encode():
        ''' requests to insert terminal:
            0x00026200
            0x00026201   
        '''
        probe_id = get_payload(msg.decode())
        DAOT.create_terminal({'probe_id':int(probe_id),'device_id':'terminal_{}'.format(probe_id),'type':'type_{}'.format(probe_id)})
        ser.on_send(msg)
        print('terminal has been created')
    
    elif cmd == CMD['CHECK_CHANNEL'].encode():
        ''' requests to check channel:
            0x00026400
            0x00026401   
        '''
        channel_id = get_payload(msg.decode())
        if (len(DAOC.channels)!=0 and DAOC.channels[int(channel_id)]["channel_status"]=="New"):
            ser.on_send("0x0003"+CMD['CREATE_CHANNEL']+DAOC.channels[int(channel_id)]["card_name"][5:]+DAOC.channels[int(channel_id)]["terminal_type"][5:])
        else:
            print('No new channel')
                
    elif cmd == CMD['CHANGE_STATUS'].encode():
        ser.on_send(msg)
        
    elif cmd == CMD['LOCK_CHANNEL'].encode():
        ''' requests to lock channel:
            0x00026700
            0x00026701   
        '''
        channel_id = get_payload(msg.decode())
        DAOC.channels[int(channel_id)]['channel_status'] ='Locked' 
        print('channel {} is locked'.format(int(channel_id)))
        
    elif cmd == CMD['FREE_CHANNEL'].encode():
        ''' requests to free channel:
            0x00026800
            0x00026801   
        '''
        channel_id = get_payload(msg.decode())
        DAOC.channels[int(channel_id)]['channel_status'] ='Free' 
        print('channel {} is free'.format(int(channel_id)))  
        
    elif(cmd == CMD['DELETE_CARD'].encode()):
        ''' requests to delete cards:
            0x00026900
            0x00026901
            0x00026910
            0x00026911
        '''
        slot_id = get_payload(msg.decode())
        ser.on_send(msg)
        DAO.delete_card(int(slot_id))
        print('card {} has been deleted'.format(int(slot_id)))
    
    elif(cmd == CMD['DELETE_TERMINAL'].encode()):
        ''' requests to delete terminals:
            0x00027000
            0x00027001
        '''
        probe_id = get_payload(msg.decode())
        ser.on_send(msg)
        DAOT.delete_terminal(int(probe_id))
        print('terminal {} has been deleted'.format(int(probe_id)))
        
    elif(cmd == CMD['DELETE_CHANNEL'].encode()):
        ''' requests to delete channels:
            0x00027200
            0x00027201
        '''
        channel_id = get_payload(msg.decode())
        if (len(DAOC.channels)!=0):
            if (int(channel_id) not in DAOC.channels[0].values() or int(channel_id) not in DAOC.channels[1].values()):
                ser.on_send(msg)
                print('channel has been deleted.')
            else:
                print('channel exist')
        else:
            print('all channels have been deleted')
            
    elif cmd not in CMD.values():
        ''' error request:
            0x000171
        '''
        ser.on_send("0x0001"+CMD['COMMAND_ERROR'])
        print('command error')
    time.sleep(0.1)

@ser.on_log()
def handle_logging(level, info):
    print(level, info)
