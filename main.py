#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 03:31:14 2020

@author: kictakimuhabirsincap
"""
from bs4 import BeautifulSoup
import requests

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

r = requests.get('https://erasmus.sakarya.edu.tr/tr/duyuru/goruntule/liste')
source = BeautifulSoup(r.content,"lxml")

duyurular = source.find_all("h5",attrs={"class":"event-title"})


sendable = ''
for duyuru in duyurular:
    sendable = sendable + '\n' +duyuru.text


print(sendable)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('LOGINMAIL', '********')

server.sendmail('FROM', 'WHERE', sendable.encode(encoding='UTF-8',errors='strict'))