#encoding=utf-8
from datetime import datetime
from flask import render_template, session, redirect, url_for,request,Response
from . import main
from forms import LoginForm,ShareForm
from .. import db
from models import User


@main.route('/', methods=['GET', 'POST'])
def index():
	share_form=ShareForm()
 	return render_template('index.html',form=share_form)
@main.route('/share', methods=['GET', 'POST'])
def share():
	share_form=ShareForm()
	if share_form.validate_on_submit():
		s1_name=request.form.get('s1')
		return render_template('index.html',s1=s1_name)
	return Responce("invalid input")

@main.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		db_user=mongo.db.users.find_one({'email':form.email.data})
		if db_user is not None:
			db_password=db_user.get('password',None)
			if User.veryfy_passwd(db_passwd,form.password.data):
				user=User(db_user['_id'])
				login_user(user)
				flash('登录成功','SUCCESS')
				return redirect(request.args.get('next') or url_for('main.index'))
			else:
				flash('邮箱或密码错误','WARNING')
		else:
			flash('不存在该用户','WARNING')

	return render_template('login.html', form=form)

@main.route('/data', methods=['GET', 'POST'])
def data():
	
 	return render_template('data.html')

@main.route('/video', methods=['GET', 'POST'])
def video():
	
 	return render_template('video.html')

@main.route('/wenzhang', methods=['GET', 'POST'])
def wenzhang():
	
 	return render_template('wenzhang.html')



