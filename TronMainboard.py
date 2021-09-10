from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
from TronHighscore import Ui_Highscore
from TronResolution import Ui_Resolution
from TronNameEnter import Ui_NameEnter

class Ui_MainWindow(object):
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
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(60, 370, 141, 61))
        self.Exit.clicked.connect(self.ExitButton)
        self.Exit.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"font: 12pt \"Agency FB\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.Exit.setObjectName("Exit")
        self.Resolution = QtWidgets.QPushButton(self.centralwidget)
        self.Resolution.setGeometry(QtCore.QRect(60, 270, 141, 61))
        self.Resolution.clicked.connect(self.ResolutionFun)
        self.Resolution.clicked.connect(MainWindow.close)
        self.Resolution.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"font: 12pt \"Agency FB\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.Resolution.setObjectName("Resolution")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(60, 100, 141, 61))
        self.Play.clicked.connect(self.PlayFun)
        self.Play.clicked.connect(MainWindow.close)
        self.Play.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"font: 12pt \"Agency FB\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.Play.setObjectName("Play")
        self.Highscore = QtWidgets.QPushButton(self.centralwidget)
        self.Highscore.setGeometry(QtCore.QRect(60, 180, 141, 61))
        self.Highscore.clicked.connect(self.HighscoreFun)
        self.Highscore.clicked.connect(MainWindow.close)
        self.Highscore.setStyleSheet("background-color: rgb(35, 134, 255);\n"
"font: 12pt \"Agency FB\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: rgb(28, 43, 255);\n"
"padding: 4px;")
        self.Highscore.setObjectName("Highscore")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 50, 331, 51))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"text-decoration: underline;\n"
"font: 75 25pt \"Agency FB\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tron: Legacy"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.Resolution.setText(_translate("MainWindow", "Resolution"))
        self.Play.setText(_translate("MainWindow", "Play"))
        self.Highscore.setText(_translate("MainWindow", "Highscore"))
        self.label_2.setText(_translate("MainWindow", "Tron Legacy"))

    
    def PlayFun(self):
        self.aplikacijaPlay = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NameEnter()
        self.ui.setupUi(self.window)
        self.window.show()
    def HighscoreFun(self):
        self.aplikacijaHighscore= QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Highscore()
        self.ui.setupUi(self.window)
        self.window.show()
    def ResolutionFun(self):
        self.aplikacijaResolution= QtWidgets.QApplication(sys.argv)
        self.window= QtWidgets.QMainWindow()
        self.ui = Ui_Resolution()
        self.ui.setupUi(self.window)
        self.window.show()

    def ExitButton(self):
        sys.exit()
        
if  __name__ == "__main__":
        import sys
        aplikacija = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window)
        window.show()
        sys.exit(aplikacija.exec_())