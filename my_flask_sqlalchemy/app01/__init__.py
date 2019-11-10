from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# 蓝图导入要写在db下面，不然会报错
from app01.views import user


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SESSION_COOKIE_NAME'] = "I am not SESSION"
    # sqlalchemy配置
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@127.0.0.1:3306/test?charset=utf8"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 当前版本flask-sqlalchemy为避免一些问题，设置为False

    app.register_blueprint(user.user)
    # 初始化sqlalchemy对象，使其和app建立联系
    db.init_app(app=app)
    return app
