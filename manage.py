# coding:utf8
from app import app
from flask_script import Manager, Server

manage = Manager(app)

# 启动命令
manage.add_command("runserver", Server(use_debugger=True))


if __name__ == "__main__":
    manage.run()
