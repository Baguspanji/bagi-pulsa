import logging
from aplikasi.dashboard import blueprint
from aplikasi.dashboard.utils import req_operator, req_operator_edit
from aplikasi.base.controller import *
from flask import session, render_template, redirect, url_for, request, jsonify

@blueprint.route('/')
def dashboard():
    data = {'menu_active': 'master'}
    layanan = req_operator()
    message = layanan.to_dict(orient='records')

    return open_page('dashboard.html', data=data, message=message)

@blueprint.route('/req', methods=['POST'])
def req_operator_edit_json():
	status_provider=request.form.get('status_provider')
	kode_provider=request.form.get('kode_provider')

	data=req_operator_edit(status_provider, kode_provider)

	return jsonify({'rc':'00','rc_desc':'success','data':data})