# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eval.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from won import Ui_Dialog_won
from lost import Ui_Dialog_lost

class Ui_Dialog_eval(object):
    cou1 = 0
    cou2 = 0
    
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.pt2 = QtWidgets.QLineEdit(Dialog)
        self.pt2.setObjectName("pt2")
        self.horizontalLayout_2.addWidget(self.pt2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.t2combo = QtWidgets.QComboBox(Dialog)
        self.t2combo.setObjectName("t2combo")
        self.t2combo.addItem("")
        self.t2combo.activated.connect(self.combitemt2)
        self.horizontalLayout_2.addWidget(self.t2combo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lisplayt2 = QtWidgets.QListWidget(Dialog)
        self.lisplayt2.setObjectName("lisplayt2")
        self.horizontalLayout_8.addWidget(self.lisplayt2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.lispointst2 = QtWidgets.QListWidget(Dialog)
        self.lispointst2.setObjectName("lispointst2")
        self.horizontalLayout_8.addWidget(self.lispointst2)
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
        self.fr.clicked.connect(self.seeresult)
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
        self.cancel.clicked.connect(self.co)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Evaluate"))
        self.t1combo.setItemText(0, _translate("Dialog", "select team"))
        self.t2combo.setItemText(0, _translate("Dialog", "select team"))
        self.label.setText(_translate("Dialog", "Evaluate the Performance of your Fantasy Team"))
        self.label_5.setText(_translate("Dialog", "Points"))
        self.label_4.setText(_translate("Dialog", "Team_1"))
        self.label_3.setText(_translate("Dialog", "Points"))
        self.label_2.setText(_translate("Dialog", "Team_2"))
        self.fr.setText(_translate("Dialog", "Find Result"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        
    def combitemt1(self):
        while Ui_Dialog_eval.cou1 < 1:
            _translate = QtCore.QCoreApplication.translate
            MyTeam = sqlite3.connect('FanCrickets.db')
            Te = MyTeam.cursor()
            count = 1
            qur = "SELECT DISTINCT Name from teams WHERE Name != '{}';".format(self.t2combo.currentText())
            Te.execute(qur)
            result = Te.fetchall()
            for record in result:
                self.t1combo.addItems(record)
                self.t1combo.setItemText(count,_translate("Form", '{}'.format(record[0])))
                count += 1
            Ui_Dialog_eval.cou1 += 1
            MyTeam.close()  
        self.t1list()
    
    def combitemt2(self):
        while Ui_Dialog_eval.cou2 < 1:
            _translate = QtCore.QCoreApplication.translate
            MyTeam = sqlite3.connect('FanCrickets.db')
            Te = MyTeam.cursor()
            count = 1
            qur = "SELECT DISTINCT Name from teams WHERE Name != '{}';".format(self.t1combo.currentText())
            Te.execute(qur)
            result = Te.fetchall()
            for record in result:
                self.t2combo.addItems(record)
                self.t2combo.setItemText(count,_translate("Form", '{}'.format(record[0])))
                count += 1
            Ui_Dialog_eval.cou2 += 1
            MyTeam.close()
        self.t2list()
        
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
 
            
    def t2list(self):
        self.lisplayt2.clear()
        self.lispointst2.clear()
        player = []
        point = []
        total = 0
        MyTeam = sqlite3.connect('FanCrickets.db')
        Te = MyTeam.cursor()
        sq = "SELECT Players, Value from teams WHERE Name == '{}';".format(self.t2combo.currentText())
        Te.execute(sq)
        while True:
            record=Te.fetchone()
            if record==None:
                break
            player.append(record[0])
            point.append(record[1])
        MyTeam.close()
        for index in range(len(player)):
            self.lisplayt2.addItem(player[index])
            self.lispointst2.addItem(str(point[index]))
        for i in range(len(point)):
            total += point[i]
        self.pt2.setText('{}'.format(total))
        
        
    def seeresult(self):
        try:
            t1 = float(self.pt1.text())
            t2 = float(self.pt2.text())
            self.t2combo.setEnabled(False)
            self.t1combo.setEnabled(False)
            if t1 > t2:
                if (self.t1combo.currentText() != self.t2combo.currentText()):
                    self.wondail()
            else:
                if (self.t1combo.currentText() != self.t2combo.currentText()):
                    self.lostdail()
        except:
            if (self.t1combo.currentText() == self.t2combo.currentText()):
                self.lisplayt1.clear()
                self.lispointt1.clear()
                self.lisplayt2.clear()
                self.lispointst2.clear()
                print("Same Teams invalid")
                
    def wondail(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_won()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
    
    def lostdail(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_lost()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        
    def co(self):
        Ui_Dialog_eval.cou1 = 0
        Ui_Dialog_eval.cou2 = 0
        self.lisplayt1.clear()
        self.lispointt1.clear()
        self.lisplayt2.clear()
        self.lispointst2.clear()
        
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_eval()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
