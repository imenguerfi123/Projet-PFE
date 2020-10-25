from flask import Flask,  request
from flask_restplus import Api, Resource, fields
from server.instance import server
from models.channel import channel
from werkzeug.contrib.fixers import ProxyFix
from functools import wraps 
from resources.terminal import *
from resources.card import *
app, api = server.app, server.api


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message' : 'Token is missing.'}, 401

        if token != 'mytoken':
            return {'message' : 'Your token is wrong, wrong, wrong!!!'}, 401

        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)

    return decorated

ns_channel = server.api.namespace('Channels', description='Channels operations')

#Channels
class ChannelDAO(object):
    def __init__(self):
        self.counter = 0
        self.channels = []
        self.nbr_Probes_max= 2

    def get_channel_by_id(self, channel_id):   
        ''' Fetch channel
            :return a channel given its identifier
            channel_id: integer
            card_name: string
            terminal_type: string
            channel_status: string
        '''
        for channel in self.channels:
            if channel['channel_id'] == channel_id:
                return channel
        api.abort(404, "channel {} doesn't exist".format(channel_id))

    def create_channel(self, data):
        '''create a new channel 
         dictionary(e.g:{'card_name': 'name', 'terminal_type': 'type', 'channel_status': 'Free' } )
        ''' 
        if  len(self.channels) < self.nbr_Probes_max :
            if (len(DAO.cards)!=0 and len(DAOT.terminals)!=0):
                channel = data 
                if ((channel['card_name'] in  DAO.cards[0].values()) or (channel['card_name'] in  DAO.cards[1].values()) or (channel['card_name'] in  DAO.cards[2].values())or (channel['card_name'] in  DAO.cards[3].values())):
                    if (channel['terminal_type'] in  DAOT.terminals[0].values() or channel['terminal_type'] in  DAOT.terminals[1].values()):
                        channel['channel_status'] = 'New'
                        channel['channel_id'] = self.counter 
                        self.counter = self.counter + 1
                        return channel
                    else:
                        api.abort(500, "name error , please verify your terminal name.")
                else:
                    api.abort(500, "name error , please verify your card name.")
            else:
                api.abort(500, "we can not create channel, please insert card and terminal first then try again.")
        if self.counter == self.nbr_Probes_max :
            api.abort(500, "The number of channels is exactly equal to the numbers of the probes.")

    def update_channel(self, channel_id, data):
        ''' Update a channel given its identifier "channel_id" 
        '''
        channel = self.get_channel_by_id(channel_id)
        if channel['channel_status'] == "Free" or channel['channel_status'] == "New":
            channel['channel_status'] = 'New'
            channel.update(data)
            return channel
        else:
           api.abort(500, "channel is locked, you can't up date")

    def delete_channel(self, channel_id):
        ''' Delete a channel given its identifier "channel_id" 
        '''
        channel = self.get_channel_by_id(channel_id)
        if channel['channel_status'] == "Free" or channel['channel_status'] == "New":
            self.channels.remove(channel)
        else:
           api.abort(500, "channel is locked, you can't delete it")

DAOC = ChannelDAO()

@ns_channel.route('/')
class ChannelList(Resource):

    ''' Shows a list of all channels, and lets you POST to add new channels
    '''
    @api.doc(security='apikey')
    @token_required
    @ns_channel.doc('list_channels')
    @ns_channel.marshal_list_with(channel, envelope='channels')
    def get(self):
        ''' List all channels
        '''
        if (len(DAOC.channels)==0):
            api.abort(500, "We have no channel.")
        else:
            return DAOC.channels
     
    @api.doc(security='apikey')
    @token_required
    @ns_channel.doc('create_channel')
    @ns_channel.expect(channel)
    @ns_channel.marshal_with(channel, code=201)
    def post(self):
        ''' Create a new channel
        '''
        return DAOC.create_channel(api.payload), 201


@ns_channel.route('/<int:channel_id>')
@ns_channel.response(404, 'Channel not found')
@ns_channel.param('channel_id', 'The channel identifier')
class Channel(Resource):
    ''' Show a single channel item and lets you delete them
    '''
    @api.doc(security='apikey')
    @token_required
    @ns_channel.doc('get_channel')
    @ns_channel.marshal_with(channel)
    def get(self, channel_id):
        ''' Fetch a given resource
        '''
        return DAOC.get_channel_by_id(channel_id)
     
    @api.doc(security='apikey')
    @token_required
    @ns_channel.doc('delete_channel')
    @ns_channel.response(204, 'Channel deleted')
    def delete(self, channel_id):
        ''' Delete a channel given its identifier
        '''
        DAOC.delete_channel(channel_id)
        return '', 204
     
    @api.doc(security='apikey')
    @token_required
    @ns_channel.expect(channel)
    @ns_channel.marshal_with(channel)
    def put(self, channel_id):
        ''' Update a channel given its identifier
        '''
        return DAOC.update_channel(channel_id, api.payload)
