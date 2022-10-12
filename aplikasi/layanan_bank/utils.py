import pymysql
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from flask import g, Flask, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch


def req_layanan_bank():
    sql = "SELECT kode_bank, nama_bank, logo_bank, status_bank, biaya_bank FROM data_bank"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

def req_layanan_bank_edit(status_bank, kode_bank):
    sql = "UPDATE data_bank SET status_bank=%s where kode_bank=%s"
    param = (status_bank, kode_bank)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'} 

def show_layanan_bank(kode_bank):
    sql = "SELECT kode_bank, biaya_bank FROM data_bank where kode_bank=%s"
    param = (kode_bank,)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def send_layanan_bank(biaya_bank, kode_bank):
    sql1 = "UPDATE akun_bank SET biaya_bank=%s where kode_bank=%s"
    param = (biaya_bank, kode_bank)
    res1 = db_exec(sql1, param)
    
    sql = "UPDATE data_bank SET biaya_bank=%s where kode_bank=%s"
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}
