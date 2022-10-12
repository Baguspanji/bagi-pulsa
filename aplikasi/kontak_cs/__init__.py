from flask import Blueprint

blueprint= Blueprint(
    'kontak_cs_blueprint',
    __name__,
    url_prefix='/kontak_cs',
    template_folder='templates',
    static_folder='static'
)
