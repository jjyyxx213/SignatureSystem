# -*- coding:utf-8 -*-
from . import home
from flask import render_template

@home.route('/', methods=['GET'])
def index():
    return render_template("home/index.html")