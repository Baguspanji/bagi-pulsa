from aplikasi.master import blueprint
# from aplikasi.posting.utils import req_posting, req_posting_hapus
from aplikasi.base.controller import *
# from aplikasi.apilog.routes import ApiKategoriPosting
from aplikasi.utils import db_con, db_exec, db_fetch
from flask import g, Flask, json, current_app as app
from flask import session, render_template, redirect, url_for, request, jsonify

def select_role(id):
    sql = "SELECT username, password, role FROM user_web where id=%s"
    param = (id)
    res = db_fetch(sql, param)
    return db_fetch(sql, param)

def edit_role(role, id):
    sql = "UPDATE user_web SET role=%s WHERE id=%s"
    param = (role, id)
    res = db_exec(sql, param)
    if res:
        return {'rc': '00', 'rc_desc': 'Sukses'}
    return {'rc': '06', 'rc_desc': 'Gagal'}
