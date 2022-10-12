import logging
from aplikasi.error_handling import blueprint
from aplikasi.base.controller import *
from flask import session, render_template, redirect, url_for, request



@blueprint.route('/')
@blueprint.route('/error_handling')
def errorHandling():
    return open_page('error_handling.html')
