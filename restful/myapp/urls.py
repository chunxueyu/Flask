from .apis import *
from flask_restful import Api


# 实例化Api
api = Api()
def init_urls(app):
    api.init_app(app)

# 添加路由
api.add_resource(NewsResource,"/news/")
api.add_resource(NewsTwoResponse,"/newstwo/")
api.add_resource(NewsThreeResponse,"/newsthree/")
api.add_resource(LocationResponse,"/test/")