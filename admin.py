from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 21, 891, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 350, 171, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.objectInput = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.objectInput.setObjectName("objectInput")
        self.verticalLayout.addWidget(self.objectInput)
        self.addObject = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addObject.setObjectName("addObject")
        self.verticalLayout.addWidget(self.addObject)
        self.deleteObject = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteObject.setObjectName("deleteObject")
        self.verticalLayout.addWidget(self.deleteObject)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(270, 350, 171, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.subjectName = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.subjectName.setObjectName("subjectName")
        self.verticalLayout_2.addWidget(self.subjectName)
        self.subjectRights = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.subjectRights.setObjectName("subjectRights")
        self.verticalLayout_2.addWidget(self.subjectRights)
        self.addSubject = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addSubject.setObjectName("addSubject")
        self.verticalLayout_2.addWidget(self.addSubject)
        self.deleteSubject = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.deleteSubject.setObjectName("deleteSubject")
        self.verticalLayout_2.addWidget(self.deleteSubject)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 330, 171, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 330, 171, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.addObject.clicked.connect(self.handler_addObject)
        self.deleteObject.clicked.connect(self.handler_deleteObject)
        self.addSubject.clicked.connect(self.handler_addSubject)
        self.deleteSubject.clicked.connect(self.handler_deleteSubject)
        self.configure_table()
        self.tableWidget.setSortingEnabled(False)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addObject.setText(_translate("MainWindow", "Добавить"))
        self.deleteObject.setText(_translate("MainWindow", "Удалить"))
        self.addSubject.setText(_translate("MainWindow", "Добавить / Изменить"))
        self.deleteSubject.setText(_translate("MainWindow", "Удалить"))
        self.label.setText(_translate("MainWindow", "Управление объектом"))
        self.label_2.setText(_translate("MainWindow", "Управление субъектом"))
    def configure_table(self):
        with open("matrix.txt", "r+") as m:
            print("Successfully opened file")
            filenames = ""
            matrix = []
            for count, line in enumerate(m):
                line = line.replace("\n", "")
                if count == 0:
                    matrix.append(line)
                    line = line.split(" ")
                    filenames = line
                    #line[-1] = line[-1].replace("\n", '')
                    amount_files = len(line)
                else:
                    matrix.append(line)
            self.tableWidget.setColumnCount(amount_files)
            self.tableWidget.setRowCount(count)
            self.tableWidget.setHorizontalHeaderLabels(filenames)
            self.tableWidget.setVerticalHeaderLabels([i.split(" ")[0] for i in matrix if i != matrix[0]])
            res = []
            for rights in matrix:
                res.append(rights.replace('\n', ''))
            print("Content of matrix", res)
            matrix = res
            m.close()
        self.configure_rights(matrix, filenames)
    def configure_rights(self, matrix, filenames):
        users = [i.split(" ")[0] for i in matrix if i != matrix[0]]
        for i in range(1, len(matrix)):
            user = matrix[i].split(" ")[0]
            user_rights = matrix[i].split(" ")[1]
            print(user, user_rights)
            for sym in user_rights:
                if sym in filenames:
                    index = filenames.index(sym)
                    self.tableWidget.setItem(users.index(user), index, QTableWidgetItem("+"))
                else:
                    print(f"File '{sym}' doesn't exist")
        self.tableWidget.update()
    def handler_addObject(self):
        with open("matrix.txt", "r+") as m:
            content = m.readlines()
            obj_name = self.objectInput.toPlainText()
            self.objectInput.clear()
            if obj_name not in content[0]:
                content[0] = content[0].replace("\n", f" {obj_name}\n")
                m.seek(0,0)
                m.writelines(content)
        self.configure_table()

    def handler_addSubject(self):
        sub_name = self.subjectName.toPlainText()
        new_rights = self.subjectRights.toPlainText()
        with open("matrix.txt", "r+") as m:
            f_line = m.readline()
            all_lines = m.readlines()
            all_names = [x.split(" ")[0] for x in all_lines]
            if sub_name in all_names:
                all_lines[all_names.index(sub_name)] = sub_name + " " + new_rights + "\n"
                cont = [f_line] + all_lines
                m.seek(0)
                m.writelines(cont)
            else:
                all_lines.append(sub_name + " " + new_rights + "\n")
                cont = [f_line] + all_lines
                m.seek(0,0)
                m.writelines(cont)
            print(cont)
        self.configure_table()
    def handler_deleteSubject(self):
        pass
    def handler_deleteObject(self):
        with open("matrix.txt", "r+") as m:
            f_line = m.readline()
            all_lines = m.readlines()
            obj_name = self.objectInput.toPlainText()
            self.objectInput.clear()
            if obj_name in f_line:
                f_line = f_line.replace(f" {obj_name}", "")
                m.seek(0)
                m.writelines([f_line]+all_lines)
                print(f"Writing {[f_line]+all_lines}")
                m.seek(0,0)
                print(f"Reading {m.readlines()}")
        self.configure_table()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())