from flask import Flask

from .views import blue
from .views.views_user import user

def create_app():
    app = Flask(__name__)
    # 设置加密密钥
    app.config['SECRET_KEY'] = "nihaoaxiaopenguou"
    # 注册到蓝图里
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=user)
    return app