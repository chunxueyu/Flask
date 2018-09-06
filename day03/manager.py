from flask_script import Manager
from myapp.models import *
from myapp import init_myapp
from flask_migrate import MigrateCommand

app = init_myapp("debug")

manager = Manager(app)
# 这是添加迁移的命令
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()
