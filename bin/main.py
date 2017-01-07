import ConfigParser
import numpy as np

config = ConfigParser.SafeConfigParser()
config.read('./config.ini')

name =  config.get('fruit', 'name')
price =  np.float64(config.get('fruit', 'price'))
print price
