import logging
from aplikasi.kontak_cs import blueprint
from aplikasi.kontak_cs.utils import req_kontak_cs, req_kontak_edit
from aplikasi.base.controller import *
from flask import session, render_template, redirect, url_for, request, jsonify

@blueprint.route('/', methods=['GET'])
def kontak_cs():
	data = { 'menu_active': 'master'}
	kontak = req_kontak_cs()
	message = kontak.to_dict(orient='records')

	return open_page('kontak_cs.html', data=data, message=message[0])

	
@blueprint.route('/req', methods=['POST'])
def req_kontak_edit_json():
	no_telp=request.form.get('no_telp')
	kode_kontak=request.form.get('kode_kontak')

	data=req_kontak_edit(no_telp, kode_kontak)

	return jsonify({'rc':'00','rc_desc':'success','data':data})
