#!/home/taha/Dropbox/aruba/aruba/bin/python3
import os

from flask_migrate import Migrate , MigrateCommand
from flask_script import Manager


from app.main import db, create_app
from app import blueprint


app = create_app('prod')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0', port=8080)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == "__main__":
    manager.run()


