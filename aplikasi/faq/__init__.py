from flask import Blueprint

blueprint= Blueprint(
    'faq_blueprint',
    __name__,
    url_prefix='/faq',
    template_folder='templates',
    static_folder='static'
)
