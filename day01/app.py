from flask import render_template
from flask_script import Manager

# 实例化一个app
# app = Flask(__name__)
from myapp import create_app

app = create_app()
manager = Manager(app=app)

# 通过装饰器解释路由
@app.route('/')
def hello_world():
    # 返回结果
    return '<h1>Hello World!<h1>'

@app.route("/index/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    manager.run()
    # app.run(
    #     host="0.0.0.0",
    #     port=12354,
    #     debug=True
    # )
