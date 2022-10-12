import logging
from aplikasi.layanan_bank import blueprint
from aplikasi.layanan_bank.utils import req_layanan_bank, req_layanan_bank_edit, send_layanan_bank, show_layanan_bank
from aplikasi.base.controller import *

from flask import session, render_template, redirect, url_for, request, jsonify


@blueprint.route('/', methods=['GET'])
def layanan_bank():
	data = { 'menu_active': 'master'}
	bank = req_layanan_bank()
	message = bank.to_dict(orient='records')

	return open_page('layanan_bank.html', data=data, message=message)

@blueprint.route('/req', methods=['POST'])
def req_bank_edit_json():
	status_bank=request.form.get('status_bank')
	kode_bank=request.form.get('kode_bank')

	data=req_layanan_bank_edit(status_bank, kode_bank)

	return jsonify({'rc':'00','rc_desc':'success','data':data})

@blueprint.route('/send', methods=['POST'])
def biaya_bank_json():
	biaya_bank=request.form.get('biaya_bank')
	kode_bank=request.form.get('kode_bank')
	data=send_layanan_bank(biaya_bank, kode_bank)

	return jsonify({'rc':'00','rc_desc':'success','data':data})

@blueprint.route('/show', methods=['POST'])
def layanan_bank_show_json():
    kode_bank=request.form.get('kode_bank')

    show = show_layanan_bank(kode_bank)
    data = show.to_dict(orient='records')

    return jsonify({'data':data})