from flask import Flask, request, jsonify, render_template, make_response, url_for
import logging
app=Flask(__name__)
app.config['JSON_AS_ASCII']=False
@app.route('/')
def hello():
    return '<p>阿松大</p>'

@app.route('/a1/<username>')
def hello1(username):
    return f'这是{username}'

@app.route('/a2/<string:username>')
def hello2(username):
    return f'这是限定字符串的{username}'

@app.route('/reques/a1',methods=['get'])
def he_request_args():
    logging.error(f'request的参数：{request.args},request的url：{request.url}')
    req=request.args
    print(req['a']+'   ',req.get('b'))
    return 'request-args'

@app.route('/reques/a2',methods=['post'])
def he_request_json():
    logging.error(f'request的参数：{request.json},request的url：{request.url}')
    req=request.json
    print(req['a']+'   ',req.get('b'))
    return 'request-args'

@app.route('/reques/a3',methods=['put','post'])
def he_request_form():
    logging.error(f'request的参数：{request.form},request的url：{request.url}')
    req=request.form
    req_a=req['a']
    req_b=req.get('b')
    #print(req['a']+'   ',req.get('b'))
    return 'request-args'

@app.route('/reques/a4/',methods=['put','post'])
def he_request_file():
    fil=request.files.get('file11111')
    #logging.error(f'request的参数：{request.files},request的url：{request.url}')
    logging.error(f'request的文件对象：{fil}')
    logging.error(f'request的文件名字：{fil.filename}')
    fil.save('./a1.png')
    #print(req['a']+'   ',req.get('b'))
    return 'request-args'

@app.route('/tuple')
def re_tump():
    return {'qwe':'我爱我的家哦','asd':'你是哇','a':{'asd':'ss'}},201,{'ads':123,'qqq':'qwea'}

@app.route('/json_a')
def re_tump1():
    return jsonify(a=1,b='2',c='阿德撒旦'),201,{'ads':123,'qqq':'qwea'}

@app.route('/json_b')
def re_tump2():
    return jsonify(a=1,b='2',c='阿德撒旦'),201,{'ads':123,'qqq':'qwea'}

@app.route('/h')
def re_tump3():
    return render_template('demo.html')

@app.route('/h1')
def re_tump4():
    res=make_response(render_template('demo.html'))

    res.set_cookie('qwe','qweqq')
    res.headers['qqw']='qq'
    return res

@app.route('/api/v1/hello')
def hello_view():
    # 数据库交互
    # 实例化 Students 模型对象
    print(url_for('re_tump4'))
    return {"code": "0", "msg": "success"}

@app.route('/api/v2', endpoint="hello777")
def hello_view1():
    # 数据库交互
    # 实例化 Students 模型对象
    print(url_for('hello777'))
    return {"code": "0", "msg": "success"}
if __name__=="__main__":
    app.run(debug=True)