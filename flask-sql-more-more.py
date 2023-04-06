from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import *
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:zyf123456@120.24.5.133:3306/bigsister?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)
# 定义数据库的表 需要继承 db.Model

#一对多
class Teacher(db.Model):
    __tablename__ = "teacher_more" # 设置数据库表名
    # 每一个类变量表示一个数据库表的列名
    # 第一个参数是表示数据的类型， primary_key=True 表示是主键
    id = Column(Integer, primary_key=True)
    # unique = True 表示是不能重复的  nullable=False 表示不可以为空
    teacher_name = Column(String(80), unique=True, nullable=False)
    xx = db.relationship('Students', secondary='Teacher_student_more', backref='xx1')
    def __repr__(self):
        # 数据库的 魔法方法 直观展示数据
        '''[<User "张三">,<User "李四">]'''
        return f'<User  {self.teacher_name}  '

class Students(db.Model):
    __tablename__ = "students_more" # 设置数据库表名
    # 每一个类变量表示一个数据库表的列名
    # 第一个参数是表示数据的类型， primary_key=True 表示是主键
    id = Column(Integer, primary_key=True)
    # unique = True 表示是不能重复的  nullable=False 表示不可以为空
    username = Column(String(80), unique=True, nullable=False)
    def __repr__(self):
        # 数据库的 魔法方法 直观展示数据
        '''[<User "张三">,<User "李四">]'''
        return f'<User  {self.username}  '


class Teacher_student(db.Model):
    __tablename__ = "Teacher_student_more" # 设置数据库表名
    # 每一个类变量表示一个数据库表的列名
    # 第一个参数是表示数据的类型， primary_key=True 表示是主键
    tea_id = Column(Integer,ForeignKey('teacher_more.id') ,primary_key=True)
    # unique = True 表示是不能重复的  nullable=False 表示不可以为空
    stu_id=Column(Integer,ForeignKey('students_more.id'),primary_key=True)



if __name__=="__main__":
    with app.app_context():
        #db.create_all()
        # abd=Teacher(id=1,teacher_name='老师1')
        # abd2 = Teacher(id=2, teacher_name='老师2')
        # abd3=Teacher(id=3, teacher_name='老师3')
        # adb=Students(id=1,username='罗大炮')
        # adb1 = Students(id=2, username='罗2炮')
        # adb2 = Students(id=3, username='罗3炮')
        # adb3 = Students(id=4, username='罗4炮')
        # db.session.add_all([abd, abd2, abd3, adb, adb1, adb2, adb3])
        # abd.xx=[adb,adb1]
        # abd2.xx=[adb2,adb3]
        #db.session.add(abd)

        # db.session.commit()
        # db.session.close()
        a=Teacher.query.filter_by(teacher_name='老师1').first()
        #print(a.teacher_name)
        print(a.xx[0].username)
        print(a.xx)
        b = Students.query.filter_by(username='罗大炮').first()
        print(b.xx1[0].teacher_name)
        print(b.xx1)

