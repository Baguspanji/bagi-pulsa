import pymysql
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from flask import g, Flask, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch

def req_kontak_cs():
    sql = "SELECT kode_kontak, no_telp FROM kontak_cs"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

def req_kontak_edit(no_telp, kode_kontak):
    sql = "UPDATE kontak_cs SET no_telp=%s where kode_kontak=%s"
    param = (no_telp, kode_kontak)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}

