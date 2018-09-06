from flask import Flask
from flask_session import Session
from redis import StrictRedis

from .models import db
from .views import blue


def creat_app():
    app = Flask(__name__)
    # 注意这些配置要放前面，最后写蓝图，不然会加载不出来
    app.config['SECRET_KEY'] = "nihaoaxiaopenguou"
    # 指定session的类型
    app.config["SESSION_TYPE"] = "redis"
    # 设置的redis保存位置，保存在一库
    app.config["SESSION_REDIS"] = StrictRedis(host="127.0.0.1",db=1)
    # 说明数据库的连接
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:471753@106.12.109.74/fl02"
    # 设置修改追踪
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # 实例化session
    se = Session()
    se.init_app(app=app)

    # 初始化sqlalchemy
    db.init_app(app)


    #  注册蓝图
    app.register_blueprint(blueprint=blue)
    return app