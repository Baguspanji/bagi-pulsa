import uuid
import pandas as pd
import pymysql
from werkzeug.wrappers import BaseRequest
from werkzeug.wsgi import responder
from werkzeug.exceptions import HTTPException, NotFound
from imaplib import IMAP4_SSL
from flask import session, g, Flask, render_template, redirect, url_for, request, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch
from aplikasi.base.sidebar import menuList


def req_syarat(kode):
    sql = "SELECT judul, deskripsi, kode FROM syarat_ketentuan where kode = %s"
    param = (kode,) 
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def req_kebijakan(kode):
    sql = "SELECT judul, deskripsi, kode FROM kebijakan_privasi where kode = %s"
    param = (kode,) 
    res = db_fetch(sql, param)
    return db_fetch(sql, param)
    
def req_faq(kode):
    sql = "SELECT judul, deskripsi, kode FROM faq where kode = %s"
    param = (kode,) 
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def open_page(url,data=None, message=None, respon=None):
    
    if 'loggedin' in session :
        if session['loggedin'] == True:
            try:
                return render_template(url, menuList=menuList(),data=data, message=message, respon=respon)
            except Exception as e:
                print(e)
                return render_template('error_handling.html',data={'url':url,'error':e})
        else:
            return redirect(url_for('base_blueprint.user_login'))

    return redirect(url_for('base_blueprint.user_login'))

def jsonResponse(result):
    # result = result.to_json(orient="records")
    # parsed = json.loads(result)
    # return parsed
    return result.to_dict(orient='records') 


def logout():
    session['loggedin'] = False
    session['uid'] = ''
    session['profil'] = ''
    return True
