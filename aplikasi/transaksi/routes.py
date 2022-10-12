import logging
from aplikasi.transaksi import blueprint
from aplikasi.transaksi.utils import req_transaksi, req_transaksi_edit
from aplikasi.base.controller import *
from datetime import datetime
# from aplikasi.apilog.routes import ApiKategoriPosting
from flask import session, render_template, redirect, url_for, request, jsonify


@blueprint.route('/', methods=['GET'])
def transaksi():
	data = {'menu_active': 'master'}
	transaksi = req_transaksi()
	message = transaksi.to_dict(orient='records')

	for hasil in message:
		date_time = hasil['last_date'].strftime("%d %B %Y %H:%M")
		hasil['last_date'] = date_time

	return open_page('transaksi.html', data=data, message=message)

@blueprint.route('/req', methods=['POST'])
def req_transaksi_edit_json():
	status=request.form.get('status')
	kode_transaksi=request.form.get('kode_transaksi')

	data=req_transaksi_edit(status, kode_transaksi)

	return jsonify({'rc':'00','rc_desc':'success','data':data})