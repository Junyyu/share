#coding=utf-8
from flask_wtf import Form,RecaptchaField
from flask_wtf.html5 import EmailField
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
	email = EmailField('邮箱',validators=[DataRequired()])
	password = PasswordField('密码',validators=[DataRequired()])
	submit = SubmitField('登录')
class RegisterForm(Form):
	email = EmailField('邮箱',validators=[DataRequired()])
	username = StringField('用户名',validators=[DataRequired()])
	password = PasswordField('密码',validators=[DataRequired()])

	repeat = PasswordField('重置密码',validators=[DataRequired()])
	submit = SubmitField('注册')
class  ShareForm(Form):
	s1=StringField(validators=[DataRequired()])
	submit = SubmitField('Share')
