import logging
from aplikasi.rate_operator import blueprint
from aplikasi.rate_operator.utils import req_rate_operator, req_rate_operator_edit, show_rate_operator
from aplikasi.base.controller import *

from flask import session, render_template, redirect, url_for, request, jsonify


@blueprint.route('/', methods=['GET'])
def rate_operator():
	data = { 'menu_active': 'master'}
	operator = req_rate_operator()
	message = operator.to_dict(orient='records')

	return open_page('rate_operator.html', data=data, message=message)

@blueprint.route('/req', methods=['POST'])
def rate_operator_edit_json():
    nilai_minimal=request.form.get('nilai_minimal')
    nilai_maksimal=request.form.get('nilai_maksimal')
    rate=request.form.get('rate')
    no_admin=request.form.get('no_admin')
    kode_provider=request.form.get('kode_provider')

    data=req_rate_operator_edit(nilai_minimal, nilai_maksimal, rate, no_admin, kode_provider)

    return jsonify({'rc':'00','rc_desc':'success','data':data})

@blueprint.route('/show', methods=['POST'])
def rate_operator_show_json():
    kode_provider=request.form.get('kode_provider')

    rate = show_rate_operator(kode_provider)
    data = rate.to_dict(orient='records')

    return jsonify({'data':data})
