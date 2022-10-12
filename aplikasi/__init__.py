import os
import yaml
import logging
import logging.config
from flask import g, Flask
from flask_cors import CORS
from importlib import import_module
from konfigurasi.config import Config


def register_extension(app):
    CORS(app)


def register_logging(app):
    with open('konfigurasi/logging.yaml', 'r') as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)
        f.close()


def register_blueprint(app):
    """
        Semua folder yang merupakan module harus memiliki file __init__.py
    """
    base = os.path.abspath(os.path.dirname(__file__))
    listdir = [n for n in os.listdir(base) if os.path.isdir(f"{base}/{n}")]

    for modul in listdir:
        try:
            m = import_module(f"aplikasi.{modul}.routes")
            app.register_blueprint(m.blueprint)
        except ModuleNotFoundError:
            continue


def middleware(app):
    # @app.before_request
    # def validasi_login():
    #     if 'loggedin' not in session \
    #             and request.endpoint != 'base_blueprint.user_login':
    #         return redirect(url_for('base_blueprint.user_login'))

    @app.after_request
    def after_request(response):
        response.headers['Cache-Control'] = 'public, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        return response

    @app.teardown_appcontext
    def close_db(error):
        """ Paksa tutup koneksi database bila ada """
        if hasattr(g, 'db_rekonsiliasi'):
            g.db_rekonsiliasi.close()
        if hasattr(g, 'db_ppob'):
            g.db_ppob.close()
        if hasattr(g, 'db_admin'):
            g.db_admin.close()


def create_app(config=Config):
    app = Flask(__name__, static_folder='base/static')
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config.from_object(Config)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # inisialisasi extension
    register_extension(app)
    # inisialisasi logging
    register_logging(app)
    # inisialisasi semua blueprint
    register_blueprint(app)
    # inisialisasi middleware
    middleware(app)
    return app
