#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui

# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName('天气预报')

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName('Form')
        Form.resize(800, 600)
        # self.groupBox = QtWidgets.QGroupBox(Form)
        # self.groupBox.setGeometry(QtCore.QRect(10, 10, 431, 251))
        # self.groupBox.setObjectName('groupbox')
        # self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        # self.lineEdit.setGeometry(QtCore.QRect(10, 20, 100, 200))
        self.lineEdit.setObjectName('lineEdit')
        # self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText = QtWidgets.QTextEdit(Form)
        self.resultText.setGeometry(QtCore.QRect(10, 60, 411, 181))
        self.resultText.setObjectName('resultText')
        # self.label = QtWidgets.QLabel(self.groupBox)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 72, 21))
        self.label.setObjectName('label')
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(90, 300, 93, 28))
        self.okButton.setObjectName('okButton')
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setGeometry(QtCore.QRect(20, 30, 93, 28))
        self.clearButton.setObjectName('clearButton')

        self.retranslateUi(Form)
        self.okButton.clicked.connect(Form.queryWeather)
        self.clearButton.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate('Form', '天气预报'))
        # self.groupBox.setTitle(_translate('Form', '查询城市天气'))
        self.label.setText(_translate('Form', '城市'))
        self.okButton.setText(_translate('Form', '查询'))
        self.clearButton.setText(_translate('Form', '清空'))
