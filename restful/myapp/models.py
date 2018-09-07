from myapp.extension import db

class News(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    title = db.Column(
        db.String(20)
    )
    def to_dict(self):
        return {"id":self.id,"title":self.title}