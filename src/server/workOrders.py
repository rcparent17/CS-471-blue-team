import databaseHelper
import datetime

# these are the function definitions for scheduling and editing work orders.
# they are meant to be called from a GUI, so there is no main method here.

def scheduleWorkOrder(name, items):
    timeCreated = str(datetime.datetime.now())
    timeStarted = "Not Started"
    timeFinished = "Not Finished"
    databaseHelper.addWorkOrder(name, items, timeCreated, timeStarted, timeFinished)

def startWorkOrder(ID):
    order = databaseHelper.getWorkOrderByID(ID)
    timeStarted = str(datetime.datetime.now())
    databaseHelper.updateWorkOrder(order[0], order[1], order[2], order[3], timeStarted, order[5])

def finishWorkOrder(ID):
    order = databaseHelper.getWorkOrderByID(ID)
    timeFinished = str(datetime.datetime.now())
    databaseHelper.updateWorkOrder(order[0], order[1], order[2], order[3], order[4], timeFinished)

