from app import app, create_app
from flask_script import Manager, Server

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

if __name__ == '__newsapp__':
    manager.run()