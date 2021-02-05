# -*- coding: utf-8 -*-
'''
Author: Zhao kf
Date: 2021-01-18 08:53:09
LastEditTime: 2021-01-19 13:13:13
LastEditors: Zhao kf
Description: 
    Running this python file to generate database tables.
FilePath: /dicom_manage/dicom_server/create_db.py
'''

from flask_dicom.dbuser_dicom import model, db
from datetime import datetime

if __name__== '__main__':
    "Drop all tables"
    db.drop_all()
    "Create all tables"
    db.create_all()
    "Add to two users"
    db.session.add(model.User('test1','test1'))
    db.session.commit()
    db.session.add(model.User('test2','test2'))
    db.session.commit()
    "Add history item"
    db.session.add(model.History(1,'test1',model.User.__name__,'testing',datetime.now()))
    db.session.commit()

