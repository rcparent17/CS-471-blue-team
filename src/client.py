import xmlrpc.client

# Establish connection with an XML-RPC server
# See docs.python.org/3/library/xmlrpc.client.html for more
#   Input:      Output (tuple):
#   ------      ---------------
#   N/A         String          Server Address
#               String          RPC port
#               ServerProxy     Server object
def configServer():
    address = input("Server address: ")
    port    = input("Listening port: ")

    # ServerProxy object - manages communication with remote server
    server = xmlrpc.client.ServerProxy("http://" + address + ":" + port)

    # pong() returns True to verify connection to server
    if (not server.pong()):
        print("Server connection failed, please try again.")
        print("  Attempted to pong() server at address " + address)
        print("  using port " + port)
        return ("0.0.0.0", "00000", None)

    # Return tuple containing server details in case useful
    return (address, port, server)



# Main
address = None
port    = None
server  = None

(address, port, server) = configServer()
if(address is not None):
    print("Connection established successfully")
else:
    quit()

