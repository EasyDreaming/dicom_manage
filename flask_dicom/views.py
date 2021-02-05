# -*- coding: utf-8 -*-
'''
Author: Zhao kf
Date: 2021-01-18 08:53:23
LastEditTime: 2021-01-19 12:45:06
LastEditors: Zhao kf
Description: 
    Main file to register all the buleprints. 
    Every module should be considered as a buleprint to be added.
FilePath: /dicom_manage/dicom_server/flask_dicom/views.py
'''
from flask_dicom import app
from flask_dicom.login_dicom import login_views
from flask_dicom.main import main_views

# Login module: for validing and managing users.
app.register_blueprint(login_views.login_dicom, url_prefix='/')

# Main module: main views.
app.register_blueprint(main_views.main_dicom, url_prefix='/')
