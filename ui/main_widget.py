# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 262, 641))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_groups = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_groups.setObjectName("label_groups")
        self.verticalLayout.addWidget(self.label_groups)
        self.list_groups = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.list_groups.setViewMode(QtWidgets.QListView.ListMode)
        self.list_groups.setUniformItemSizes(False)
        self.list_groups.setWordWrap(False)
        self.list_groups.setSelectionRectVisible(False)
        self.list_groups.setObjectName("list_groups")
        self.verticalLayout.addWidget(self.list_groups)
        self.btn_createGroup = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_createGroup.setObjectName("btn_createGroup")
        self.verticalLayout.addWidget(self.btn_createGroup)
        self.btn_editGroup = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_editGroup.setObjectName("btn_editGroup")
        self.verticalLayout.addWidget(self.btn_editGroup)
        self.btn_deleteGroup = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_deleteGroup.setObjectName("btn_deleteGroup")
        self.verticalLayout.addWidget(self.btn_deleteGroup)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_prompt = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_prompt.setObjectName("label_prompt")
        self.verticalLayout.addWidget(self.label_prompt)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(290, 10, 721, 641))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_groupTitle = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_groupTitle.setText("")
        self.label_groupTitle.setObjectName("label_groupTitle")
        self.verticalLayout_2.addWidget(self.label_groupTitle)
        self.edit_groupDescription = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.edit_groupDescription.setText("")
        self.edit_groupDescription.setReadOnly(True)
        self.edit_groupDescription.setObjectName("edit_groupDescription")
        self.verticalLayout_2.addWidget(self.edit_groupDescription)
        spacerItem1 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_addTask = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_addTask.setObjectName("btn_addTask")
        self.horizontalLayout_2.addWidget(self.btn_addTask)
        self.btn_editTask = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_editTask.setObjectName("btn_editTask")
        self.horizontalLayout_2.addWidget(self.btn_editTask)
        self.btn_deleteTask = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_deleteTask.setObjectName("btn_deleteTask")
        self.horizontalLayout_2.addWidget(self.btn_deleteTask)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.btn_addManyTasks = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_addManyTasks.setObjectName("btn_addManyTasks")
        self.verticalLayout_2.addWidget(self.btn_addManyTasks)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.check_favorite = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.check_favorite.setObjectName("check_favorite")
        self.horizontalLayout_5.addWidget(self.check_favorite)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.list_tasks = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.list_tasks.setObjectName("list_tasks")
        self.verticalLayout_2.addWidget(self.list_tasks)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_copyTasks = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_copyTasks.setObjectName("btn_copyTasks")
        self.horizontalLayout_3.addWidget(self.btn_copyTasks)
        self.btn_copyDates = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_copyDates.setObjectName("btn_copyDates")
        self.horizontalLayout_3.addWidget(self.btn_copyDates)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_groups.setText(_translate("MainWindow", "Группы"))
        self.btn_createGroup.setText(_translate("MainWindow", "Создать группу"))
        self.btn_editGroup.setText(_translate("MainWindow", "Редактировать группу"))
        self.btn_deleteGroup.setText(_translate("MainWindow", "Удалить группу"))
        self.label_prompt.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Подсказка<br/>Доступен двойной клик по группе/задаче</p></body></html>"))
        self.btn_addTask.setText(_translate("MainWindow", "Добавить задачу"))
        self.btn_editTask.setText(_translate("MainWindow", "Редактировать задачу"))
        self.btn_deleteTask.setText(_translate("MainWindow", "Удалить задачу"))
        self.btn_addManyTasks.setText(_translate("MainWindow", "Добавить несколько задач"))
        self.check_favorite.setText(_translate("MainWindow", "В избранном"))
        self.btn_copyTasks.setText(_translate("MainWindow", "Скопировать задачи"))
        self.btn_copyDates.setText(_translate("MainWindow", "Скопировать задачи (только дата и время)"))