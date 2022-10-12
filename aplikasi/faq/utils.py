import pymysql
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from flask import g, Flask, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch

def req_faq_show():
    sql = "SELECT kode, judul, deskripsi, link FROM faq"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

def req_faq_edit(deskripsi, kode):
    sql = "UPDATE faq SET deskripsi=%s where kode=%s"
    param = (deskripsi, kode)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}

