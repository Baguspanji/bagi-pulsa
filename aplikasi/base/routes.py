import hashlib
import logging
import json
from flask.json import jsonify
from aplikasi.base import blueprint
from aplikasi.api_media import generate_captcha
# from aplikasi.apilog.routes import ApiLogin, ApiLogout
from aplikasi.master.routes import login, role
from aplikasi.base.controller import req_kebijakan, req_syarat, req_faq
from flask import session, render_template, redirect, url_for, request


@blueprint.route('/')
@blueprint.route('/index')
def route_default():
    # return redirect(url_for('base_blueprint.for_mobile'))

    try:
        # Jika sudah login, arahkan ke dashboard
        if session['loggedin']:
            return redirect(url_for('home_blueprint.index'))
    except Exception:
        pass

    # Jika belum login, paksa user untuk login
    return redirect(url_for('base_blueprint.user_login'))

@blueprint.route('/syarat/<kode>/mobile.htm', methods=['GET'])
def for_syarat(kode):
    mobile = req_syarat(kode)
    data = mobile.to_dict(orient='records')
    b_desk = data[0]['deskripsi']
    convert = b_desk.decode("utf-8")
    message = convert
    
    return render_template('for_mobile/for_mobile.htm', message=message)

@blueprint.route('/kebijakan/<kode>/mobile.htm', methods=['GET'])
def for_kebijakan(kode):
    mobile = req_kebijakan(kode)
    data = mobile.to_dict(orient='records')
    b_desk = data[0]['deskripsi']
    convert = b_desk.decode("utf-8")
    message = convert
    
    return render_template('for_mobile/for_mobile.htm', message=message)
    
@blueprint.route('/faq/<kode>/mobile.htm', methods=['GET'])
def for_faq(kode):
    mobile = req_faq(kode)
    data = mobile.to_dict(orient='records')
    b_desk = data[0]['deskripsi']
    convert = b_desk.decode("utf-8")
    message = convert
    
    return render_template('for_mobile/for_mobile.htm', message=message)

@blueprint.route('/login', methods=['GET', 'POST'])
def user_login():
    message = None
    if request.method == 'POST':
        user = request.form.get('username')
        # session['email'] = email
        pwori = request.form.get('password')
        pw = hashlib.md5(pwori.encode('utf-8')).hexdigest()
        resp_data = login(user, pw)
        data_role = role(user, pw)

        if resp_data['rc'] == '00':
            session['loggedin'] = True
            datas = data_role[0]
            session['data'] = json.loads(datas['role'])
            return redirect(url_for('dashboard_blueprint.dashboard'))
        else:
            message = "Kata Sandi Salah!" 
            
    return render_template('login/login.html', message=message)

@blueprint.route('/logout', methods=['POST'])
def signout():
    session['loggedin'] = False

    return redirect(url_for('base_blueprint.user_login'))
