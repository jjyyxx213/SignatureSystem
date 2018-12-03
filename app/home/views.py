# -*- coding:utf-8 -*-
from . import home
from flask import render_template, request, current_app
from qrcode import QRCode, constants

@home.route('/', methods=['GET'])
def index():
    return render_template('home/index.html')

@home.route('/qrcode/add', methods=['GET'])
def add_qrcode():
    data = request.args.get('data', 'www.baidu.com?a=1234&b=4567')
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        image_factory=None,
        mask_pattern=None
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    path = current_app.config['USER_UPLOAD_DIR'] + 'x.png'
    assert img.save(path)
    return 'ok'

