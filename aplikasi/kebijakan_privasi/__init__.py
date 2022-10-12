from flask import Blueprint

blueprint= Blueprint(
    'kebijakan_privasi_blueprint',
    __name__,
    url_prefix='/kebijakan_privasi',
    template_folder='templates',
    static_folder='static'
)
