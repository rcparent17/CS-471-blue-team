import xmlrpc.client
import sys
from PyQt5 import QtWidgets
import uiFunction

# Establish connection with an XML-RPC server
# See docs.python.org/3/library/xmlrpc.client.html for more
#   Input:      Output (tuple):
#   ------      ---------------
#   N/A         String          Server Address
#               String          RPC port
#               ServerProxy     Server object
def configServer(address, port):

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
def main():
    address = "127.0.0.1"
    port    = "5258"
    server  = None

    (address, port, server) = configServer(address, port)
    if(address is not None):
        #The program has connected to the server
        print("Connection established successfully")
        guiController = uiFunction.UIHandler()
        guiController.main_Loop()

    else:
        quit()

#entry point
if __name__ == "__main__":
    main()