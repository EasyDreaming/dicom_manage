'''
Author: Zhao kf
Date: 2021-01-19 09:51:56
LastEditTime: 2021-01-20 09:26:28
LastEditors: Zhao kf
Description: 
FilePath: /dicom_manage/dicom_server/flask_dicom/login_dicom/__init__.py
'''
from flask_login import LoginManager
from flask_dicom import app

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_dicom.login'
login_manager.login_message = u'进行下一步操作前,需要先登录...'