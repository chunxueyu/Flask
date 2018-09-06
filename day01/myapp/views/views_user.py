from flask import Blueprint, request, render_template, abort, make_response, redirect, url_for, session

user = Blueprint("user",__name__)
@user.route("/login/",methods=["GET","POST"])
def login_api():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        # 处理登录逻辑
        params = request.form
        user_name = params.get("uname")
        # 设置cookie
        # response = make_response("ok")
        response = redirect(url_for("user.user_index"))
        # response.set_cookie("uname",user_name)
        session["uname"] = user_name
        return response
    else:
        abort(405)

@user.route("/logout/",methods=["GET","POST"])
def logout_api():
    # res = make_response("退出成功")
    # res.delete_cookie("uname")
    res = redirect(url_for("user.user_index"))
    # res.delete_cookie("session")
    session.pop("uname")
    return res

@user.route("/user/index/")
def user_index():
    # 获取登录的用户
    # user_name = request.cookies.get("uname","游客")
    user_name = session.get("uname")
    return render_template("index.html",uname=user_name)