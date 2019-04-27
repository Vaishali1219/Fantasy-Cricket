# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allrdail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_all(object):
    def setupUi(self, Dialog_all):
        Dialog_all.setObjectName("Dialog")
        Dialog_all.resize(332, 119)
        self.label = QtWidgets.QLabel(Dialog_all)
        self.label.setGeometry(QtCore.QRect(20, -10, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.OK1 = QtWidgets.QPushButton(Dialog_all)
        self.OK1.setGeometry(QtCore.QRect(120, 70, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.OK1.setFont(font)
        self.OK1.setObjectName("OK1")

        self.retranslateUi(Dialog_all)
        self.OK1.clicked.connect(Dialog_all.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_all)

    def retranslateUi(self, Dialog_all):
        _translate = QtCore.QCoreApplication.translate
        Dialog_all.setWindowTitle(_translate("Dialog_all", "Dialog"))
        self.label.setText(_translate("Dialog_all", "You can\'t select more than three All - Rounder"))
        self.OK1.setText(_translate("Dialog_all", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_all = QtWidgets.QDialog()
    ui = Ui_Dialog_all()
    ui.setupUi(Dialog_all)
    Dialog_all.show()
    sys.exit(app.exec_())
