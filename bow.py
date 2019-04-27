# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_bow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(321, 121)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.OK3 = QtWidgets.QPushButton(Dialog)
        self.OK3.setGeometry(QtCore.QRect(110, 70, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.OK3.setFont(font)
        self.OK3.setObjectName("OK3")

        self.retranslateUi(Dialog)
        self.OK3.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "You can\'t select more than three Bowlers"))
        self.OK3.setText(_translate("Dialog", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_bow = QtWidgets.QDialog()
    ui = Ui_Dialog_bow()
    ui.setupUi(Dialog_bow)
    Dialog_bow.show()
    sys.exit(app.exec_())
