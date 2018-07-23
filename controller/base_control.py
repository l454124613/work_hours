# -*- coding:utf-8 -*-
# Author:lixuecheng
from module.database import engine
from sqlalchemy.orm import sessionmaker
from tools.err_return import return400
from flask_restful import reqparse, Resource

session_class = sessionmaker(bind=engine)
session = session_class()


def get_data_by_name(u, name):
    return session.query(u).filter_by(name=name).all()


def create_data(u, is_check_name=None, **kwargs):
    try:
        parser = reqparse.RequestParser()
        dd = dict()
        for i, j in kwargs.items():
            parser.add_argument(j)
        args = parser.parse_args()
        print(args)
        if is_check_name and args[is_check_name]:
            if len(get_data_by_name(u, args[is_check_name])) > 0:
                return False
        for i, j in kwargs.items():
            dd[i] = args[j]
        re_user = u(**dd)
        print(111)
        session.add(re_user)
        session.commit()
        return True

    except Exception as e:
        session.rollback()
        print(e)
        raise Exception(e)


def get_all_data(u, status=1):
    users1 = session.query(u).filter_by(status=status).all()
    u2 = []
    for u1 in users1:
        u2.append(u1.toJson())
    return u2


def get_data_by_id(u, data_id):
    return session.query(u).filter_by(id=data_id)


def delete_data(u, uid):
    try:
        get_data_by_id(u, uid).delete()
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception(e)


def update_status(u, uid, num):
    try:
        get_data_by_id(u, uid).update({'status': num})
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception(e)


def update_data(u, uid, **kwargs):
    try:
        parser = reqparse.RequestParser()
        dd = dict()
        for i, j in kwargs.items():
            parser.add_argument(j)
        args = parser.parse_args()
        for i, j in kwargs.items():
            dd[i] = args[j]
        d = get_data_by_id(u, uid)
        print(dd)

        d.update(dd)
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception(e)
