from flask import Flask

from myapp import settings
from myapp.extension import init_ext
from myapp.views import init_myblue


def init_myapp(env_name):
    app = Flask(__name__)

    # 实例化配置
    app.config.from_object(settings.config.get(env_name))
    # 各种插件
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    init_ext(app)
    # 蓝图
    init_myblue(app)
    return app