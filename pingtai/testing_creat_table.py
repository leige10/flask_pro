from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request
from sqlalchemy import *
from flask_restx import Resource,Api,Namespace
import logg
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:zyf123456@120.24.5.133:3306/test_houtai?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)
api=Api(app)
lo=logg.get_logger()
class Testcase(db.Model):
    __tablename__='testcase'
    id=Column(Integer,primary_key=True)
    case_title=Column(String(80),unique=False,nullable=False)
    case_remark=Column(String(300),unique=False,nullable=False)

case_us=Namespace('case_u',description='用例管理')
@case_us.route('')
class Testcase_jj(Resource):
    def get(self):
        lo.info(f'get method {request.args}')
        return {'code':0,'msg':'get'}

    def post(self):
        #jj=request.json
        #lo.info(f'post method mm{jj}')
        return {'code':0,'msg':'post'}

    def put(self):
        lo.info('put method')
        return {'code':0,'msg':'put'}
    def delete(self):
        lo.info('delete method')
        return {'code':0,'msg':'delete'}

api.add_namespace(case_us,'/testcase')


if __name__=="__main__":
    with app.app_context():
        #db.create_all()
        app.run(debug=True)