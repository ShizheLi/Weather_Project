#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from WeatherWin import Ui_Form
import requests

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def queryWeather(self):
        print('  queryWeather  ')
        cityName = self.ui.weatherComboBox.currentText()
        cityCode = self.transCityName(cityName)

        url = 'https://devapi.qweather.com/v7/weather/now'
        params = {
            'location': cityCode,
            'key': '8e54dd30c3f2413f8c5002d067b932ed'
        }
        response = requests.get(url=url, params=params)
        print(response.json())

        msg1 = '温度: %s' % response.json()['now']['temp'] + '\n'
        msg2 = '天气: %s' % response.json()['now']['text'] + '\n'
        msg3 = '风向: %s' % response.json()['now']['windDir'] + '\n'
        result = msg1 + msg2 + msg3

        self.ui.resultText.setText(result)

    def transCityName(self, cityName):
        cityCode = ''
        if cityName == '北京':
            cityCode = '101010100'
        elif cityName == '天津':
            cityCode = '101030100'
        elif cityName == '上海':
            cityCode = '101020100'
        
        return cityCode

    def clearResult(self):
        print('  clearResult  ')
        self.ui.resultText.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
