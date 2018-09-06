import os

from flask import Flask

from myapp import settings
from myapp.extension import init_ext
from myapp.settings import BASE_DIR
from myapp.views import init_blue


def create_app(env_name="debug"):
    static_path = os.path.join(BASE_DIR,"static")
    templates_path = os.path.join(BASE_DIR,"templates")
    app = Flask(__name__,
                static_folder=static_path,
                template_folder=templates_path
                )
    # 配置
    app.config.from_object(settings.config.get(env_name))
    # 初始化第三方插件
    init_ext(app)
    # 注册蓝图
    init_blue(app)
    return app