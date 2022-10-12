import logging
import uuid
import hashlib
import pymysql
import random
import string
import pandas as pd
import numpy as np
from aplikasi.master import blueprint
import requests
# from aplikasi.posting.utils import req_posting, req_posting_hapus
from aplikasi.base.controller import *
# from aplikasi.apilog.routes import ApiKategoriPosting
from aplikasi.utils import db_con, db_exec, db_fetch
from flask import g, Flask, json, current_app as app
from flask import session, render_template, redirect, url_for, request, jsonify


def login(user, pw):
    # hsl = request.get_json(force=True)
    # user = hsl['user']
    # passw = hsl['passw']
    # print('fff', user )
    post = poster(user, pw)
    message = post.to_dict(orient='records')
    if message == [] or message == None:
        data = {"rc" : "06"}
    else:
        if message[0]['username'] == user and message[0]['password'] == pw:
            session['profil'] = message[0]['username']
            data = {"rc" : "00"}

    return data
    
def role(user, pw):
    post = poster_role(user, pw)
    message = post.to_dict(orient='records')
    if message == [] or message == None:
        data = {"rc" : "06"}
    else:
        data = message
    return data

def poster(user, pw):
    sql = "SELECT id, username, password FROM user_web where (username=%s and password=%s)"
    param = (user, pw)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def poster_role(user, pw):
    sql = "SELECT role FROM user_web where (username=%s and password=%s)"
    param = (user, pw)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

#get_list_rate
@blueprint.route('/list_rate', methods=['GET'])
def rate():
    data_rate = req_rate() 
    message = data_rate.to_dict(orient='records')
    
    if message != []:
        data = {"rc" : "00", "data" : message}
    else:
        data = {"rc" : "06", "rc_desc" : "gagal"}

    return data

def req_rate():
    sql = "SELECT kode_provider, nama_provider, status_provider, logo_provider, nilai_minimal, nilai_maksimal, rate, no_admin FROM data_provider"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)


#get_status_provider
@blueprint.route('/status_provider', methods=['GET'])
def status_provider():
    data_status = req_status_provider() 
    data = data_status.to_dict(orient='records')
    for datas in data:
        if datas['nama_provider'] == 'xl':
            data_xl = {
                "kode_provider" : datas['kode_provider'],
                "logo_provider" : datas['logo_provider'],
                "nama_provider" : datas['nama_provider'],
                "nilai_maksimal" : datas['nilai_maksimal'],
                "nilai_minimal" : datas['nilai_minimal'],
                "no_admin" : datas['no_admin'],
                "rate" : datas['rate'],
                "status_provider" : datas['status_provider']
            }
        if datas['nama_provider'] == 'tri':
            data_tri = {
                "kode_provider" : datas['kode_provider'],
                "logo_provider" : datas['logo_provider'],
                "nama_provider" : datas['nama_provider'],
                "nilai_maksimal" : datas['nilai_maksimal'],
                "nilai_minimal" : datas['nilai_minimal'],
                "no_admin" : datas['no_admin'],
                "rate" : datas['rate'],
                "status_provider" : datas['status_provider']
            }
        if datas['nama_provider'] == 'axis':
            data_axis = {
                "kode_provider" : datas['kode_provider'],
                "logo_provider" : datas['logo_provider'],
                "nama_provider" : datas['nama_provider'],
                "nilai_maksimal" : datas['nilai_maksimal'],
                "nilai_minimal" : datas['nilai_minimal'],
                "no_admin" : datas['no_admin'],
                "rate" : datas['rate'],
                "status_provider" : datas['status_provider']
            }
        if datas['nama_provider'] == 'indosat':
            data_indosat = {
                "kode_provider" : datas['kode_provider'],
                "logo_provider" : datas['logo_provider'],
                "nama_provider" : datas['nama_provider'],
                "nilai_maksimal" : datas['nilai_maksimal'],
                "nilai_minimal" : datas['nilai_minimal'],
                "no_admin" : datas['no_admin'],
                "rate" : datas['rate'],
                "status_provider" : datas['status_provider']
            }
        if datas['nama_provider'] == 'telkomsel':
            data_telkomsel= {
                "kode_provider" : datas['kode_provider'],
                "logo_provider" : datas['logo_provider'],
                "nama_provider" : datas['nama_provider'],
                "nilai_maksimal" : datas['nilai_maksimal'],
                "nilai_minimal" : datas['nilai_minimal'],
                "no_admin" : datas['no_admin'],
                "rate" : datas['rate'],
                "status_provider" : datas['status_provider']
            }

    return {"xl":data_xl, "tri":data_tri, "axis":data_axis, "indosat":data_indosat, "telkomsel":data_telkomsel}

