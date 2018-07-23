# -*- coding:utf-8 -*-
# Author:lixuecheng
import requests

a = requests.post('http://localhost:7788/login', json={'user_name': 'Kelly Roberts', 'user_passwd': 'star'})
print(a.headers)
print(a.status_code)
print(a.content)
print(a.text)
token = a.headers['token']
# print('-----------------------------------------------------------')
# a = requests.get('http://localhost:7788/user/1',
#                  headers={'token': token})
# print(a.status_code)
# print(a.content)
# print(a.text)
# print('-----------------------------------------------------------')
# a = requests.get('http://localhost:7788/users',
#                  headers={'token': token})
# print(a.status_code)
# print(a.content)
# print(a.text)
# print('-----------------------------------------------------------')
# a = requests.post('http://localhost:7788/users',
#                   headers={'token': token},
#                   data={"user_name": "test52", "user_passwd": '1'})
# print(a.status_code)
# print(a.content)
# print(a.text)
# print('-----------------------------------------------------------')
# a = requests.put('http://localhost:7788/user/3',
#                   headers={'token': token},
#                   data={"user_name": "test31", "user_passwd": '1'})
# print(a.status_code)
# print(a.content)
# print(a.text)
print('-----------------------------------------------------------')
a = requests.delete('http://localhost:7788/user/3',
                  headers={'token': token}
                  )
print(a.status_code)
print(a.content)
print(a.text)
