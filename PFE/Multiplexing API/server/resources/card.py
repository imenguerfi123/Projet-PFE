from flask import Flask,  request
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
from functools import wraps 
from server.instance import server
from models.card import card
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

ns_card = server.api.namespace('Cards', description='Cards operations')


#Cards
class CardDAO(object):
    def __init__(self):
        self.counter = 0
        self.cards = []
        self.nbr_slots_max= 4
        
    def get_card_by_id(self, slot_id):
        ''' Fetch card
            :return card given its identifier
            slot_id: integer
            name: str
        ''' 
        for card in self.cards:
            if card['slot_id'] == slot_id:
                return card
        api.abort(404, "card {} doesn't exist".format(slot_id))

    def create_card(self, data):
        ''' create a new card
            dictionary(e.g:{"name":"card_1"})
        '''
        if self.counter < self.nbr_slots_max :
            card = data
            self.cards.append(card)
            self.counter = self.counter + 1
            return card
        api.abort(500, "The maximum number of slots has been exceeded .")

    def update_card(self, slot_id, data):
        ''' Update a card given its identifier "slot_id" 
        ''' 
        card = self.get_card_by_id(slot_id)
        card.update(data)
        return card

    def delete_card(self, slot_id):
        ''' Delete a card given its identifier
        '''
        card = self.get_card_by_id(slot_id)
        self.cards.remove(card)

DAO = CardDAO()


@ns_card.route('/')
class CardList(Resource):
        
    ''' Shows a list of all cards, and lets you POST to add new cards
    '''
    @api.doc(security='apikey')
    @token_required
    @ns_card.doc('list_cards')
    @ns_card.marshal_list_with(card, envelope='cards')
    def get(self):
        ''' List all cards
        '''
        if (len(DAO.cards)==0):
            api.abort(500, "Card not connected .")
        else:
            return DAO.cards
    


@ns_card.route('/<int:slot_id>')
@ns_card.response(404, 'Card not found')
@ns_card.param('slot_id', 'The card identifier')
class Card(Resource):
    ''' Show a single card item and lets you delete them
    '''
    @api.doc(security='apikey')
    @token_required
    @ns_card.doc('get_card')
    @ns_card.marshal_with(card)
    def get(self, slot_id):
        ''' Fetch a given resource
        '''
        return DAO.get_card_by_id(slot_id)
   
    @api.doc(security='apikey')
    @token_required
    @ns_card.expect(card)
    @ns_card.marshal_with(card)
    def put(self, slot_id):
        ''' Update a card given its identifier
        '''
        return DAO.update_card(slot_id, api.payload)