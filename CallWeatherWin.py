#!/usr/bin/python3
# -*- coding: utf-8 -*-

from cProfile import run
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
        cityName = self.ui.lineEdit.text()
        cityCode = self.transCityName(cityName)

        # 实况天气
        url = 'https://devapi.qweather.com/v7/weather/now'
        params = {
            'location': cityCode,
            'key': '8e54dd30c3f2413f8c5002d067b932ed'
        }
        response = requests.get(url=url, params=params)

        self.ui.textEdit.setText(response.json()['now']['temp'] + ' 度')
        self.ui.textEdit_7.setText(response.json()['now']['text'])
        self.ui.textEdit_11.setText(response.json()['now']['windDir'])
        self.ui.textEdit_12.setText(response.json()['now']['windScale'] + ' 级')
        self.ui.textEdit_13.setText(response.json()['now']['humidity'] + ' %')

        # 生活指数
        url = 'https://devapi.qweather.com/v7/indices/1d'
        params = {
            'location': cityCode,
            'type': '0',
            'key': '8e54dd30c3f2413f8c5002d067b932ed'
        } 
        response = requests.get(url=url, params=params)
        
        self.ui.textEdit_14.setText(response.json()['daily'][0]['category'] + '。' + response.json()['daily'][0]['text'])
        self.ui.textEdit_15.setText(response.json()['daily'][2]['category'] + '。' + response.json()['daily'][2]['text'])
        self.ui.textEdit_16.setText(response.json()['daily'][4]['category'] + '。' + response.json()['daily'][4]['text'])
        self.ui.textEdit_17.setText(response.json()['daily'][8]['category'] + '。' + response.json()['daily'][8]['text'])
        self.ui.textEdit_18.setText(response.json()['daily'][15]['category'] + '。' + response.json()['daily'][15]['text'])


        # 空气质量
        url = 'https://devapi.qweather.com/v7/air/now'
        params = {
            'location': cityCode,
            'key': '8e54dd30c3f2413f8c5002d067b932ed'
        }
        response = requests.get(url=url, params=params)

        self.ui.textEdit_2.setText(response.json()['now']['aqi'])
        self.ui.textEdit_19.setText(response.json()['now']['category'])
        self.ui.textEdit_20.setText(response.json()['now']['primary'])
        self.ui.textEdit_21.setText(response.json()['now']['pm2p5'])
        self.ui.textEdit_22.setText(response.json()['now']['pm10'])

        # 未来天气
        url = 'https://devapi.qweather.com/v7/weather/3d'
        params = {
            'location': cityCode,
            'key': '8e54dd30c3f2413f8c5002d067b932ed'
        }
        response = requests.get(url=url, params=params)

        self.ui.textEdit_3.setText(response.json()['daily'][0]['fxDate'])
        self.ui.textEdit_4.setText(response.json()['daily'][1]['fxDate'])
        self.ui.textEdit_5.setText(response.json()['daily'][2]['fxDate'])
        self.ui.textEdit_6.setText(response.json()['daily'][0]['tempMin'] + '到' + response.json()['daily'][0]['tempMax'] + '度')
        self.ui.textEdit_8.setText(response.json()['daily'][1]['tempMin'] + '到' + response.json()['daily'][1]['tempMax'] + '度')
        self.ui.textEdit_9.setText(response.json()['daily'][2]['tempMin'] + '到' + response.json()['daily'][2]['tempMax'] + '度')
        self.ui.textEdit_25.setText(response.json()['daily'][0]['textDay'])
        self.ui.textEdit_10.setText(response.json()['daily'][1]['textDay'])
        self.ui.textEdit_24.setText(response.json()['daily'][2]['textDay'])
        self.ui.textEdit_23.setText(response.json()['daily'][0]['sunrise'])
        self.ui.textEdit_27.setText(response.json()['daily'][1]['sunrise'])
        self.ui.textEdit_28.setText(response.json()['daily'][2]['sunrise'])
        self.ui.textEdit_26.setText(response.json()['daily'][0]['sunset'])
        self.ui.textEdit_29.setText(response.json()['daily'][1]['sunset'])
        self.ui.textEdit_30.setText(response.json()['daily'][2]['sunset'])
        


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
        self.ui.textEdit.clear()
        self.ui.textEdit_7.clear()
        self.ui.textEdit_11.clear()
        self.ui.textEdit_12.clear()
        self.ui.textEdit_13.clear()
        self.ui.textEdit_14.clear()
        self.ui.textEdit_15.clear()
        self.ui.textEdit_16.clear()
        self.ui.textEdit_17.clear()
        self.ui.textEdit_18.clear()
        self.ui.textEdit_2.clear()
        self.ui.textEdit_19.clear()
        self.ui.textEdit_20.clear()
        self.ui.textEdit_21.clear()
        self.ui.textEdit_22.clear()
        self.ui.textEdit_3.clear()
        self.ui.textEdit_4.clear()
        self.ui.textEdit_5.clear()
        self.ui.textEdit_6.clear()
        self.ui.textEdit_8.clear()
        self.ui.textEdit_9.clear()
        self.ui.textEdit_25.clear()
        self.ui.textEdit_10.clear()
        self.ui.textEdit_24.clear()
        self.ui.textEdit_23.clear()
        self.ui.textEdit_27.clear()
        self.ui.textEdit_28.clear()
        self.ui.textEdit_26.clear()
        self.ui.textEdit_29.clear()
        self.ui.textEdit_30.clear()
        self.ui.lineEdit.clear()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.setObjectName('MainWindow')
    win.setStyleSheet("#MainWindow{border-image:url(images/5fb4be5ead03c1605680734311.jpg);}")
    win.show()
    sys.exit(app.exec_())
