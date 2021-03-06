#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2017 Richard Hughes <richard@hughsie.com>
# Licensed under the GNU General Public License Version 2

from app import app as application

if __name__ == '__main__':
    from flask import Flask
    server = Flask(__name__)
    server.wsgi_app = application
    server.run(host=application.config['IP'], port=application.config['PORT'])
