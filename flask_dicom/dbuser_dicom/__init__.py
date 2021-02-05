'''
Author: Zhao kf
Date: 2021-01-19 09:51:12
LastEditTime: 2021-01-19 12:32:54
LastEditors: Zhao kf
Description: 
    All databases of information of users and their operations should be modeled here.
FilePath: /dicom_manage/dicom_server/flask_dicom/dbuser_dicom/__init__.py
'''
from flask_sqlalchemy import SQLAlchemy
from flask_dicom import app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbuser:123456POST@127.0.0.1:5432/flask_dicom'
# If more than one database are needed, then adding it here.
SQLALCHEMY_BINDS = {

}

db = SQLAlchemy(app)