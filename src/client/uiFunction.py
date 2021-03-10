#Author: Guy Compton
#Date: 3/2/2021
#Purpose: This file will contain four classes.
#           - UIHandler will open and close the different UIs
#           - LoginHandler will connect all of the widgets on Login.py with Functions
#           - EmployeeHandler will connect all of the widgets in Employee.py with functions and contain the name of the employee
#           - AdminHandler will connect all of the widgets in admin.py with functions and contain the name of the admin

#import
import employee, login, admin
from PyQt5 import QtWidgets
import sys



###########################################################################################
#UI Handler
#This class will be in charge of handling of UIs. This includes closing and opening the UIs
class UIHandler():

    #constructor of UIHandler
    def __init__(self, server):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = None
        self.currWindow = QtWidgets.QMainWindow()
        self.server = server
        self.switchto_Login()
        pass
    
    #This function will start the main loop for event handling
    def main_Loop(self):
        self.currWindow.show()
        sys.exit(self.app.exec_())
        pass
    
    #This function will display the login screen
    def switchto_Login(self):
        self.ui = LoginHandler(self, self.server)
        self.ui.setup_UI(self.currWindow)
        self.ui.assign_Buttons()
        pass

    #This function will display the admin screen
    def switchto_Admin(self):
        self.ui = AdminHandler(self, self.server)
        self.ui.setup_UI(self.currWindow)
        self.ui.assign_Buttons()
        pass

    #This function will display the employee screen
    def switchto_Employee(self):
        self.ui = EmployeeHandler(self, self.server)
        self.ui.setup_UI(self.currWindow)
        self.ui.assign_Buttons()
        pass

#UI Handler
###########################################################################################

###########################################################################################
#LoginHandler
class LoginHandler():
    
    #Constructor of LoginHandler
    def __init__(self, parent, server):
        self.ui = None
        self.parent = parent
        self.server = server
        pass
    
    #This function sets up the UI of the Login Window
    def setup_UI(self, window):
        self.ui = login.Ui_LoginWindow()
        self.ui.setupUi(window)
        pass

    #This function will give each button a function that will be executed once the button is clicked
    def assign_Buttons(self):
        self.ui.pushButton.clicked.connect(self.Button_Quit_Function)
        self.ui.pushButton_2.clicked.connect(self.Button_Login_Function)
        pass

    #This function will send the username and password to the server, requesting to login
    def Button_Login_Function(self):
        logged_in_user = self.server.login(self.ui.lineEdit.text(), self.ui.lineEdit_2.text())
        if logged_in_user == "login###failed":
            print("Login failed, either password is incorrect or user " + self.ui.lineEdit.text() + " does not exist.")
            pass
        self.parent.switchto_Employee()
        pass

    #This function will exit the program
    def Button_Quit_Function(self):
        quit()
        pass

#LoginHandler
###########################################################################################

###########################################################################################
#AdminHandler
class AdminHandler():
    
    def __init__(self, parent, server):
        self.ui = None
        pass

    def setup_UI(self, window):
        self.ui = admin.Ui_adminWindow()
        self.ui.setupUi(window)
        pass

#AdminHandler
###########################################################################################

###########################################################################################
#EmployeeHandler
class EmployeeHandler():
    
    def __init__(self, parent, server):
        self.ui = None
        pass

    def setup_UI(self, window):
        self.ui = employee.Ui_employeeWindow()
        self.ui.setupUi(window)
        pass

#EmployeeHandler
###########################################################################################