#!/home/taha/Dropbox/wifi/wifigelocation/bin/python3
import os

from flask_migrate import Migrate , MigrateCommand
from flask_script import Manager


from app.main import db, create_app
from app import blueprint


app = create_app('dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()




if __name__ == "__main__":
    manager.run()


