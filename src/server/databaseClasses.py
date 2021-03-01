class EmployeeWorkTime:
    def __init__(self, full_name, hours, last_clock_in, last_clock_out):
        self.full_name = full_name
        self.hours = hours
        self.last_clock_in = last_clock_in
        self.last_clock_out = last_clock_out


class Inventory:
    def __init__(self, id, name, cost, stock):
        self.id = id
        self.name: str = name
        self.cost = cost
        self.stock: int = stock


class Transaction:
    """
    Note: the id should be None when being created
    to be inserted into the database. It should be
    some number when pulled from the database
    """

    def __init__(self, id, total_cost, time, items, customer_name):
        self.id = id
        self.total_cost = total_cost
        self.time = time
        self.items = items
        self.customer_name = customer_name


class UserAccesses:
    def __init__(self, id, username, time, type):
        self.id = id
        self.username = username
        self.time = time
        self.type = type


class Users:
    def __init__(self, username, permissions, password):
        self.username = username
        self.permissions = permissions
        self.password = password


class WorkOrders:
    def __init__(self, id, name, items, time_created, time_started, time_finished):
        self.id = id
        self.name = name
        self.items = items
        self.time_created = time_created
        self.time_started = time_started
        self.time_finished = time_finished
