import serial,time
import json
import pprint

## Change this to match your local settings
port = 'COM3'
baudrate = 115200

class SerialHandler():
    """ This Class instantiates a serial thread and has functions for facilitating communication
    to the serial interface """
 
    def __init__(self):
        """ Initialises the variables used in this class, baudrate=, port= and timeout=  can be adjusted
        But have initial values of 115200, 'COM3' and 1 respectively """

        self.RPI = serial.Serial(port, 
        baudrate, 
        timeout=0.01,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE, 
        bytesize=serial.EIGHTBITS )
        self.counter = 0   
        self.counter1 = 0 
        self.counter2 = 0
        self.counter3 = 0
        self.nbr_slots_max= 4
        self.nbr_probes_max= 2
        self.terminals_vcc=[{'terminal_vcc':'0v'}, {'terminal_vcc':'0v'}, {'terminal_vcc':'5v'}, {'terminal_vcc':'5v'}]
       
        
    def getcommand(self):
        """This function is dedicated to open a 'commands.txt' file which contains our commands
        """
        commandsList = []
        with open('commands.txt') as f:
            for jsonObj in f:
                commandDict = json.loads(jsonObj)
                commandsList.append(commandDict)
        return (commandsList)

    def get_length(self, msg):
        """this function returns the the request length
        """
        return msg[2:6]

    def get_cmd(self, msg):
        """this function returns the request command
        """
        return msg[6:8]

    def get_payload_O1(self, msg):
        """this function returns the first payload byte
        """
        return msg[8:10]
        
    def get_payload_O2(self, msg):
        """this function returns the second payload byte
        """
        return msg[10:12]
       
       
    def run(self):
        """this function the main class function which performs all the class"""
        print('Running. Press CTRL-C to exit.')
        command = self.getcommand()
        if self.RPI.isOpen():
            """checking the serial port opening"""
            print("{} connected!".format(self.RPI.port))
            try:
                while True:               
                    time.sleep(0.1) #wait for RPI to answer                
                    cmd1=input("Enter command : ") #give the user a hand to enter a command
                    self.RPI.write(cmd1.encode())
                    while self.RPI.inWaiting()==0: pass
                    while  self.RPI.inWaiting()>0:
                        print ("Attempt to Read")
                        answer=self.RPI.readline() #read from the serial port
                        cmd = self.get_cmd(answer) #get the command part 
                        time.sleep(0.1)
 
                        if cmd == command[0]['LOGIN'].encode(): 
                            ''' requests to insert cards:
                                0x00026100
                                0x00026101
                                0x00026110
                                0x00026111
                            '''
                            print(answer)
                            if (len(dataC['card'])!=0 ):
                                if self.counter < self.nbr_slots_max:
                                    self.RPI.write(("0x0002"+command[0]['CREATE_CARD']+dataC['card'][self.counter]['slot_id']).encode())
                                    print('a new card has been added')
                                    self.counter = self.counter + 1
                                else:    
                                    print("The maximum number of slots has been exceeded .")
                            else:
                                print('we have no card, insert card and try again')
                            
                        elif cmd == command[0]['INSERT_TERMINAL'].encode():
                            ''' requests to insert terminal:
                                0x00026200
                                0x00026201   
                            '''
                            print(answer)
                            if (len(dataT['terminal'])!=0):
                                if self.counter1 < self.nbr_probes_max:
                                    self.RPI.write(("0x0002"+command[0]['CREATE_TERMINAL']+dataT['terminal'][self.counter1]['probe_id']).encode())
                                    print('a new terminal has been added')
                                    self.counter1 = self.counter1 + 1
                                else:
                                    print("The maximum number of probes has been exceeded.")
                            else:
                                print('we have no terminal, insert terminal and try again')  
                        
                        elif (cmd==command[0]['CREATE_CHANNEL'].encode()):
                            ''' requests to create channel:
                                0x0003650000
                                0x0003650001
                                0x0003650101
                                0x0003650100 
                                0x0003651000
                                0x0003651100                                 
                            '''
                            print(answer)
                            slot_id = self.get_payload_O1(answer.decode())
                            probe_id = self.get_payload_O2(answer.decode())
                            dataCH['channel'].append({
                                                'channel_id': self.counter2,
                                                'slot_id': int(slot_id),
                                                'probe_id': int(probe_id),
                                                'channel_status': 'New'
                                                 })
                            self.counter2 = self.counter2 + 1
                            print("a new channel has been created")
                            self.RPI.flushInput()
                            
                        elif (cmd==command[0]["CHANGE_STATUS"].encode()):
                            ''' requests to check status:
                                0x00026600
                                0x00026601                                
                            '''
                            channel_id = self.get_payload_O1(answer.decode())
                            if (self.terminals_vcc[self.counter3]['terminal_vcc']=='5v'):
                                dataCH['channel'][int(channel_id)]['channel_status'] = 'Locked'
                                print('channel {} is locked'.format(int(channel_id)))
                                self.RPI.write(("0x0002"+command[0]["LOCK_CHANNEL"]+channel_id).encode()) 
                                                               
                            else :
                                dataCH['channel'][int(channel_id)]['channel_status'] = 'Free'
                                self.RPI.write(("0x0002"+command[0]["FREE_CHANNEL"]+channel_id).encode())
                                print('channel {} is free'.format(int(channel_id)))
                            self.counter3 = self.counter3 + 1
                      
                        elif (cmd==command[0]["DELETE_CARD"].encode()):
                            ''' requests to delete cards:
                                0x00026900
                                0x00026901
                                0x00026910
                                0x00026911
                            '''
                            if (len(dataC['card'])!=0):
                                del dataC['card'][len(dataC['card'])-1]
                                print('card has been deleted.')
                            else:
                                print(" all cards have been deleted .") 
                                
                        elif (cmd==command[0]["DELETE_TERMINAL"].encode()):
                            ''' requests to delete terminals:
                                0x00027000
                                0x00027001
                            '''
                            if (len(dataT['terminal'])!=0):
                                del dataT['terminal'][len(dataT['terminal'])-1]
                                print('terminal has been deleted.') 
                                self.terminals_vcc[len(dataT['terminal'])]['terminal_vcc']='0v' 
                            else:
                                print(" all terminals have been deleted .")     
                        
                        elif (cmd==command[0]["DELETE_CHANNNEL"].encode()):
                            ''' requests to delete channels:
                                0x00027200
                                0x00027201
                            '''
                            channel_id = self.get_payload_O1(answer.decode())
                            if (len(dataCH['channel'])!=0):
                                del dataCH['channel'][int(channel_id)]
                                print('channel {} has been deleted.'.format(int(channel_id)))
                            else:
                                print(" all channels have been deleted .") 
                        
                        elif (cmd==command[0]["COMMAND_ERROR"].encode()):
                            ''' error request:
                                0x000171
                            '''
                            print('incorrect command, try again')
                            pass      
                        
                        else:
                            pass        
                            
         
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
        else:
            print("Cannot open serial port.")
                
if __name__ == '__main__':
	
    data = {}
    dataC = {}
    dataT = {}
    dataCH = {}
    dataC['card'] = [{'slot_id': '00','name': 'card_2'},{'slot_id': '01','name': 'card_2'}, {'slot_id': '10','name': 'card_3'},{'slot_id': '11','name': 'card_4'}]
    dataT['terminal'] = [{'probe_id': '00','device_id': 'terminal_1','type': 'type_1'}, {'probe_id': '01','device_id': 'terminal_2','type': 'type_2'}]
    dataCH['channel'] = []
    ser = SerialHandler()
    ser.run()
    