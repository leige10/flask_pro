from flask import Flask
from flask_restx import Resource, Api, Namespace,fields

app = Flask(__name__)
api = Api(app)
hello_ns = Namespace("demo", description="demo学习")


@hello_ns.route("")
class Demo(Resource):
    # restful 风格的 get 方法
    @hello_ns.doc(params={'id': 'An ID'})
    def get(self):
        return {"code": 0, "msg": "get success"}

    post_model = api.model('PostModel', {
        'name': fields.String(description='The name', required=True),
        'type': fields.String(description='The object type', enum=['A', 'B']),
        'age': fields.Integer(min=0),
    })

    # restful 风格的 post 方法
    @hello_ns.doc(body=post_model)
    def post(self):
        return {"code": 0, "msg": "post success"}


api.add_namespace(hello_ns, '/hello')

if __name__ == '__main__':
    app.run(debug=True)