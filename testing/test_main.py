'''
Author: Zhao kf
Date: 2021-01-18 09:51:22
LastEditTime: 2021-01-19 09:45:45
LastEditors: Zhao kf
Description: testing for main.py
FilePath: /dicom_manage/dicom_server/testing/test_main.py
'''
import sys
sys.path.append('../')
from flask_dicom import app
from flask_dicom import views
from flask import url_for, redirect
from testing import *
# import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_main_hello_world(self):
        print(url_for('hello_world'))
        print(redirect(url_for('hello_world')))

    def test_main_login(self):
        print(url_for('login'))
        print(redirect(url_for('login')))

if __name__ == '__main__':
    with app.test_request_context():
        unittest.main()
