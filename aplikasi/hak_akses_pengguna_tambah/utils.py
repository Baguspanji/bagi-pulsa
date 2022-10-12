import pymysql
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from flask import g, Flask, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch

def hak_akses_pengguna_tambah_show():
    sql = "SELECT id, username, password FROM user_web"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

def req_akses_pengguna_tambah(user, password, role):
    sql = "INSERT INTO user_web (username, password, role) VALUES (%s, %s, %s)"
    param = (user, password, role)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}

