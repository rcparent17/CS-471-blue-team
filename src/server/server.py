from xmlrpc.server import SimpleXMLRPCServer

# Default fields
port = 5258

########################
# Function Definitions #
########################

# Used to verify the connection to the server
def pong():
    return True



################
# Start Server #
################

# Set up logging
#logging.basicConfig(level=logging.DEBUG)

# Instantiate server
# See docs.python.org/3/library/xmlrpc.server.html for more
server = SimpleXMLRPCServer(('127.0.0.1', port), logRequests=True)

# Register functions - enables RPC calls
server.register_function(pong)



##################
# Listen Forever #
##################

try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
