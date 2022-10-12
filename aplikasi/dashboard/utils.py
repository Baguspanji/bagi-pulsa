import pymysql
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from flask import g, Flask, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch

def req_operator():
    sql = "SELECT kode_provider, nama_provider, status_provider, logo_provider FROM data_provider"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

def req_operator_edit(status_provider, kode_provider):
    sql = "UPDATE data_provider SET status_provider=%s where kode_provider=%s"
    param = (status_provider, kode_provider)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}