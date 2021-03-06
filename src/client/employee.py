# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CS-471 Employee.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmployeeWindow(object):
    def setupUi(self, EmployeeWindow):
        EmployeeWindow.setObjectName("EmployeeWindow")
        EmployeeWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(EmployeeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Employee_lineEdit_Search = QtWidgets.QLineEdit(self.centralwidget)
        self.Employee_lineEdit_Search.setObjectName("Employee_lineEdit_Search")
        self.verticalLayout_2.addWidget(self.Employee_lineEdit_Search)
        self.Employee_Button_Search = QtWidgets.QPushButton(self.centralwidget)
        self.Employee_Button_Search.setObjectName("Employee_Button_Search")
        self.verticalLayout_2.addWidget(self.Employee_Button_Search)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Employee_label_Selected = QtWidgets.QLabel(self.centralwidget)
        self.Employee_label_Selected.setObjectName("Employee_label_Selected")
        self.horizontalLayout_3.addWidget(self.Employee_label_Selected)
        self.Employee_SpinBox_Quantity = QtWidgets.QSpinBox(self.centralwidget)
        self.Employee_SpinBox_Quantity.setObjectName("Employee_SpinBox_Quantity")
        self.horizontalLayout_3.addWidget(self.Employee_SpinBox_Quantity)
        self.Employee_Button_AddItem = QtWidgets.QPushButton(self.centralwidget)
        self.Employee_Button_AddItem.setObjectName("Employee_Button_AddItem")
        self.horizontalLayout_3.addWidget(self.Employee_Button_AddItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.Employee_Button_Confirm = QtWidgets.QPushButton(self.centralwidget)
        self.Employee_Button_Confirm.setObjectName("Employee_Button_Confirm")
        self.verticalLayout_2.addWidget(self.Employee_Button_Confirm)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.Employee_Tree_Inventory = QtWidgets.QTreeWidget(self.centralwidget)
        self.Employee_Tree_Inventory.setColumnCount(3)
        self.Employee_Tree_Inventory.setObjectName("Employee_Tree_Inventory")
        self.horizontalLayout_2.addWidget(self.Employee_Tree_Inventory)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Employee_Button_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Employee_Button_Quit.setObjectName("Employee_Button_Quit")
        self.horizontalLayout.addWidget(self.Employee_Button_Quit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        EmployeeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EmployeeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        EmployeeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EmployeeWindow)
        self.statusbar.setObjectName("statusbar")
        EmployeeWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(EmployeeWindow)
        self.toolBar.setObjectName("toolBar")
        EmployeeWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(EmployeeWindow)
        QtCore.QMetaObject.connectSlotsByName(EmployeeWindow)

    def retranslateUi(self, EmployeeWindow):
        _translate = QtCore.QCoreApplication.translate
        EmployeeWindow.setWindowTitle(_translate("EmployeeWindow", "MainWindow"))
        self.Employee_Button_Search.setText(_translate("EmployeeWindow", "Search"))
        self.Employee_label_Selected.setText(_translate("EmployeeWindow", "Selected:"))
        self.Employee_Button_AddItem.setText(_translate("EmployeeWindow", "Add"))
        self.treeWidget.headerItem().setText(0, _translate("EmployeeWindow", "Name"))
        self.treeWidget.headerItem().setText(1, _translate("EmployeeWindow", "Cost"))
        self.treeWidget.headerItem().setText(2, _translate("EmployeeWindow", "Quantity"))
        self.Employee_Button_Confirm.setText(_translate("EmployeeWindow", "Confirm"))
        self.Employee_Tree_Inventory.headerItem().setText(0, _translate("EmployeeWindow", "Name"))
        self.Employee_Tree_Inventory.headerItem().setText(1, _translate("EmployeeWindow", "Cost"))
        self.Employee_Tree_Inventory.headerItem().setText(2, _translate("EmployeeWindow", "Stock"))
        self.Employee_Button_Quit.setText(_translate("EmployeeWindow", "Quit"))
        self.toolBar.setWindowTitle(_translate("EmployeeWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeeWindow = QtWidgets.QMainWindow()
    ui = Ui_EmployeeWindow()
    ui.setupUi(EmployeeWindow)
    EmployeeWindow.show()
    sys.exit(app.exec_())
