import logging
from aplikasi.service import blueprint
from aplikasi.service.utils import req_service, req_service_edit
from aplikasi.base.controller import *
from flask import session, render_template, redirect, url_for, request, jsonify

@blueprint.route('/')
def service():
    data = {'menu_active': 'master'}
    layanan = req_service()
    message = layanan.to_dict(orient='records')

    return open_page('service.html', data=data, message=message)

@blueprint.route('/req', methods=['POST'])
def req_service_edit_json():
	status_service=request.form.get('status_service')
	kode_service=request.form.get('kode_service')

	data=req_service_edit(status_service, kode_service)

	return jsonify({'rc':'00','rc_desc':'success','data':data})