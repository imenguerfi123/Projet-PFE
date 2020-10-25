from server.instance import server
import sys, os

# Need to import all resources
from resources.card import *
from resources.terminal import *
from resources.channel import *
from serialworker.serial import *

if __name__ == '__main__':
    server.run()