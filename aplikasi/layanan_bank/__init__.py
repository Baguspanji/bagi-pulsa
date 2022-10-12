from flask import Blueprint

blueprint= Blueprint(
    'layanan_bank_blueprint',
    __name__,
    url_prefix='/layanan_bank',
    template_folder='templates',
    static_folder='static'
)
