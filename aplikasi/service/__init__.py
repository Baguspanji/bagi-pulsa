from flask import Blueprint

blueprint= Blueprint(
    'service_blueprint',
    __name__,
    url_prefix='/service',
    template_folder='templates',
    static_folder='static'
)
