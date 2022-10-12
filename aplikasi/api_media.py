import os
import shutil
import hashlib
import requests
from flask import current_app as app


def generate_captcha():
    """
        Generate Captcha
        Menghasilkan link captcha dan text captcha nya
    """
    height, width = 80, 80
    url = f"{app.config['MEDIA_HANDLER_HOST']}/get_captcha/{height}/{width}"
    headers = {'Content-Type': 'application/json'}
    ret = requests.get(url, headers=headers)
    ret = ret.json()
    if ret['rc'] == '00':
        text_capcha = ret['text']
        print(f">>> Text Captcha = {text_capcha}")
        link_capcha = ret['links']
        hash_captcha = hashlib.md5(text_capcha.encode('utf-8')).hexdigest()

        # download gambar captcha ke folder lokal
        r = requests.get(link_capcha, stream=True)
        if r.status_code == 200:
            base = os.path.abspath(os.path.dirname(__file__))
            path = f"{base}/base/static/assets/img/captcha"
            nama_file = f"{path}/{hash_captcha}.jpg"
            with open(nama_file, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            return hash_captcha
