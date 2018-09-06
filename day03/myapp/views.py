import random

from flask import Blueprint, render_template, request
from flask_sqlalchemy import Pagination

from myapp.models import *
from myapp.extension import db

blue = Blueprint("day3",__name__)

def init_myblue(app):
    app.register_blueprint(blue)

# 创建数据库
@blue.route("/createdb/")
def create_all():
    db.create_all()
    return "ok"

# 插入数据
@blue.route("/insertdb/")
def insert_data():
    u = User()
    u.name = "flask" + str(random.randrange(100))
    u.age = random.randrange(100)

    # 添加
    db.session.add(u)
    # 提交
    db.session.commit()
    return u.name

@blue.route("/getone/")
def get_one_data():
    # 拿到对象
    res = User.query.filter_by(id=1).first()
    print(type(res))
    # print(dir(res))
    # print(res)
    return "ok"

@blue.route("/delete/")
def delete_one():
    # 先查询
    user = User.query.filter_by(id=1).first()
    # 删除
    db.session.delete(user)
    # 提交,对数据库做完操作后都要提交
    db.session.commit()
    return "success"

@blue.route("/query/")
def my_query():
    # res = User.query.filter(User.id.__gt__(2))
    # res = User.query.filter(User.id.in_([2,4]))
    # res = User.query.filter(User.name.contains("8"))
    # res = User.query.filter(User.name.endswith("1"))
    # res = User.query.filter(User.name.like("%k12"))
    # res = User.query.order_by(User.age)
    # res = User.query.filter(User.id.__lt__(5)).order_by(User.age)
    # 跳过18条记录
    # res = User.query.offset(18).order_by(User.age)
    # offset和order_by顺序不一样会报错
    # res = User.query.order_by(User.age).offset(18)
    # get只能查主键（id)
    # get_res = User.query.get(3)
    # print(get_res)
    # 前5个
    # res = User.query.limit(5)
    # 跳过5个数据，再拿4条数据
    res = User.query.offset(5).limit(4)

    return render_template("users.html",users=res)

@blue.route("/paginate/")
def my_data():
    # 拿参数
    params = request.args
    page_num = int(params.get("page"))
    per_page = int(params.get("per_page"))
    # 计算位移 手动分页
    # users = User.query.offset((page_num - 1)*per_page).limit(per_page)
    # 自带分页
    users = User.query.paginate(page_num,per_page,error_out=False).items
    return render_template("users.html",users=users)


@blue.route("/grade/")
def create_grade():
    gs = []
    for i in range(3):
        tmp = Grade(name="逗逼%d班"%i)
        gs.append(tmp)
    db.session.add_all(gs)
    db.session.commit()
    return "ok"

@blue.route("/stu/")
def create_stu():
    g_id = request.args.get("gid")
    stus = []
    for i in range(20):
        s = Stu()
        s.name = "东东%d"%i
        s.grade_id = int(g_id)
        stus.append(s)
    db.session.add_all(stus)
    db.session.commit()
    return "hello"


@blue.route("/get_grade_by_stu/<int:sid>")
def get_grade(sid):
    stu = Stu.query.get(sid)
    # 拿班级信息,只能拿到id
    res = stu.grade_id
    print(res)
    grade = Grade.query.get(stu.grade_id)
    return grade.name

@blue.route("/get_stus/<int:gid>")
def get_stus(gid):
    # 通过gid找到班级
    grade = Grade.query.get(gid)
    print(grade)
    # 第一种方案，通过gid找
    # stu = Stu.query.filter(Stu.grade_id==gid)
    # 第二种方案，通过外键找
    stu = grade.stus
    print(stu)
    return render_template("users.html",users=stu)

@blue.route("/collect/<int:uid>/<int:item_id>")
def collect(uid,item_id):

    data = Collect(
        user=uid,
        item=item_id
    )
    db.session.add(data)
    db.session.commit()
    return "收藏成功"

@blue.route("/get_col_item/<int:uid>")
def get_item(uid):
    # user = User.query.get(uid)
    res = Collect.query.filter(Collect.user==uid)
    print(res)
    return "ok"


