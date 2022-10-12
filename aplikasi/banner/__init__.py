from flask import Blueprint

blueprint= Blueprint(
    'banner_blueprint',
    __name__,
    url_prefix='/banner',
    template_folder='templates',
    static_folder='static'
)
