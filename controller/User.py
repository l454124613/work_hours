# -*- coding:utf-8 -*-
# Author:lixuecheng
from module.user import MUser as u
from tools.token import set_user
from controller.base_control import session, return400, reqparse, Resource, get_all_data, get_data_by_id, update_data, \
    update_status, create_data, get_data_by_name


def check_passwd(name, password):
    try:
        u_re = get_data_by_name(u, name)
        if len(u_re) == 1:
            if u_re[0].password == password:
                return True, u_re[0].id
            else:
                return False, 0
        else:
            return False, 0
    except Exception as e:

        raise Exception(e)


set_user(get_all_data(u))


class User(Resource):
    def get(self, uid):
        try:
            # print(get_user_by_id(uid))
            return get_data_by_id(u, uid).one().toJson()
        except Exception as e:
            return return400(e)

    def delete(self, uid):
        try:
            update_status(u, uid, 2)
            set_user(get_all_data(u))
            return get_all_data(u), 200
        except Exception as e:
            return return400(e)

    def put(self, uid):
        try:
            update_data(u, uid, name='user_name')
            return get_all_data(u), 200
        except Exception as e:
            return return400(e)


class Users(Resource):
    def get(self):
        try:
            return get_all_data(u)
        except Exception as e:
            return400(e)

    def post(self):
        try:

            is_ok = create_data(u, is_check_name='user_name', name='user_name', password='user_passwd')

            if is_ok:
                set_user(get_all_data(u))
                return get_all_data(u), 201
            else:
                return [], 200
        except Exception as e:

            return return400(e)
