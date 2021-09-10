
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import sys

class Ui_Resolution(object):
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.ResolutionOne)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 141, 61))
        self.pushButton.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"text-decoration: underline;\n"
"font: 8pt \"Old English Text MT\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 130, 141, 61))
        self.pushButton_2.clicked.connect(self.ResolutionTwo)
        self.pushButton_2.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"text-decoration: underline;\n"
"font: 8pt \"Old English Text MT\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 210, 141, 61))
        self.pushButton_3.clicked.connect(self.ResolutionThree)
        self.pushButton_3.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"text-decoration: underline;\n"
"font: 8pt \"Old English Text MT\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 290, 141, 61))
        self.pushButton_4.clicked.connect(self.ResolutionFour)
        self.pushButton_4.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"text-decoration: underline;\n"
"font: 8pt \"Old English Text MT\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 370, 141, 61))
        self.pushButton_5.clicked.connect(self.Fullscreen)
        self.pushButton_5.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"text-decoration: underline;\n"
"font: 12pt \"Agency FB\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.pushButton_5.setObjectName("pushButton_5")
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
        self.pushButton_7.clicked.connect(self.ExitButton)
        self.pushButton_7.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"font: 12pt \"Agency FB\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resolution"))
        self.pushButton.setText(_translate("MainWindow", "1900x1000"))
        self.pushButton_2.setText(_translate("MainWindow", "1200x1000"))
        self.pushButton_3.setText(_translate("MainWindow", "800x800"))
        self.pushButton_4.setText(_translate("MainWindow", "800x600"))
        self.pushButton_5.setText(_translate("MainWindow", "Fullscreen"))
        self.pushButton_6.setText(_translate("MainWindow", "Back"))
        self.pushButton_7.setText(_translate("MainWindow", "Exit"))


    def ExitButton(self):
        sys.exit()
        
    def ResolutionOne(self):
        list1 = [1900,1200,800,1920]
        list2 = [1080,800,600,1080]
        for width, height in zip(list1, list2):
            sql = ("DELETE FROM main WHERE width=%s OR height=%s")
            val = (width, height)
            mycursor.execute(sql, val)
            mydb.commit()
        width = 1900
        height = 1080
        sql = ("INSERT INTO  main (width,height) VALUES ((%s),(%s))")
        val = (width, height)
        mycursor.execute(sql,val)
        mydb.commit()

    def ResolutionTwo(self):
        list1 = [1900,1200,800,800,1920]
        list2 = [1080,1080,800,600,1080]
        sql = ("DELETE FROM main WHERE width IS NULL")
        mycursor.execute(sql)
        sql = ("DELETE FROM main WHERE height IS NULL")
        mycursor.execute(sql)
        for width, height in zip(list1, list2):
            sql = ("DELETE FROM main WHERE width=%s OR height=%s")
            val = (width, height)
            print(width, height)
            mycursor.execute(sql, val)
            mydb.commit()
        width = 1200
        height = 1080
        sql = ("INSERT INTO  main (width,height) VALUES ((%s),(%s))")
        val = (width, height)
        mycursor.execute(sql,val)
        mydb.commit()
    def ResolutionThree(self):
        list1 = [1900,1200,800,1920]
        list2 = [1080,800,600,1080]
        for width, height in zip(list1, list2):
            sql = ("DELETE FROM main WHERE width=%s OR height=%s")
            val = (width, height)
            print(width, height)
            mycursor.execute(sql, val)
            mydb.commit()
        width = 800
        height = 800
        sql = ("INSERT INTO  main (width,height) VALUES ((%s),(%s))")
        val = (width, height)
        mycursor.execute(sql,val)
        mydb.commit()
    def ResolutionFour(self):
        list1 = [1900,1200,800,1920]
        list2 = [1080,800,600,1080]
        for width, height in zip(list1, list2):
            sql = ("DELETE FROM main WHERE width=%s OR height=%s")
            val = (width, height)
            print(width, height)
            mycursor.execute(sql, val)
            mydb.commit()
        width = 800
        height = 600
        sql = ("INSERT INTO  main (width,height) VALUES ((%s),(%s))")
        val = (width, height)
        mycursor.execute(sql,val)
        mydb.commit()
    def Fullscreen(self):
        list1 = [1900,1200,800,1920]
        list2 = [1080,800,600,1080]
        for width, height in zip(list1, list2):
            sql = ("DELETE FROM main WHERE width=%s AND height=%s")
            val = (width, height)
            print(width, height)
            mycursor.execute(sql, val)
            mydb.commit()
        import tkinter as tk
        root = tk.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        print(width, height)
        sql = ("INSERT INTO  main (width,height) VALUES ((%s),(%s))")
        val = (width, height)
        mycursor.execute(sql,val)
        mydb.commit()