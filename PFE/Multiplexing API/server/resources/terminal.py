from flask import Flask,  request
from flask_restplus import Api, Resource, fields
from server.instance import server
from models.terminal import terminal
from werkzeug.contrib.fixers import ProxyFix
from functools import wraps 
#from flask_serial import Serial

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


ns_terminal = server.api.namespace('Terminals', description='Terminals operations')

#Terminals
class TerminalDAO(object):
    def __init__(self):
        self.counter = 0
        self.terminals = []
        self.nbr_probes_max= 2

    def get_terminal_by_id(self, probe_id):
        ''' Fetch terminal
            :return terminal
            probe_id: integer
            device_id: str
            type: str
        ''' 
        for terminal in self.terminals:
            if terminal['probe_id'] == probe_id:
                return terminal
        api.abort(404, "terminal {} doesn't exist".format(probe_id))

    def create_terminal(self, data):
        ''' create a new terminal
            dictionary(e.g:{"device_id":"terminal_1", "type":"type_1"}
        ''' 
        if self.counter < self.nbr_probes_max :
            terminal = data
            self.terminals.append(terminal)
            self.counter = self.counter + 1
            return terminal
        api.abort(500, "The maximum number of probes has been exceeded .")

    def update_terminal(self, probe_id, data):
        ''' Update a terminal given its identifier "probe_id" 
        ''' 
        terminal = self.get_terminal_by_id(probe_id)
        terminal.update(data)
        return terminal

    def delete_terminal(self, probe_id):
        ''' Delete a terminal given its identifier "probe_id" 
        '''
        terminal = self.get_terminal_by_id(probe_id)
        self.terminals.remove(terminal)


DAOT = TerminalDAO()

@ns_terminal.route('/')
class TerminalList(Resource):        
    ''' Shows a list of all terminals, and lets you POST to add new terminals
    '''
    @api.doc(security='apikey')
    @token_required
    @ns_terminal.doc('list_terminals')
    @ns_terminal.marshal_list_with(terminal, envelope='terminals')
    def get(self):
        ''' List all terminals
        '''
        if (len(DAOT.terminals)==0):
            api.abort(500, "Terminal not connected.")
        else:
            return DAOT.terminals


@ns_terminal.route('/<int:probe_id>')
@ns_terminal.response(404, 'Terminal not found')
@ns_terminal.param('probe_id', 'The terminal identifier')
class Terminal(Resource):
    ''' Show a single terminal item and lets you delete them
    '''
    @api.doc(security='apikey')
    @token_required
    @ns_terminal.doc('get_terminal')
    @ns_terminal.marshal_with(terminal)
    def get(self, probe_id):
        ''' Fetch a given resource
        '''
        return DAOT.get_terminal_by_id(probe_id)
     
    @api.doc(security='apikey')
    @token_required
    @ns_terminal.expect(terminal)
    @ns_terminal.marshal_with(terminal)
    def put(self, probe_id):
        ''' Update a card given its identifier
        '''
        return DAOT.update_terminal(probe_id, api.payload)