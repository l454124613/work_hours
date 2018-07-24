from flask import Flask, send_from_directory, jsonify, request, g
import os
from flask_restful import reqparse, abort, Api, Resource
from controller.todo import Todo, TodoList
from controller.login import Login
from controller.User import User, Users
from tools.token import set_user, get_token, return400, return401, return403, get_name_by_id
from flask_cors import CORS
from controller.Log import set_log

app = Flask(__name__, static_url_path='')

app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.before_request
def before_request():
    g.info = {}

    # print(dir(request))
    g.info['method'] = request.method
    g.info['path'] = request.path
    g.info['get'] = request.data.decode('utf8')
    if '/login' == request.path or '/favicon.ico' == request.path \
            or request.path.startswith('/css/') or request.path.startswith('/js/') or '/' == request.path:
        pass
    else:
        if request.headers.has_key('token'):
            token_one = request.headers.get('token')
            status_num, token_res, uid = get_token(token=token_one)
            if status_num == 3:
                return return403('权限被修改')
            elif status_num == 4:
                return return401('登录超时')
            elif status_num == 5:
                return return400('请求内容有错误5')
            elif status_num == 6:
                return return401('查无此用户')
            else:
                g.token = token_res
                g.user_id = uid


        else:
            # pass
            return return400('请求内容有错误0')
            # abort(400)
            # abort(400, message='请求内容有错误')
        # aa.get('token')

    # print(dir(request))


@app.after_request
def after_request(response):
    # print(dir(response))
    # print(response.data.decode('utf8'))
    # print(dir(response.expires))
    g.info['send'] = str(response.status_code) + ',' + response.data.decode('utf8')
    g.info['token'] = 'NO TOKEN'
    # print(response.status_code)
    if str(response.status_code).startswith('20'):
        try:
            response.headers['Access-Control-Expose-Headers'] = 'token'

            response.headers['token'] = g.token
            g.info['token'] = g.token
            g.info['uid'] = g.user_id
            g.info['name'] = get_name_by_id('n' + str(g.user_id))
            set_log(g.info['method'], g.info['path'], g.info['token'], g.info['get'], g.info['send'], g.info['uid'],
                    g.info['name'])

        except Exception as e:
            print('app_78', e)
            pass
    # print(dir(response))
    return response


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='static/favicon.icon')


api.add_resource(Login, '/login')
api.add_resource(Users, '/users')
api.add_resource(User, '/user/<uid>')

if __name__ == '__main__':
    app.run(port=7788, debug=True)
