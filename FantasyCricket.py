# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FantasyCricket.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from allrdail import Ui_Dialog_all
from bats import Ui_Dialog_bat
from bow import Ui_Dialog_bow
from wcktdail import Ui_Dialog_wk
from save import Ui_Dialog_save
from openteam import Ui_Dialog_openteam
from evalu import Ui_Dialog_eval  

class Ui_FantasyCricket(object):
    bat_count = 0
    bow_count = 0
    ar_count = 0
    wk_count = 0
    total = 0
    teamname = ''
    scores = []
    
    def setupUi(self, FantasyCricket):
        FantasyCricket.setObjectName("FantasyCricket")
        FantasyCricket.resize(803, 738)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        FantasyCricket.setFont(font)
        self.centralwidget = QtWidgets.QWidget(FantasyCricket)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.bat = QtWidgets.QLineEdit(self.centralwidget)
        self.bat.setEnabled(False)
        self.bat.setObjectName("bat")
        self.horizontalLayout_2.addWidget(self.bat)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.bow = QtWidgets.QLineEdit(self.centralwidget)
        self.bow.setEnabled(False)
        self.bow.setObjectName("bow")
        self.horizontalLayout_2.addWidget(self.bow)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.ar = QtWidgets.QLineEdit(self.centralwidget)
        self.ar.setEnabled(False)
        self.ar.setObjectName("ar")
        self.horizontalLayout_2.addWidget(self.ar)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.wk = QtWidgets.QLineEdit(self.centralwidget)
        self.wk.setEnabled(False)
        self.wk.setObjectName("wk")
        self.horizontalLayout_2.addWidget(self.wk)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.pa = QtWidgets.QLineEdit(self.centralwidget)
        self.pa.setEnabled(False)
        self.pa.setObjectName("pa")
        self.horizontalLayout_4.addWidget(self.pa)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.tn = QtWidgets.QLineEdit(self.centralwidget)
        self.tn.setEnabled(False)
        self.tn.setObjectName("tn")
        self.horizontalLayout_4.addWidget(self.tn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.pu = QtWidgets.QLineEdit(self.centralwidget)
        self.pu.setEnabled(False)
        self.pu.setObjectName("pu")
        self.horizontalLayout_4.addWidget(self.pu)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bat_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.bat_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bat_btn.setFont(font)
        self.bat_btn.setObjectName("bat_btn")
        self.horizontalLayout_3.addWidget(self.bat_btn)
        self.bow_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.bow_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bow_btn.setFont(font)
        self.bow_btn.setObjectName("bow_btn")
        self.horizontalLayout_3.addWidget(self.bow_btn)
        self.ar_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.ar_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ar_btn.setFont(font)
        self.ar_btn.setObjectName("ar_btn")
        self.horizontalLayout_3.addWidget(self.ar_btn)
        self.wk_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.wk_btn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.wk_btn.setFont(font)
        self.wk_btn.setObjectName("wk_btn")
        self.horizontalLayout_3.addWidget(self.wk_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.dis_lis = QtWidgets.QListWidget(self.centralwidget)
        self.dis_lis.setEnabled(False)
        self.dis_lis.setObjectName("dis_lis")
        self.dis_lis.itemDoubleClicked.connect(self.loadPlayer)
        self.verticalLayout_2.addWidget(self.dis_lis)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.lis = QtWidgets.QListWidget(self.centralwidget)
        self.lis.setEnabled(False)
        self.lis.setObjectName("lis")
        self.horizontalLayout_5.addWidget(self.lis)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        FantasyCricket.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FantasyCricket)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        self.menuManageTeams = QtWidgets.QMenu(self.menubar)
        self.menuManageTeams.setObjectName("menuManageTeams")
        FantasyCricket.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FantasyCricket)
        self.statusbar.setObjectName("statusbar")
        FantasyCricket.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(FantasyCricket)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(FantasyCricket)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(FantasyCricket)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(FantasyCricket)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManageTeams.addAction(self.actionNEW_Team)
        self.menuManageTeams.addSeparator()
        self.menuManageTeams.addAction(self.actionOPEN_Team)
        self.menuManageTeams.addSeparator()
        self.menuManageTeams.addAction(self.actionSAVE_Team)
        self.menuManageTeams.addSeparator()
        self.menuManageTeams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManageTeams.menuAction())
        self.menuManageTeams.triggered[QtWidgets.QAction].connect(self.enableItems)
        self.retranslateUi(FantasyCricket)
        self.bat_btn.clicked.connect(lambda:self.loadList(self.bat_btn))
        self.bow_btn.clicked.connect(lambda:self.loadList(self.bow_btn))
        self.ar_btn.clicked.connect(lambda:self.loadList(self.ar_btn))
        self.wk_btn.clicked.connect(lambda:self.loadList(self.wk_btn))
        QtCore.QMetaObject.connectSlotsByName(FantasyCricket)

    def retranslateUi(self, FantasyCricket):
        _translate = QtCore.QCoreApplication.translate
        FantasyCricket.setWindowTitle(_translate("FantasyCricket", "FantasyCricketGame"))
        self.label.setText(_translate("FantasyCricket", "Your Selections"))
        self.label_3.setText(_translate("FantasyCricket", "Batsman (BAT)"))
        self.label_2.setText(_translate("FantasyCricket", "Bowlers (BWL)"))
        self.label_4.setText(_translate("FantasyCricket", "Alllrounder (AR)"))
        self.label_5.setText(_translate("FantasyCricket", "Wicket-Keeper (WK)"))
        self.label_7.setText(_translate("FantasyCricket", "Points Availablel"))
        self.label_6.setText(_translate("FantasyCricket", "Team Name"))
        self.label_8.setText(_translate("FantasyCricket", "Points Used"))
        self.bat_btn.setText(_translate("FantasyCricket", "BAT"))
        self.bow_btn.setText(_translate("FantasyCricket", "BOW"))
        self.ar_btn.setText(_translate("FantasyCricket", "AR"))
        self.wk_btn.setText(_translate("FantasyCricket", "WK"))
        self.menuManageTeams.setTitle(_translate("FantasyCricket", "ManageTeams"))
        self.actionNEW_Team.setText(_translate("FantasyCricket", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("FantasyCricket", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("FantasyCricket", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("FantasyCricket", "EVALUATE Team"))

    def enableItems(self, action):
        txt = (action.text())
        if txt == "NEW Team":
            self.bat_btn.setEnabled(True)
            self.bow_btn.setEnabled(True)
            self.ar_btn.setEnabled(True)
            self.wk_btn.setEnabled(True)
            self.dis_lis.setEnabled(True)
            self.lis.setEnabled(True)
            self.tn.setEnabled(True)
            self.dis_lis.clear()
            self.lis.clear()
            self.tn.clear()
            self.bat.clear()
            self.bow.clear()
            self.ar.clear()
            self.wk.clear()
            self.pa.clear()
            self.pu.clear()
            Ui_FantasyCricket.bat_count = 0
            Ui_FantasyCricket.bow_count = 0
            Ui_FantasyCricket.ar_count = 0
            Ui_FantasyCricket.wk_count = 0
            Ui_FantasyCricket.total = 0
            Ui_FantasyCricket.scores = []
        elif  txt == "SAVE Team":
            self.insertPlayers()
            self.bat_btn.setEnabled(False)
            self.bow_btn.setEnabled(False)
            self.ar_btn.setEnabled(False)
            self.wk_btn.setEnabled(False)
            self.dis_lis.setEnabled(False)
            self.lis.setEnabled(False)
            self.tn.setEnabled(False)
        elif txt == "OPEN Team":
            self.dis_lis.clear()
            self.lis.clear()
            self.tn.clear()
            self.bat.clear()
            self.bow.clear()
            self.ar.clear()
            self.wk.clear()
            self.pa.clear()
            self.pu.clear()
            self.bat_btn.setEnabled(False)
            self.bow_btn.setEnabled(False)
            self.ar_btn.setEnabled(False)
            self.wk_btn.setEnabled(False)
            self.dis_lis.setEnabled(False)
            self.lis.setEnabled(False)
            self.tn.setEnabled(False)
            Ui_FantasyCricket.bat_count = 0
            Ui_FantasyCricket.bow_count = 0
            Ui_FantasyCricket.ar_count = 0
            Ui_FantasyCricket.wk_count = 0
            Ui_FantasyCricket.total = 0
            Ui_FantasyCricket.scores = []
            self.openform()
        elif txt == "EVALUATE Team":
            self.evalteam()
            

    def loadList(self, tx):
        self.dis_lis.clear()
        cat = tx.text()
        player = []
        MyTeam = sqlite3.connect('FanCrickets.db')
        Te = MyTeam.cursor()
        sq = "SELECT Player from stats WHERE ctg == '{}';".format(cat)
        Te.execute(sq)
        while True:
            record=Te.fetchone()
            if record==None:
                break
            player.append(record[0])
        MyTeam.close()
        for index in range(len(player)):
            self.dis_lis.addItem(player[index])

    def loadPlayer(self, item):
            if self.bat_btn.isChecked() == True:
                if Ui_FantasyCricket.bat_count < 3:
                    self.getPoints(item.text())
                    po = float(self.pa.text())
                    Ui_FantasyCricket.total += po
                    self.dis_lis.takeItem(self.dis_lis.row(item))
                    self.lis.addItem(item.text())
                    Ui_FantasyCricket.bat_count += 1
                    bc = Ui_FantasyCricket.bat_count 
                    self.bat.setText('{}'.format(bc))
                    self.pu.setText('{}'.format(Ui_FantasyCricket.total))
                else:
                    self.batdail()
                    
            elif self.bow_btn.isChecked() == True:
                if Ui_FantasyCricket.bow_count < 4:
                    self.getPoints(item.text())
                    po = float(self.pa.text())
                    Ui_FantasyCricket.total += po
                    self.dis_lis.takeItem(self.dis_lis.row(item))
                    self.lis.addItem(item.text())
                    Ui_FantasyCricket.bow_count += 1
                    bc = Ui_FantasyCricket.bow_count 
                    self.bow.setText('{}'.format(bc))
                    self.pu.setText('{}'.format(Ui_FantasyCricket.total))
                else:
                    self.bowdail()
                
            elif self.ar_btn.isChecked() == True:
                if Ui_FantasyCricket.ar_count < 3:
                    self.getPoints(item.text())
                    po = float(self.pa.text())
                    Ui_FantasyCricket.total += po
                    self.dis_lis.takeItem(self.dis_lis.row(item))
                    self.lis.addItem(item.text())
                    Ui_FantasyCricket.ar_count += 1
                    bc = Ui_FantasyCricket.ar_count 
                    self.ar.setText('{}'.format(bc))
                    self.pu.setText('{}'.format(Ui_FantasyCricket.total))
                else:
                    self.alldail()
                
            elif self.wk_btn.isChecked() == True:
                if Ui_FantasyCricket.wk_count < 1:
                    self.getPoints(item.text())
                    po = float(self.pa.text())
                    Ui_FantasyCricket.total += po
                    self.dis_lis.takeItem(self.dis_lis.row(item))
                    self.lis.addItem(item.text())
                    Ui_FantasyCricket.wk_count += 1
                    bc = Ui_FantasyCricket.wk_count 
                    self.wk.setText('{}'.format(bc))
                    self.pu.setText('{}'.format(Ui_FantasyCricket.total))
                else:
                    self.wkdail()

    def getPoints(self, i):
        team = sqlite3.connect('FanCrickets.db')
        Te = team.cursor()
        if self.bat_btn.isChecked() == True:
            sq = "SELECT Runs from stats WHERE Player == '{}';".format(i)
            Te.execute(sq)
            while True:
                record=Te.fetchone()
                if record==None:
                    break
                runs = int(record[0])
            sq = "SELECT Fours, Sixes, Bowled from match WHERE Player == '{}';".format(i)
            Te.execute(sq)
            while True:
                record=Te.fetchone()
                if record==None:
                    break
                f = int(record[0])
                s = int(record[1])
                balls = int(record[2])
#            team.close()
            self.Batting_Score(runs, f, s, balls)
            
        elif (self.bow_btn.isChecked() == True):
            team = sqlite3.connect('FanCrickets.db')
            Te = team.cursor()
            sq = "SELECT Runs from stats WHERE Player == '{}';".format(i)
            Te.execute(sq)
            while True:
                record=Te.fetchone()
                if record==None:
                    break
                runs = int(record[0])
            sq = "SELECT Bowled, Wickets, Catches, Stumping, RunOut from match WHERE Player == '{}';".format(i)
            Te.execute(sq)
            while True:
                record=Te.fetchone()
                if record==None:
                    break
                balls = int(record[0])
                wickets = int(record[1])
                catches = int(record[2])
                stumping = int(record[3])
                runout = int(record[4])
#                team.close()
                self.Cal_Score(runs, balls, wickets, catches, stumping, runout)
                
        elif (self.wk_btn.isChecked() == True):
            team = sqlite3.connect('FanCrickets.db')
            Te = team.cursor()
            sq = "SELECT Runs from stats WHERE Player == '{}';".format(i)
            Te.execute(sq)
            while True:
                record=Te.fetchone()
                if record==None:
                    break
                runs = int(record[0])
            sq = "SELECT Bowled, Wickets, Catches, Stumping, RunOut from match WHERE Player == '{}';".format(i)
            Te.execute(sq)
            while True:
                record=Te.fetchone()
                if record==None:
                    break
                balls = int(record[0])
                wickets = int(record[1])
                catches = int(record[2])
                stumping = int(record[3])
                runout = int(record[4])
#                team.close()
                self.Cal_Score(runs, balls, wickets, catches, stumping, runout)
                
        elif self.ar_btn.isChecked() == True:
            team = sqlite3.connect('FanCrickets.db')
            Te = team.cursor()
            sq = "SELECT Runs from stats WHERE Player == '{}';".format(i)
            Te.execute(sq)
            while True:
                record=Te.fetchone()
                if record==None:
                    break
                runs = int(record[0])
            sq = "SELECT Fours, Sixes, Bowled, Wickets, Catches, Stumping, RunOut from match WHERE Player == '{}';".format(i)
            Te.execute(sq)
            while True:
                record=Te.fetchone()
                if record==None:
                    break
                fours = int(record[0])
                sixs = int(record[1])
                balls = int(record[2])
                wickets = int(record[3])
                catches = int(record[4])
                stumping = int(record[5])
                runout = int(record[6])
#                team.close()
                self.AR_Score(runs, fours, sixs, balls, wickets, catches, stumping, runout)
             
            

    def Batting_Score(self, r, fours, sixs, b):
        sco = 0
        sco = r / 2
        
        if r > 50:
            sco += 5
        elif r > 100:
            sco += 10
        if b != 0:
            stRate = (r / b) * 100
            if (stRate >= 80) and (stRate <= 100):
                sco += 2
            if (stRate > 100):
                sco += 4
            for k in range(fours):
                sco += 1
            for l in range(sixs):
                sco += 2
        self.pa.setText('{}'.format(sco))
        Ui_FantasyCricket.scores.append(sco)

    def Cal_Score(self, r, b, w, c, s, ro):
        sc = 0
        o = b // 6
        if o !=0:
            ER = r / o
        else:
            ER = 0
        
        for i in range(0, w):
            sc += 10
            
        if w in (3, 4):
            sc += 5
        elif w >= 5:
            sc += 10
            
        if ER > 3.5 and ER <= 4.5:
            sc += 4
        elif ER >= 2 and ER <= 3.5:
            sc += 7
        elif ER < 2:
            sc += 10

        if ((c != 0) or (s != 0) or (ro != 0)):
            sc += 10

        self.pa.setText('{}'.format(sc))
        Ui_FantasyCricket.scores.append(sc)

    def AR_Score(self, r, f, s, b, w, c, st, ro):
        sco = 0
        sco = r / 2
        
        if r > 50:
            sco += 5
        elif r > 100:
            sco += 10
        if b != 0:
            stRate = (r / b) * 100
            if (stRate >= 80) and (stRate <= 100):
                sco += 2
            if (stRate > 100):
                sco += 4
            for k in range(f):
                sco += 1
            for l in range(s):
                sco += 2

        o = b // 6
        if o != 0:
            ER = r / o
        else:
            ER = 0
        
        for i in range(0, w):
            sco += 10
            
        if w in (3, 4):
            sco += 5
        elif w >= 5:
            sco += 10
            
        if ER > 3.5 and ER <= 4.5:
            sco += 4
        elif ER >= 2 and ER <= 3.5:
            sco += 7
        elif ER < 2:
            sco += 10

        if ((c != 0) or (st != 0) or (ro != 0)):
            sco += 10

        self.pa.setText('{}'.format(sco))
        Ui_FantasyCricket.scores.append(sco)
        
    def alldail(self):
        Dialog_all = QtWidgets.QDialog()
        ui = Ui_Dialog_all()
        ui.setupUi(Dialog_all)
        Dialog_all.show()
        Dialog_all.exec_()
        
    def batdail(self):
        Dialog_bats = QtWidgets.QDialog()
        ui = Ui_Dialog_bat()
        ui.setupUi(Dialog_bats)
        Dialog_bats.show()
        Dialog_bats.exec_()
        
    def bowdail(self):
        Dialog_bow = QtWidgets.QDialog()
        ui = Ui_Dialog_bow()
        ui.setupUi(Dialog_bow)
        Dialog_bow.show()
        Dialog_bow.exec_()
    
    def wkdail(self):
        Dialog_wk = QtWidgets.QDialog()
        ui = Ui_Dialog_wk()
        ui.setupUi(Dialog_wk)
        Dialog_wk.show()
        Dialog_wk.exec_()
        
    def savedail(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_save()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        
    def insertPlayers(self):
        player = []
        for record in range(self.lis.count()):
            player.append(self.lis.item(record).text())
        for index in range(len(player)):
            MyTeam = sqlite3.connect('FanCrickets.db')
            Te = MyTeam.cursor()
            qur = "INSERT into teams (Name, Players, Value) VALUES ('{}', '{}', {});".format(self.tn.text(), player[index], Ui_FantasyCricket.scores[index])
            data = Te.execute(qur)
            MyTeam.commit()
        if (data):
            self.savedail()
            
    def evalteam(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_eval()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        
    def openform(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_openteam()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        
             
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FantasyCricket = QtWidgets.QMainWindow()
    ui = Ui_FantasyCricket()
    ui.setupUi(FantasyCricket)
    FantasyCricket.show()
    sys.exit(app.exec_())
