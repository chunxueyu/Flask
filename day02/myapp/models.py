from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = "dada"
    id = db.Column(
        db.Integer,
        autoincrement=True,
        primary_key=True
    )
    name = db.Column(
        db.String(20),
        nullable=False
    )
    age = db.Column(
        db.Integer
    )