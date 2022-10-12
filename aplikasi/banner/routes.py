import logging
import os
from aplikasi.banner import blueprint
from aplikasi.banner.utils import req_banner
from aplikasi.base.controller import *
from flask import session, render_template, redirect, url_for, request, jsonify

@blueprint.route('/')
def banner():
    data = {'menu_active': 'master'}
    banner = req_banner()
    message = banner.to_dict(orient='records')

    return open_page('banner.html', data=data, message=message)

@blueprint.route('/req1', methods=['POST'])
def req_banner_edit_json1():
    kode_banner='th8ewoi945j'
    os.remove(os.path.join("aplikasi/base/static/assets/images", str(kode_banner)+'.jpg'))
    hasilfile = request.files['file']
    hasilfile.filename = str(kode_banner)+'.jpg'
    # file1 = hasilfile.filename
    # os.path.join("aplikasi", hasilfile.filename)
    hasilfile.save(os.path.join("aplikasi/base/static/assets/images", hasilfile.filename))

    return jsonify({'rc':'00','rc_desc':'success'})

@blueprint.route('/req2', methods=['POST'])
def req_banner_edit_json2():
    kode_banner='hjd345mgy760'
    os.remove(os.path.join("aplikasi/base/static/assets/images", str(kode_banner)+'.jpg'))
    hasilfile = request.files['file']
    hasilfile.filename = str(kode_banner)+'.jpg'
    # file1 = hasilfile.filename
    # os.path.join("aplikasi", hasilfile.filename)
    hasilfile.save(os.path.join("aplikasi/base/static/assets/images", hasilfile.filename))

    return jsonify({'rc':'00','rc_desc':'success'})

@blueprint.route('/req3', methods=['POST'])
def req_banner_edit_json3():
    kode_banner='klop295qwerty'
    os.remove(os.path.join("aplikasi/base/static/assets/images", str(kode_banner)+'.jpg'))
    hasilfile = request.files['file']
    hasilfile.filename = str(kode_banner)+'.jpg'
    # file1 = hasilfile.filename
    # os.path.join("aplikasi", hasilfile.filename)
    hasilfile.save(os.path.join("aplikasi/base/static/assets/images", hasilfile.filename))

    return jsonify({'rc':'00','rc_desc':'success'})