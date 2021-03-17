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
        self.ui.pushButton.clicked.connect(self.button_Quit_Function)
        self.ui.pushButton_2.clicked.connect(self.button_Login_Function)
        pass

    #This function will send the username and password to the server, requesting to login
    def button_Login_Function(self):
        logged_in_user = self.server.login(self.ui.lineEdit.text(), self.ui.lineEdit_2.text())
        if logged_in_user == "login###failed":
            print("Login failed, either password is incorrect or user " + self.ui.lineEdit.text() + " does not exist.")
            pass
        self.parent.switchto_Employee()
        pass

    #This function will exit the program
    def button_Quit_Function(self):
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
        self.server = server
        pass

    def setup_UI(self, window):
        self.ui = employee.Ui_EmployeeWindow()
        self.ui.setupUi(window)
        self.fill_Inventory_List(self.get_Inventory())
        pass

    def assign_Buttons(self):
        self.ui.Employee_Button_Search.clicked.connect(self.button_Search_Function)
        self.ui.Employee_Button_Quit.clicked.connect(self.button_Quit_Function)
        self.ui.Employee_Button_AddItem.clicked.connect(self.button_AddItem_Function)
        self.ui.Employee_Button_Confirm.clicked.connect(self.button_Confirm_Function)
        pass

    def get_Inventory(self):
        return self.server.get_all_inventory()
    
    #Takes a List of Tuples. Each item is a tuple of this form: (ID, Name, Cost, Stock)
    def fill_Inventory_List(self, list):
        self.ui.Employee_Tree_Inventory.clear()
        for item in list:
            newTreeItem = QtWidgets.QTreeWidgetItem(self.ui.Employee_Tree_Inventory)
            newTreeItem.setText(0, str(item[1])) #Name
            newTreeItem.setText(1, str(item[2])) #Cost
            newTreeItem.setText(2, str(item[3])) #Stock
        pass

    def button_AddItem_Function(self):
        selected_Item = self.ui.Employee_Tree_Inventory.selectedItems()[0]
        if(self.ui.Employee_SpinBox_Quantity.value() != 0 and int(selected_Item.text(2)) > self.ui.Employee_SpinBox_Quantity.value()):
            newTreeItem = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
            newTreeItem.setText(0, selected_Item.text(0))
            newTreeItem.setText(1, selected_Item.text(1))
            newTreeItem.setText(2, str(self.ui.Employee_SpinBox_Quantity.value()))
        pass

    def button_Confirm_Function(self):
        item_List = []
        price = 0
        price_string = "cash "
        customer = "Dale"

        for i in range(0, self.ui.treeWidget.topLevelItemCount()):
            qauntity = int(self.ui.treeWidget.topLevelItem(i).text(2))
            for index in range(qauntity):
                item_List.append(self.ui.treeWidget.topLevelItem(i).text(0))
                price += int(self.ui.treeWidget.topLevelItem(i).text(1))
        price_string = price_string + str(price) + ".00"
        self.server.submit_transaction([price_string], item_List, customer)
        self.ui.treeWidget.clear()
        self.fill_Inventory_List(self.get_Inventory())
        pass

    def button_Search_Function(self):
        return_List = []
        tuple_list = self.get_Inventory()
        search_Str = self.ui.Employee_lineEdit_Search.text()
        length = len(search_Str)
        for item in tuple_list:
            for index in range(len(item[1]) - length + 1):
                if search_Str == item[1][index:index + length]:
                    return_List.append(item)
                    break
        self.fill_Inventory_List(return_List)
        pass
    
    def button_Quit_Function(self):
        quit()
        pass

#EmployeeHandler
###########################################################################################