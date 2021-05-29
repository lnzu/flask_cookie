import sys,os

sys.path.append('./utils/')
sys.path.append('./utils/lnzupy/')

from utils.lnzupy import fileos
from utils import datas
from utils import config
from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
import yaml

app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    ck = request.cookies
    title=config.getSiteTitle()
    print(len(ck))
    if request.method == 'GET':
        
        if 'cookie' in ck:
            if ck['cookie']==datas.getLocalCookie()['cookie']:
                return render_template('index.html')
            else:
                return render_template('login.html',title=title)
        else:
            return render_template('login.html',title=title)
            
    elif request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        loginout = request.form.get('login_out')
        
        if user==config.getUserName() and password==config.getUserPasswd():
            
            resp = make_response(render_template('index.html'))
            datas.setLocalCookie()
            resp.set_cookie('cookie',datas.getLocalCookie()['cookie'],config.getOnlineTime())
            
            return resp
            
        elif loginout == 'True':
            resp = make_response(render_template('login.html',title=title))
            datas.setLocalCookie()
            resp.set_cookie('cookie',datas.getLocalCookie()['cookie'],0)
            
            return resp
            
        else:
            return render_template('login.html',erro='密码或用户名错误',title=title)
            
            

@app.route('/login',methods=['GET', 'POST'])      
def login():
    if request.method == "POST":
        user = request.form.get('user')
        password = request.form.get('password')
        
        if user==config.getUserName() and password==config.getUserPasswd():
            
            resp = make_response(render_template('index.html'))
            datas.setLocalCookie()
            resp.set_cookie('cookie',datas.getLocalCookie()['cookie'],config.getOnlineTime())
            
            return resp
        else:
            return '密码或者用户名错误'
    elif request.method == "GET":
        return '请使用浏览器打开'
        


@app.route('/loginout',methods=['GET', 'POST'])
def loginOut():
    if request.method == "POST":
        resp = make_response(render_template('login.html'))
        datas.setLocalCookie()
        resp.set_cookie('cookie',datas.getLocalCookie()['cookie'],0)
        
        return resp
        
        
@app.route('/test',methods=['GET', 'POST'])
def test():
    if request.method == "GET":
        
        print(request.args)
        
        return 'jbjd'
    elif request.method == "POST":
        print(request.form)
        
        return 'bhvjb'
        

if __name__ =='__main__':
    pass
    app.run('127.0.0.1',5000)
