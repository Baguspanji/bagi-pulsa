from flask import Blueprint

blueprint= Blueprint(
    'transaksi_blueprint',
    __name__,
    url_prefix='/transaksi',
    template_folder='templates',
    static_folder='static'
)
