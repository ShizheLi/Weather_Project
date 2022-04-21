#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from WeatherWin import Ui_Form
# from Ui_WeatherWin import Ui_Form
import requests

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def queryWeather(self):
        print('  queryWeather  ')
        cityName = self.ui.lineEdit.text()
        # cityName = self.ui.weatherComboBox.currentText()
        cityCode = self.transCityName(cityName)

        url = 'https://devapi.qweather.com/v7/weather/now'
        params = {
            'location': cityCode,
            'key': '8e54dd30c3f2413f8c5002d067b932ed'
        }
        response = requests.get(url=url, params=params)
        # print(response.json())

        msg0 = '更新时间: %s' % response.json()['updateTime'] + '\n'
        msg1 = '温度: %s' % response.json()['now']['temp'] + '度' + '\n'
        msg2 = '天气: %s' % response.json()['now']['text'] + '\n'
        msg3 = '风向: %s' % response.json()['now']['windDir'] + '\n'
        msg4 = '风力: %s' % response.json()['now']['windScale'] + '级' + '\n'
        msg5 = '湿度: %s' % response.json()['now']['humidity'] + '%' + '\n'
        result = msg0 + msg1 + msg2 + msg3 + msg4 + msg5

        self.ui.resultText.setText(result)

        url = 'https://devapi.qweather.com/v7/indices/1d'
        params = {
            'location': cityCode,
            'type': '0',
            'key': '8e54dd30c3f2413f8c5002d067b932ed'
        } 
        response = requests.get(url=url, params=params)

        msg1 = '运动指数: %s' % response.json()['daily'][0]['category'] + '， ' + response.json()['daily'][0]['text'] + '\n'
        msg2 = '穿衣指数: %s' % response.json()['daily'][2]['category'] + '\n'
        msg3 = '紫外线指数: %s' % response.json()['daily'][4]['category'] + '\n'
        msg4 = '感冒指数: %s' % response.json()['daily'][8]['category'] + '\n'
        msg5 = '防晒指数: %s' % response.json()['daily'][15]['category'] + '\n'
        result = msg1 + msg2 + msg3 + msg4 + msg5
        # print(response.json())

        self.ui.textEdit_2.setText(result)

        url = 'https://devapi.qweather.com/v7/air/now'
        params = {
            'location': cityCode,
            'key': '8e54dd30c3f2413f8c5002d067b932ed'
        }
        response = requests.get(url=url, params=params)

        msg1 = '空气质量指数: %s' % response.json()['now']['aqi'] + '\n'
        msg2 = '空气质量等级: %s' % response.json()['now']['category'] + '\n'
        msg3 = 'PM2.5: %s' % response.json()['now']['pm2p5'] + '\n'
        msg4 = 'PM10: %s' % response.json()['now']['pm10'] + '\n'
        result = msg1 + msg2 + msg3 + msg4

        self.ui.textEdit_3.setText(result)

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
        self.ui.resultText.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