def req_status_provider():
    sql = "SELECT kode_provider, nama_provider, status_provider, logo_provider, nilai_minimal, nilai_maksimal, rate, no_admin FROM data_provider"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)
    
#get_status_service
@blueprint.route('/status_service', methods=['GET'])
def status_service():
    data_status = req_status_service() 
    data = data_status.to_dict(orient='records')
    for datas in data:
        if datas['nama'] == 'chat':
            data_chat = {
                "kode_service" : datas['id'],
                "nama_service" : datas['nama'],
                "status_service" : datas['status']
            }

    return {"chat":data_chat}
    
def req_status_service():
    sql = "SELECT id, nama, status FROM service"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

#get_data_bank
@blueprint.route('/data_bank', methods=['GET'])
def data_bank():
    status = 1
    data_bank = req_data_bank(status) 
    message = data_bank.to_dict(orient='records')
    
    if message != []:
        data = {"rc" : "00", "data" : message}
    else:
        data = {"rc" : "06", "rc_desc" : "gagal"}

    return data

def req_data_bank(status):
    sql = "SELECT kode_bank, nama_bank, logo_bank, status_bank, biaya_bank FROM data_bank where status_bank=%s"
    param = (status,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)


#post_transaksi
@blueprint.route('/post_transaksi', methods=['POST'])
def data_transaksi():
    hsl = request.get_json(force=True)
    no_hp = hsl['no_hp']
    nominal_pulsa = hsl['nominal_pulsa']
    nominal_diterima = hsl['nominal_diterima']
    kode_akun = hsl['kode_akun']
    kode_provider = hsl['kode_provider']
    email_user = hsl['email_user']
    nama_user = hsl['nama_user']
    last_date = hsl['last_date']
    status = 0

    # letters = string.ascii_lowercase
    # kode_transaksi = ''.join(random.choice(letters) for i in range(20))
    kode_transaksi = uuid.uuid4().hex

    data_bank = req_data_bank_post(kode_akun) 
    hsl_data_bank = data_bank.to_dict(orient='records')
    kode_akun = hsl_data_bank[0]['kode_akun']
    nama_bank = hsl_data_bank[0]['nama_bank']
    biaya_bank = hsl_data_bank[0]['biaya_bank']
    atas_nama = hsl_data_bank[0]['atas_nama']
    no_rek_user = hsl_data_bank[0]['no_rek_user']

    data_rate = req_rate_post(kode_provider) 
    hsl_data_rate = data_rate.to_dict(orient='records')
    kode_provider = hsl_data_rate[0]['kode_provider']
    nama_provider = hsl_data_rate[0]['nama_provider']
    logo_provider = hsl_data_rate[0]['logo_provider']
    rate = hsl_data_rate[0]['rate']
    no_admin = hsl_data_rate[0]['no_admin']

    ins_data_transaksi = insert_data_transaksi(kode_transaksi, no_hp, nominal_pulsa, nominal_diterima, kode_akun, nama_bank, biaya_bank, atas_nama, no_rek_user, kode_provider, nama_provider, logo_provider, rate, no_admin, email_user, nama_user, status, last_date)
    # data_transaksi = req_data_transaksi(kode_transaksi)

    # message = data_transaksi.to_dict(orient='records')
    datas = req_data_transaksi(kode_transaksi)
    hasil = datas.to_dict(orient='records')
    message = ins_data_transaksi 

    if message['rc'] == '00':
        data = hasil[0]
    else:
        data = {"rc" : "06", "rc_desc" : "gagal"}

    return data

