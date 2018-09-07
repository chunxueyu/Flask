from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_caching import Cache


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
debugtoobal = DebugToolbarExtension()
cache = Cache(config={'CACHE_TYPE': 'redis',
                      'CACHE_REDIS_HOST':'127.0.0.1',
                      'CACHE_REDIS_DB':2})
api = Api()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app=app,db=db)
    bootstrap.init_app(app=app)
    debugtoobal.init_app(app)
    cache.init_app(app=app)
    api.init_app(app)