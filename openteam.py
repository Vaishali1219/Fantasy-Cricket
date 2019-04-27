# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openteam.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog_openteam(object):
    cou1 = 0
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(671, 530)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.pt1 = QtWidgets.QLineEdit(Dialog)
        self.pt1.setObjectName("pt1")
        self.horizontalLayout_4.addWidget(self.pt1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.t1combo = QtWidgets.QComboBox(Dialog)
        self.t1combo.setObjectName("t1combo")
        self.t1combo.addItem("")
        self.t1combo.activated.connect(self.combitemt1)
        self.horizontalLayout_4.addWidget(self.t1combo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lisplayt1 = QtWidgets.QListWidget(Dialog)
        self.lisplayt1.setObjectName("lisplayt1")
        self.horizontalLayout_7.addWidget(self.lisplayt1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.lispointt1 = QtWidgets.QListWidget(Dialog)
        self.lispointt1.setObjectName("lispointt1")
        self.horizontalLayout_7.addWidget(self.lispointt1)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fr = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fr.setFont(font)
        self.fr.setObjectName("fr")
        self.fr.clicked.connect(self.t1list)
        self.horizontalLayout_6.addWidget(self.fr)
        self.cancel = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_6.addWidget(self.cancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Dialog)
        self.cancel.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Open Team"))
        self.t1combo.setItemText(0, _translate("Dialog", "select team"))
        self.label.setText(_translate("Dialog", "Fantasy Team"))
        self.label_5.setText(_translate("Dialog", "Points"))
        self.label_4.setText(_translate("Dialog", "Team"))
        self.fr.setText(_translate("Dialog", "Open"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        
    def combitemt1(self):
        while Ui_Dialog_openteam.cou1 < 1:
            _translate = QtCore.QCoreApplication.translate
            MyTeam = sqlite3.connect('FanCrickets.db')
            Te = MyTeam.cursor()
            count = 1
            qur = "SELECT DISTINCT Name from teams;"
            Te.execute(qur)
            result = Te.fetchall()
            for record in result:
                self.t1combo.addItems(record)
                self.t1combo.setItemText(count,_translate("Form", '{}'.format(record[0])))
                count += 1
            Ui_Dialog_openteam.cou1 += 1
            MyTeam.close()
    
    def t1list(self):
        self.lisplayt1.clear()
        self.lispointt1.clear()
        player = []
        point = []
        total = 0
        MyTeam = sqlite3.connect('FanCrickets.db')
        Te = MyTeam.cursor()
        sq = "SELECT Players, Value from teams WHERE Name == '{}';".format(self.t1combo.currentText())
        Te.execute(sq)
        while True:
            record=Te.fetchone()
            if record==None:
                break
            player.append(record[0])
            point.append(record[1])
        MyTeam.close()
        for index in range(len(player)):
            self.lisplayt1.addItem(player[index])
            self.lispointt1.addItem(str(point[index]))
        for i in range(len(point)):
            total += point[i]
        self.pt1.setText('{}'.format(total))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_openteam()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
