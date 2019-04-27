# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bats.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_bat(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(327, 134)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.OK2 = QtWidgets.QPushButton(Dialog)
        self.OK2.setGeometry(QtCore.QRect(120, 80, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.OK2.setFont(font)
        self.OK2.setObjectName("OK2")

        self.retranslateUi(Dialog)
        self.OK2.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "You can\'t select more than three Batsman"))
        self.OK2.setText(_translate("Dialog", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_bats = QtWidgets.QDialog()
    ui = Ui_Dialog_bat()
    ui.setupUi(Dialog_bats)
    Dialog_bats.show()
    sys.exit(app.exec_())
