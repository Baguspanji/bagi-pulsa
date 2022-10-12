import logging
from aplikasi.hak_akses_pengguna_edit import blueprint
from aplikasi.base.sidebar import menuList
from aplikasi.base.controller import *
# from aplikasi.apilog.routes import ApiHakAkses
from aplikasi.hak_akses_pengguna_edit.utils import select_role, edit_role
from flask import session, render_template, redirect, url_for, request, jsonify


@blueprint.route('/', methods=['GET', 'POST'])
def hak_akses_pengguna_edit():
	data = { 'menu_active': 'master'}
	message = menuList()[0]['item']

	return open_page('hak_akses_pengguna_edit.html', data=data, message=message)

@blueprint.route('/put', methods=['POST'])
def put_role_user():
	message = None
	data = request.form
	result = data.to_dict()
	id = result['id']
	datas = result['role']
	role = datas
	message = edit_role(role, id)

	return message

@blueprint.route('/req', methods=['GET'])
def get_data_role_user():
	id = request.args["kode"]
	syarat = select_role(id)
	hasil = syarat.to_dict(orient='records')
	role = hasil[0]
	message = {'roles':[role]}

	return jsonify(message)

