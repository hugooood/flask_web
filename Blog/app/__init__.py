#程序工厂函数

from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask_admin import Admin,BaseView,expose,AdminIndexView

# 延迟创建app
bootstrap = Bootstrap()
db = SQLAlchemy()
admin = Admin(
        name='不准看',
        template_mode='bootstrap3',
        url='/',

        index_view=AdminIndexView(
        name='home',
        #template='welcome.html',
        url='/hello_admin'
        )
)


login_manager = LoginManager()

#可以设置None,'basic','strong'  以提供不同的安全等级,一般设置strong,如果发现异常会登出用户
login_manager.session_protection = "strong"

login_manager.login_view = "auth.login" #auth是对应的蓝本名
# #这里填写你的登陆界面的路由

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)


    
    #附加路由和自定义的错误页面

    #注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    return app
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'wqesdczcasfsav'#密钥

# app.config.from_object("config") #从config.py读入配置

#这个import语句放在这里, 防止views, models import发生循环import
# from .main import views
# import models