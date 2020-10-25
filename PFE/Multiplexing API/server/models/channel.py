from flask_restplus import fields
from server.instance import server

'''we use the fields module to describe the structure of our response'''

channel = server.api.model('channels', {
    'channel_id': fields.Integer(readonly=True, description='The channel unique identifier'),
    'card_name': fields.String(required=True, description='The channel details'),
    'terminal_type': fields.String(required=True, description='The channel details'),
    'channel_status': fields.String(readonly=True, description='The channel details')

})