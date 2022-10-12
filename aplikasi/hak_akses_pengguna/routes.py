import logging
import hashlib
from aplikasi.hak_akses_pengguna import blueprint
from aplikasi.hak_akses_pengguna.utils import hak_akses_show, show_hak_akses_pengguna, req_hak_akses_edit, req_hak_akses_edit_user
from aplikasi.base.controller import *
from flask import session, render_template, redirect, url_for, request, jsonify

@blueprint.route('/', methods=['GET'])
def hak_akses_pengguna():
	data = { 'menu_active': 'master'}
	syarat = hak_akses_show()
	hasil = syarat.to_dict(orient='records')

	message = hasil

	return open_page('hak_akses_pengguna.html', data=data, message=message)
	
@blueprint.route('/req', methods=['POST'])
def hak_akses_edit_json():
	username=request.form.get('username')
	pw=request.form.get('password')
	id=request.form.get('id')
	
	result = hashlib.md5(pw.encode())
	password = result.hexdigest()

	data=req_hak_akses_edit(username, password, id)
	return data

@blueprint.route('/req_user', methods=['POST'])
def hak_akses_edit_user_json():
	username=request.form.get('username')
	id=request.form.get('id')

	data=req_hak_akses_edit_user(username, id)
	return data

@blueprint.route('/show', methods=['POST'])
def hak_akses_show_json():
    id=request.form.get('id')

    hasil = show_hak_akses_pengguna(id)
    data = hasil.to_dict(orient='records')

    return jsonify({'data':data})