import sqlite3


def addEmployeeWorkTime(full_name, hours, last_clock_in, last_clock_out):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'INSERT INTO "Employee Work Time"(FullName,Hours,"Last Clock In","Last Clock Out") VALUES(?,?,?,?)'
    args = (full_name, hours, last_clock_in, last_clock_out)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()


def addTransaction(name, cost, stock):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = "INSERT INTO Transaction(Name,Cost,Stock) VALUES(?,?,?)"
    args = (name, cost, stock)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()


def addUserAccesses(username, time, type):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'INSERT INTO "User Accesses"(Username,Time,Type) VALUES(?,?,?)'
    args = (username, time, type)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()


def addUser(username, permissions, password):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = "INSERT INTO Users(Username,Time,Type) VALUES(?,?,?)"
    args = (username, permissions, password)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()


def addWorkOrder(name, items, time_created, time_started, time_finished):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'INSERT INTO "Work Orders"(Name,Items,"Time Created","Time Started","Time Finished") VALUES(?,?,?,?,?)'
    args = (name, items, time_created, time_started, time_finished)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()


def getEmployeeWorkTimeByFullName(full_name):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'SELECT * FROM "Employee Work Time" WHERE FullName=?'
    cursor = conn.cursor()
    args = (full_name,)
    cursor.execute(query, args)
    conn.commit()
    conn.close()
    return cursor.fetchone()


def getInventoryByID(ID):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = "SELECT * FROM Inventory WHERE ID=?"
    cursor = conn.cursor()
    args = (ID,)
    cursor.execute(query, args)
    conn.commit()
    conn.close()
    return cursor.fetchone()


def getTransactionByID(ID):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = "SELECT * FROM Transaction WHERE ID=?"
    cursor = conn.cursor()
    args = (ID,)
    cursor.execute(query, args)
    conn.commit()
    conn.close()
    return cursor.fetchone()


def getUserAccessesByID(ID):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'SELECT * FROM "User Accesses" WHERE ID=?'
    cursor = conn.cursor()
    args = (ID,)
    cursor.execute(query, args)
    conn.commit()
    conn.close()
    return cursor.fetchone()


def getUsersByUsername(username):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = "SELECT * FROM Users WHERE Username=?"
    cursor = conn.cursor()
    args = (username,)
    cursor.execute(query, args)
    conn.commit()
    conn.close()
    return cursor.fetchone()


def getWorkOrdersByID(ID):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'SELECT * FROM "Work Orders" WHERE ID=?'
    cursor = conn.cursor()
    args = (ID,)
    cursor.execute(query, args)
    conn.commit()
    conn.close()
    return cursor.fetchone()


def updateEmployeeWorkTime(full_name, hours, last_clock_in, last_clock_out):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'UPDATE "Employee Work Time" SET Hours=?, "Last Clock In"=?, "Last Clock Out"=?  WHERE FullName=?'
    cursor = conn.cursor()
    args = (hours, last_clock_in, last_clock_out, full_name)
    cursor.execute(query, args)
    conn.commit()
    conn.close()


def updateInventory(ID, name, cost, stock):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = "UPDATE Inventory SET Name=?, Cost=?, Stock=?  WHERE ID=?"
    cursor = conn.cursor()
    args = (name, cost, stock, ID)
    cursor.execute(query, args)
    conn.commit()
    conn.close()

def addInventory(ID, name, cost, stock):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'INSERT INTO "Inventory"(ID,Name,Cost,Stock) VALUES(?,?,?,?)'
    args = (ID, name, cost, stock)
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()

def updateTransactions(ID, total_cost, time, items, customer_name):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'UPDATE Transaction SET "Total Cost"=?, Time=?, Items=?, "Customer Name"=?  WHERE ID=?'
    cursor = conn.cursor()
    args = (total_cost, time, items, customer_name, ID)
    cursor.execute(query, args)
    conn.commit()
    conn.close()


def updateUserAccesses(ID, username, time, type):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'UPDATE "User Accesses" SET Username=?, Time=?, Time=?  WHERE ID=?'
    cursor = conn.cursor()
    args = (username, time, type, ID)
    cursor.execute(query, args)
    conn.commit()
    conn.close()


def updateUser(username, permission, password):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = "UPDATE User SET Permissions=?, Password=?  WHERE Username=?"
    cursor = conn.cursor()
    args = (permission, password, username)
    cursor.execute(query, args)
    conn.commit()
    conn.close()


def updateWorkOrders(ID, name, items, time_created, time_started, time_finished):
    conn = sqlite3.connect("..\\..\\database\\motorcycle_shop.db")
    query = 'UPDATE "Work Orders" SET Name=?, Items=?, "Time Created"=?, "Time Started"=?, "Time Finished"=?  WHERE ID=?'
    cursor = conn.cursor()
    args = (name, items, time_created, time_started, time_finished, ID)
    cursor.execute(query, args)
    conn.commit()
    conn.close()
