# Form implementation generated from reading ui file '/Users/lishizhe/Desktop/公选课/python与深度学习基础/Weather_Project/WeatherWin.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(41, 34, 125, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(174, 31, 68, 41))
        self.okButton.setObjectName("okButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(238, 31, 68, 41))
        self.clearButton.setObjectName("clearButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 10, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 340, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 130, 261, 161))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 10, 31, 18))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 31, 18))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 70, 31, 18))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 100, 31, 18))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 130, 31, 18))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(90, 10, 151, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_7.setGeometry(QtCore.QRect(90, 40, 151, 21))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_11 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_11.setGeometry(QtCore.QRect(90, 70, 151, 21))
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_12.setGeometry(QtCore.QRect(90, 100, 151, 21))
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_13.setGeometry(QtCore.QRect(90, 130, 151, 21))
        self.textEdit_13.setObjectName("textEdit_13")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 40, 401, 261))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 60, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 60, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(20, 120, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 170, 71, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(20, 220, 60, 16))
        self.label_13.setObjectName("label_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_14.setGeometry(QtCore.QRect(100, 10, 291, 41))
        self.textEdit_14.setObjectName("textEdit_14")
        self.textEdit_15 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_15.setGeometry(QtCore.QRect(100, 60, 291, 41))
        self.textEdit_15.setObjectName("textEdit_15")
        self.textEdit_16 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_16.setGeometry(QtCore.QRect(100, 110, 291, 41))
        self.textEdit_16.setObjectName("textEdit_16")
        self.textEdit_17 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_17.setGeometry(QtCore.QRect(100, 160, 291, 41))
        self.textEdit_17.setObjectName("textEdit_17")
        self.textEdit_18 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_18.setGeometry(QtCore.QRect(100, 210, 291, 41))
        self.textEdit_18.setObjectName("textEdit_18")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(40, 370, 261, 171))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(30, 110, 60, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(30, 140, 60, 16))
        self.label_18.setObjectName("label_18")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 20, 111, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_19 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_19.setGeometry(QtCore.QRect(120, 50, 111, 21))
        self.textEdit_19.setObjectName("textEdit_19")
        self.textEdit_20 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_20.setGeometry(QtCore.QRect(120, 80, 111, 21))
        self.textEdit_20.setObjectName("textEdit_20")
        self.textEdit_21 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_21.setGeometry(QtCore.QRect(120, 110, 111, 21))
        self.textEdit_21.setObjectName("textEdit_21")
        self.textEdit_22 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_22.setGeometry(QtCore.QRect(120, 140, 111, 21))
        self.textEdit_22.setObjectName("textEdit_22")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(340, 370, 431, 171))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 10, 104, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_4.setGeometry(QtCore.QRect(200, 10, 104, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_5.setGeometry(QtCore.QRect(310, 10, 104, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(20, 50, 31, 16))
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(10, 80, 60, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setGeometry(QtCore.QRect(10, 110, 60, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setGeometry(QtCore.QRect(10, 140, 60, 16))
        self.label_24.setObjectName("label_24")
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_6.setGeometry(QtCore.QRect(90, 50, 104, 21))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_8 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_8.setGeometry(QtCore.QRect(200, 50, 104, 21))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_9.setGeometry(QtCore.QRect(310, 50, 104, 21))
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_10.setGeometry(QtCore.QRect(200, 80, 104, 21))
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_23 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_23.setGeometry(QtCore.QRect(90, 110, 104, 21))
        self.textEdit_23.setObjectName("textEdit_23")
        self.textEdit_24 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_24.setGeometry(QtCore.QRect(310, 80, 104, 21))
        self.textEdit_24.setObjectName("textEdit_24")
        self.textEdit_25 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_25.setGeometry(QtCore.QRect(90, 80, 104, 21))
        self.textEdit_25.setObjectName("textEdit_25")
        self.textEdit_26 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_26.setGeometry(QtCore.QRect(90, 140, 104, 21))
        self.textEdit_26.setObjectName("textEdit_26")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label_21.setObjectName("label_21")
        self.textEdit_27 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_27.setGeometry(QtCore.QRect(200, 110, 104, 21))
        self.textEdit_27.setObjectName("textEdit_27")
        self.textEdit_28 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_28.setGeometry(QtCore.QRect(310, 110, 104, 21))
        self.textEdit_28.setObjectName("textEdit_28")
        self.textEdit_29 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_29.setGeometry(QtCore.QRect(200, 140, 104, 21))
        self.textEdit_29.setObjectName("textEdit_29")
        self.textEdit_30 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_30.setGeometry(QtCore.QRect(310, 140, 104, 21))
        self.textEdit_30.setObjectName("textEdit_30")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(510, 340, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        Form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请输入城市名称"))
        self.okButton.setText(_translate("Form", "确定"))
        self.clearButton.setText(_translate("Form", "清空"))
        self.label_3.setText(_translate("Form", "生活指数"))
        self.label_4.setText(_translate("Form", "空气质量"))
        self.label.setText(_translate("Form", "温度"))
        self.label_5.setText(_translate("Form", "天气"))
        self.label_6.setText(_translate("Form", "风向"))
        self.label_7.setText(_translate("Form", "风力"))
        self.label_8.setText(_translate("Form", "湿度"))
        self.label_9.setText(_translate("Form", "运动指数"))
        self.label_10.setText(_translate("Form", "穿衣指数"))
        self.label_11.setText(_translate("Form", "紫外线指数"))
        self.label_12.setText(_translate("Form", "感冒指数"))
        self.label_13.setText(_translate("Form", "防晒指数"))
        self.label_2.setText(_translate("Form", "实时天气"))
        self.label_14.setText(_translate("Form", "空气质量指数"))
        self.label_15.setText(_translate("Form", "空气质量等级"))
        self.label_16.setText(_translate("Form", "主要污染物"))
        self.label_17.setText(_translate("Form", "PM2.5"))
        self.label_18.setText(_translate("Form", "PM10"))
        self.label_20.setText(_translate("Form", "温度"))
        self.label_22.setText(_translate("Form", "当日天气"))
        self.label_23.setText(_translate("Form", "日出时间"))
        self.label_24.setText(_translate("Form", "日落时间"))
        self.label_21.setText(_translate("Form", "日期"))
        self.label_19.setText(_translate("Form", "未来3日天气"))
