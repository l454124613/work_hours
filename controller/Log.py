# -*- coding:utf-8 -*-
# Author:lixuecheng
from module.log import MLog
from controller.base_control import session, return400, reqparse, Resource, create_data, get_all_data


def set_log(method, path, token, get_info, send_info, user_id, user_name):
    create_data(MLog, is_skip_args=True, method=method, path=path, token=token, get_info=get_info, send_info=send_info,
                user_id=user_id,
                user_name=user_name)


class Logs(Resource):
    def get(self):
        return get_all_data(MLog)
