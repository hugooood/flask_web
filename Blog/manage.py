#启动脚本
import os
from app import create_app,db
from app.models import User,Role
from flask_script import Manager,Server,Shell
from flask_migrate import Migrate,MigrateCommand
#from flask_admin import Admin


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)
migrate = Migrate(app,db) #数据库迁移



#admin = Admin(app,name='microblog', template_mode='bootstrap3')

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand) 


# manager.add_command("runserver",
# 		Server(host="127.0.0.1",port=8888,use_debugger=True))

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# db = SQLAlchemy(app)

if __name__ == '__main__':
	manager.run()