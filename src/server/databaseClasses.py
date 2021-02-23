class EmployeeWorkTime:
    def __init__(self, full_name, hours, last_clock_in, last_clock_out):
        self.full_name = full_name
        self.hours = hours
        self.last_clock_in = last_clock_in
        self.last_clock_out = last_clock_out


class Inventory:
    def __init__(self, ID, name, cost, stock):
        self.ID = ID
        self.name = name
        self.cost = cost
        self.stock = stock


class Transactions:
    def __init__(self, ID, total_cost, time, items, customer_name):
        self.ID = ID
        self.total_cost = total_cost
        self.time = time
        self.items = items
        self.customer_name = customer_name


class UserAccesses:
    def __init__(self, ID, username, time, type):
        self.ID = ID
        self.username = username
        self.time = time
        self.type = type


class Users:
    def __init__(self, username, permissions, password):
        self.username = username
        self.permissions = permissions
        self.password = password


class WorkOrders:
    def __init__(self, ID, name, items, time_created, time_started, time_finished):
        self.ID = ID
        self.name = name
        self.items = items
        self.time_created = time_created
        self.time_started = time_started
        self.time_finished = time_finished