def req_data_bank_post(kode_akun):
    sql = "SELECT kode_akun, nama_bank, biaya_bank, atas_nama, no_rek_user FROM akun_bank where kode_akun=%s"
    param = (kode_akun,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def req_rate_post(kode_provider):
    sql = "SELECT kode_provider, nama_provider, logo_provider, rate, no_admin FROM data_provider where kode_provider=%s"
    param = (kode_provider,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def req_data_transaksi(kode_transaksi):
    sql = "SELECT kode_transaksi, no_hp, nominal_pulsa, nominal_diterima, kode_provider, nama_provider, logo_provider, rate, no_admin, email_user, nama_user, status, last_date, kode_akun, nama_bank, biaya_bank, atas_nama, no_rek_user FROM history_transaksi where kode_transaksi=%s"
    param = (kode_transaksi,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def insert_data_transaksi(kode_transaksi, no_hp, nominal_pulsa, nominal_diterima, kode_akun, nama_bank, biaya_bank, atas_nama, no_rek_user, kode_provider, nama_provider, logo_provider, rate, no_admin, email_user, nama_user, status, last_date):
    sql = "INSERT INTO history_transaksi (kode_transaksi, no_hp, nominal_pulsa, nominal_diterima, kode_akun, nama_bank, biaya_bank, atas_nama, no_rek_user, kode_provider, nama_provider, logo_provider, rate, no_admin, email_user, nama_user, status, last_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    param=(kode_transaksi, no_hp, nominal_pulsa, nominal_diterima, kode_akun, nama_bank, biaya_bank, atas_nama, no_rek_user, kode_provider, nama_provider, logo_provider, rate, no_admin, email_user, nama_user, status, last_date)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00'}
    return {'rc': '06'}


#get_history_transaksi
@blueprint.route('/history_transaksi', methods=['POST'])
def history_transaksi():
    hsl = request.get_json(force=True)
    email_user = hsl['email_user']
    history_transaksi = req_history_transaksi(email_user) 
    message = history_transaksi.to_dict(orient='records')
    
    if message != []:
        data = {"rc" : "00", "data" : message}
    else:
        data = {"rc" : "06", "rc_desc" : "gagal"}

    return data

def req_history_transaksi(email_user):
    sql = "SELECT kode_transaksi, no_hp, nominal_pulsa, nominal_diterima, kode_akun, nama_bank, biaya_bank, atas_nama, no_rek_user, kode_provider, nama_provider, logo_provider, rate, no_admin, email_user, nama_user, status, DATE_FORMAT(last_date, '%%Y-%%m-%%d %%H:%%i') as last_date FROM history_transaksi where email_user=%s ORDER BY last_date DESC"
    param = (email_user,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)


#post_akun_bank
@blueprint.route('/post_akun_bank', methods=['POST'])
def post_akun_bank():
    hsl = request.get_json(force=True)
    kode_bank = hsl['kode_bank']
    no_rek_user = hsl['no_rek_user']
    atas_nama = hsl['atas_nama']
    email_user = hsl['email_user']
    nama_user = hsl['nama_user']
    last_date = hsl['last_date']

    # letters = string.ascii_lowercase
    # kode_akun = ''.join(random.choice(letters) for i in range(20))
    kode_akun = uuid.uuid4().hex

    data_bank = req_data_bank_get(kode_bank) 
    hsl_data_bank = data_bank.to_dict(orient='records')
    kode_bank = hsl_data_bank[0]['kode_bank']
    nama_bank = hsl_data_bank[0]['nama_bank']
    logo_bank = hsl_data_bank[0]['logo_bank']
    biaya_bank = hsl_data_bank[0]['biaya_bank']

    ins_akun_bank = insert_akun_bank(kode_akun, kode_bank, nama_bank, logo_bank, biaya_bank, atas_nama, no_rek_user, email_user, nama_user, last_date)
    data_akun_bank = req_akun_bank(kode_akun)

    message = data_akun_bank.to_dict(orient='records')

    if message != []:
        data = {"rc" : "00", "data" : message}
    else:
        data = {"rc" : "06", "rc_desc" : "gagal"}

    return data

def req_data_bank_get(kode_bank):
    sql = "SELECT kode_bank, nama_bank, logo_bank, biaya_bank FROM data_bank where kode_bank=%s"
    param = (kode_bank,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def req_akun_bank(kode_akun):
    sql = "SELECT kode_akun, kode_bank, nama_bank, logo_bank, biaya_bank, atas_nama, no_rek_user, email_user, nama_user, last_date FROM akun_bank where kode_akun=%s"
    param = (kode_akun,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def insert_akun_bank(kode_akun, kode_bank, nama_bank, logo_bank, biaya_bank, atas_nama, no_rek_user, email_user, nama_user, last_date):
    sql = "INSERT INTO akun_bank (kode_akun, kode_bank, nama_bank, logo_bank, biaya_bank, atas_nama, no_rek_user, email_user, nama_user, last_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    param=(kode_akun, kode_bank, nama_bank, logo_bank, biaya_bank, atas_nama, no_rek_user, email_user, nama_user, last_date)
    res = db_exec(sql, param)
    return res


#get_akun_bank
@blueprint.route('/get_akun_bank', methods=['POST'])
def get_akun_bank():
    hsl = request.get_json(force=True)
    email_user = hsl['email_user']
    get_akun_bank = req_get_akun_bank(email_user) 
    message = get_akun_bank.to_dict(orient='records')
    
    if message != []:
        data = {"rc" : "00", "data" : message}
    else:
        data = {"rc" : "06", "rc_desc" : "gagal"}

    return data

def req_get_akun_bank(email_user):
    sql = "SELECT kode_akun, kode_bank, nama_bank, logo_bank, biaya_bank, atas_nama, no_rek_user, email_user, nama_user, last_date FROM akun_bank where email_user=%s"
    param = (email_user,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)


#delete_akun_bank
@blueprint.route('/delete_akun_bank', methods=['POST'])
def delete_akun_bank():
    hsl = request.get_json(force=True)
    kode_akun = hsl['kode_akun']
    delete_akun_bank = req_delete_akun_bank(kode_akun) 
    message = delete_akun_bank
    
    if message['rc'] == '00':
        data = {"rc" : "00", "rc_desc" : "berhasil"}
    else:
        data = {"rc" : "06", "rc_desc" : "gagal"}

    return data

def req_delete_akun_bank(kode_akun):
    sql = "DELETE FROM akun_bank WHERE kode_akun=%s"
    param = (kode_akun,)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00'}
    return {'rc': '06'}
    
    
#get_kontak_cs
@blueprint.route('/kontak_cs', methods=['GET'])
def get_kontak_cs():
    get_kontak = req_get_kontak() 
    message = get_kontak.to_dict(orient='records')
    
    if message != []:
        data = {"rc" : "00", "kode_kontak" : message[0]['kode_kontak'], "no_telp" : message[0]['no_telp']}
    else:
        data = {"rc" : "06", "rc_desc" : "gagal"}

    return data

def req_get_kontak():
    sql = "SELECT kode_kontak, no_telp FROM kontak_cs"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)


#get_banner
@blueprint.route('/banner', methods=['GET'])
def get_banner():
    get_banner = req_get_banner() 
    message = get_banner.to_dict(orient='records')
    
    if message != []:
        data = {"rc" : "00", "data" : message}
    else:
        data = {"rc" : "06", "rc_desc" : "gagal"}

    return data

def req_get_banner():
    sql = "SELECT kode_banner, gambar_banner FROM banner"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)
    
@blueprint.route('/bigquery', methods=['GET'])
def get_bigquery():
    url = 'http://localhost/bigquery'
    requests.get(url=url)
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)