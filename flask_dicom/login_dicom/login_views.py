'''
Author: Zhao kf
Date: 2021-01-19 09:53:14
LastEditTime: 2021-01-20 09:26:43
LastEditors: Zhao kf
Description: Login views 
FilePath: /dicom_manage/dicom_server/flask_dicom/login_dicom/login_views.py
'''
from flask_dicom.login_dicom import login_manager
from flask_dicom.dbuser_dicom import model
from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_required, login_user, logout_user

login_dicom = Blueprint('login_dicom', __name__)

@login_manager.user_loader
def load_user(user_id):
    return model.User.query.get(user_id)

@login_dicom.route('/login', methods=['GET', 'POST'])
def login():
    """valid and login the user.
    """
    error_info = u'请登录...'
    if request.method == 'POST':
        user_name = request.form.get('username')
        user_password = request.form.get('password')
        remember_me = request.form.get('remember_me')
    else:
        user_name = request.args.get('username')
        user_password = request.args.get('password')
        remember_me = request.args.get('remember_me')
    
    if user_name and user_password :
        user2log = model.User.query.filter_by(user_name=user_name).first()
        if user2log and user2log.verify_password(user_password):
            if remember_me:
                remember_me = True
            else:
                remember_me = False
            login_user(user2log, remember=remember_me)
            return redirect(url_for('main_dicom.index'))
        else:
            error_info = u'账号或密码不正确...'
    return render_template('login_dicom/login.html', error_info=error_info)
    

@login_dicom.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_dicom.login'))
