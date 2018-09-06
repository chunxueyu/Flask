from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def init_ext(app):
    Session(app)
    db.init_app(app)
    migrate.init_app(app=app,db=db)
