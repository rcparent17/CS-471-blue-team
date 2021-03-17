from xmlrpc.server import SimpleXMLRPCServer
from typing import List
import databaseHelper
from databaseClasses import Inventory
from transactions import Money, Cash, CreditCard, MemberCard, UnprocessedTransaction

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


def get_all_inventory() -> List[tuple]:
    """
    Returns a list of tuples of the form
    (ID, Name, Cost, Stock)
    representing the current inventory database
    """
    inventory = databaseHelper.getAllInventory()
    return inventory


def submit_transaction(payments, item_names, customer_name) -> str:
    """
    Arguments:
    payment - a list of strings of one of the following forms
      * cash #.#
      * credit #.# <card number> <zip code>
      * member #.# <card_number> <member_pin>
      where #.# is a dollar and cent amount, like 245.32

    item_names - a list of strings of the names of the items being bought.
                 if an item is bought more than once, put it in the list
                 more than once

    customer_name - The name of the customer
    """
    if item_names and payments:
        constructed_payments = []
        for payment in payments:
            values = payment.split()
            if values[0] == "cash":
                dollars, cents = values[1].split(".")
                money = Money(int(dollars), int(cents))
                constructed_payments.append(Cash(money))
            elif values[0] == "credit":
                dollars, cents = values[1].split(".")
                money = Money(int(dollars), int(cents))
                constructed_payments.append(CreditCard(money, values[2], values[3]))
            elif values[0] == "member":
                dollars, cents = values[1].split(".")
                money = Money(int(dollars), int(cents))
                constructed_payments.append(CreditCard(money, values[2], values[3]))
            else:
                return "Malformed payment"

        items = [databaseHelper.getInventoryByName(item) for item in item_names]

        if not all(items):
            return "Item missing from database"
        transaction = UnprocessedTransaction(constructed_payments, items, customer_name)

        if transaction.items_are_valid():
            transaction.process()
            return "Success"
        else:
            return "Items invalid"
    return "Items or payment missing"


def main():
    ################
    # Start Server #
    ################

    # Set up logging
    # logging.basicConfig(level=logging.DEBUG)

    # Instantiate server
    # See docs.python.org/3/library/xmlrpc.server.html for more
    server = SimpleXMLRPCServer(("127.0.0.1", port), logRequests=True)

    # Register functions - enables RPC calls
    server.register_function(pong)
    server.register_function(login)
    server.register_function(get_all_inventory)
    server.register_function(submit_transaction)

    ##################
    # Listen Forever #
    ##################

    try:
        print("Use Control-C to exit")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")


if __name__ == "__main__":
    main()
