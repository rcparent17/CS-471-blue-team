from xmlrpc.server import SimpleXMLRPCServer
import databaseHelper

# Default fields
port = 5258

# each entry is formatted like this: {username (str): permissions (int)}
logged_in_users = {}

########################
# Function Definitions #
########################

# Used to verify the connection to the server
def pong():
    return True

# Used to log a user in
def login(username, password):
    registered_users = databaseHelper.getAllUsers()
    for user in registered_users:
        if user[0] == username and user[2] == password:
            logged_in_users[username] = int(user[1])
            return username
    return "login###failed"

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
server.register_function(login)



##################
# Listen Forever #
##################

try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
