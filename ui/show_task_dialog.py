# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_task_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 341)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 691, 302))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layout_form = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout_form.setContentsMargins(0, 0, 0, 0)
        self.layout_form.setObjectName("layout_form")
        self.edit_datetime = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_datetime.setReadOnly(True)
        self.edit_datetime.setObjectName("edit_datetime")
        self.layout_form.addWidget(self.edit_datetime, 2, 1, 1, 1)
        self.edit_title = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_title.setReadOnly(True)
        self.edit_title.setObjectName("edit_title")
        self.layout_form.addWidget(self.edit_title, 0, 1, 1, 1)
        self.label_description = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_description.setObjectName("label_description")
        self.layout_form.addWidget(self.label_description, 1, 0, 1, 1)
        self.label_datetime = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_datetime.setObjectName("label_datetime")
        self.layout_form.addWidget(self.label_datetime, 2, 0, 1, 1)
        self.label_title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_title.setObjectName("label_title")
        self.layout_form.addWidget(self.label_title, 0, 0, 1, 1)
        self.edit_description = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.edit_description.setReadOnly(True)
        self.edit_description.setObjectName("edit_description")
        self.layout_form.addWidget(self.edit_description, 1, 1, 1, 1)
        self.image = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMinimumSize(QtCore.QSize(300, 300))
        self.image.setMaximumSize(QtCore.QSize(300, 300))
        self.image.setText("")
        self.image.setObjectName("image")
        self.layout_form.addWidget(self.image, 0, 3, 3, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout_form.addItem(spacerItem, 0, 2, 3, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_description.setText(_translate("Dialog", "Описание"))
        self.label_datetime.setText(_translate("Dialog", "Дата и время"))
        self.label_title.setText(_translate("Dialog", "Название"))
