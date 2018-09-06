from flask import Blueprint, render_template, request, abort, g, jsonify,json

from myapp.extension import cache
from .models import *

PER_PAGE = 3

blue = Blueprint("fl04", __name__)


def init_blue(app):
    app.register_blueprint(blue)


@blue.route("/news/")
# @cache.cached(timeout=50)   # 加了这个东西,页面点击后不能跳转
def get_news():
    print("进来了")
    page = request.args.get("page")
    page_obj = News.query.paginate(int(page), PER_PAGE, False)
    return render_template("news.html", pagination=page_obj)


@blue.route("/newscache/")
def get_news_cache():
    # 拿客户端ip
    key = request.remote_addr + "cache"
    res = cache.get(key)
    if res:
        return res
    else:
        print("进来了")
        print(g.id)
        page = request.args.get("page")
        page_obj = News.query.paginate(int(page), PER_PAGE, False)
        html =  render_template("news.html", pagination=page_obj)
        # 把页面设置到缓存
        cache.set(key,html,20)
        return html

@blue.route("/score/")
def get_score():
    data = {
        "code":1,
        "msg":"ok",
        "data":[59,59,60,61,90,85]
    }
    # 转的是字符串,前端需要转成json
    # return json.dumps(data)
    # 转的是整个数据结构
    return jsonify(data)

@blue.before_request
def fanpa():
    # 拿ip
    addr = request.remote_addr
    agent = request.user_agent
    print(agent)
    g.id = addr
    if agent:
        pass
    else:
        return "你是垃圾爬虫师",500
    key = addr + "spider"
    tmp = cache.get(key)
    if tmp:
        if int(tmp) >= 20:
            return "搞你M啊",500
        else:
            cache.set(key,int(tmp) + 1,5)
    else:
        cache.set(key,1,5)
    print("爬虫处理")
