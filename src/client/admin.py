# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CS-471 Admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminWindow(object):
    def setupUi(self, adminWindow):
        adminWindow.setObjectName("adminWindow")
        adminWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(adminWindow)
        self.centralwidget.setObjectName("centralwidget")
        adminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        adminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminWindow)
        self.statusbar.setObjectName("statusbar")
        adminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(adminWindow)
        QtCore.QMetaObject.connectSlotsByName(adminWindow)

    def retranslateUi(self, adminWindow):
        _translate = QtCore.QCoreApplication.translate
        adminWindow.setWindowTitle(_translate("adminWindow", "Admin View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminWindow = QtWidgets.QMainWindow()
    ui = Ui_adminWindow()
    ui.setupUi(adminWindow)
    adminWindow.show()
    sys.exit(app.exec_())
