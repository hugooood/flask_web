#程序工厂函数

from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

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