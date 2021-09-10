
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mysql.connector
class Ui_Highscore(object):
    global mydb
    mydb = mysql.connector.connect(user='root', password='wildfactor', host='127.0.0.1',port=3306,database='tron',
    auth_plugin='mysql_native_password')
    global mycursor
    mycursor = mydb.cursor()
    def exit(self):
        sys.exit(0)
    def BackButton(self):
        from TronMainboard import Ui_MainWindow
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 581)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.063, x2:0, y2:1, stop:0 rgba(0, 0, 105, 159), stop:1 rgba( 0,0 121, 174));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -50, 911, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("TronSlika.jpg"))
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 470, 141, 61))
        self.pushButton_6.clicked.connect(self.BackButton)
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_6.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"font: 12pt \"Agency FB\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 470, 141, 61))
        self.pushButton_7.clicked.connect(self.exit)
        self.pushButton_7.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"font: 12pt \"Agency FB\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 611, 321))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:white;\n"
"font: 10pt \"Agency FB\";")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 50, 501, 31))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"Agency FB\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Highscore"))
        self.pushButton_6.setText(_translate("MainWindow", "Back"))
        self.pushButton_7.setText(_translate("MainWindow", "Exit"))
        sql = ("SELECT name,points FROM highscore ORDER BY points DESC")
        mycursor.execute(sql)
        i = mycursor.fetchall()
        i = ','.join(str(o) for o in i)
        i = i.replace("(","")
        i = i.replace(")","")
        i = i.replace(",","\n")
        i = i.replace("'","")
        i = i.replace("[","")
        i = i.replace("]","")
        value = (f"\n{i}\n")
        self.label_2.setText(_translate("MainWindow", value))
        
        self.label_3.setText(_translate("MainWindow", "HIGH SCORE"))
