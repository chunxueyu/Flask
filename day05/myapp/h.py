from flask import Blueprint, request, jsonify
from .models import *
blue = Blueprint("day05", __name__)
PER_PAGE = 3
def init_blue(app):
    app.register_blueprint(blue)

@blue.route("/news/")
def get_news():
    page = int(request.args.get("page", 1))
#     查数据 获得分页对象
    paganition = News.query.paginate(page, PER_PAGE, False)
    # 获取分页数据
    news_data = paganition.items
    # 将对象转成字典
    res = []
    for i in news_data:
        res.append(i.to_dict())
    #     判断是否有前一页
    has_prev = paganition.has_prev
    # 前一页页码
    prev_num = 1
    if has_prev:
        prev_num = paganition.prev_num

    has_next = paganition.has_next
    # 下一页 页码默认是最后
    next_num = paganition.pages
    if has_next:
        next_num = paganition.next_num
    #     页码数值的范围
    page_range = range(1, paganition.pages + 1)
    json_data = {
        "has_prev": has_prev,
        "has_next": has_next,
        "page_range": list(page_range),
        "prev_num": prev_num,
        "next_num": next_num,
        "news": res
    }
    return jsonify(json_data)