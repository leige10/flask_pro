from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import *
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:zyf123456@120.24.5.133:3306/bigsister?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)
# 定义数据库的表 需要继承 db.Model

#一对多
class Class(db.Model):
    __tablename__ = "class" # 设置数据库表名
    # 每一个类变量表示一个数据库表的列名
    # 第一个参数是表示数据的类型， primary_key=True 表示是主键
    id = Column(Integer, primary_key=True)
    # unique = True 表示是不能重复的  nullable=False 表示不可以为空
    classname = Column(String(80), unique=True, nullable=False)

class Students(db.Model):
    __tablename__ = "students" # 设置数据库表名
    # 每一个类变量表示一个数据库表的列名
    # 第一个参数是表示数据的类型， primary_key=True 表示是主键
    id = Column(Integer, primary_key=True)
    # unique = True 表示是不能重复的  nullable=False 表示不可以为空
    username = Column(String(80), unique=True, nullable=False)
    gender = Column(String(3))
    class_id=Column(Integer,ForeignKey('class.id'))
    xx=db.relationship('Class',backref='xx1')

if __name__=="__main__":
    with app.app_context():
        #db.create_all()
        # abd=Class(id=1,classname='班级1')
        # abd2 = Class(id=2, classname='班级2')
        # abd3 = Class(id=3, classname='班级3')
        # adb=Students(id=1,username='罗大炮',gender='男',class_id=1)
        # adb1 = Students(id=2, username='罗2炮', gender='男', class_id=2)
        # adb2 = Students(id=3, username='罗3炮', gender='男', class_id=3)
        # adb3 = Students(id=4, username='罗4炮', gender='男', class_id=1)
        # #db.session.add(abd)
        # db.session.add_all([adb3])
        # db.session.commit()
        # db.session.close()

        # dba=Students.query.filter_by(username='罗2炮').first()
        # print(dba.xx.classname)
        #
        # dba=Class.query.filter_by(classname='班级1').first()
        # print(dba.xx1[0].username)
        # print(dba.xx1[1].username)

        dba=Students.query.filter_by(username='罗2炮').first()
        dba.xx.classname='班级罗22'
        db.session.commit()
        db.session.close()

        dba=Class.query.filter_by(classname='班级1').first()
        dba.xx1[0].username='罗半炮'
        db.session.commit()
        db.session.close()
