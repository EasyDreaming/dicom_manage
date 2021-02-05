# -*- coding: utf-8 -*-
'''
Author: Zhao kf
Date: 2021-01-18 08:28:52
LastEditTime: 2021-01-19 13:06:41
LastEditors: Zhao kf
Description: 
    Data models used in applications. If a data model should be added,  it should be added in this file.
FilePath: /dicom_manage/dicom_server/flask_dicom/dbuser_dicom/model.py
'''

from datetime import datetime
from flask_dicom.dbuser_dicom import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


user_length = 64
data_item_length = 64
passwd_length = 256
history_item_length = 128
text_type_db = str

class User(db.Model, UserMixin):
    '''
        User table: for recording users.
    '''
    __tablename__ = 'FlaskUser'
    uid = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(user_length), unique=True)
    password_hash = db.Column(db.String(passwd_length))
     
    def __init__(self, user_name: str, password: str):
        '''
        description: Adding new user.
        param :
            user_name:  
            password:
        return : None
        '''
        self.user_name = user_name
        self.password_hash = generate_password_hash(password)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password: str):
        '''
        description: Update the password.
        param :
            password:
        return : None
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def get_id(self) -> text_type_db:
        try:
            return text_type_db(self.uid)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    @property
    def id(self) -> int:
        return self.uid

    def __repr__(self):
        return '''
        <User item>
        <User %r>
        ''' % (self.user_name)

class History(db.Model):
    '''
        History table: for recording history of every operation of every user.
    '''
    __tablename__ = "History"
    uid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(user_length))
    data_item = db.Column(db.String(data_item_length))                  # name of database.
    history_item = db.Column(db.String(history_item_length))            # what operations the user do.
    operation_date = db.Column(db.DateTime())                           
    
    def __init__(self, user_id: int, user_name: str, data_item: str, history_item: str, operation_date: str =None):
        self.user_id = user_id
        self.user_name = user_name
        self.data_item = data_item
        self.history_item = history_item
        if operation_date is None:
            operation_date = datetime.now()
        if not isinstance(operation_date, datetime):
            raise AttributeError('operation date must be an isinstance of datetime')
        self.operation_date = operation_date

    @property
    def id(self) -> int:
        return self.uid

    @property
    def userid(self) -> int:
        return self.user_id

    @property
    def username(self) -> str:
        return self.user_name

    @property
    def dataitem(self) -> str:
        """
        docstring
        """
        return self.data_item
    
    def get_id(self) -> text_type_db:
        try:
            return text_type_db(self.uid)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __repr__(self):
        return '''
        <History item>
        <History id %r>
        <History user_id %r>
        <History user_name %r>
        <History data_item %r>
        <History history_item %r>
        <History operation_date %r>
        ''' % (
            self.uid,
            self.user_id,
            self.user_name,
            self.data_item,
            self.history_item,
            self.operation_date
            )
