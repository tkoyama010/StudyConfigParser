import ConfigParser
import numpy as np

config = ConfigParser.SafeConfigParser()
config.read('./config.ini')

print config.get('fruit', 'name')

