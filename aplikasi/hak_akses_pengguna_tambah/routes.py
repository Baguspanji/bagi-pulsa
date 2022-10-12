import logging
import string
import hashlib
import random
from aplikasi.hak_akses_pengguna_tambah import blueprint
from aplikasi.hak_akses_pengguna_tambah.utils import req_akses_pengguna_tambah
from aplikasi.base.sidebar import menuList
from aplikasi.base.controller import *
from flask import session, render_template, redirect, url_for, request, jsonify

@blueprint.route('/', methods=['GET'])
def hak_akses_pengguna_tambah():
	# syarat = hak_akses_show()
	# hasil = syarat.to_dict(orient='records')
	
	# b_desk = hasil[0]['deskripsi']
	# deskripsi = b_desk.decode("utf-8")
	# judul = hasil[0]['judul']
	# kode = hasil[0]['kode']

	# message = hasil
	message = menuList()[0]['item']
	return open_page('hak_akses_pengguna_tambah.html', message=message)

	
@blueprint.route('/req', methods=['POST'])
def req_hak_akses_pengguna_tambah():
	user=request.form.get('user')
	role=request.form.get('role')
	pw=request.form.get('pw')
	result = hashlib.md5(pw.encode())
	password = result.hexdigest()

	data=req_akses_pengguna_tambah(user, password, role)

	return data
