import random

from flask import Blueprint, session, render_template
from .models import db, Person

blue = Blueprint("blue",__name__)

# create you function

@blue.route("/set/")
def set_session():
    session["uname"] = "lala"
    return "ok"

@blue.route("/get/")
def get_session():
    return session.get("uname","没拿到")

@blue.route("/index/")
def index():
    res = [1,2,3,4,5,6]
    return render_template("index.html",datas=res)

@blue.route("/index_plus/")
def index_plus():
    return render_template("index_plus.html"),

@blue.route("/filter/")
def my_filter():
    return render_template("filter.html",p1="<h1>hello world<h1>")


# model 操作
@blue.route("/createdb/")
def createdb():
    db.create_all()
    return "ok"

@blue.route("/dropdb/")
def dropdb():
    db.drop_all()
    return "跑咯"

@blue.route("/createdata/")
def create_data():
    # p = Person(
    #     name="小明%d"%random.randrange(50),
    #     age=random.randrange(80)
    # )
    # db.session.add(p)

    instances = []
    for i in range(5):
        p = Person(
            name="小明%d"%random.randrange(50),
            age=random.randrange(80)
        )
        instances.append(p)
    db.session.add_all(instances)

    # 提交我们的事务
    db.session.commit()
    return "创建了{name}".format(name=p.name)

@blue.route("/datalist/")
def get_list():
    res = Person.query.all()
    for i in res:
        print(i.name,str(i.age))
    return "lala"

