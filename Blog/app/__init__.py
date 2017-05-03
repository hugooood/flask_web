#程序工厂函数

from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
from config import config

# 延迟创建app
bootstrap = Bootstrap()
db = SQLAlchemy()
#loginManager = LoginManager()

#loginManager.session_protection = "None"
#可以设置None,'basic','strong'  以提供不同的安全等级,一般设置strong,如果发现异常会登出用户

# loginManager.login_view = "login"
# #这里填写你的登陆界面的路由

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    #loginManager.init_app(app)


    
    #附加路由和自定义的错误页面

    #注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'wqesdczcasfsav'#密钥

# app.config.from_object("config") #从config.py读入配置

#这个import语句放在这里, 防止views, models import发生循环import
# from .main import views
# import models