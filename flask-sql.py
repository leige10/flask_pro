from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import *
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:zyf123456@120.24.5.133:3306/bigsister?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)
# 定义数据库的表 需要继承 db.Model
class User(db.Model):
    __tablename__ = "user" # 设置数据库表名
    # 每一个类变量表示一个数据库表的列名
    # 第一个参数是表示数据的类型， primary_key=True 表示是主键
    id = Column(Integer, primary_key=True)
    # unique = True 表示是不能重复的  nullable=False 表示不可以为空
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    gender = Column(String(3))

    def __repr__(self):
        # 数据库的 魔法方法 直观展示数据
        '''[<User "张三">,<User "李四">]'''
        return f'<User {self.id} {self.username}  {self.email}'
if __name__=="__main__":
    with app.app_context():
        #db.create_all()
        # abd=User(id=2,username='螺旋形1',email='q1q@.com',gender='nan')
        # db.session.add(abd)
        # db.session.commit()
        # db.session.close()
        #db.drop_all()

        # dba=User.query.all()
        # for i in dba:
        #     print(i.id,i.username,i.email,i.gender)

        # dba=User.query.filter_by(gender='男').all()
        # print(dba)
        # dba=User.query.filter_by(gender='男').first()
        # aa=dba.id+1
        # print(aa)

        # dba=User.query.filter_by(gender='男').filter_by(username='企微').all()
        # print(dba)

        # dba=User.query.filter_by(gender='男').filter_by(username='企微').update({'username':'阿松大'})
        # db.session.commit()
        # db.session.close()

        dba=User.query.filter_by(gender='男').filter_by(username='阿松大').delete()
        db.session.commit()
        db.session.close()
