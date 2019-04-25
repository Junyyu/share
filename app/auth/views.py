#encoding=utf-8
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, 
    current_user
from . import auth
from .. import db
from app.models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm,ProfileForm
from app.util import bson_obj_id ,AllowFile
from gridfs import GridFS,NoFile
from datetime import datetime






@auth.route('/login', methods=['GET', 'POST'])
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

	return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    	form = RegistrationForm()
    	if form.validate_on_submit():
        	email =form.email.data
		uname=form.username.data
		passwd=form.password.data
		rp_passwd=form.repeat.data
		if passwd != rp_password:
			flash('两次密码不相同','WARNING')
		elif mongo.db.users.find_one({'email':email})is not None:
			flash('该邮箱已被注册','WARNING')
		else:
			mongo.db.users.insert({'email':email,'username':uname,'password':User.gen_passwd_hash(passwd)})
			flash('注册成功','SUCCESS')
			send_email(user.email, 'Confirm Your Account','auth/email/confirm', user=user, token=token)
        		flash('A confirmation email has been sent to you by email.')
        		return redirect(url_for('auth.login'))
    	return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@auth.route('/confirm')
def confirm(token):
	user=User.verify_auth_token(token)
	if user:
		print(user)
		r=mongo.db['users'].updata(
		{'_id',:user['_id']},
		{'$set':
			{
				'active':Ture
			}
		}		
		)
        
    		if r:
        
			flash('You have confirmed your account. Thanks!')
      		else:
        		flash('The confirmation link is invalid or has expired.')
    	return redirect(url_for('main.index'))




    else:
        flash('Invalid request.')
    return redirect(url_for('main.index'))
