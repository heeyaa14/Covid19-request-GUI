#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

import requests
from bs4 import BeautifulSoup
from PyQt5.QtGui import QFont
import re

class CORONA(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        last_update_label = QLabel("last updated", self)
        last_update_label.setAlignment(Qt.AlignCenter)

        case_number_label = QLabel("확진 : ", self)
        case_number_label.setAlignment(Qt.AlignCenter)

        death_count_label = QLabel("사망 : ", self)
        death_count_label.setAlignment(Qt.AlignCenter)

        recovered_label = QLabel("격리해제 : ", self)
        recovered_label.setAlignment(Qt.AlignCenter)

        # Font settings
        global_font = case_number_label.font()
        global_font.setPointSize(20)
        global_font.setBold(True)
        global_font.setFamily("nanumgothic")

        last_update_font = last_update_label.font()
        last_update_font.setPointSize(10)
        last_update_label.setStyleSheet("Color : grey")

        last_update_label.setFont(last_update_font)
        case_number_label.setFont(global_font)
        death_count_label.setFont(global_font)
        recovered_label.setFont(global_font)

        # COVID-19 Parse
        corona_status = self.parseHTML()

        case_number_label.setText(
            case_number_label.text() + corona_status[0] + "명")  # 확진자 수
        death_count_label.setText(
            death_count_label.text() + corona_status[1] + "명")  # 사망자 수
        recovered_label.setText(
            recovered_label.text() + corona_status[2] + "명")    # 격리해제 수
        last_update_label.setText(corona_status[3])

        # add labels to widgets
        layout = QVBoxLayout()
        layout.addWidget(last_update_label)
        layout.addWidget(case_number_label)
        layout.addWidget(death_count_label)
        layout.addWidget(recovered_label)

        self.setLayout(layout)
        self.setWindowTitle("한국 코로나 바이러스 현황")
        self.setGeometry(400, 400, 400, 300)
        self.show()

    def parseHTML(self):
        corona_status = []

        # 요청받아온 url
        req = requests.get(
            "https://www.worldometers.info/coronavirus/country/south-korea/"
        )
        html = req.text
        soup = BeautifulSoup(html, "html.parser")

        last_update = soup.findAll(text=re.compile("updated"))
        numbers = soup.select("div.maincounter-number > span")

        for txt in numbers:
            corona_status.append(txt.text.strip(" "))   # 띄어쓰기 해제

        corona_status.append(last_update[0])

        return corona_status

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CORONA()
    sys.exit(app.exec_())

