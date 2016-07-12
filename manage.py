from flask_script import Manager, prompt_bool
from service import config, create_app, db, models
from flask_migrate import MigrateCommand

app = create_app(config.DevelopmentConfig)

manager = Manager(app, with_default_commands=False)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host='localhost', port=80)

@MigrateCommand.command
def create():
    db.create_all()

@MigrateCommand.command
def drop():
    if prompt_bool('Are you sure you want to drop all tables', default=False):
        db.drop_all()

@MigrateCommand.command
def populate():
    user = models.users.Users()

    user.sid = "004398952"
    user.role = 3
    user.name = 'Ruben Castaneda'
    user.email = 'rubennc1994@gmail.com'

    db.session.add(user)
    db.session.commit()
    pass

if __name__ == '__main__':
    manager.run()