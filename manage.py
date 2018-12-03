# -*- coding:utf-8 -*-
import os
from app import create_app, db
from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG_TXL') or 'default')

manager = Manager(app)
migrate = Migrate(app, db)

# 添加迁移数据库脚本的命令
manager.add_command('db', MigrateCommand)

# 添加初始化脚本的命令
# python manage.py dbinit
@manager.command
def dbinit():
    print ('dbinit')

if __name__ == '__main__':
    manager.run()