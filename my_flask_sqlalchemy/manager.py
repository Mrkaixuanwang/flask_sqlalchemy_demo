from app01 import create_app, db
from flask_script import Manager  # 指令模块
from flask_migrate import Migrate, MigrateCommand  # 数据库迁移模块

app = create_app()
manager = Manager(app)

# 添加数据库迁移指令集
mig = Migrate(app, db)
manager.add_command("db", MigrateCommand)
'''
python manager.py db init 初始化数据库，会在目录下生成migrations目录
python manager.py db migrate  相当于django的makemigrations
python manager.py db upgrade  相当于django的migrate
'''



'''
通过Manager的装饰器，自定义指令集
'''
# 不选项的指令  python manager.py func hell0
@manager.command
def func(args):
    print(args)
    return args


# 带选项的指令 python manager.py show --name rose -s hello
@manager.option("-n", "--name", dest="name")
@manager.option("-s", "--string", dest="string")
def show(name, string):
    print(name, string)


if __name__ == "__main__":
    manager.run()  # 指令启动flask项目 python manager.py runserver -h 0.0.0. -p 8888
