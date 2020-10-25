import requests
import json

#Cards
class Card():
    def __init__(self, host='192.168.8.102', port='5000'):
        self.url = 'http://{host}:{port}'.format(host=host, port=port)
        self.headers = {'Content-Type': 'application/json' , 'X-API-KEY': 'mytoken'}
        self.counter = 0
        self.nbr_slots_max= 4
        
    def _url(self, path):
        ''' Constructs full URL
            :param path: Relative path
            :type path: str
            :return: Full URL
        '''
        return self.url + path
        
    def get_card_list(self):
        ''' List all cards
            :return cards list
            slot_id: integer
            name: str
        '''  
        response = requests.get(self._url('/Cards'),
            headers=self.headers
        )
        print(response.status_code)
        print(response.headers)
        print (response.content)
    
    '''def create_card(self, card_data):
        
        if self.counter < self.nbr_slots_max :
            response = requests.post(self._url('/Cards/'),
                headers=self.headers,
                data=json.dumps(card_data) 
            )
            card_data['id'] = self.counter = self.counter + 1
            print(response.status_code)
            print(response.headers)
            print(response.content)'''
     
    def get_card_by_id(self, slot_id):
        ''' Show a single card item 
        ''' 
        response = requests.get(
            "{}{}".format(self._url('/Cards/'), slot_id),
            headers=self.headers
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)
       
    def update_card(self, slot_id, card_data):
        ''' Update a card given its identifier "slot_id" 
        ''' 
        response = requests.put(
            "{}{}".format(self._url('/Cards/'), slot_id),
            headers=self.headers,
            data=json.dumps(card_data)             
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)
       
    def delete_card(self, slot_id):
        ''' Delete a card given its identifier "slot_id" 
        ''' 
        response = requests.delete(
            "{}{}{}".format(self.url, '/Cards/', slot_id),
            headers=self.headers
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)
        
        
#Terminals 
class Terminal():
    def __init__(self, host='192.168.8.102', port='5000'):
        self.url = 'http://{host}:{port}'.format(host=host, port=port)
        self.headers = {'Content-Type': 'application/json' , 'X-API-KEY': 'mytoken'}
        self.counter = 0
        self.nbr_Probes_max= 2
    
    def _url(self, path):
        ''' Constructs full URL
            :param path: Relative path
            :type path: str
            :return: Full URL
        '''
        return self.url + path
      
    def get_terminal_list(self):
        ''' List all terminals
            :return terminals list
            probe_id: integer
            device_id: str
            type: str
        ''' 
        response = requests.get(self._url('/Terminals'),
            headers=self.headers
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)
    
      
    '''def create_terminal(self, terminal_data):
       
        if self.counter < self.nbr_Probes_max :
            response = requests.post(self._url('/Terminals/'),
                headers=self.headers,
                data=json.dumps(terminal_data) 
            )
            terminal_data['id'] = self.counter = self.counter + 1
            print(response.status_code)
            print(response.headers)
            print(response.content)'''
    
      
    def get_terminal_by_id(self, probe_id):
        ''' Show a single terminal item 
        '''
        response = requests.get(
            "{}{}".format(self._url('/Terminals/'), probe_id),
            headers=self.headers
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)
    
      
    def update_terminal(self, probe_id, terminal_data):
        ''' Update a terminal given its identifier "probe_id" 
        '''  
        response = requests.put(
            "{}{}".format(self._url('/Terminals/'), probe_id),
            headers=self.headers,
            data=json.dumps(terminal_data)             
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)
    
       
    def delete_terminal(self, probe_id):
        ''' Delete a terminal given its identifier "probe_id" 
        '''
        response = requests.delete(
            "{}{}".format(self._url('/Terminals/'), probe_id),
            headers=self.headers
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)

#Channel
class Channel():
    def __init__(self, host='192.168.8.102', port='5000'):
        self.url = 'http://{host}:{port}'.format(host=host, port=port)
        self.headers = {'Content-Type': 'application/json' , 'X-API-KEY': 'mytoken'}
        self.nbr_Probes_max= 2
        self.counter = 0
    
    def _url(self, path):
        ''' Constructs full URL
            :param path: Relative path
            :type path: str
            :return: Full URL
        '''
        return self.url + path

        
    def get_channel_list(self):
        ''' List all channels
            :return channels list
            channel_id: integer
            slot_id: string
            probe_id: string
        ''' 
        response = requests.get(self._url('/Channels'),
            headers=self.headers
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)
    
      
    def create_channel(self, channel_data):
        '''create a new channel 
         dictionary(e.g:{'card_name': 'name', 'terminal_type': 'type', 'channel_status': 'Free' })
        ''' 
        if self.counter < self.nbr_Probes_max :
            response = requests.post(self._url('/Channels/'),
                headers=self.headers,
                data=json.dumps(channel_data) 
            )
            channel_data['id'] = self.counter = self.counter + 1
            print(response.status_code)
            print(response.headers)
            print(response.content)

         
    def get_channel_by_id(self, channel_id):
        ''' Show a single channel item 
        '''
        response = requests.get(
            "{}{}".format(self._url('/Channels/'), channel_id),
            headers=self.headers
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)
    
       
    def update_channel(self, channel_id, channel_data):
        ''' Update a channel given its identifier "channel_id" 
        '''
        response = requests.put(
            "{}{}".format(self._url('/Channels/'), channel_id),
            headers=self.headers,
            data=json.dumps(channel_data)             
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)
    
        
    def delete_channel(self, channel_id):
        ''' Delete a channel given its identifier "channel_id" 
        '''
        response = requests.delete(
            "{}{}".format(self._url('/Channels/'), channel_id),
            headers=self.headers
        )
        print(response.status_code)
        print(response.headers)
        print(response.content)

if __name__ == "__main__":

    cad= Card()
    cad.get_card_list()
    cad.get_card_by_id(1)
    cad.update_card( 1, {"name":"card_01"})
    cad.delete_card(1)
    ter=Terminal()
    ter.get_terminal_list()
    ter.get_terminal_by_id(1)
    ter.update_terminal(1, {'device_id': 'terminal_01','type': 'type_01'})
    cha=Channel()
    cha.get_channel_list()
    cha.create_channel({'card_name': 'name', 'terminal_type': 'type', 'channel_status': 'Free' })
    cha.get_channel_by_id(1)
    cha.update_channel(1, {'card_name': 'name', 'terminal_type': 'type', 'channel_status': 'New' } )
    cha.delete_channel(1)
