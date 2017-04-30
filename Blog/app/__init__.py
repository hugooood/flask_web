from flask import Flask

app = Flask(__name__)

app.config.from_object("config") #从config.py读入配置

#这个import语句放在这里, 防止views, models import发生循环import
from app import views,models