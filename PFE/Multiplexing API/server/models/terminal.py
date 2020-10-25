from flask_restplus import fields
from server.instance import server

'''we use the fields module to describe the structure of our response'''

terminal = server.api.model('terminals', {
    'probe_id': fields.Integer(readonly=True, description='The card unique identifier'),
    'device_id': fields.String(required=True, description='The card details'),
    'type': fields.String(required=True, description='The card details')
})