#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName('Form')
        Form.resize(800, 600)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 50, 110, 20))
        self.lineEdit.setObjectName('lineEdit')
        self.resultText = QtWidgets.QTextEdit(Form)
        self.resultText.setGeometry(QtCore.QRect(40, 110, 240, 150))
        self.resultText.setObjectName('resultText')
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 50, 100, 20))
        self.label.setObjectName('label')
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(300, 40, 70, 30))
        self.okButton.setObjectName('okButton')
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setGeometry(QtCore.QRect(300, 100, 70, 30))
        self.clearButton.setObjectName('clearButton')
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(600, 50, 60, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(500, 80, 251, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 360, 60, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(50, 410, 291, 151))
        self.textEdit_3.setObjectName("textEdit_3")

        self.retranslateUi(Form)
        self.okButton.clicked.connect(Form.queryWeather)
        self.clearButton.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate('Form', '天气预报'))
        self.label.setText(_translate('Form', '城市'))
        self.okButton.setText(_translate('Form', '查询'))
        self.clearButton.setText(_translate('Form', '清空'))
        self.label_2.setText(_translate("Form", "实时天气"))
        self.label_3.setText(_translate("Form", "生活指数"))
        self.label_4.setText(_translate("Form", "空气质量"))




