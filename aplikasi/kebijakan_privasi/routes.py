import logging
from aplikasi.kebijakan_privasi import blueprint
from aplikasi.kebijakan_privasi.utils import req_kebijakan_show, req_kebijakan_edit
from aplikasi.base.controller import *
from flask import session, render_template, redirect, url_for, request, jsonify

@blueprint.route('/', methods=['GET'])
def kebijakan_privasi():
	data = { 'menu_active': 'master'}
	syarat = req_kebijakan_show()
	hasil = syarat.to_dict(orient='records')
	
	b_desk = hasil[0]['deskripsi']
	deskripsi = b_desk.decode("utf-8")
	judul = hasil[0]['judul']
	kode = hasil[0]['kode']

	message = {'deskripsi': deskripsi, 'judul': judul, 'kode': kode}

	return open_page('kebijakan_privasi.html', data=data, message=message)

	
@blueprint.route('/req', methods=['POST'])
def req_kebijakan_edit_json():
	deskripsi=request.form.get('deskripsi')
	kode=request.form.get('kode')

	data=req_kebijakan_edit(deskripsi, kode)

	return jsonify({'rc':'00','rc_desc':'success','data':data})
