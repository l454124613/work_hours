# -*- coding: utf-8 -*-
import base64
import json
import time
from tools.err_return import return400, return401, return403

# from controller.User import get_all_users
# from module.user import MUser

user = dict()
user_name = dict()
user_name['n0'] = '尚未登录人员'


# user['u1'] = 0
#
# user1 = {'vid': 1, 'uid': 2}


def set_user(users):
    if type(users) is dict:
        user['u' + str(users['id'])] = users['vid']
        user_name['n' + str(users['id'])] = users['name']
    elif type(users) is list:
        for u in users:
            set_user(u)
    elif type(users) is str:
        # print(str(users))
        set_user(json.loads(users))
    else:
        print(type(users))
        print('没用户')


def get_name_by_id(id):
    return user_name.get(id)


# def re_flash_users():
#     set_user(get_all_users())
#     print(user)

# print(user)
# print(get_all_users())
# set_user(get_all_users())
# print(get_all_users())


'''
状态1：无影响；2：新token；3：权限修改；4：登录超时;5:token不合法;6:无此账号
'''


def get_token(token=None, user_id=None):
    t = time.strftime("%Y%m%d%H%M%S", time.localtime())
    ss = dict()
    status_num = 1
    if token:
        token_dict = ''
        try:
            token_dict = get_id_by_token(token)
        except:
            return 5, '', '0'
        time_status = check_time(token_dict['t'], t)
        uid = token_dict['u']
        if 'u' + str(uid) not in user.keys():
            return 6, '', uid
        vid = user['u' + str(uid)]
        is_same_vid = (vid == token_dict['v'])
        if time_status == 1 and is_same_vid:
            return status_num, token, uid  # token无误
        elif time_status == 2:
            ss['v'] = vid
            ss['u'] = uid
            ss['t'] = t
            if is_same_vid:

                pass
            else:
                return 3, '', uid

        elif time_status == 3:
            return 4, '', uid
        else:
            print('token46')
            pass

    else:
        if user_id:
            ss['v'] = user['u' + str(user_id)]
            ss['u'] = user_id
            ss['t'] = t
        else:
            print('token63')
    # print(ss)
    # print(user_id)
    s1 = json.dumps(ss)
    s2 = s1.encode("UTF-8")
    a = base64.b85encode(s2)
    b = base64.urlsafe_b64encode(a)
    c = b.decode('UTF-8')
    d = c.count('=', 10)
    return 2, c.strip('=') + str(d), user_id


def get_id_by_token(token):
    a = '=' * int(token[-1])
    b = base64.urlsafe_b64decode(token[:-1] + a)
    c = base64.b85decode(b)
    return json.loads(c)


def check_time(t, t_now):
    t1 = t_now
    if int(t1) - int(t) < 10001:
        return 1  # 小于1小时
    elif int(t1) - int(t) < 30001:
        return 2  # 小于3小时
    else:
        return 3  # 大于3小时

# a = get_token()
# a = get_token(user_id=1)
# a = get_token(token='ZG0_cnNJdl9HSkdifHQ_YnN7PC1GKVNiPWJScyQrQX5HO0JJNTBPY0djaG5SR0JZK0plRQ2')
# print(a)
# print(check_token(a))

# print()
# ss = '{"vid":12132,"uid":1232,"vv":201802052312}'
# s2 = ss.encode('UTF-8')
# a = base64.b85encode(s2)
# # a = base64.urlsafe_b64encode(s2)
# # b = base64.b32encode(chr(len(a)).encode('UTF-8')).decode('UTF-8')
# # c = a.decode('UTF-8')
# d = base64.urlsafe_b64encode(a)
#
# # print(b.rstrip('=')+c)
# e = d.decode('UTF-8')
# i = e.count('=', 10)
# # print(i)
# e3 = e.strip('=') + str(i)
# print(e3)
# f2 = '=' * int(e3[-1])
# e2 = base64.urlsafe_b64decode(e + f2)
# f = base64.b85decode(e2)
# print(f.decode('UTF-8'))
# g = json.loads(f.decode('UTF-8'))
# print(g['uid'])
