from flask import Flask
from flask_restplus import Api, Resource, fields
from environment.instance import environment_config
from environment.instance import environment_config
from werkzeug.contrib.fixers import ProxyFix
from flask_serial import Serial

authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'X-API-KEY'
    }
}

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SERIAL_TIMEOUT'] = 0.01
        self.app.config['SERIAL_PORT'] = '/dev/ttyS0'
        self.app.config['SERIAL_BAUDRATE'] = 9600
        self.app.config['SERIAL_BYTESIZE'] = 8
        self.app.config['SERIAL_PARITY'] = 'N'
        self.app.config['SERIAL_STOPBITS'] = 1
        self.api = Api(self.app, 
            authorizations=authorizations,
            version='1.0', 
            title='Multiplexing API',
            description='A simple Multiplexing API', 
            doc = environment_config["swagger-url"]
        )

    def run(self):
        self.app.run(
                debug = environment_config["debug"], 
                port = environment_config["port"],
                host = environment_config["host"]
            )

server = Server()