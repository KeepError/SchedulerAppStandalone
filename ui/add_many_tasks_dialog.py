# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_many_tasks_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(623, 503)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(11, 11, 601, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layout_form = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout_form.setContentsMargins(0, 0, 0, 0)
        self.layout_form.setObjectName("layout_form")
        self.layout_startDate = QtWidgets.QHBoxLayout()
        self.layout_startDate.setObjectName("layout_startDate")
        self.edit_date = QtWidgets.QDateEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_date.sizePolicy().hasHeightForWidth())
        self.edit_date.setSizePolicy(sizePolicy)
        self.edit_date.setObjectName("edit_date")
        self.layout_startDate.addWidget(self.edit_date)
        self.edit_time = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_time.sizePolicy().hasHeightForWidth())
        self.edit_time.setSizePolicy(sizePolicy)
        self.edit_time.setObjectName("edit_time")
        self.layout_startDate.addWidget(self.edit_time)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_startDate.addItem(spacerItem)
        self.layout_form.addLayout(self.layout_startDate, 0, 1, 1, 1)
        self.label_weekDays = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_weekDays.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_weekDays.setObjectName("label_weekDays")
        self.layout_form.addWidget(self.label_weekDays, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.layout_form.addItem(spacerItem1, 3, 0, 1, 2)
        self.label_tasks = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_tasks.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_tasks.setObjectName("label_tasks")
        self.layout_form.addWidget(self.label_tasks, 2, 0, 1, 1)
        self.label_startDate = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_startDate.setObjectName("label_startDate")
        self.layout_form.addWidget(self.label_startDate, 0, 0, 1, 1)
        self.edit_tasks = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.edit_tasks.setObjectName("edit_tasks")
        self.layout_form.addWidget(self.edit_tasks, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.layout_form.addWidget(self.label, 6, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.layout_form.addItem(spacerItem2, 7, 0, 1, 2)
        self.label_info = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_info.setStyleSheet("QLabel {\n"
"color: rgb(255, 53, 53);\n"
"}")
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.layout_form.addWidget(self.label_info, 9, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.layout_form.addItem(spacerItem3, 1, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.layout_form.addItem(spacerItem4, 5, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layout_form.addWidget(self.buttonBox, 10, 0, 1, 2)
        self.layout_weekDays = QtWidgets.QGridLayout()
        self.layout_weekDays.setObjectName("layout_weekDays")
        self.btn_deleteWeekDay = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_deleteWeekDay.sizePolicy().hasHeightForWidth())
        self.btn_deleteWeekDay.setSizePolicy(sizePolicy)
        self.btn_deleteWeekDay.setObjectName("btn_deleteWeekDay")
        self.layout_weekDays.addWidget(self.btn_deleteWeekDay, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_weekDays.addItem(spacerItem5, 1, 2, 1, 1)
        self.list_weekDays = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.list_weekDays.setObjectName("list_weekDays")
        self.layout_weekDays.addWidget(self.list_weekDays, 0, 0, 1, 3)
        self.btn_addWeekDay = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addWeekDay.sizePolicy().hasHeightForWidth())
        self.btn_addWeekDay.setSizePolicy(sizePolicy)
        self.btn_addWeekDay.setObjectName("btn_addWeekDay")
        self.layout_weekDays.addWidget(self.btn_addWeekDay, 1, 0, 1, 1)
        self.layout_form.addLayout(self.layout_weekDays, 4, 1, 1, 1)
        self.label_remark = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_remark.setObjectName("label_remark")
        self.layout_form.addWidget(self.label_remark, 8, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.edit_date.setDisplayFormat(_translate("Dialog", "dd.MM.yyyy"))
        self.edit_time.setDisplayFormat(_translate("Dialog", "HH:mm"))
        self.label_weekDays.setText(_translate("Dialog", "Дни недели *"))
        self.label_tasks.setText(_translate("Dialog", "<html><head/><body><p>Задачи *</p></body></html>"))
        self.label_startDate.setText(_translate("Dialog", "Начальная дата"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>Важно: Каждое название задачи пишется с новой строки<br>            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Задачи создаются в том же порядке, в каком были добавлены дни недели</p></body></html>"))
        self.btn_deleteWeekDay.setText(_translate("Dialog", "Удалить"))
        self.btn_addWeekDay.setText(_translate("Dialog", "Добавить"))
        self.label_remark.setText(_translate("Dialog", "* Обязательно к заполнению"))
