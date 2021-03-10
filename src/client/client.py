import xmlrpc.client
import pickle
import uiFunction

current_user = ""

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
    return server

# handles logging into the server
def login_to_server(server, username, password):
    logged_in_user = server.login(username, password)
    if logged_in_user == "login###failed":
        print("Login failed, either password is incorrect or user " + username + " does not exist.")
        return False
    current_user = logged_in_user
    return True

# Main
def main():
    address = "127.0.0.1"
    port    = "5258"
    server  = None

    server = configServer(address, port)
    if(address is not None):
        print("Connection established successfully")
        guiHandler = uiFunction.UIHandler(server)
        guiHandler.main_Loop()
    else:
        quit()

if __name__ == "__main__":
    main()