#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_Weather import Ui_MainWindow
import requests

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def queryWeather(self):
        print('  queryWeather  ')
        cityName = self.ui.lineEdit.text()
        cityCode = self.transCityName(cityName)

        url = 'https://devapi.qweather.com/v7/weather/now'
        params = {
            'location': cityCode,
            'key': '8e54dd30c3f2413f8c5002d067b932ed'
        }
        response = requests.get(url=url, params=params)

        self.ui.lineEdit_2.setText(response.json()['now']['temp'])
        self.ui.lineEdit_3.setText(response.json()['now']['text'])

    def transCityName(self, cityName):
        cityCode = ''
        url = 'https://geoapi.qweather.com/v2/city/lookup'
        params = {
            'location': cityName,
            'key': '8e54dd30c3f2413f8c5002d067b932ed'
        }
        response = requests.get(url=url, params=params)
        cityCode = response.json()['location'][0]['id']
        
        return cityCode

    def clearResult(self):
        print('  clearResult  ')
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
