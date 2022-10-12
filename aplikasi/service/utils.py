import pymysql
import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from flask import g, Flask, json, current_app as app
from aplikasi.utils import db_con, db_exec, db_fetch

def req_service():
    sql = "SELECT id, nama, status FROM service"
    res = db_fetch(sql, None)
    return db_fetch(sql, None)

def req_service_edit(status_service, kode_service):
    sql = "UPDATE service SET status=%s where id=%s"
    param = (status_service, kode_service)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}