# -*- coding:utf-8 -*-
# Author:lixuecheng
from flask import jsonify


def return400(msg):
    if type(msg) is dict or type(msg) is list:
        return jsonify(msg), 400
    else:
        return {'msg': str(msg)}, 400


def return401(msg):
    if type(msg) is dict or type(msg) is list:
        return jsonify(msg), 401
    else:
        return {'msg': msg}, 401


def return403(msg):
    if type(msg) is dict or type(msg) is list:
        return jsonify(msg), 403
    else:
        return {'msg': msg}, 403
