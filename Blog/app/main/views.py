from flask_login import login_required,current_user
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm,ArticleForm
from .. import db
from ..models import User,Article
from datetime import datetime

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