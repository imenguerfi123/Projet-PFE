from flask_restplus import fields
from server.instance import server

'''we use the fields module to describe the structure of our response'''

card = server.api.model('cards', {
    'slot_id': fields.Integer(readonly=True, description='The card unique identifier'),
    'name': fields.String(required=True, description='The card details')
})