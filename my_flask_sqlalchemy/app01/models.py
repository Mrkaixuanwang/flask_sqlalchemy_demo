from app01 import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)


# 只有在执行该文件的时候，才会执行以下代码
if __name__ == '__main__':
    from app01 import create_app

    app = create_app()
    db.create_all(app=app)
