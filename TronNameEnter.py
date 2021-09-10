
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import sys
import time
class Ui_NameEnter(object):
    global mydb
    mydb = mysql.connector.connect(user='root', password='wildfactor', host='127.0.0.1',port=3306,database='tron',
    auth_plugin='mysql_native_password')
    global mycursor
    mycursor = mydb.cursor()
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 161, 31))
        self.label_2.setStyleSheet("background-color: rgb(37, 142, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 290, 161, 31))
        self.label_3.setStyleSheet("background-color: rgb(37, 142, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 171, 161, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 360, 161, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 430, 201, 71))
        self.pushButton.clicked.connect(self.Entry)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton.setStyleSheet("background-color: rgb(37, 142, 255);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "PLAYER ONE:NAME"))
        self.label_3.setText(_translate("MainWindow", "PLAYER TWO "))
        self.lineEdit.setText(_translate("MainWindow", ""))
        self.lineEdit_2.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "START"))
    def Entry(self):
        name1  = self.lineEdit.text()
        name2 = self.lineEdit_2.text()

        print(name1)
        print(name2)
        sqlDEL1 = ("DELETE FROM imena")
        mycursor.execute(sqlDEL1)
        sql = (" INSERT INTO imena (name1,name2) VALUES (%s,%s)")
        val = (name1,name2) 
        mycursor.execute(sql,val)
        mydb.commit()
        time.sleep(1)
        sql = ("SELECT name FROM highscore")
        mycursor.execute(sql)
        a = mycursor.fetchall()
        a = ','.join(str(o) for o in a)
        a = a.replace("(","")
        a = a.replace(")","")
        a = a.replace(",","")
        a = a.replace("'","")
        a = a.replace("[","")
        a = a.replace("]","")
        names = str(a)
        if name1  not in names:
            sql = (" INSERT INTO highscore(name) VALUE (%s)")
            val = (name1,)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            pass
        if name2 not in names:
            sql = (" INSERT INTO highscore(name) VALUE (%s)")
            val = (name2,)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            pass

        from TronLoadingScreen import Ui_LoadingScreen
        self.aplikacijaLoadingScreen = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self.window)
        self.window.show()