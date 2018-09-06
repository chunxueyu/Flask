import uuid

from flask import Blueprint, url_for, redirect, request, make_response, render_template, abort

# 蓝图的名字和导入的名字
blue = Blueprint("first",__name__)



@blue.route("/index_uuid/<uuid:uid>")
def index_uuid(uid):
    uuid_val = uuid.uuid4()
    print(uuid_val)
    print(uid)
    return "ok"

@blue.route("/index_any/<any(a,b,c):pa>" ,methods = ["POST","GET"])
def index_any(pa):
    print(pa)
    print(type(pa))
    return ("ok")

@blue.route('/hehe/')
def hello_world():
    # 返回结果
    return '<h1>Hello World!<h1>'


@blue.route("/index_path/<path:p>")
def index(p):
    print(type(p))
    return "你的参数是%s" %p

@blue.route("/check/")
def check_utl():
    # res = url_for("first.hello_world")
    res = url_for("first.index",p=4,a=2,b="h",c=3)
    print(res)
    return redirect(res)

@blue.route("/req/",methods=["GET","POST","DELETE"])
def my_req():
    req = request
    print(req.path)
    print(req.cookies)
    print(req.method)
    print(req.url)
    print(req.headers)
    print(req.args)
    print("************"*3)
    print(req.form)
    print(req.files)
    # print(dir(req))
    return "ok",403

@blue.route("/response/")
def my_res():
    response = make_response("达达快递",500)
    # response.status_code = 404
    # response.data = "呵呵"
    print(dir(response))
    return response

@blue.route("/nan/")
def template_res():
    html = render_template("index.html")
    print(html)
    res = make_response(html,500)
    return res

@blue.route("/ab/")
def my_abort():
    abort(500)
    return "ok"

@blue.errorhandler(500)
def try_error(ex):
    return "真好 又错了"