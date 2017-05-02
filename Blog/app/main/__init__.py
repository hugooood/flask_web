#创建蓝本
from flask import Blueprint

                
main = Blueprint('main',#所在包名
                __name__)

from . import views,errors