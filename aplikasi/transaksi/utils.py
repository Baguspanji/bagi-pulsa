import pymysql
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from flask import g, Flask, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch


def req_transaksi():
    sql = "SELECT kode_transaksi, no_hp, nominal_pulsa, kode_akun, nama_bank, no_rek_user, email_user, nama_user, status, last_date FROM history_transaksi ORDER BY last_date DESC"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

def req_transaksi_edit(status, kode_transaksi):
    sql = "UPDATE history_transaksi SET status=%s where kode_transaksi=%s"
    param = (status, kode_transaksi)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}

# def req_posting_hapus(id):

#     sql = "DELETE FROM mst_posting WHERE id = %s"
#     param = (id)
#     res = db_exec(sql, param)
#     if res:
#         return {'rc': '00', 'rc_desc': 'Sukses'}
#     return {'rc': '06', 'rc_desc': 'Gagal'}


