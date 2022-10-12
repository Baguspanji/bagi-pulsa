from flask import Blueprint

blueprint= Blueprint(
    'hak_akses_pengguna_edit_blueprint',
    __name__,
    url_prefix='/hak_akses_pengguna_edit',
    template_folder='templates',
    static_folder='static'
)
