# -*- coding: utf-8 -*-
'''
Author: Zhao kf
Date: 2021-01-18 08:53:57
LastEditTime: 2021-01-19 09:30:06
LastEditors: Zhao kf
Description: 
    Running this python file to start the application.
FilePath: /dicom_manage/dicom_server/run.py
'''

from flask_dicom import app

if __name__ == '__main__':
#    db.create_all()
    app.run('0.0.0.0',port=13004,debug=True)
