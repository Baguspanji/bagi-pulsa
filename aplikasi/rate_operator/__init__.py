from flask import Blueprint

blueprint= Blueprint(
    'rate_operator_blueprint',
    __name__,
    url_prefix='/rate_operator',
    template_folder='templates',
    static_folder='static'
)
