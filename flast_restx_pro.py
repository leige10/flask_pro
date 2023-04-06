from flask import Flask,request
from flask_restx import Resource,Api,Namespace
import json,logging
app=Flask(__name__)

api=Api(app)

@api.route('/h11/<namm>','/h111/<namm>')
class hello123(Resource):
    def get(self,namm):
        logging.error(f'{request.args["a"]}')
        print(f'{request.args["a"]}')
        return f'123+{namm}'
    def post(self):
        return {'qq':'撒大大111'}

@api.route('/h12')
class hello1234(Resource):
    def get(self):
        b={'a1sd':'撒大大'}
        a=json.dumps(b,ensure_ascii=False)
        return a
    def post(self):
        return ''

@api.route('/h13')
class hello12(Resource):
    def get(self):

        return {'qwe':'撒旦'},201,{'Content-Type':'application/json;charset=utf-8'}
    def post(self):
        return ''



# or

@api.route('/todo/<int:todo_id>','/qqwwee')
class HelloWorld(Resource):
    def get(self,todo_id):
        return f'qqq{todo_id}'

hellow_us=Namespace('demo',description='hello的描述')
@hellow_us.route('')
class HelloWorld11(Resource):
    def get(self):
        return f'qqq'
api.add_namespace(hellow_us,'/hell1')





if __name__=="__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)