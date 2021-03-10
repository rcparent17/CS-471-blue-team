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

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = None
        self.currWindow = QtWidgets.QMainWindow()
        self.switchto_Login()
        pass
    
    def main_Loop(self):
        self.currWindow.show()
        sys.exit(self.app.exec_())
        pass
    
    def switchto_Login(self):
        self.ui = LoginHandler(self)
        self.ui.setup_UI(self.currWindow)
        self.ui.assign_Buttons()
        pass

    def switchto_Admin(self):
        newUI = AdminHandler()
        newUI.setup_UI(self.currWindow)
        pass

    def switchto_Employee(self):
        newUI = EmployeeHandler()
        newUI.setup_UI(self.currWindow)
        pass
#UI Handler
###########################################################################################

###########################################################################################
#LoginHandler
class LoginHandler():
    
    def __init__(self, parent):
        self.ui = None
        self.parent = parent
        pass

    def setup_UI(self, window):
        self.ui = login.Ui_LoginWindow()
        self.ui.setupUi(window)
        pass

    def assign_Buttons(self):
        self.ui.pushButton.clicked.connect(self.Button_Quit_Function)
        self.ui.pushButton_2.clicked.connect(self.Button_Login_Function)
        pass

    def Button_Login_Function(self):
        self.parent.switchto_Employee()
        pass

    def Button_Quit_Function(self):
        
        pass
#LoginHandler
###########################################################################################

###########################################################################################
#AdminHandler
class AdminHandler():
    
    def __init__(self):
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
    
    def __init__(self):
        self.ui = None
        pass

    def setup_UI(self, window):
        self.ui = employee.Ui_employeeWindow()
        self.ui.setupUi(window)
        pass
#EmployeeHandler
###########################################################################################