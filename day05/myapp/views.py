from flask import Blueprint, request, jsonify, abort
from flask_restful import Resource

from myapp.extension import api
from .models import *


PER_PAGE = 3
blue = Blueprint("day05",__name__)
def init_blue(app):
    app.register_blueprint(blue)

@blue.route("/news/")
def get_news():
    page = int(request.args.get("page",1))
    # 查数据 获得分页对象
    pagination = News.query.paginate(page,PER_PAGE,False)
    #  获取分页数据
    news_data = pagination.items
    # 将对象转为字典
    res = []
    for i in news_data:
        res.append(i.to_dict())
    # 判断是否有前一夜页
    has_prev = pagination.has_prev
    # 前一页页码
    pre_num = 1
    if has_prev:
        pre_num = pagination.prev_num
    has_next = pagination.has_next
    # 下一页页码，默认是最后
    next_num = pagination.pages
    if has_next:
        next_num = pagination.next_num
    # 页面数值的范围
    page_range = range(1,pagination.pages + 1)
    json_data = {
        "has_prev":has_prev,
        "has_next":has_next,
        "page_range":list(page_range),
        "prev_num":pre_num,
        "next_num":next_num,
        'news':res,
        "code":1,
        "current_page":page
    }
    return jsonify(json_data)

# 原生restful
@blue.route("/restnews/",methods=["GET","POST","PUT","DELETE"])
def rest_news():
    if request.method == "GET":
        # 获取数据
        return jsonify({"msg":"hehe"})
    elif request.method == "POST":
        # 增加资源的操作
        params = request.form
        # 一段操作
        return jsonify({"msg":"haha"})
    elif request.method == "PUT":
        pass
    # 资源修改 修改个假新闻
    elif request.method == "DELETE":
        # 删除假新闻
        pass
    else:
        abort(405)

class Hello(Resource):
    def get(self):
        return {'msg':"Hello Restful"}
api.add_resource(Hello,"/hello/")
