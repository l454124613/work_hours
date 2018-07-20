# -*- coding:utf-8 -*-
# Author:lixuecheng
from module.user import MUsers as u, sessionmaker, engine
from flask_restful import reqparse, abort, Resource, request
from tools.err_return import return400
from tools.token import set_user
import json

session_class = sessionmaker(bind=engine)
session = session_class()


def create_user(name, password):
    try:
        if len(get_user_by_name(name)) > 0:
            return False
        re_user = u(name=name, password=password)
        session.add(re_user)
        session.commit()
        set_user(get_all_users())
        return True
    except Exception as e:
        session.rollback()
        raise Exception(e)


def get_user_by_name(name):
    return session.query(u).filter_by(name=name).all()


def check_passwd(name, password):
    try:
        u_re = get_user_by_name(name)
        if len(u_re) == 1:
            if u_re[0].password == password:
                return True, u_re[0].id
            else:
                return False,0
        else:
            return False,0
    except Exception as e:

        raise Exception(e)


def get_all_users():
    users1 = session.query(u).all()
    u2 = []
    for u1 in users1:
        u2.append(u1.toJson())
    return u2


set_user(get_all_users())


def get_user_by_id(uid):
    return session.query(u).filter_by(id=uid)


def delete_user(uid):
    try:
        get_user_by_id(uid).delete()
        session.commit()
        set_user(get_all_users())
    except Exception as e:
        session.rollback()
        raise Exception(e)


def update_user(uid):
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('user_name')
        args = parser.parse_args()
        get_user_by_id(uid).update({u.name: args['user_name']})
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception(e)


class User(Resource):
    def get(self, uid):
        try:
            # print(get_user_by_id(uid))
            return get_user_by_id(uid).one().toJson()
        except Exception as e:
            return return400(e)

    def delete(self, uid):
        try:
            delete_user(uid)
            return get_all_users(), 200
        except Exception as e:
            return return400(e)

    def put(self, uid):
        try:
            update_user(uid)
            return get_all_users(), 200
        except Exception as e:
            return return400(e)


class Users(Resource):
    def get(self):
        try:
            return get_all_users()
        except Exception as e:
            return400(e)

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('user_name')
            parser.add_argument('user_passwd')
            args = parser.parse_args()
            is_ok = create_user(args['user_name'], args['user_passwd'])
            if is_ok:

                return get_all_users(), 201
            else:
                return [], 200
        except Exception as e:
            return return400(e)
