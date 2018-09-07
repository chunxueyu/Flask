from flask_restful import Resource, marshal_with

from .models import News
from .utils import *

# 一层json
class NewsResource(Resource):
    @marshal_with(news_fileds)
    def get(self):
        news = News.query.first()
        return news

#两层json嵌套
class NewsTwoResponse(Resource):
    @marshal_with(news_two_fields)
    def get(self):
        news = News.query.first()
        return {"data":news}

# 嵌套列表,参数解析
class NewsThreeResponse(Resource):
    @marshal_with(news_three_fields)
    def get(self):
        param = new_parse.parse_args()
        id = param.get("id")
        print(id)
        # 很奇怪，这里的all()换不成first()
        all_news = News.query.all()
        return {"data":["he","hehe","hehehe"],"news":all_news}

# 继承
class LocationResponse(Resource):
    def get(self):
        param = test_one_parse.parse_args()
        return param
    def post(self):
        c_name = test_pares.parse_args().get("c_name")
        return {"param":c_name}