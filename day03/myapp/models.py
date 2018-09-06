from myapp.extension import db

class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20)
    )
    age = db.Column(
        db.Integer,
        default=1
    )
    # collects = db.relationship(
    #     "Collect",
    #     barkerf = "user",
    #     lazy = True
    # )

class Item(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20)
    )
    # collects = db.relationship(
    #     "Collect",
    #     backref="item",
    #     lazy=True
    # )

class Collect(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    user = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )
    item = db.Column(
        db.Integer,
        db.ForeignKey("item.id"),
        nullable=False
    )
    __table_args__ = (db.UniqueConstraint("user","item",name="user_item_uin_unique"),)

class Grade(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20)
    )
    stus = db.relationship(
        "Stu",
        backref="grade",
        lazy=True
    )
    def __repr__(self):
        return self.name

class Stu(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20)
    )
    grade_id = db.Column(
        db.Integer,
        db.ForeignKey("grade.id"),
        nullable=False
    )
