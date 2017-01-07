import ConfigParser
import numpy as np

config = ConfigParser.SafeConfigParser()
config.read('./config.ini')

name =  config.get('fruit', 'name')
price =  float(config.get('fruit', 'price'))
