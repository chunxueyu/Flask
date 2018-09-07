from flask_restful import fields,reqparse

news_fileds = {
    "id":fields.Integer,
    # "title":fields.String
    "content":fields.String(attribute="title")
}

news_two_fields = {
    "code":fields.Integer(default=1),
    "msg":fields.String(default="ok"),
    "data":fields.Nested(news_fileds)
}

news_three_fields = {
    "code":fields.Integer(default=1),
    "msg":fields.String(default="ok"),
    "data":fields.List(fields.String),
    "news":fields.Nested(news_fileds)
}
new_parse = reqparse.RequestParser()
new_parse.add_argument("id",type=int,required=True,action="append",help="必填字段")

# 继承
test_pares = reqparse.RequestParser()
test_pares.add_argument("c_name",location="form")
test_one_parse = new_parse.copy()
test_one_parse.add_argument("mid",type=int)
test_one_parse.remove_argument("id")
