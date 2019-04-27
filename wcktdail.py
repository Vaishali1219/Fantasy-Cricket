# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wcktdail.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_wk(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 117)
        self.OK = QtWidgets.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(120, 70, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.OK.setFont(font)
        self.OK.setObjectName("OK")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.OK.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.OK.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate("Dialog", "You can\'t select more than one wicket-keeper"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_wk = QtWidgets.QDialog()
    ui = Ui_Dialog_wk()
    ui.setupUi(Dialog_wk)
    Dialog_wk.show()
    sys.exit(app.exec_())
