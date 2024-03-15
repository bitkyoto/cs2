from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(259, 99, 281, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.userName = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.userName.setObjectName("userName")
        self.verticalLayout.addWidget(self.userName)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.askedRights = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.askedRights.setObjectName("askedRights")
        self.verticalLayout.addWidget(self.askedRights)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.realRights = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.realRights.setReadOnly(True)
        self.realRights.setObjectName("realRights")
        self.verticalLayout.addWidget(self.realRights)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.pushButton.clicked.connect(self.check)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def check(self):
        user = self.userName.toPlainText()
        asked = self.askedRights.toPlainText()
        with open(f"config/matrix2.txt", "r") as m:
            content = m.readline().split("|")
            users = [i.split("_")[0] for i in content if i != content[0]]
            print(users)
            if user in users:
                final = "".join([sym for sym in asked if (sym in content[users.index(user)+1] and sym in content[0])])
                self.realRights.setText(final)
            else:
                self.realRights.setText("User not found!")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите имя"))
        self.label_2.setText(_translate("MainWindow", "Введите запрашиваемы права"))
        self.label_3.setText(_translate("MainWindow", "Ваши реальные права"))
        self.pushButton.setText(_translate("MainWindow", "Проверить"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())