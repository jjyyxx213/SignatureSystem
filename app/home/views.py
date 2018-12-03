# -*- coding:utf-8 -*-
from . import home
from flask import render_template, request
from qrcode import QRCode, constants

@home.route('/', methods=['GET'])
def index():
    return render_template("home/index.html")

@home.route('/qrcode/add', methods=['GET'])
def add_qrcode():
    data = request.args.get('data', '')
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

