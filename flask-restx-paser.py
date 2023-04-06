from flask import Flask, request
from flask_restx import Resource, Api, Namespace,fields
#from backend_demo.demo.log_util import logger

app = Flask(__name__)
api = Api(app)
hello_ns = Namespace("demo", description="demo学习")

@hello_ns.route("")
class Demo(Resource):
    get_parser = api.parser()
    get_parser.add_argument('id',type=int,location='json')

    @hello_ns.expect(get_parser)
    def get(self):
        #logger.info(f"request.args ===>{request.args}")
        print(request.args)
        return {"code": 0, "msg": "get success"}

api.add_namespace(hello_ns,"/hello1")

if __name__ == '__main__':
    app.run(debug=True)