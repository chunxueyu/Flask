from flask import Flask

from myapp import settings
from myapp.extension import init_ext
# from myapp.views import init_blue
from myapp.urls import init_urls

def create_app(env_name="debug"):
    app = Flask(__name__)
    app.config.from_object(settings.config.get(env_name))
    # 初始化第三方插件
    init_ext(app)
    # 注册蓝图
    # init_blue(app)

    init_urls(app)
    return app