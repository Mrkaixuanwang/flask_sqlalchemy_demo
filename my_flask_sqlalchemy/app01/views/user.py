from flask import Blueprint
from app01.models import db, Users

user = Blueprint("user", __name__)


@user.route("/reg/<username>")
def reg(username):
    user = Users(name=username)
    db.session.add(user)
    db.session.commit()
    return '添加成功'


@user.route('/user_list')
def user_list():
    users = db.session.query(Users).all()
    return f"当前用户个数为{len(users)}个"
