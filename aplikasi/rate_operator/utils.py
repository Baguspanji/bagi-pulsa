import pymysql
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from flask import g, Flask, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch


def req_rate_operator():
    sql = "SELECT kode_provider, nama_provider, nilai_minimal, nilai_maksimal, rate, no_admin FROM data_provider"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

def show_rate_operator(kode_provider):
    sql = "SELECT kode_provider, nilai_minimal, nilai_maksimal, rate, no_admin FROM data_provider where kode_provider=%s"
    param = (kode_provider,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def req_rate_operator_edit(nilai_minimal, nilai_maksimal, rate, no_admin, kode_provider):
    sql = "UPDATE data_provider SET nilai_minimal=%s, nilai_maksimal=%s, rate=%s, no_admin=%s where kode_provider=%s"
    param = (nilai_minimal, nilai_maksimal, rate, no_admin, kode_provider)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}
