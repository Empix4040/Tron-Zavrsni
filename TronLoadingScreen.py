
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import mysql.connector
import random

class Ui_LoadingScreen(object):
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
        self.label_2.setGeometry(QtCore.QRect(30, 340, 800, 31))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.963, y1:0.920455, x2:1, y2:1, stop:0 rgba(89, 182, 182, 1), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"Agency FB\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(160, 390, 571, 23))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("background-color: rgb(255,0,255);")
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(100)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def handleTimer(self):
        value = self.progressBar.value()
        if value < 100:
            value = value + 1
            self.progressBar.setValue(value)
        else:
            self.timer.stop()
            from game import tron,music
            music()
            tron()

            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tips"))
        sql = ("SELECT facts FROM facts")
        mycursor.execute(sql)
        
        values = mycursor.fetchall()
        lista  = []
        for value in values:
            value = ','.join(str(o) for o in value)
            value = value.replace("(","")
            value = value.replace(")","")
            value = value.replace(",","")
            value = value.replace("'","")
            value = value.replace("[","")
            value = value.replace("]","")
            lista.append(value)

            
        self.label_2.setText(_translate("MainWindow",random.choice(lista)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoadingScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
