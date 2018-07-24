# -*- coding:utf-8 -*-
# Author:lixuecheng
from flask_restful import reqparse, abort, Resource
from flask import g
from tools.token import get_token
from controller.User import check_passwd


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_name')
        parser.add_argument('user_passwd')
        user = parser.parse_args()
        u = user.get('user_name')
        p = user.get('user_passwd')
        is_ok, id = check_passwd(u, p)
        if is_ok:

            _, token2, uid = get_token(user_id=id)
            g.token = token2
            g.user_id = uid
            return {'ok': True}
        else:
            return {'ok': False}
