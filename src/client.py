import xmlrpc.client
import pickle
import getpass

current_user = ""

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

# handles logging into the server
def login_to_server(server, username, password):
    logged_in_user = server.login(username, password)
    if logged_in_user == "login###failed":
        print("Login failed, either password is incorrect or user " + username + " does not exist.")
        return False
    current_user = logged_in_user
    return True

# Main
address = None
port    = None
server  = None

username = input("Username: ")
password = getpass.getpass()

(address, port, server) = configServer()
if(address is not None):
    if (login_to_server(server, username, password)):
        print("Connection established successfully")
    else:
        print("Connection established, but login failed")
else:
    quit()

