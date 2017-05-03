from flask_login import login_required,current_user
#from flask_admin import Admin
from flask import render_template, session, redirect, url_for
from . import main
from .. import admin
from .forms import NameForm,ArticleForm
from .. import db
from ..models import User,Article
from datetime import datetime

from flask_admin import Admin,BaseView,expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path

#Blog首页
@main.route('/', methods=['GET', 'POST'])
#@main.route('/index', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():#(wtf)检查是否是一个 POST 请求并且请求是否有效
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html',
                            form=form, name=session.get('name'),
                            known=session.get('known', False),
                            current_time=datetime.utcnow())


#编写文章
@main.route('/edit',methods=['GET','POST'])
#@login_required #需要登录
def edit():
    form = ArticleForm()
    if form.validate_on_submit():
        # 文章内容以markdown的格式存储，需要显示页面时可通过markdown模块解析后显示。如
        # print(markdown.markdown(form.content.data))
        article = Article(title=form.title.data,
            tags=form.tags.data,
            categories=form.categories.data,
            content=form.content.data,
            timestamp=datetime.utcnow(),
            )
            #author=current_user._get_current_object())#实现登录后补上
        try:
            db.session.add(article)
            db.session.commit()
        except Exception as e:
            print(str(e))
        return redirect(url_for('main.index'))

    return render_template('edit01.html',form=form)


#后台管理
class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin.html')
    # def is_accessible(self):
    #     return login.current_user.is_authenticated()
admin.add_view(MyView(name='Hello')) #admin在app.__init__中定义
admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(MyView(name='Hello 2', endpoint='test2', category='Test'))
admin.add_view(MyView(name='Hello 3', endpoint='test3', category='Test'))

#模型视图
admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Article,db.session))

#os.pardir 路径上级
path = os.path.join(os.path.dirname(__file__),os.pardir, 'images')
admin.add_view(FileAdmin(path, '/static/', name='上传图片'))