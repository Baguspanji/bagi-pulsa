import pymysql
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from flask import g, Flask, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch

def req_banner():
    sql = "SELECT kode_banner, gambar_banner FROM banner"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

def req_banner_edit(gambar_banner, kode_banner):
    sql = "UPDATE banner SET gambar_banner=%s where kode_banner=%s"
    param = (gambar_banner, kode_banner)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}