# -*- coding: utf-8 -*-
'''
Author: Zhao kf
Date: 2021-01-18 08:54:14
LastEditTime: 2021-01-19 12:31:09
LastEditors: Zhao kf
Description: 
FilePath: /dicom_manage/dicom_server/flask_dicom/__init__.py
'''

from flask import Flask

app = Flask(__name__)

app.secret_key = '123456+sault'

from flask_dicom.dbuser_dicom import model
from flask_dicom import views