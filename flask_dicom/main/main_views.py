'''
Author: Zhao kf
Date: 2021-01-19 10:32:23
LastEditTime: 2021-01-20 15:03:53
LastEditors: Zhao kf
Description: 
FilePath: /dicom_manage/dicom_server/flask_dicom/main/main_views.py
'''
from flask import Blueprint, render_template
from flask_login import login_required
from flask_dicom.login_dicom.login_views import login_dicom

main_dicom = Blueprint('main_dicom', __name__)

@main_dicom.route('/', methods=['GET', 'POST'])    
@main_dicom.route('/index')
@login_required
def index():
    return render_template('main/index.html')

@main_dicom.route('/message', methods=['GET', 'POST'])
@login_required
def message():
    return "message to users"

@main_dicom.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    return "search results"
