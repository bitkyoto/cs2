from PyQt5.QtWidgets import QTableWidgetItem

from PyQt5 import *


class Ui_MainWindow(object):
    path = "config/matrix2.txt"
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 350, 171, 182))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
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
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(270, 350, 171, 299))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.subjectName = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.subjectName.setObjectName("subjectName")
        self.verticalLayout_2.addWidget(self.subjectName)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
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
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(660, 370, 171, 141))
        self.listWidget.setObjectName("listWidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(850, 370, 151, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(850, 390, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.SaveAs = QtWidgets.QPushButton(self.centralwidget)
        self.SaveAs.setGeometry(QtCore.QRect(850, 440, 151, 28))
        self.SaveAs.setObjectName("SaveAs")
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(850, 480, 151, 28))
        self.load.setObjectName("load")
        self.updatelist = QtWidgets.QPushButton(self.centralwidget)
        self.updatelist.setGeometry(QtCore.QRect(660, 520, 171, 23))
        self.updatelist.setObjectName("updatelist")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.addObject.clicked.connect(self.handler_addObject)
        self.deleteObject.clicked.connect(self.handler_deleteObject)
        self.addSubject.clicked.connect(self.handler_addSubject)
        self.deleteSubject.clicked.connect(self.handler_deleteSubject)
        self.SaveAs.clicked.connect(self.save_handler)
        self.load.clicked.connect(self.load_handler)
        self.updatelist.clicked.connect(self.update_list)
        self.config_table()
        self.update_list()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Имя объекта"))
        self.addObject.setText(_translate("MainWindow", "Добавить"))
        self.deleteObject.setText(_translate("MainWindow", "Удалить"))
        self.label_4.setText(_translate("MainWindow", "Имя субъекта"))
        self.label_5.setText(_translate("MainWindow", "Права субъекта"))
        self.addSubject.setText(_translate("MainWindow", "Добавить / Изменить"))
        self.deleteSubject.setText(_translate("MainWindow", "Удалить"))
        self.label.setText(_translate("MainWindow", "Управление объектом"))
        self.label_2.setText(_translate("MainWindow", "Управление субъектом"))
        self.label_6.setText(_translate("MainWindow", "Имя файла"))
        self.SaveAs.setText(_translate("MainWindow", "Save"))
        self.load.setText(_translate("MainWindow", "Load"))
        self.updatelist.setText(_translate("MainWindow", "Обновить"))

    def save_handler(self):
        filename = self.textEdit.toPlainText()
        self.textEdit.clear()
        with open(self.path, 'r') as firstfile, open(f"config/{filename}", 'w') as secondfile:
            for line in firstfile:
                secondfile.write(line)
        self.update_list()
    def load_handler(self):
        filename = self.listWidget.currentItem()
        if filename is not None and f"config/{filename.text()}" != self.path:
            # Загрузка матрицы из файла. Нужно ли делать её "основной"???
            # self.path = f"config/{filename.text()}"
            # self.config_table()
            with open(self.path, 'w+') as firstfile, open(f"config/{filename.text()}", 'r') as secondfile:
                for line in secondfile:
                    firstfile.write(line)
            self.config_table()

    def update_list(self):
        self.listWidget.clear()
        import os
        files = [f for f in os.listdir("C:/Users/hello/PycharmProjects/cs2/config") if os.path.isfile("C:/Users/hello/PycharmProjects/cs2/config" + "/" + f)]
        print(files)
        self.listWidget.addItems(files)

    def handler_addObject(self):
        obj_name = self.objectInput.toPlainText()
        self.objectInput.clear()
        with open(self.path, "r+") as m:
            content = m.readline().split("|")
            if obj_name not in content[0]:
                content[0] = content[0] + obj_name
            else:
                print(f"add_Object: {obj_name} already exists")
            m.close()
        with open(self.path, "w+") as m:
            content_towrite = "|".join(content)
            print(f"add_Object: Writing {content_towrite} to file")
            m.writelines(content_towrite)
        self.config_table()

    def handler_deleteObject(self):
        obj_name = self.objectInput.toPlainText()
        self.objectInput.clear()
        with open(self.path, "r+") as m:
            content = m.readline().split("|")
            if obj_name in content[0]:
                content[0] = content[0].replace(obj_name, "")
            m.close()
        with open(self.path, "w+") as m:
            content_towrite = "|".join(content)
            print(f"add_Object: Writing {content_towrite} to file")
            m.writelines(content_towrite)
            m.close()
        self.config_table()

    def handler_addSubject(self):
        sub_name = self.subjectName.toPlainText()
        new_rights = self.subjectRights.toPlainText()
        self.subjectName.clear()
        self.subjectRights.clear()
        with open(self.path, "r+") as m:
            content = m.readline().split("|")
            users = [i.split("_")[0] for i in content if i != content[0]]
            print(users)
            if sub_name in users:
                content[users.index(sub_name) + 1] = sub_name + "_" + new_rights
            else:
                content.append(sub_name + "_" + new_rights)
        print(f"add_Subject: Writing {content} to file")
        with open(self.path, "w+") as m:
            content_towrite = "|".join(content)
            print(f"add_Object: Writing {content_towrite} to file")
            m.writelines(content_towrite)
            m.close()
        self.config_table()

    def handler_deleteSubject(self):
        sub_name = self.subjectName.toPlainText()
        new_rights = self.subjectRights.toPlainText()
        self.subjectName.clear()
        self.subjectRights.clear()
        with open(self.path, "r+") as m:
            content = m.readline().split("|")
            users = [i.split("_")[0] for i in content if i != content[0]]
            if sub_name in users:
                print(f"Удаляем {content[users.index(sub_name) + 1]}")
                content.pop(users.index(sub_name) + 1)
            else:
                print(f"delete_Subject: User {sub_name} doesn't exist")
        with open(self.path, "w+") as m:
            content_towrite = "|".join(content)
            print(f"delete_Subject: Writing {content} to file")
            m.writelines(content_towrite)
            m.close()
        self.config_table()

    def config_table(self):
        with open(self.path, "r+") as m:
            print("Opened file")
            content = m.readline().split("|")
            amount_files = len(content[0])
            amount_subjects = len(content) - 1
            filenames = [i for i in content[0]]
            users = [i.split("_")[0] for i in content if i != content[0]]
            self.tableWidget.setColumnCount(amount_files)
            self.tableWidget.setRowCount(amount_subjects)
            self.tableWidget.setHorizontalHeaderLabels(filenames)
            self.tableWidget.setVerticalHeaderLabels(users)
            print("Content of matrix", content)
            for row in range(self.tableWidget.rowCount()):
                for col in range(self.tableWidget.colorCount()):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(""))
            for i in range(1, len(content)):
                user, user_rights = content[i].split("_")
                for sym in user_rights:
                    if sym in filenames:
                        index = filenames.index(sym)
                        self.tableWidget.setItem(users.index(user), index, QTableWidgetItem("+"))
            self.tableWidget.update()
            m.close()

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label_3.setText(_translate("MainWindow", "Имя объекта"))
            self.addObject.setText(_translate("MainWindow", "Добавить"))
            self.deleteObject.setText(_translate("MainWindow", "Удалить"))
            self.label_4.setText(_translate("MainWindow", "Имя субъекта"))
            self.label_5.setText(_translate("MainWindow", "Права субъекта"))
            self.addSubject.setText(_translate("MainWindow", "Добавить / Изменить"))
            self.deleteSubject.setText(_translate("MainWindow", "Удалить"))
            self.label.setText(_translate("MainWindow", "Управление объектом"))
            self.label_2.setText(_translate("MainWindow", "Управление субъектом"))
            self.label_6.setText(_translate("MainWindow", "Имя файла"))
            self.SaveAs.setText(_translate("MainWindow", "Save"))
            self.load.setText(_translate("MainWindow", "Load"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())