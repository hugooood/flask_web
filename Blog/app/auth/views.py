#用户认证蓝本
#蓝本中的路由和视图函数

from flask import render_template,redirect,request,url_for,flash
from . import auth
from ..models import User
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm,RegistrationForm

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user,form.remember_me.data)
        return redirect(request.args.get('next') or url_for('main.index'))
    flash('Invalid username or password.')
    #注:auth文件夹在templates中
    return render_template('auth/login.html',form=form)

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
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)