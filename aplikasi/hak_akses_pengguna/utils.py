import pymysql
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from flask import g, Flask, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch

def hak_akses_show():
    sql = "SELECT id, username, password FROM user_web"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

def show_hak_akses_pengguna(id):
    sql = "SELECT id, username FROM user_web where id=%s"
    param = (id,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def req_hak_akses_edit(username, password, id):
    sql = "UPDATE user_web SET username=%s, password=%s where id=%s"
    param = (username, password, id)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}

def req_hak_akses_edit_user(username, id):
    sql = "UPDATE user_web SET username=%s where id=%s"
    param = (username, id)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}
