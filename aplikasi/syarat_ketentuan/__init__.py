from flask import Blueprint

blueprint= Blueprint(
    'syarat_ketentuan_blueprint',
    __name__,
    url_prefix='/syarat_ketentuan',
    template_folder='templates',
    static_folder='static'
)
